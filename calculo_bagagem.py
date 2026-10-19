#Uma companhia aérea permite que seus clientes do tpo premium despachem bagagens de até 32 kg sem nenhum custo adicional, enquanto os clientes do tipo gold podem levar malas de até 28kg sem nenhm custo adicional e todos os demais devem pagar por qualquer bagagem despachada.

tipo_cliente = input("Informe o tipo de cliente: PREMIUM, GOLD, OU REGULAR ")
peso_bagagem = float(input("Informe o peso da bagagem em kg: "))

if tipo_cliente.upper() == "PREMIUM":
    #O QUE ACONTECE SE O CLIENTE FOR PREMIUM
    if peso_bagagem <= 32:
        #EXIBIR MENSAGEM AVISANDO QUE O CLIENTE PODE DESPACHAR A BAGAGEM SEM CUSTO ADICIONAL
        print(
            f"Cliente {tipo_cliente}, sua bagagem esta autorizada para despacho sem custo adicional.")
        
    else:
        peso_excedente = peso_bagagem - 32
        #EXIBIR MENSAGEM AVISANDO O CLIENTE SOBRE O PESO EXCEDENTE
        print(
            f"Cliente {tipo_cliente}, têm direito a despacharem bagagens até 32kg. A bagagem atual execede este peso em {peso_excedente} kg. Favor dirigir-se ao balcão de check-in para verificar o valor a ser pago pela bagagem.")
elif tipo_cliente.upper() == "GOLD":
    #O QUE ACONTECE SE O CLIENTE FOR GOLD
    if peso_bagagem <= 28:
        #EXIBIR MENSAGEM AVISANDO QUE PODE LEVAR A BAGAGEM
        print(
            f"Cliente {tipo_cliente}, sua bagagem está dentro do limite permitido de 28kg e está autorizada para despacho sem custo adicional.")
    else:
        peso_excedente = peso_bagagem - 28
        #EXIBIR MENSAGEM AVISANDO SOBRE O PESO EXCEDENTE
        print(
                f"Cliente {tipo_cliente} têm direito a despacharem bagagens de até 28kg. A bagagem atual excede este peso em {peso_excedente}kg. Favor dirigir-se ao balcão de check-in para verificar o valor a ser pago pela bagagem.")
else:
    #SE O CLIENTE FOR DO TIPO REGULAR, ELE SEMPRE TERÁ QUE PAGAR PELA BAGAGEM DESPACHADA
    print(
        f"Cliente do tipo {tipo_cliente}, não tem direito a bagagem gratuita. Favor dirigir-se ao balcão de check-in para verificar o valor a ser pago pela bagagem.")
    