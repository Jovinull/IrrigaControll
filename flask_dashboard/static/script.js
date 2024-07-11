document.addEventListener('DOMContentLoaded', function() {
    setInterval(function() {
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                document.getElementById('humidity').textContent = `Umidade do ar (%): ${data.humidity}`;
                document.getElementById('temperature').textContent = `Temperatura (C): ${data.temperature}`;
                document.getElementById('soilMoisture').textContent = `Umidade do solo (%): ${100 - data.soilMoisture}`;
            })
            .catch(error => console.error('Erro ao buscar dados:', error));
    }, 2000); // Atualiza a cada 2 segundos
});
