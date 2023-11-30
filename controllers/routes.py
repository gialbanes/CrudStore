from flask import render_template, request, url_for, redirect
from models.database import db, Produto

def init_app(app):
    @app.route('/')
    def index():
        produtos = Produto.query.all()
        return render_template('index.html', produtos=produtos)

    @app.route('/add', methods=['GET','POST'])
    def add():
        if request.method == 'POST':
            produto = Produto(request.form['nome'], request.form['descricao'], request.form['valor'])
            db.session.add(produto)
            db.session.commit()
            return redirect(url_for('gerenciar'))
        return render_template('add.html')
    
    @app.route('/gerenciar', methods=['GET','POST'])
    def gerenciar():
       produtos = Produto.query.all()
       return render_template('gerenciar.html', produtos=produtos)
       """  if request.method == 'POST':
            produto = Produto(request.form['nome'], request.form['descricao'], request.form['valor'])
            db.session.get(produto)
            db.session.commit() 
            return redirect(url_for('index'))
        return render_template('gerenciar.html') """

    @app.route('/edit/<int:id>', methods=['GET','POST'])
    def edit(id):
        produto =  Produto.query.get(id)
        if request.method == 'POST':
            produto.nome = request.form['nome']
            produto.valor = request.form['valor']
            produto.descricao = request.form['descricao']
            db.session.commit()
            return redirect(url_for('gerenciar'))
        return render_template('edit.html',produto=produto)

    @app.route('/delete/<int:id>')
    def delete(id):
        produto = Produto.query.get(id)
        # Deleta o dado, a partir da ID
        db.session.delete(produto)
        db.session.commit()
        return redirect(url_for('gerenciar'))