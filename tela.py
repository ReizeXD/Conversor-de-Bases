import customtkinter
from tkinter import *
import tkinter as tk
from CTkMessagebox import CTkMessagebox

from principal import *

#VARIÁVEIS
teste=''
is_inteiro=True
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10= "#146C94"   # azul

root=customtkinter.CTk()

class validation():
    def validade_Entry(self,text):
            if text=="":return True
            try:
                value=int(text)
            except ValueError:
                return False
            return 1<=value<=36
    
class conversor_de_bases(validation):
    def __init__(self):
        self.root=root
        self.valide_entradas()
        self.tela()
        self.frames_de_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        customtkinter.set_appearance_mode("dark")
        root.mainloop()
    
    def tela(self):
        self.root.title("Conversor de Bases")
        self.root.configure(background="white")
        self.root.geometry("500x300")
        self.root.resizable(False,False)
    
    def frames_de_tela(self):
        self.frame_1=customtkinter.CTkFrame(self.root,bg_color=co6,fg_color=co0, 
                                            corner_radius=15,border_width=2,border_color=co6)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.3)
     
        self.frame_2=customtkinter.CTkFrame(self.root,bg_color=co6,fg_color=co0, 
                                            corner_radius=15,border_width=2,border_color=co6)
        self.frame_2.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.6)

    def widgets_frame1(self):
        global inteiro
        #FUNÇÃO SOBRE
        def switch():       
            global is_inteiro
            if is_inteiro: 
                is_inteiro = False
                self.numero.destroy()
            else: 
                is_inteiro = True
                self.numeroint.destroy()
                self.numerofloat.destroy()
                self.virgula.destroy()
            self.widgets_frame2()
        
        self.modo=customtkinter.CTkLabel(self.frame_1,text="Conversor de Bases",anchor=NW,
                                         font=("Cooper Black", 40, "underline", "bold"),justify=CENTER)
        self.modo.place(relx=0.07, rely=0.05)
        
        self.inteiro_button =customtkinter.CTkSwitch(self.frame_1, command = switch,text="Modo Número Real")
        self.inteiro_button.place(relx=0.39, rely=0.58, relheight=0.4)

    def widgets_frame2(self):
        #FUNÇÃO INSERIR NA ENTRY
        def inserir():
            global teste
           
            baseini=self.baseini.get()
            basefinal=self.basefinal.get()
            if baseini=="1" or basefinal=="1":
                CTkMessagebox(title="Error", message='Não é possivel utilizar 1 como base!'
                    , icon="cancel")
            else:
                if is_inteiro==True:
                    numero=self.numero.get().upper()
                    if numero=="" and baseini=="" or basefinal=="" :
                        CTkMessagebox(title="Error", message='Preencha todos os campos!'
                    , icon="cancel")
                    else:
                        baseini=int(baseini)
                        basefinal=int(basefinal)
                        chamar=main_inteiro(numero,baseini,basefinal)
                        if chamar==False:
                            CTkMessagebox(title="Error", message="Esse número não é compaivel com a respectiva base!"
                            , icon="cancel")
                        else:
                            teste=chamar
                            self.resultentry.delete(0,END)
                            self.resultentry.insert(END,teste)
                else:
                    numeroint=self.numeroint.get().upper()
                    numerodec=self.numerofloat.get().upper()
                    if numeroint=="" or numerodec=="" or baseini=="" or basefinal=="" :
                        CTkMessagebox(title="Error", message='Preencha todos os campos'
                    , icon="cancel")
                    else:
                        baseini=int(baseini)
                        basefinal=int(basefinal)
                        chamar1=main_inteiro(numeroint,baseini,basefinal)
                        chamar2=main_reais(numerodec,baseini,basefinal)
                        chamar=str(chamar1)+","+str(chamar2)
                        if chamar1==False or chamar1==False:
                            CTkMessagebox(title="Error", message="Esse número não é compaivel com a respectiva base!"
                        , icon="cancel")
                        else:
                            teste=chamar
                            self.resultentry.delete(0,END)
                            self.resultentry.insert(END,teste)
        #FUNÇÃO SOBRE
        def sobre():
            Help=customtkinter.CTk()
            Help.title("Sobre o projeto:")
            Help.geometry("450x300")
            Help.configure(background=co0)
            Help.resizable(width=FALSE, height=FALSE)

            texto="Universidade Federal de Alagoas-UFAL\n\nProjeto Conversor de Bases\n\nDisciplina: Introdução a Ciência da Computação (ICC)\n\n\n\n\n\n\nAnderson da Silva Passos"
            canvas=customtkinter.CTkCanvas(Help, width= 500, height= 350, bg=co0)
            canvas.create_text(220, 130, text=texto, fill=co1, font=('Helvetica 10 bold'))
            canvas.pack() 
            Help.mainloop()
        #BASES              
        self.baseini=customtkinter.CTkEntry(self.frame_2,placeholder_text="Base Inicial",
                                              placeholder_text_color=co1, justify=CENTER)
        self.baseini.place(x=60,y=20)
        self.baseini.configure(validate="key", validatecommand=(self.validade,'%P'))
        self.basefinal=customtkinter.CTkEntry(self.frame_2, placeholder_text="Base Final",
                                              placeholder_text_color=co1,justify=CENTER)
        self.basefinal.place(x=60,y=80)
        self.basefinal.configure(validate="key", validatecommand=(self.validade,'%P'))
        
        #NUMERO
        if is_inteiro==True:
            self.numero=customtkinter.CTkEntry(self.frame_2, placeholder_text="Número",
                                                placeholder_text_color=co1,justify=CENTER)
            self.numero.place(x=270,y=20)
        else:
            self.numero.destroy()
            self.numeroint=customtkinter.CTkEntry(self.frame_2, placeholder_text="Inteiro",
                                                placeholder_text_color=co1,justify=CENTER)
            self.numeroint.place(x=270,y=20,relwidth=0.13)
            self.virgula=customtkinter.CTkLabel(self.frame_2,justify=CENTER, text=",",
                                                font=("Cooper Black", 15, "bold"))
            self.virgula.place(x=338,y=20)
            self.numerofloat=customtkinter.CTkEntry(self.frame_2, placeholder_text="Decimal",
                                                placeholder_text_color=co1,justify=CENTER)
            self.numerofloat.place(x=350,y=20,relwidth=0.13)


        #RESULTADO
        self.resultado=customtkinter.CTkLabel(self.frame_2,text="Resultado",anchor=NW,
                                              font=("Arial",15),justify=CENTER)
        self.resultado.place(x=310,y=58)
        self.resultentry=customtkinter.CTkEntry(self.frame_2,justify=CENTER)
        self.resultentry.delete(0,END)
        self.resultentry.insert(END,teste)
        self.resultentry.place(x=270,y=80)
        #BOTÃO CONVERTER
        self.converter=customtkinter.CTkButton(self.frame_2,text="Converter", command=inserir)
        self.converter.place(x=170,y=130)
        #BOTÃO SOBRE
        self.help=customtkinter.CTkButton(self.frame_2,text="?", command=sobre)
        self.help.place(x=450,y=160,relwidth=0.05, relheight=0.08)
    
    def valide_entradas(self):
        self.validade=self.root.register(self.validade_Entry)
    
conversor_de_bases()  



