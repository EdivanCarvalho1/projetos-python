saldo = 2000;
limite_saque = 500;
qntd_saques = 3;

def sacar (valor, limite_saque, qnt_saques):
    global saldo;
    if (valor > saldo):
        print ("Saldo insuficiente");
    elif(valor >)
    else:
        saldo -= valor;
        print ("Saque realizado");
        print (f"Saldo atual: {saldo}");
        
def depositar (valor):
    global saldo;
    saldo += valor;
    print ("Deposito realizado");
    print (f"Saldo atual: {saldo}");
    
def extrato ():
    print (f"Saldo atual: {saldo}");
    
    
while True:
    print ("O que deseja fazer?");
    print ("[1] Sacar");
    print ("[2] Depositar");
    print ("[3] Extrato");
    print ("[4] Sair");
    opcao = int(input());
    if (opcao == 1):
        valor = float(input("Valor a ser sacado: "));
        sacar (valor, limite_saque, qntd_saques);
    elif (opcao == 2):
        valor = float(input("Valor a ser depositado: "));
        depositar (valor);
    elif (opcao == 3):
        extrato ();
    elif (opcao == 4):
        break;
    else:
        print ("Opção inválida");  