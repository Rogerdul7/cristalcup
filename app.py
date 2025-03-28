
from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "segredo_cristalcup")

def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == 'admin' and senha == '1234':
            session['usuario'] = usuario
            return redirect(url_for('painel'))
        else:
            return render_template('login.html', erro='Usuário ou senha incorretos')
    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('painel.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

# As outras rotas (cadastrar time, jogador, jogo, resultado, artilharia, notícia) serão coladas aqui depois

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
