import sqlite3
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
cursor.execute(
    'CREATE TABLE IF NOT EXISTS Contato('
    'ID INTEGER PRIMARY KEY, '
    'Nome TEXT,'
    'Email TEXT,'
    'Assunto TEXT,'
    'Mensagem TEXT)'
)