#ingenieria en sistemas
#primer semestre
#christian ivan rivera marroquin
#carne: 0907-19-14757

from tkinter import*
raiz=Tk()
miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#---------------- aca son las ventanas donde se teclea------------

cuadrouno=Entry(miFrame)
cuadrouno.grid(row=0, column=1)

cuadrodos=Entry(miFrame)
cuadrodos.grid(row=2, column=1)

cuadroresultado=Entry(miFrame)
cuadroresultado.grid(row=3, column=1)

#-------------




raiz.mainloop()