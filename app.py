from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos (simulando um banco de dados)
produtos = [
    {"id": 1, "nome": "Produto 1", "descricao": "Descrição do Produto 1", "preco": 10.00},
    {"id": 2, "nome": "Produto 2", "descricao": "Descrição do Produto 2", "preco": 20.00},
    {"id": 3, "nome": "Produto 3", "descricao": "Descrição do Produto 3", "preco": 30.00}
]

# Página inicial - Lista de produtos
@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

# Página para adicionar um novo produto
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        novo_produto = {
            'id': len(produtos) + 1,
            'nome': request.form['nome'],
            'descricao': request.form['descricao'],
            'preco': float(request.form['preco'])
        }
        produtos.append(novo_produto)
        mensagem = "Produto adicionado com sucesso!"
        message_type = "success"        
        return render_template('adicionar.html', message=mensagem, message_type=message_type)
    return render_template('adicionar.html')

# Página para editar um produto existente
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if request.method == 'POST':
        produto['nome'] = request.form['nome']
        produto['descricao'] = request.form['descricao']
        produto['preco'] = float(request.form['preco'])
        mensagem = "Produto editado com sucesso!"
        message_type = "success"        
        # return redirect(url_for('index'))
        return render_template('editar.html', produto=produto, message=mensagem, message_type=message_type)
    return render_template('editar.html', produto=produto)

# Rota para deletar um produto
@app.route('/deletar/<int:id>')
def deletar_produto(id):
    global produtos
    produtos = [p for p in produtos if p['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
