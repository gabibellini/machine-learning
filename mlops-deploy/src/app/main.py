from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import pickle
import os

# carregando o modelo
modelo = pickle.load(open('models/modelo.sav', 'rb'))
colunas = ['tamanho', 'ano', 'garagem']

# autenticação com variável do ambiente
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return "Minha primeira API."

@app.route('/sentiment/<frase>')
@basic_auth.required
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang = 'pt-br', to ='en')
    polaridade = tb_en.polarity
    return "Polaridade: {}".format(polaridade)

app.run(debug = True, host = '0.0.0.0')
