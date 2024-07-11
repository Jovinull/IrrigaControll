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

1. **Ler a umidade e temperatura do ar**: Utilizando o sensor DHT22, o ESP32 coleta dados de umidade e temperatura do ambiente.
2. **Ler a umidade do solo**: Utilizando um sensor de umidade do solo, o ESP32 monitora a umidade da terra.
3. **Controlar um relé**: Com base na leitura da umidade do solo, o ESP32 ativa ou desativa um relé para controlar a irrigação.
4. **Expor uma API HTTP**: O ESP32 possui um servidor web embutido que fornece os dados dos sensores em formato JSON, acessível através de uma rota específica.

## Configuração do Dashboard Flask

O dashboard Flask exibe os dados coletados pelo ESP32 em uma interface web. Ele inclui várias rotas para renderizar páginas HTML e fornecer dados JSON.

1. **Rota Inicial**: Exibe a página principal do dashboard.
2. **Rota de Dados**: Fornece os dados dos sensores em formato JSON, obtendo-os do servidor web do ESP32.
3. **Rotas de Informação**: Inclui páginas sobre o projeto e a equipe.

### Principais Arquivos e Funções

- `app.py`: Código principal do servidor Flask, contendo as rotas e lógica para se comunicar com o ESP32.
- `templates/`: Contém os arquivos HTML para renderizar as páginas web.
  - `index.html`: Página principal do dashboard, exibe os dados dos sensores.
  - `sobre.html`: Página com informações sobre o projeto.
  - `equipe.html`: Página com informações sobre a equipe.
- `static/`: Contém os arquivos estáticos como CSS e JavaScript.
  - `style.css`: Estilos para o dashboard.
  - `sobre.css`: Estilos para a página sobre.
  - `equipe.css`: Estilos para a página da equipe.
  - `script.js`: Script para atualizar os dados dos sensores em tempo real.

## Execução do Projeto

### Executando o Código do ESP32

1. Carregue o código do ESP32 usando o Arduino IDE.
2. Certifique-se de que o ESP32 está conectado à rede WiFi correta.
3. O ESP32 iniciará um servidor web local para fornecer os dados dos sensores.

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
