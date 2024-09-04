from flask import Flask, render_template, g, request, redirect
import sqlite3

def ligar_banco():
    banco = g._database = sqlite3.connect('banco.db')
    return banco

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo = 'Eliane Potiguara')


if __name__ == '__main__':
    app.run()
