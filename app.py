from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
  {
    'id': 1,
    'title': 'O senhor dos Anéis - A Sociedade do Anel',
    'autor': 'J.R.R Tolkien'
  },
  {
    'id': 2,
    'title': 'Harry Potter e a Pedra Filosofal',
    'autor': 'J.K Howling'
  },
  {
    'id': 3,
    'title': 'James Clear',
    'autor': 'Hábitos Atômicos'
  }
]

#Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
  return jsonify(livros)

#Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
  for livro in livros:
    if livro.get('id') == id:
      return jsonify(livro)

#Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
  livro_alterado = request.get_json()
  for indice,livro in enumerate(livros):
    if livro.get('id') == id:
      livros[indice].update(livro_alterado)
      return jsonify(livros[indice])

app.run(port=5000, host='localhost', debug=True)