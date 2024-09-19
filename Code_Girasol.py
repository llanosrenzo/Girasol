from turtle import *
from math import *

name = input('Ingrese tu nombre :').upper()
# Configuración inicial
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
golden_ang = 137.508
phi = golden_ang * (pi / 180)

# Dibujo de las semillas en espiral
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

# Función para dibujar un punto
def point(x, y):
    penup()
    goto(x, y)
    pendown()
    color('black')
    fillcolor('#FFA216')
    begin_fill()
    circle(4)
    end_fill()

# Función para dibujar la palabra "AMISTAD"
def draw_text(x, y):
    penup()
    goto(x, y + 45)
    pendown()
    color('white')
    write(name, align="center", font=("Arial", 120, "bold"))

# Llamada a las funciones de dibujo
draw_text(0, -50)  # Posición de la palabra

hideturtle()

# Mantener la ventana abierta
done()
