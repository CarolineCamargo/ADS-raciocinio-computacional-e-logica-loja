
def obter_limite ():
    print ("Olá, meu nome é Caroline de Camargo Flach,\nBem-vindo(a) a minha loja!\n")
    print ("Irei realizar uma análise de crédito para o(a) senhor(a), para isto é necessário que preencha os dados a seguir")
    cargo = input("Digite qual seu cargo na empresa em que trabalha atualmente: ")       
    salário = float(input("Digite qual seu salário: "))
    ano_nasc = int(input ("Digite seu ano de nascimento: "))
    print ("Seu cargo é: ", cargo)
    print ("Seu salário é: R${0:.2f}".format(salário))
    print ("Seu ano de nascimento é: ", ano_nasc)



    import datetime
    now = datetime.datetime.now()
    ano_atual = now.year

    idade = ano_atual - ano_nasc
    print ("Sua idade aproximada é: ", idade)
    limite = float((salário * (idade / 1000)) + 100)
    print ("\nDe acordo com a análise de crédito realizada, seu limite de gasto na loja é de: R${0:.2f}\n".format (limite))

    return limite, idade


def verificar_produto (limite):
    produto = input("Digite o nome do produto que deseja comprar: ")
    preço = float(input("Digite o valor do produto que deseja comprar: "))
    
    porc60 = float(limite * 0.6)
    porc90 = float(limite * 0.9)

    
    if preço <= porc60:
        print ("Liberado!")
    elif porc60 < preço < porc90:
        print ("Liberado ao parcelar em até 2 vezes")
    elif porc90 <= preço <= limite:
        print ("Liberado ao parcelar em 3 ou mais vezes")
    else:
        print("Bloqueado")

    
    print()
    print()

    qtde_nomecompl = "Caroline de Camargo Flach"
    qtde_nome = "Caroline"
    if len(qtde_nomecompl) <= preço <= idade or idade <= preço <= len (qtde_nomecompl):
        print ("Foi liberado um desconto no valor de: R$ {0:.2f}".format (len(qtde_nome)))
        total = preço - len(qtde_nome)
        print ("O valor total do produto com desconto é: R${0:.2f}\n\n".format (total))
        limite = limite - preço + len (qtde_nome)
    else :
        limite = limite - preço

                
  

    return limite


limite, idade = obter_limite()


qtde_produto = int(input("Informe quantos produtos deseja cadastrar: "))
print()

for p in range (qtde_produto):
    if p <= limite :
        limite = verificar_produto(limite)
        if p < limite:
            print ("Seu limite de gasto ainda não foi atingido!\n")
        else:
            print ("Seu limite de gasto foi atingido!")
        

