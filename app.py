from flask_cors import CORS
from flask import Flask, jsonify

from processdata import processdata #arquivo criado no passo anterior, ele converte os dados de .csv para lista

app = Flask(__name__)
CORS(app)# Neste caso, a URL direcionará para home.
@app.route('/')
def displaylocations():    # Puxa os arquivos do CSV
   l = processdata()    # Entrega os dados para o serviço que chamou essa API.
   return jsonify(l)

if __name__ == '__main__':
   app.run(host="localhost", port=8000, debug=True)# subindo a aplicação em http://localhost:8000/
