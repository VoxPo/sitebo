import mysql.connector
from flask import Flask, render_template, request, url_for, flash, redirect, session
from forms import formLogin, formNovoUsuario
from hashlib import sha256

app = Flask(__name__)

app.config['SECRET_KEY'] = '2dc162370584a8d07a41582768c0478d'

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@$$w0rd',
    database = 'ead_senac',
)

@app.route ("/")
def index():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/login", methods=['get', 'post'])
def login():
    titulo = 'Login de acesso'
    descricao = 'Formulario de login'

    form_login = formLogin()
    form_novo_login = formNovoUsuario()

    if form_login.validate_on_submit() and 'submitLogin' in request.form:
       
        cursor = mydb.cursor()

        email = form_login.email.data
        senha = form_login.senha.data
        hashSenha = sha256(senha.encode())

        comando = f'Select * from alunos where email = "{email}"'
        cursor.execute(comando)
        result = cursor.fetchall()

        if hashSenha.hexdigest() ==  result[0][5] :
            session['nome_usuario'] = result[0][1]
            flash(f'Login realizado com sucesso: {form_login.email.data}', 'alert-primary')
            return redirect(url_for('index'))
        else:
            flash(f'Usuario ou senha incorreta para: {form_login.email.data}', 'alert-danger')
            return redirect(url_for('login'))

    if form_novo_login.validate_on_submit() and 'submit' in request.form:    
        cursor = mydb.cursor()

        nome = form_novo_login.nome.data
        telefone = form_novo_login.celular.data
        email = form_novo_login.email.data
        cpf = form_novo_login.cpf.data
        senha = form_novo_login.senha.data
        hashSenha = sha256(senha.encode())

        query = f'INSERT INTO alunos (nome, email, telefone, cpf, senha) VALUES ("{nome}", "{email}", "{telefone}", "{cpf}", "{hashSenha.hexdigest()}")'
        print(query)
        cursor.execute(query)
        mydb.commit()

        flash(f'CADASTRO REALIZADO COM SUCESSO: {form_novo_login.nome.data}' , 'alert-success')
        return redirect(url_for('index'))

    return render_template("login.html", descricao = descricao, form_login = form_login, form_novo_login = form_novo_login, titulo = titulo)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/EAD")
def ead():
    return render_template("ead.html")

if __name__ == '__main__' :
    app.run(debug=True)    