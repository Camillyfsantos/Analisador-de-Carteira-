# Projeto 01 - Anaslisador de carteira 

from datetime import datetime

ativos = []

def mostrar_menu (): 
    print("=== ANALISADOR DE CARTEIRA ===")
    print("1 - Cadastrar ativos")
    print("2 - Visualizar ativos")
    print("3 - Consultar ativos")
    print("4 - Calcular resultado")
    print("5 - Analisar carteira")
    print("6 - Sair")

def cadastrar_ativo():
    codigo = input("Digite o código do ativo: "). upper()
    nome = input("Digite o nome do ativo: ")
    tipo = input("Digite o tipo do ativo: ")
    quantidade = int(input("Digite a quantidade: "))
    preco_compra = float(input("Digite o preço de compra: "))
    preco_atual = float(input("Digite o preço atual: "))
    data_operacao = datetime.strptime(
        input("Digite a data da operação (dd/mm/aaaa): "),
        "%d/%m/%Y"
        )
    ativo = [
        codigo,
        nome,
        tipo,
        quantidade,
        preco_compra,
        preco_atual,
        data_operacao
        ]
    if quantidade < 0 or preco_compra < 0 or preco_atual < 0:
        print("Dados Inválidos")
    else:
        ativos.append(ativo)

def visualizar_ativos():
    
    if len(ativos) == 0:
        print("Nenhum ativo cadastrado")
    else:
        print(f"Você possui {len(ativos)} ativo(s) cadastrado(s).")
    
        for ativo in ativos:
            print("Código: ", ativo[0])
            print("Prefixo: ", ativo[0][:2])
            print("Nome: ", ativo[1])
            print("Tipo: ", ativo[2])
            print("Quantidade: ", ativo[3])
            print("Preço de Compra: ", ativo[4])
            print("Preço atual: ", ativo[5])
            print("Data da operação: ", ativo[6].strftime("%d/%m/%Y"))
        
def consultar_ativos():
    codigo_busca = input("Digite o código do ativo: "). upper()
    
    encontrado = False
    
    for ativo in ativos: 
        if ativo[0] == codigo_busca:
            mostrar_detalhes(ativo)
            encontrado = True 
    if encontrado == False:
        print("Ativo não encontrado.")
        
def mostrar_detalhes(ativo):
    print("Código:", ativo[0])
    print("Nome:", ativo[1])
    print("Tipo:", ativo[2])
    print("Quantidade:", ativo[3])
    print("Preço de compra:", ativo[4])
    print("Preço atual:", ativo[5])
    print("Data da operação:", ativo[6].strftime("%d/%m/%Y"))
        
def calcular_resultado(ativo, mostrar_detalhes=True):
    valor_investido = ativo[3]*ativo[4]
    valor_atual = ativo[3]*ativo[5]
    lucro_prejuizo = valor_atual - valor_investido
    rentabilidade = (lucro_prejuizo / valor_investido) * 100
    
    if mostrar_detalhes:
       print(f"Valor investido: {valor_investido:.2f}")
       print(f"Valor atual: {valor_atual:.2f}")
       print(f"Lucro/Prejuízo: {lucro_prejuizo:.2f}")
       print(f"Rentabilidade: {rentabilidade:.2f}%")
    
    return [valor_investido, valor_atual, lucro_prejuizo, rentabilidade]

def buscar_ativo(codigo_busca):
    for ativo in ativos:
        if ativo[0] == codigo_busca:
            return ativo
    return None

def analisar_carteira():
    if len(ativos) == 0:
        print("Nenhum ativo cadastrado")
    else:
        print(f"Analisando {len(ativos)} ativos...")
        
        resultados = []
        lucros = []
        
        for ativo in ativos:
            resultado = calcular_resultado(ativo, False)
            resultados.append(resultado)
            lucros.append(resultado[2])
            
        maior_lucro = max(lucros)
        
        for ativo in ativos:
            resultado = calcular_resultado(ativo, False)

            if resultado[2] == maior_lucro:
                print("Ativo com maior lucro:", ativo[0])
        
opcao = 0

while opcao != 6:
    mostrar_menu()
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        cadastrar_ativo()
    elif opcao == 2:
        visualizar_ativos()
    elif opcao == 3:
        consultar_ativos()
    elif opcao == 4:
        codigo_busca = input("Digite o código do ativo: ").upper()
        ativo = buscar_ativo(codigo_busca)
        if ativo is None:
            print("Ativo não encontrado.")
        else:
            resultado = calcular_resultado(ativo)
    elif opcao == 5:
        analisar_carteira()
            
    else:  
        print("opção invalida")
        

        

    
    
    
    
        
    
    
