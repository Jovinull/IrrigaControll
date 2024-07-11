from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Rota inicial da página web
@app.route('/')
def index():
    return render_template('index.html')

# Rota para fornecer os dados dos sensores em formato JSON
@app.route('/data')
def get_sensor_data():
    # Substitua pelo endereço IP do seu ESP32
    esp32_ip = 'http://192.168.186.3/data'
    try:
        response = requests.get(esp32_ip)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        print(f"Erro na requisição para o ESP32: {e}")
        return jsonify({'error': 'Erro ao acessar o ESP32'}), 500
    
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para a página Equipe
@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

if __name__ == '__main__':
    app.run(debug=True)
