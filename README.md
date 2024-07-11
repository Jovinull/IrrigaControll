# Sistema de Irrigação Automática com ESP32 e Dashboard Flask

Este projeto implementa um sistema de irrigação automática utilizando um ESP32 para monitorar a umidade do solo e controlar um relé, além de exibir os dados coletados em um dashboard desenvolvido com Flask.

## Sumário

- [Sistema de Irrigação Automática com ESP32 e Dashboard Flask](#sistema-de-irrigação-automática-com-esp32-e-dashboard-flask)
  - [Sumário](#sumário)
  - [Introdução](#introdução)
  - [Componentes Utilizados](#componentes-utilizados)
  - [Configuração do ESP32](#configuração-do-esp32)
    - [Código do ESP32](#código-do-esp32)

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
