#ingenieria en sistemas
#primer semestre
#christian ivan rivera marroquin
#carne: 0907-19-14757



#----------- no funciono de la forma que pense hacerlo :( espero llegar a ganar GG


from tkinter import*
raiz=Tk()
miFrame=Frame(raiz, width=1200, height=600)

miFrame.pack()

operacion=""

#-----------------funcion multiplicar---------
def multiplicar():
    global operacion
    operacion="multiplicacion"

#---------------- aca son las ventanas donde se teclea------------

cuadrouno=Entry(miFrame)
cuadrouno.grid(row=0, column=1)

cuadrodos=Entry(miFrame)
cuadrodos.grid(row=1, column=1)

cuadrotres=Entry(miFrame)
cuadrotres.grid(row=2, column=1)

cuadroresultado=Entry(miFrame)
cuadroresultado.grid(row=3, column=1)

#-------------aca se agregara los cuadros de texto---------
cuadrouno=Label(miFrame, text="coloca el primer numero")
cuadrouno.grid(row=0, column=0)

cuadrodos=Label(miFrame, text="coloca el segundo numero" )
cuadrodos.grid(row=1, column=0)

cuadrotres=Label(miFrame, text='coloque terer dato ')
cuadrotres.grid(row=2, column=0)

cuadroresultado=Label(miFrame, text="resulado final")
cuadroresultado.grid(row=3, column=0)

#-----------los botones------------
boton1=Button(miFrame, text= "validacion", command=lambda:multiplicar()) #validar
boton1.grid(row=4, column=1,)

boton2=Button(miFrame, text="ejecucion")#ejecuta las funcion
boton2.grid(row=5, column=1)




raiz.mainloop()