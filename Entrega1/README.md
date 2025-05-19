# Sistema de Monitoramento de Solo 

 Sistema automatizado de monitoramento de umidade e nutrientes do solo utilizando a placa ESP32. A lógica de controle aciona uma bomba d'água (simulada por um relé) sempre que a umidade do solo estiver abaixo do limite ideal, além de indicar a presença de fósforo e potássio via botões indicando se possui/não possui.

---

## Componentes Utilizados

- ESP32
- Sensor DHT22 (temperatura e umidade)
- LDR simulando sensor de pH
- 2 botões (detectam presença de fósforo e potássio)
- Módulo Relé (aciona bomba)
- LED (indica bomba ligada)
- Resistores e jumpers

---

## Funcionamento

### Sensores:
- DHT22 → mede temperatura e umidade do solo.
- LDR (pH simulado) → leitura analógica convertida em valor de pH.
- Botões → retornam valores booleanos indicando presença de fósforo e potássio.

Saída:
- Se a umidade do solo < 60%, o relé é acionado para simular irrigação.
- O LED é aceso junto ao relé para indicar bomba ligada.
- A cada dois segundos os dados são lidos nos sensores e impressos.

---

## Saída dos Dados

```txt
EX : Temp: 15.0°C | Umidade SOLO: 25.5% | pH simulado: 7 | Fósforo: 1 | Potássio: 0

