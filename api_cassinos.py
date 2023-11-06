from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/doublebetbry', methods=['GET'])
def get_doublebetbry():
    conexão = sqlite3.connect('api.db')
    comando = f"SELECT valor1, valor2, valor3, valor4, valor5, valor6, valor7, identify FROM api WHERE casa='double_betbry'"
    cursor = conexão.execute(comando)
    resultado = cursor.fetchone()
    cursor.close()
    conexão.close()
    return jsonify(resultado)

@app.route('/crashbrabet', methods=['GET'])
def get_crashbrabet():
    conexão = sqlite3.connect('api.db')
    comando = f"SELECT valor1, valor2, valor3, valor4, valor5, valor6, valor7, identify FROM api WHERE casa='crash_brabet'"
    cursor = conexão.execute(comando)
    resultado = cursor.fetchone()
    cursor.close()
    conexão.close()
    return jsonify(resultado)

@app.route('/crashblaze', methods=['GET'])
def get_crashblaze():
    conexão = sqlite3.connect('api.db')
    comando = f"SELECT valor1, valor2, valor3, valor4, valor5, valor6, valor7, identify FROM api WHERE casa='crash_blaze'"
    cursor = conexão.execute(comando)
    resultado = cursor.fetchone()
    cursor.close()
    conexão.close()
    return jsonify(resultado)

@app.route('/doublebrabet', methods=['GET'])
def get_doublebrabet():
    conexão = sqlite3.connect('api.db')
    comando = f"SELECT valor1, valor2, valor3, valor4, valor5, valor6, valor7, identify FROM api WHERE casa='double_brabet'"
    cursor = conexão.execute(comando)
    resultado = cursor.fetchone()
    cursor.close()
    conexão.close()
    return jsonify(resultado)

@app.route('/doubleblaze', methods=['GET'])
def get_doubleblaze():
    conexão = sqlite3.connect('api.db')
    comando = f"SELECT valor1, valor2, valor3, valor4, valor5, valor6, valor7, identify FROM api WHERE casa='double_blaze'"
    cursor = conexão.execute(comando)
    resultado = cursor.fetchone()
    cursor.close()
    conexão.close()
    return jsonify(resultado)

app.run(port=5000,host='localhost',debug=True)