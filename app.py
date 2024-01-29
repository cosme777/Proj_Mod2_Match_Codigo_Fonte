import requests
import json
from babel.numbers import format_currency
from decimal import Decimal
from datetime import datetime
import pytz
import locale


# Defina a formatação local para separador de milhar e vírgula para as casas decimais
#locale.setlocale(locale.LC_ALL, '')

# Define o fuso horário do Brasil
fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')
# Obtém a data e hora atual com o fuso horário do Brasil
data_hora_brasil = datetime.now(fuso_horario_brasil)
# Data e hora do Brasil
data_atual = data_hora_brasil.strftime("%d/%m/%Y - %H:%M")


# Lista de moedas
MOEDAS = ["USD","EUR","GBP","JPY","CAD","AUD","CHF","CNY","BRL",]

print('\n'f'\033[1mCONVERSOR ONLINE\033[0m','\n')
print('''
\033[1mMoedas Disponíveis:\033[0m 

[ USD ] - Dólar Americano
[ EUR ] - Euro
[ GBP ] - Libra Esterlina
[ JPY ] - Iene Japonês
[ CAD ] - Dólar Canadense 
[ AUD ] - Dólar Australiano
[ CHF ] - Franco Suíço 
[ CNY ] - Yuan Renminb Chinês
[ BRL ] - Real Brasileiro
''')

      
# Solicita o valor a ser convertido
def solicita_valor():
    while True:
        valor_input = input("Insira o valor a ser convertido: ")
        if "." in valor_input:
            print("Apenas números sem '.' e ','")
        else:
            try:
                valor = float(valor_input)
                return valor
            except ValueError:
                print("Valor inválido. Insira apenas números.")
    

# Solicita a moeda de entrada
def solicita_moeda_entrada():
    moeda_entrada = input("Insira a moeda de origem: ").upper()
    while moeda_entrada not in MOEDAS:
        print("Moeda inválida. Tente novamente.")
        moeda_entrada = input("Insira a moeda de origem: ").upper()
    return moeda_entrada

# Solicita a moeda de origem
def solicita_moeda_origem():
    moeda_origem = input("Insira a moeda de destino: ").upper()
    while moeda_origem not in MOEDAS:
        print("Moeda inválida. Tente novamente.")
        moeda_origem = input("Insira a moeda de destino: ").upper()
    return moeda_origem

# Realiza a conversão
def converte_moedas(valor, moeda_entrada, moeda_origem):
    # Obtém a taxa de conversão
    url = "https://api.exchangerate-api.com/v4/latest/{}".format(moeda_entrada)
    response = requests.get(url)
    data = json.loads(response.text)
    taxa_conversao = data["rates"][moeda_origem]

    # Realiza a conversão
    valor_convertido = valor * taxa_conversao

    # Formata o valor convertido
    valor_convertido = "{:.2f}".format(valor_convertido)

    print('\n'f'\033[1mResultado da Pesquisa\033[0m','\n')

    print(f"A taxa de conversão de {moeda_entrada} para {moeda_origem} é {taxa_conversao}")

    return valor_convertido

# Programa principal
if __name__ == "__main__":
    # Exibe a lista de moedas
# exibe_moedas()

    # Solicita o valor a ser convertido
    valor = solicita_valor()

    # Solicita a moeda de entrada
    moeda_entrada = solicita_moeda_entrada()

    # Solicita a moeda de origem
    moeda_origem = solicita_moeda_origem()

    # Realiza a conversão
    valor_convertido = converte_moedas(valor, moeda_entrada, moeda_origem)

    # Exibe o resultado
    print(f"O Valor de {valor} {moeda_entrada} equivale a {valor_convertido} em {moeda_origem}")
    print('\n''Realizada em:', data_atual,'\n')