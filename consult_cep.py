import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            print("\nEndereço encontrado:")
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados.get('uf', 'Não disponível')}")
        else:
            print("CEP não encontrado. Verifique e tente novamente.")
    else:
        print("Erro ao consultar a API.")

# Entrada do usuário
cep_usuario = input("Digite um CEP para consulta (somente números): ")
consultar_cep(cep_usuario)
