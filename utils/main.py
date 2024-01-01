import requests

api_key = "Chave_Key"
cidade = "teresina"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

requisicao = requests.get(link)
nomes_requisicao = requisicao.json()
localizacao = nomes_requisicao['coord']
clima = nomes_requisicao['weather'][0]['description']
nome = nomes_requisicao['name']
humidade = nomes_requisicao['main']['humidity']
temperatura = nomes_requisicao['main']['temp'] - 273.15
print(nomes_requisicao)
context = f"""
        Localização: {localizacao}\n
        Cidade: {nome}\n
        Temperatura: {temperatura:.2f}°C\n
        Clima: {clima}\n 
        Humidade: {humidade}
"""
print(context)