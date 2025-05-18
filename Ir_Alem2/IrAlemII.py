import requests
from datetime import datetime, timedelta

def obter_coordenadas(cidade):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt&format=json"
    resposta = requests.get(url).json()

    if "results" in resposta and len(resposta["results"]) > 0:
        resultado = resposta["results"][0]
        return resultado["latitude"], resultado["longitude"], resultado["name"]
    else:
        raise ValueError("Localização não encontrada. Verifique o nome da cidade.")

def obter_previsao(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&hourly=temperature_2m,relative_humidity_2m,precipitation"
        f"&forecast_days=1&timezone=America/Sao_Paulo"
    )
    return requests.get(url).json()

def verificar_bomba(data):
    agora = datetime.now()
    horarios = data["hourly"]["time"]
    precipitacao = data["hourly"]["precipitation"]
    umidade = data["hourly"]["relative_humidity_2m"]
    temperatura = data["hourly"]["temperature_2m"]

    # Índices para as próximas 12h
    indices_proximas_12h = [
        i for i, hora in enumerate(horarios)
        if agora <= datetime.fromisoformat(hora) <= agora + timedelta(hours=12)
    ]

    chuva_prevista = any(precipitacao[i] > 0 for i in indices_proximas_12h)
    umidade_atual = umidade[indices_proximas_12h[0]]
    temperatura_atual = temperatura[indices_proximas_12h[0]]

    if chuva_prevista:
        status_bomba = "DESLIGADA (chuva prevista)"
    elif umidade_atual < 40:
        status_bomba = "LIGADA (baixa umidade e sem chuva prevista)"
    else:
        status_bomba = "DESLIGADA (condições aceitáveis)"

    return temperatura_atual, umidade_atual, chuva_prevista, status_bomba

# ----------- EXECUÇÃO PRINCIPAL -----------
try:
    cidade = input("Digite o nome da cidade: ")
    latitude, longitude, nome_local = obter_coordenadas(cidade)
    dados_clima = obter_previsao(latitude, longitude)
    temp, umi, chuva, status = verificar_bomba(dados_clima)

    print(f"\n Localização: {nome_local} ({latitude:.2f}, {longitude:.2f})")
    print(" Dados Meteorológicos Atuais:")
    print(f"Temperatura: {temp}°C")
    print(f"Umidade relativa do ar: {umi}%")
    print(f"Previsão de chuva nas próximas 12h: {'Sim' if chuva else 'Não'}")
    print(f"\n🚰 Status da bomba de irrigação: {status}")

except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
