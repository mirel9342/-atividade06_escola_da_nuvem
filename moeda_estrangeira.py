import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            cotacao = dados[chave]
            print(f"\nCotação atual do {moeda} em relação ao Real:")
            print(f"Valor atual: R$ {cotacao['bid']}")
            print(f"Máximo do dia: R$ {cotacao['high']}")
            print(f"Mínimo do dia: R$ {cotacao['low']}")
            print(f"Última atualização: {cotacao['create_date']}")
        else:
            print("Código de moeda inválido. Tente novamente.")
    else:
        print("Erro ao acessar a API. Verifique sua conexão.")

# Entrada do usuário
moeda_usuario = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(moeda_usuario)
