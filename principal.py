from conversor import *



def main_inteiro(n,base1,base2):
    lista=[]
    condicao=Verificar_elementos(n,base1)
    if condicao==True:
        if base1==10:
            lista=dez_qualquer(n,base2)
            converter=converter_letras(lista,base2)
            convert=ConvertToStr(converter)
            limpar_lista()
            return convert
        elif base2==10:
            return qualquer_dez(n,base1)
        else:
            primeiro=qualquer_dez(n,base1)
            segundo=dez_qualquer(primeiro,base2)
            limpar_lista()
            return ConvertToStr(converter_letras(segundo,base2))
    else:
        return condicao
    
def main_reais(n,base1,base2):
    lista=[]
    condicao=Verificar_elementos(n,base1)
    if condicao==True:
        if base1==10:
            lista=dez_qualquer_fracionado(n,base2)
            limpar_lista()
            return ConvertToStr(converter_letras(lista,base2))
        elif base2==10:
            return qualquer_dez_fracionado(n,base1)
        else:
            primeiro=qualquer_dez_fracionado(n,base1)
            segundo=dez_qualquer_fracionado(primeiro,base2)
            limpar_lista()
            return ConvertToStr(converter_letras(segundo,base2))
    else:
        return condicao
