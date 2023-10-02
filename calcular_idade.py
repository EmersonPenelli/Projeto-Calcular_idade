import datetime

def obter_ano_nascimento():
    while True:
        ano_nascimento = input("Digite o ano de nascimento (1922 a 2021): ")
        try:
            ano_nascimento = int(ano_nascimento)
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano inválido. Tente novamente.")
        except ValueError:
            print("Ano inválido. Por favor, digite um valor numérico.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    return ano_atual - ano_nascimento

def main():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)

    print(f"\nNome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")

if __name__ == "__main__":
    main()
