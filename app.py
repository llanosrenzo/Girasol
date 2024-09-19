from flask import Flask, render_template
import turtle
import os
import math

app = Flask(__name__)

@app.route('/')
def index():
    # Código para crear el girasol
    # Aquí va tu código de turtle
    # Guarda la imagen como un archivo
    turtle.setup(width=800, height=600)
    turtle.speed(0)
    turtle.bgcolor('black')
    name = input('Ingrese tu nombre: ').upper()

    # Dibujo de los pétalos
    for i in range(16):
        for j in range(18):
            turtle.color('#FFA216')
            turtle.rt(90)
            turtle.circle(150 - j * 6, 90)
            turtle.lt(90)
            turtle.circle(150 - j * 6, 90)
            turtle.rt(180)
        turtle.circle(40, 24)

    # Dibujo del centro del girasol
    turtle.color('black')
    turtle.shape('circle')
    turtle.shapesize(0.5)
    turtle.fillcolor('#BB4513')

    # Dibujo de las semillas en espiral
    golden_ang = 137.508
    phi = golden_ang * (3.14159 / 180)

    for i in range(140):
        r = 4 * (i ** 0.5)
        theta = i * phi
        x = r * (3.14159 ** 0.5)
        y = r * (3.14159 ** 0.5)
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(i * golden_ang)
        turtle.pendown()
        turtle.stamp()

    # Dibujo de la palabra "AMISTAD"
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.color('white')
    turtle.write(name, align="center", font=("Arial", 24, "bold"))

    # Mantener la ventana abierta
    turtle.done()
    return "Dibujo completo"

if __name__ == '__main__':
    app.run(debug=True)
