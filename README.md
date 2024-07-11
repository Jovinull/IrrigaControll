# Sistema de Irrigação Automática com ESP32 e Dashboard Flask

Este projeto implementa um sistema de irrigação automática utilizando um ESP32 para monitorar a umidade do solo e controlar um relé, além de exibir os dados coletados em um dashboard desenvolvido com Flask.

## Sumário

- [Introdução](#introdução)
- [Componentes Utilizados](#componentes-utilizados)
- [Configuração do ESP32](#configuração-do-esp32)
- [Configuração do Dashboard Flask](#configuração-do-dashboard-flask)
- [Execução do Projeto](#execução-do-projeto)
- [Estrutura de Arquivos](#estrutura-de-arquivos)
- [Equipe](#equipe)
- [Licença](#licença)

## Introdução

O projeto visa criar um sistema de irrigação automática que otimiza o uso da água na agricultura. Utilizando um ESP32, sensores de umidade do solo e umidade do ar, e um relé para controlar a bomba de irrigação, o sistema coleta dados em tempo real e os exibe em um dashboard web.

## Componentes Utilizados

- ESP32
- Sensor DHT22 (umidade e temperatura)
- Sensor de umidade do solo
- Módulo relé
- Resistor de 10kΩ
- Jumpers e protoboard

## Configuração do ESP32

O código do ESP32 está configurado para:
- Ler a umidade e temperatura do ar usando o DHT22.
- Ler a umidade do solo usando um sensor de umidade.
- Controlar um relé baseado na leitura da umidade do solo.
- Expor uma API HTTP para fornecer os dados coletados.

### Código do ESP32

```cpp
#include <WiFi.h>
#include <WebServer.h>
#include <DHT.h>

// Definições do DHT
#define DHTPIN 4
#define DHTTYPE DHT22
#define relePin 5

DHT dht(DHTPIN, DHTTYPE);

// Definições do sensor de umidade do solo
const int soilMoisturePin = 34;
bool irrigar = false;

// Credenciais WiFi
const char* ssid = "p a";
const char* password = "fvea2556";

// Cria uma instância do servidor
WebServer server(80);

// Variáveis para armazenar os valores dos sensores
float humidity = 0.0;
float temperature = 0.0;
int soilMoisture = 0;

// Intervalo de tempo entre leituras
unsigned long previousMillis = 0;
const long interval = 2000;

// Função para lidar com a rota /data
void handleData() {
    String json = "{";
    json += "\"humidity\":" + String(humidity) + ",";
    json += "\"temperature\":" + String(temperature) + ",";
    json += "\"soilMoisture\":" + String(soilMoisture);
    json += "}";
    server.send(200, "application/json", json);
}

void setup() {
    Serial.begin(115200);
    dht.begin();
    pinMode(soilMoisturePin, INPUT);
    pinMode(relePin, OUTPUT);

    digitalWrite(relePin, HIGH);

    // Conecta ao WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Conectando ao WiFi...");
    }
    Serial.println("Conectado ao WiFi");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());

    // Define a rota /data
    server.on("/data", handleData);

    // Inicia o servidor
    server.begin();
}

void loop() {
    server.handleClient();

    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;

        // Lê os valores dos sensores
        humidity = dht.readHumidity();
        temperature = dht.readTemperature();
        soilMoisture = map(analogRead(soilMoisturePin), 0, 4095, 0, 100);

        // Verifica se a leitura dos sensores falhou
        if (isnan(humidity) || isnan(temperature)) {
            Serial.println("Falha ao ler o sensor DHT!");
        } else {
            Serial.print("Umidade do ar (%): ");
            Serial.print(humidity);
            Serial.print(" | Temperatura (C): ");
            Serial.print(temperature);
            Serial.print(" | Umidade do solo (%): ");
            Serial.println(100 - soilMoisture);
        }

        irrigar = digitalRead(soilMoisturePin);

        if(soilMoisture <= 50) {
          digitalWrite(relePin,HIGH);
          Serial.println("LOW");
        }
        else {
          digitalWrite(relePin, LOW);
          Serial.println("HIGH");
        }
    }
}
```

## Configuração do Dashboard Flask

O dashboard Flask exibe os dados coletados pelo ESP32 em uma interface web. Ele inclui várias rotas para renderizar páginas HTML e fornecer dados JSON.

### Código do Flask

```python
from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_sensor_data():
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

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### Estrutura de Arquivos

- `app.py`: Código principal do servidor Flask.
- `templates/`
  - `index.html`: Página principal do dashboard.
  - `sobre.html`: Página de informações sobre o projeto.
  - `equipe.html`: Página com informações sobre a equipe.
- `static/`
  - `style.css`: Estilos para o dashboard.
  - `sobre.css`: Estilos para a página sobre.
  - `equipe.css`: Estilos para a página da equipe.
  - `script.js`: Script para atualizar os dados dos sensores.

## Execução do Projeto

### Executando o Código do ESP32

1. Carregue o código do ESP32 usando o Arduino IDE.
2. Certifique-se de que o ESP32 está conectado à rede WiFi correta.

### Executando o Dashboard Flask

1. Instale as dependências necessárias:
    ```sh
    pip install flask flask-cors requests
    ```
2. Execute o servidor Flask:
    ```sh
    python app.py
    ```

3. Acesse o dashboard no navegador:
    ```
    http://127.0.0.1:5000
    ```

## Equipe

- **Felipe Jovino Dos Santos**
- **Gilberto Bispo Dos Santos Neto**
- **Luiz Eduardo Andrade De Oliveira**
- **Paulo Arthur Pereira Neri**

### Professores

- **Stephanie Kamarry Alves de Sousa**
- **Fábio Luiz de Sá Prudente**
- **Catuxe Varjão De Oliveira**
- **Phillipe Cardoso Santos**

## Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
