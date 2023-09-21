from datetime import datetime
from validate_docbr import CPF
import re
import requests


def valida_cpf(cpf_input):
  cpf = CPF()

  while True:

    cpf_input = re.sub('[-.]', '',cpf_input)

    resultado = cpf.validate(cpf_input)
    if resultado:
      cpf_formatado = f"{cpf_input[:3]}.{cpf_input[3:6]}.{cpf_input[6:9]}-{cpf_input[9:]}"
      return cpf_formatado
    else:
      cpf_input = input("CPF inválido. Digite novamente: ")
    
    # CONTINUE, BREAK, RETURN, ALTERACAO CONDICAO


def valida_rg(rg_input):
  
  # RG: 11.111.111.-x
  padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

  while True:

    rg_input = re.sub('[-.]','', rg_input)

    rg_input = f'{rg_input[:2]}.{rg_input[2:5]}.{rg_input[5:8]}-{rg_input[8:]}'

    if re.match(padrao_rg, rg_input):
      return rg_input
    else:
      rg_input = input("RG inválido. Digite novamente: ")


def valida_data_nascimento():
  
  while True:
    data_nascimento_input = input("Digite a data de nascimento: ")
   
    try:
      data_convertida = datetime.strptime(data_nascimento_input, '%d/%m/%Y').date()
      data_atual = datetime.now().date()

      if data_convertida < data_atual:
        return data_convertida.strftime("%d/%m/%Y")
    
      else:
        print("Data inválida. Data de nasicmento deve ser menor que a data atual.")
    
    except ValueError as e:
      print("Formato inválido. Data deve estar no formato dd/mm/yyyy.")
    except TypeError as e:
      print("Formato inválido. Data deve estar no formato dd/mm/yyyy.")
    
    
def busca_cep(cep_input):

  url = f'https://viacep.com.br/ws/{cep_input}/json/'
  
  response = requests.get(url, verify=False)
  
  if response.status_code == 200:
    data = response.json()
 
    endereco = {
      "CEP": data['cep'],
      "Logradouro": data['logradouro'],
      "Bairro": data['bairro'],
      "Cidade": data['localidade'],
      "Estado": data['uf']
      
    }
    print(endereco)

    return endereco

