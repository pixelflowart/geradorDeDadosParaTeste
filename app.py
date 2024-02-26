'''
Descrição do Projeto

Projeto #1 - Gerador de Dados P/ teste [App no Terminal]
O projeto deve iniciar apresentando uma lista de opções sobre quais dado(s) devem ser gerados, pedindo o usuário
para escolher uma ou mais opções de dados a serem gerados entre as seguintes opções: gerar nome, gerar e-mail,
gerar telefone, gerar cidade, gerar estado, além de perguntar se os dados devem ser salvos para um arquivo também.
Finalmente o usuário deve poder digitar “parar” a qualquer momento para conseguir finalizar o programa.

'''
import random
import os
# Banco de Dados para gerar dados aleatórios
nomes = [
    "João Silva",
    "Maria Santos",
    "Pedro Oliveira",
    "Ana Souza",
    "Carlos Pereira",
    "Lúcia Costa",
    "Rafaela Ferreira",
    "Márcio Almeida",
    "Fernanda Rocha",
    "Antônio Santos",
    "Cristina Lima",
    "Roberto Gomes",
    "Eduarda Martins",
    "Daniel Barbosa",
    "Mariana Cardoso",
    "Paulo Vieira",
    "Camila Oliveira",
    "Rodrigo Mendes",
    "Juliana Pereira",
    "Lucas Fernandes",
    "Patrícia Silva",
    "Guilherme Costa",
    "Isabela Gonçalves",
    "Vinícius Rodrigues",
    "Letícia Alves",
    "Felipe Oliveira",
    "Carolina Nunes"
]

telefones = [
    "123456789",
    "987654321",
    "456123789",
    "789456123",
    "321654987",
    "654987321",
    "987321654",
    "123789456",
    "456789123",
    "321987654",
    "654123789",
    "789321654",
    "123987456",
    "456321987",
    "321456987",
    "654789123",
    "789123654",
    "123654789",
    "987456321",
    "654321987",
    "321789456",
    "456987123",
    "789654321",
    "321123456",
    "456789321",
    "987321456",
    "123456987",
    "654789321"
]

emails = [
    "joao.silva@example.com",
    "maria.santos@example.com",
    "pedro.oliveira@example.com",
    "ana.souza@example.com",
    "carlos.pereira@example.com",
    "lucia.costa@example.com",
    "rafaela.ferreira@example.com",
    "marcio.almeida@example.com",
    "fernanda.rocha@example.com",
    "antonio.santos@example.com",
    "cristina.lima@example.com",
    "roberto.gomes@example.com",
    "eduarda.martins@example.com",
    "daniel.barbosa@example.com",
    "mariana.cardoso@example.com",
    "paulo.vieira@example.com",
    "camila.oliveira@example.com",
    "rodrigo.mendes@example.com",
    "juliana.pereira@example.com",
    "lucas.fernandes@example.com",
    "patricia.silva@example.com",
    "guilherme.costa@example.com",
    "isabela.goncalves@example.com",
    "vinicius.rodrigues@example.com",
    "leticia.alves@example.com",
    "felipe.oliveira@example.com",
    "carolina.nunes@example.com"
]

cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Salvador",
    "Brasília",
    "Curitiba",
    "Fortaleza",
    "Manaus",
    "Recife",
    "Goiânia",
    "Belém",
    "Porto Alegre",
    "São Luís",
    "Campinas",
    "São Gonçalo",
    "Maceió",
    "Campo Grande",
    "Teresina",
    "Natal",
    "Osasco",
    "Cuiabá",
    "Aracaju",
    "Feira de Santana",
    "Joinville",
    "Juiz de Fora",
    "Londrina",
    "Aparecida de Goiânia",
    "Santarém"
]

