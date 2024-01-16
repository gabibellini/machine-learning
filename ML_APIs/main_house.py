from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

modelo = pickle.load(open('modelo.sav', 'rb'))
colunas = ['tamanho', 'ano', 'garagem']

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'jung'
app.config['BASIC_AUTH_PASSWORD'] = '1997'

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return "Minha primeira API."

@app.route('/cotacao/', methods = ['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])

app.run(debug = True)