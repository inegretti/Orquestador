from tkinter import *
from Orquestador import *

orq = Orquestador()
ventana = Tk()
ventana.geometry("600x500")
ventana.configure(bg='#FF8904')
ventana.title("ORQUESTADOR")

etiqueta1 = Label(text="Pregunta:")
etiqueta1.configure(bg='#FF8904')
etiqueta1.place(x=20, y=15)

text_widget = Text(ventana, height=6, width=70)
text_widget.place(x=20, y=40)
text_widget.insert(END,"Ingresa aqui tu pregunta")

var1 = IntVar()
checkB = Checkbutton(ventana, text="Revision cruzada", variable=var1)
checkB.place(x=120, y=150)

etiqueta2 = Label(text="Respuesta:")
etiqueta2.configure(bg='#FF8904')
etiqueta2.place(x=20, y=190)

text_widget2 = Text(ventana, height=12, width=70)
text_widget2.place(x=20, y=220)

text_widget2.insert(END,"Respuesta del Orquestador")

def preguntar(): 
    val = text_widget.get("1.0", END).strip()
    try:
        if var1.get() == 0:
            text_widget2.delete("1.0", END)
            res = orq.consulta(val)
            text_widget2.insert(END,res)       
            if val != "Ingresa aqui tu pregunta" and val != "":
                text_widget2.delete("1.0", END)
                res = orq.consulta(val)
                text_widget2.insert(END,res)
            else:
                text_widget2.delete("1.0", END)
                text_widget2.insert(END,"debes ingresar una pregunta y no dejar el espacio en blanco")
        else:
            res=orq.revision_cruzada(val)
            text_widget2.delete("1.0", END)
            text_widget2.insert(END,res)
    except Exception as e:
        text_widget2.delete("1.0", END)
        text_widget2.insert(END,"Ocurrio un error al procesar la pregunta: "+str(e))
            

boton2 = Button(text="Preguntar", command=lambda: preguntar())
boton2.place(x=20, y=150)

ventana.mainloop()