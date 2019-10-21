
from tkinter import *
from tkinter.ttk import Combobox
import re
from tkinter import messagebox

v = Tk()

Label(v, text="Escala origen").grid(row=0, column=0)
Label(v, text="Cantidad").grid(row=1, column=0)
Label(v, text="Escala destino").grid(row=2, column=0)

cmbEO = Combobox(v)
cmbEO["values"]=["Kelvin", "Celsius", "Fahrenheit", "Reaumur"]
cmbEO.grid(row=0, column=1)

cmbED = Combobox(v)
cmbED["values"]=["Kelvin", "Celsius", "Fahrenheit", "Reaumur"]
cmbED.grid(row=2, column=1)

txtGO = Entry(v, width=10)
txtGO.grid(row=1, column=1)

txtGD = Entry(v, width=10)
txtGD.grid(row=3, column=1)
txtGD.configure(state=DISABLED)

def ConvertirTemperatura():
    #validaciones
    if cmbEO.current()>=0 and cmbED.current()>=0 and \
    re.match("^[-]?[0-9]+[.]?[0-9]*$", txtGO.get()):
        #leer datos de entrada
        go = float(txtGO.get())
        eo = cmbEO.current()
        ed = cmbED.current()

        #proceso
        if eo!= ed:
            if eo == 0:
                #desde kelvin
                if ed ==1:
                    #Hacia CELSIUS
                    gd = go - 273
                elif ed ==2:
                    #Hacia FAHRE
                    gd = go * 1.8-459.67
                else:
                    #Hacia REAUMUR
                    gd = (go-273.15)*0.8
                    


            elif eo ==1:
                #desde CELSIUS
                if ed ==0:
                    #Hacia KElVIN
                    gd = go + 273
                elif ed ==2:
                    #Hacia FAHRE
                    gd = go * 1.8+32
                else:
                    #Hacia REAUMUR
                    gd = go*0.8
                    


            elif eo ==2:
                #desde FAHRENHELT
                if ed ==0:
                    #Hacia KElVIN
                    gd = (go+459)*5/9
                elif ed ==1:
                    #Hacia CELSIUS
                    gd = (go-32)*5/9
                else:
                    #Hacia REAUMUR
                    gd = (go-32)*4/9


            else:
                #desde REAUMUR
                if ed ==0:
                    #Hacia KElVIN
                    gd = go*1.25+273
                elif ed ==1:
                    #Hacia CELSIUS
                    gd = go*1.25
                else:
                    #Hacia FAHRE
                    gd = go*2.25+32
            #mostrat el resultado
            txtGD.configure(state=NORMAL)
            txtGD.delete(0, END)
            txtGD.insert(0,gd)
            txtGD.configure(state=DISABLED)



        else:
            messagebox.showerror("","la escala debe ser diferente")


    else:
        messagebox.showerror("","Faltan datos o no son validos")


Button(v, text="Convertir", command=ConvertirTemperatura).grid(row=3, column=0)


