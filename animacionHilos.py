from tkinter import *
import random
import threading
import time

WIDTH = 500
HEIGHT = 500
pelotaNo = 0
textoX=60
textoY=0

pelota_width = 30
pelota_height = 30

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg = "light yellow")
canvas.pack()

def lanzarPelota():
    global pelotaNo
    global textoY

    xVelocity = random.randint(2, 15)
    yVelocity = random.randint(2, 15)

    color = "#"+("%06x"%random.randint(0,16777215))
    pelotaNo +=1
    numero = pelotaNo
    textoY += 20
    pelota = canvas.create_oval(0,0,30,30, width=0, fill=color )
    pelotaStatus = canvas.create_text(textoX,textoY, fill = color, text = "pelota "+str(pelotaNo)+" Activa")
    threadStatus = canvas.create_text(textoX+120,textoY, fill = color, text = threading.currentThread().name+" Arrancó")
    canvas.move(pelota, random.randint(0,200), random.randint(0,200))


    for a in range(500):
        coordinates = canvas.coords(pelota)
        print(threading.currentThread())
        if(coordinates[0]>=(WIDTH-pelota_width) or coordinates[0]<0):
            xVelocity = -xVelocity
        if(coordinates[1]>=(HEIGHT-pelota_height) or coordinates[1]<0):
            yVelocity = -yVelocity
        canvas.move(pelota,xVelocity,yVelocity)
        canvas.update()
        time.sleep(0.01)
    canvas.itemconfig(pelota, state = 'hidden')
    canvas.itemconfig(pelotaStatus,text = "pelota "+str(numero)+" inactiva")
    canvas.itemconfig(threadStatus,text = threading.currentThread().name+" terminó")


def arrancar():
   threading.Thread(target=lanzarPelota).start()

boton = Button(text="Lanzar", command=arrancar)
boton.place(x=200, y=450)

window.mainloop()