estados = [
    "AC",  # Acre
    "AL",  # Alagoas
    "AP",  # Amapá
    "AM",  # Amazonas
    "BA",  # Bahia
    "CE",  # Ceará
    "DF",  # Distrito Federal
    "ES",  # Espírito Santo
    "GO",  # Goiás
    "MA",  # Maranhão
    "MT",  # Mato Grosso
    "MS",  # Mato Grosso do Sul
    "MG",  # Minas Gerais
    "PA",  # Pará
    "PB",  # Paraíba
    "PR",  # Paraná
    "PE",  # Pernambuco
    "PI",  # Piauí
    "RJ",  # Rio de Janeiro
    "RN",  # Rio Grande do Norte
    "RS",  # Rio Grande do Sul
    "RO",  # Rondônia
    "RR",  # Roraima
    "SC",  # Santa Catarina
    "SP",  # São Paulo
    "SE",  # Sergipe
    "TO"   # Tocantins
]

opcoes = [
    "nome",
    "telefone",
    "email",
    "cidade",
    "estado"
]
# Criar tela de Apresentação do Software
opcao = ''

def estilo(texto, cor='', estilo=''):
    return f"\033[{estilo};{cor}m{texto}\033[0m"

def rodar_geracao():
    global opcao  # Indica que estamos usando a variável global 'opcao'
    print(estilo("-------------------------------------------", cor='32', estilo='1'))
    print(estilo("|||>>> Bem-vindo ao GERADOR de DADOS <<<|||", cor='32', estilo='1'))
    print(estilo("-------------------------------------------", cor='32', estilo='1'))
    print(estilo("Entre as opções abaixo, escolha quais dados quer gerar:\nPara SAIR digite 'parar'!", cor='33'))

    # Lista de Opções de Dados a serem gerados : Nomes, E-mails, Telefones, Cidade, Estado
    for indice, valor in enumerate(opcoes):
        print(estilo(f'{indice} - {valor}', cor='36'))

    # Escolher qual dado deve ser gerado
    opcao = input(estilo("Digite sua opção: -> ".lower(), cor='32')).lower()
    
    if 'parar' in opcao:
        print(estilo('Programa encerrado, com sucesso!', cor='31', estilo='1'))
        return
    else:
        
        while True:
            mensagem_erro = 'Erro: Insira apenas números!'
            try:
                numero_de_geracoes = int(input(estilo("Quantos elementos devem ser gerados? -> ", cor='32')))
                opcao_salvar_dados = int(input(estilo("[1] Exibir na tela | [2] Exibir e Salvar em arquivo texto. \nQual opção você escolhe? -> ", cor='32')))
                if str(opcao_salvar_dados) not in ['1', '2']:
                    mensagem_erro = 'Erro: Insira apenas 1 ou 2.'
                    raise ValueError(mensagem_erro)
                break
            except ValueError:
                print(estilo(mensagem_erro, cor='31'))

        os.system('cls')

        # Gerar dados
        dados_gerados = []
        geracao_de_dados = 0

        while geracao_de_dados < numero_de_geracoes:
            # Programa encerra somente quando usuário digitar "parar"
            if opcao == 'parar':
                    print("Programa encerrado.")
                    break
            dados_gerados.append({})

            if '0' in opcao:
                dados_gerados[geracao_de_dados]['nome']= random.choice(nomes)
            if '1' in opcao:
                dados_gerados[geracao_de_dados]['telefone']= random.choice(telefones)
            if '2' in opcao:
                dados_gerados[geracao_de_dados]['email']= random.choice(emails)
            if '3' in opcao:
                dados_gerados[geracao_de_dados]['cidade']= random.choice(cidades)
            if '4' in opcao:
                dados_gerados[geracao_de_dados]['estado']= random.choice(estados)
            print(estilo('>>>', cor='34'))
            print(estilo(f'DADOS GERADOS - Geração nº {geracao_de_dados+1}', cor='34', estilo='1'))


            # Exibir na tela
            if opcao_salvar_dados == "1":
                print(dados_gerados[geracao_de_dados])

            else:
            # Exibir na tela &
            # Gravar dados em arquivo txt

                print(dados_gerados[geracao_de_dados])
                with open("dados.txt", "a", encoding="utf-8") as arquivo:  # Especificando UTF-8 como encoding
                    arquivo.write(str(dados_gerados[geracao_de_dados]) + "\n")
                print('Dados salvos em arquivo texto')

            
            geracao_de_dados += 1

while 'parar' not in opcao:

    rodar_geracao()




