from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe responsável por criar a entidade "Produto" com os atributos: nome, descrição e valor. 
class Produto(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    descricao = db.Column(db.String[500])
    valor = db.Column(db.Double[3])
    
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor