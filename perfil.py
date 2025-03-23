import requests

def obter_usuario_aleatorio():
    """Obtém um usuário aleatório da API Random User Generator"""
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    response.raise_for_status()  # Lança erro se houver problema na requisição

    dados = response.json()  # Converte a resposta para JSON
    usuario = dados["results"][0]  # Acessa o primeiro usuário gerado

    nome = f'{usuario["name"]["first"]} {usuario["name"]["last"]}'
    email = usuario["email"]
    pais = usuario["location"]["country"]

    return f"Nome: {nome}\nEmail: {email}\nPaís: {pais}"

def main():
    """Função principal"""
    print("Gerando perfil de usuário aleatório...\n")
    print(obter_usuario_aleatorio())

if __name__ == "__main__":
    main()
