from flask import Flask, render_template, request, send_file
from turtle import *
import math 
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name'].upper()
        draw_sunflower(name)
        return send_file('girasol.png', mimetype='image/png')

    return render_template('index.html')

def draw_sunflower(name):
    setup(width=800, height=600)
    speed(0)
    bgcolor('black')
    goto(0, -40)

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
    phi = golden_ang * (math.pi/ 180)

    for i in range(140):
        r = 4 * math.sqrt(i)
        theta = i * phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        penup()
        goto(x, y)
        setheading(i * golden_ang)
        pendown()
        stamp()

    # Dibujo de la palabra "Feliz Día {nombre}"
    penup()
    goto(0, -50)
    pendown()
    color('white')
    write(f"Feliz Día {name}", align="center", font=("Arial", 20, "bold"))

    # Guardar la imagen
    getscreen().getcanvas().postscript(file="girasol.eps")
    os.system("convert girasol.eps girasol.png")  # Requiere ImageMagick

    done()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
