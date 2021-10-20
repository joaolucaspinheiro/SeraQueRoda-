from tkinter import *
import tkinter
from typing import Sized
import psutil
import tkinter.font as tkFont
import tkinter as tk
import platform

sistema = (platform.system())
versao = (platform.release())
ram = psutil.virtual_memory()
disco = psutil.disk_usage('/')

print(psutil.disk_partitions)
TRDISCO = disco.total/(1024**3)
ramconvertida = ram.total/(1024**3)
app = Tk()
app.title("Será que roda?")
app.geometry("1360x768")
app.configure(background= "#0c343d")

## Exibindo Titulo
mostrarTitulo = Label(app,borderwidth= 6, width= 40, relief="groove", text="Vamos checar a configuração da sua maquina gamer???",foreground="#000000", background="#eeeeee", font=("Gabriola", 20, "bold"))
mostrarTitulo.place(x= 175, y= 0, width=1000, height= 45)
##Introdução sobre a Ram
mostrarRam=Label(borderwidth  = 3,width = 40, relief="sunken", text=" Sua memoria ram tem um total de: ", foreground="#000000", background="#eeeeee", font="Bahnschrift" )
mostrarRam.place(x=0, y= 100, width=450, height= 35)
#Mostrando valores da Ram
mostrarValoresRam = Label(borderwidth  = 2,width = 40, relief="sunken", text="" + str(ramconvertida) + " GB", foreground="#00008B", background="#eeeeee", font = "Bahnschrift")
mostrarValoresRam.place (x= 450, y=100,width=250, height= 35)
## Introdução sobre SO
mostrarSO = Label(borderwidth  = 3,width = 40, relief="sunken", text= "O Sistema operacional que você usa é o: ", foreground="#000000", background="#eeeeee", font="Bahnschrift")
mostrarSO.place(x=0, y=150, width=450, height= 35)
##Mostrando qual é o SO
mostrarQualSO = Label(borderwidth= 3, width= 40, relief= "sunken", text="" + str(sistema), foreground="#00008B", background="#eeeeee", font="Bahnschrift" )
mostrarQualSO.place(x=450, y=150, width=250, height= 35)
##Introdução sobre qual versão o sistema operacional está
mostrarVersaoSO = Label(borderwidth= 3, width= 40, relief= "sunken", text= "A versão do seu SO é: ", foreground="#000000", background="#eeeeee", font="Bahnschrift" )
mostrarVersaoSO.place(x=0, y= 200, width=450, height= 35)
##Mostrando qual a versão do so
mostrarQualversaoSO = Label(borderwidth= 3, width= 40, relief= "sunken", text= "" +str(versao), foreground="#00008B", background="#eeeeee", font="Bahnschrift" )
mostrarQualversaoSO.place(x=450, y= 200, width=250, height= 35)
#Introdução sobre espaço em disco 
mostrarDisco=Label(borderwidth  = 3,width = 40, relief="sunken", text="Seu disco principal tem: ", foreground="#000000", background="#eeeeee", font = "Bahnschrift")
mostrarDisco.place(x=0, y=250, width=450, height=35)
#Mostrando espaço em disco
mostrarTotalDisco = Label (borderwidth= 3, width= 40, relief= "sunken", text= "" + str(TRDISCO) +" GB ", foreground="#00008B", background="#eeeeee", font="Bahnschrift")
mostrarTotalDisco.place(x=450, y= 250, width=250, height= 35)
app.mainloop()


