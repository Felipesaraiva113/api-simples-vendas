from flask import Flask,jsonify
import pandas as pd
app = Flask(__name__)
@app.route('/')
def homepage():
    return 'a api está no ar'
@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('vendas.csv')
    total_vendas = tabela['vendas'].sum()
    resposta = {'total_vendas': int(total_vendas)}
    return jsonify(resposta)
if __name__ == '__main__':
    app.run(debug=True)

