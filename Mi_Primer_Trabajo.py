from tkinter import *
import random

# -------------------
# variables globales
# -------------------
BASE = 400
ALTURA = 200
radio = 20
desplazamiento_x = 2
desplazamiento_y = 2
intervalo = 3

centro_x = random.randint(radio, BASE)
centro_y = random.randint(radio, ALTURA)

def mover_carro():
    global desplazamiento_x, desplazamiento_y
    
    x0, y0, x1, y1 = c.coords(mover_carro)
    if x0 < 0 or x1 > BASE: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or y1 > ALTURA: 
        desplazamiento_y = -desplazamiento_y
    c.move(mover_carro, desplazamiento_x, desplazamiento_y)
    ventana_principal.after(intervalo, mover_carro)

# -------------------
# ventana principal
# -------------------
ventana_principal = Tk()
ventana_principal.title("Mi Primer Juego")
ventana_principal.resizable(False, False)
ventana_principal.geometry("900x900")
ventana_principal.config(bg="white")

# -------------------
# frame de graficacion
# -------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="slate blue", width=480, height=240)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

#dibujar una linea rectangulo
linea_1 = c.create_rectangle(BASE/2, ALTURA/2, BASE,2, fill="grey", width=2)
linea_2 = c.create_rectangle(BASE, ALTURA, BASE/2, ALTURA/2, fill="grey", width=2)
linea_3 = c.create_rectangle(4, ALTURA, BASE/2, ALTURA/2, fill="grey", width=2)
linea_4 = c.create_rectangle(6, 2, BASE/2, ALTURA/2, fill="grey", width=2)


texto_1 = c.create_text(BASE/2, ALTURA/2, anchor="center", text="salida!!", font=("Arial", 15, "bold"), fill="blue1", activefill="yellow")
texto_2 = c.create_text(3*BASE/4, ALTURA/2, anchor="center", text="llegada!", font=("Arial", 15, "bold"), fill="orange", activefill="yellow")

# dibujar rectangulo
rect_1 = c.create_rectangle(BASE/2,ALTURA/2,BASE,ALTURA,fill="pink",outline="orange")

# -------------------
# frame de controles
# -------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="pink", width=480, height=230)
frame_controles.place(x=10,y=260)

