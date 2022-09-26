 #Melvin Josue Perez Garcia 
 #Jaime Arnoldo Rodriguez Meza
from bdb import effective
from msilib.schema import RadioButton

from tkinter import messagebox
from tkinter.ttk import Combobox
import tkinter
def boton():
    if caja1.get()=="" or caja2.get()==""or box.get()=="":
        messagebox.showerror("Cajero manco.:V ","Por favor complete los campos requeridos.")
    else:
        cantidad = int(caja2.get())
        precio = float(caja1.get())
        metopago = box.get()
        subtotal = precio*cantidad
        if metopago=="Tarjeta":
            descuento=subtotal*0.20
            total=subtotal-descuento
            messagebox.showinfo("Cajero manco","El precio del producto es: "+str(precio)+" La cantidad de producto es: "+str(cantidad)+" El metodo de pago es con tarjeta, El Descuento es del 20%, El total es: "+ str(total))
        elif metopago=="Efectivo" and subtotal<20:
            total=subtotal
            messagebox.showinfo("Cajero manco","El precio del producto es: "+str(precio)+" La cantidad de producto es: "+str(cantidad)+" El metodo de pago es en efectivo, No aplica descuento, El total es: "+ str(total))
        else:
            descuento=subtotal*0.10
            total=subtotal-descuento
            messagebox.showinfo("Cajero manco","El precio del producto es: "+str(precio)+" La cantidad de producto es: "+str(cantidad)+" El metodo de pago es en efectivo, El descuento es del 10%, El total es: "+ str(total))
        
ventana = tkinter.Tk ( )
ventana.geometry (  "300x300"  )
ventana.configure(background="black")

etiqueta = tkinter.Label ( ventana , text = " Cajero Manco ",bg="black",fg="white" )
etiqueta.pack ( )
etiqueta2= tkinter.Label ( ventana , text = "Ingrese el precio del producto.",bg="black",fg="white" )
etiqueta2.pack ( )
caja1=tkinter.Entry(ventana)
caja1.pack()
etiqueta3= tkinter.Label ( ventana , text = "Ingrese La cantidad de producto.",bg="black",fg="white" )
etiqueta3.pack ( )
caja2=tkinter.Entry(ventana)
caja2.pack()
etiqueta4= tkinter.Label ( ventana , text = "Seleccione metodo de pago.",bg="black",fg="white" )
etiqueta4.pack ( )
box=Combobox(ventana,state="readonly")
box["values"]=("Tarjeta","Efectivo")
box.pack()
boton1=tkinter.Button ( ventana , text = "Comprar" ,command=boton,bg="gray",fg="white" )
boton1.pack()



ventana.mainloop ( )