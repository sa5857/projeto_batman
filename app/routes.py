from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/fotos')
def fotos():
    return render_template('fotos.html')

@app.route('/comentarios')
def comentarios():
    return render_template('comentarios.html')
