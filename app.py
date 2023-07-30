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
@app.route('/livros', methods=['GET'])
def obter_livros():
  return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)