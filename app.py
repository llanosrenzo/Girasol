from flask import Flask, render_template
from turtle import *
import os
from math import *

app = Flask(__name__)

@app.route('/')
def index():
    # Código para crear el girasol
    # Aquí va tu código de turtle
    # Guarda la imagen como un archivo
    setup(width=800, height=600)
    speed(0)
    bgcolor('black')
    goto(0,-40)
    name = input('Ingrese tu nombre :').upper()
    # Dibujo de los pétalos
    for i in range(16):
        for j in range(18):
            color('#FFA216')
            rt(90)
            circle(150 - j * 6, 90)
            lt(90)
            circle(150 - j * 6, 90)
            rt(180)
        circle(40, 24)

    # Dibujo del centro del girasol
    color('black')
    shape('circle')
    shapesize(0.5)
    fillcolor('#BB4513')

    # Dibujo de las semillas en espiral
    golden_ang = 137.508
    phi = golden_ang * (pi / 180)

    for i in range(140):
        r = 4 * sqrt(i)
        theta = i * phi
        x = r * cos(theta)
        y = r * sin(theta)
        penup()
        goto(x, y)
        setheading(i * golden_ang)
        pendown()
        stamp()

    # Dibujo de la palabra "AMISTAD"
    # Función para dibujar la palabra "AMISTAD"
    def draw_text(x, y):
        penup()
        goto(x, y + 45)
        pendown()
        color('white')
        write(str("Feliz Día ") + name, align="center", font=("Arial", 20, "bold"))
    
    # Llamada a las funciones de dibujo
    draw_text(0, -50)  # Posición de la palabra
    
    # Mantener la ventana abierta
    done()
    
    return "Dibujo completo"

if __name__ == '__main__':
    app.run(debug=True)
