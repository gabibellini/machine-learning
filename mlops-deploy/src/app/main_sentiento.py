from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

# definir as rotas da API

@app.route('/')
def home():
    return "Minha primeira API."

@app.route('/analise_sentimento/<frase>') # tudo que o usuário digitar entrará como frase
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang = 'pt-br', to ='en')
    polaridade = tb_en.polarity
    return "Polaridade: {}".format(polaridade)

app.run(debug = True)