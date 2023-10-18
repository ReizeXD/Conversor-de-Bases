dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def qualquer_dez(n,base_qualquer_origem):
    decimal=0
    numero=list(str(n))
    numero.reverse()
    contador=0
    for x in numero:
        decimal=decimal+(dic.index(x)*(base_qualquer_origem**contador))
        contador+=1
    return decimal

def limpar_lista():
    global lista
    lista=[]
        
lista=[]
def dez_qualquer(n,base_qualquer_destino):
    n=int(n)
    if n>=base_qualquer_destino:
        resto=n%base_qualquer_destino
        n=n//base_qualquer_destino
        dez_qualquer(n,base_qualquer_destino) 
        lista.append(str(resto))
    else:
        lista.append(str(n))
    return lista
    
def converter_letras(lista2,base_qualquer_destino):
    if base_qualquer_destino>10:
        for k,v in enumerate(lista2):
            lista2[k]=dic[int(v)]
    return lista2

def ConvertToList(lista1):
    nome=''
    for c in lista1:
        nome+=str(c)+''
    return nome

def Verificar_elementos(n,base1):
    condicao=True
    verificar=[]
    n=str(n)
    for elementos in range(base1):
        verificar.append(dic[elementos])
    for string in n:
        if not string in verificar:
            condicao=False
            break
    return condicao
def dez_qualquer_fracionado(n,base_qualquer_destino):
    n=str(n)
    algarismos=len(n)
    agora=0
    casas=[]
    n=int(n)/10**algarismos
    for vez in range(4):
        if vez==0:
            agora=n
            continue
        else:
            mult=agora*base_qualquer_destino
            inteira=int(mult//1)
            casas.append(inteira)
            agora=mult-inteira
    return casas


def qualquer_dez_fracionado(n,base_qualquer_origem):
    decimal=0
    numero=str(n)
    contador=-1
    for x in numero:
        decimal=decimal+(dic.index(x)*(base_qualquer_origem**contador))
        contador-=1
    fracao=[]
    decimal=str(decimal)
    contar=len(decimal)
    for c in range(2,contar):
        fracao.append(decimal[c])
    q=''
    for algarismo in fracao:
        q+=algarismo+''
    return q
