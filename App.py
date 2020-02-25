# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:05:18 2020

@author: Miguel
"""

import tkinter as tk

calculadora = tk.Tk();

valor1 = tk.StringVar()


calculadora.title("Calculadora aritmetica")
calculadora.geometry("250x250")
calculadora.configure(background='Dark turquoise')
calculadora.columnconfigure(0, weight=0)
calculadora.columnconfigure(1, weight=1)
calculadora.rowconfigure(2, weight=1)
calculadora.resizable(0, 0)

def set_digito(num):
   valor1.set(valor1.get() + str(num))


def calcular():  
    dato = valor1.get()
    
    resultado = "";
    
    if '+' in dato:
        lista = dato.split("+")
        a = int(lista[0])
        b= int(lista[1])
        resultado = a+b;
        
    elif '-' in dato:
        lista = dato.split("-")
        a = int(lista[0])
        b= int(lista[1])
        resultado = a-b;
    elif '*' in dato:
        lista = dato.split("*")
        a = int(lista[0])
        b= int(lista[1])
        resultado = a*b;
        
    elif '/' in dato:        
        lista = dato.split("/")
        a = int(lista[0])
        b= int(lista[1])
        resultado = a/b;
        
    else:
        pass
    
    valor1.set(str(resultado))

    
    
    


tk.Entry(calculadora, textvariable = valor1, width=36).place(x = 15, y = 40, height=40)




tk.Button(calculadora,text="1",bg= "white",fg="black",command=lambda:set_digito(1)).place(x=15,y=200,width=38 , height=40)
tk.Button(calculadora,text="2",bg= "white",fg="black",command=lambda:set_digito(2)).place(x=59,y=200,width=38 , height=40)
tk.Button(calculadora,text="3",bg= "white",fg="black",command=lambda:set_digito(3)).place(x=103,y=200,width=38 , height=40)
tk.Button(calculadora,text="0",bg= "white",fg="black",command=lambda:set_digito(0)).place(x=147,y=200,width=38 , height=40)
tk.Button(calculadora,text="=",bg= "white",fg="black",command=lambda:calcular()).place(x=191,y=200,width=48 , height=40)

tk.Button(calculadora,text="4",bg= "white",fg="black",command=lambda:set_digito(4)).place(x=15,y=150,width=38 , height=40)
tk.Button(calculadora,text="5",bg= "white",fg="black",command=lambda:set_digito(5)).place(x=59,y=150,width=38 , height=40)
tk.Button(calculadora,text="6",bg= "white",fg="black",command=lambda:set_digito(6)).place(x=103,y=150,width=38 , height=40)
tk.Button(calculadora,text="+",bg= "white",fg="black",command=lambda:set_digito("+")).place(x=147,y=150,width=38 , height=40)
tk.Button(calculadora,text="-",bg= "white",fg="black",command=lambda:set_digito("-")).place(x=191,y=150,width=48 , height=40)

tk.Button(calculadora,text="7",bg= "white",fg="black",command=lambda:set_digito(7)).place(x=15,y=100,width=38 , height=40)
tk.Button(calculadora,text="8",bg= "white",fg="black",command=lambda:set_digito(8)).place(x=59,y=100,width=38 , height=40)
tk.Button(calculadora,text="9",bg= "white",fg="black",command=lambda:set_digito(9)).place(x=103,y=100,width=38 , height=40)
tk.Button(calculadora,text="*",bg= "white",fg="black",command=lambda:set_digito("*")).place(x=147,y=100,width=38 , height=40)
tk.Button(calculadora,text="/",bg= "white",fg="black",command=lambda:set_digito("/")).place(x=191,y=100,width=48 , height=40)






calculadora.mainloop();
