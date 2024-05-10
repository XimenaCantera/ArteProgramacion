# Importar solo los nombres que se necesita de "turtle"
import turtle
from random import choice, random
from freegames import vector


def value():
    """Generar un valor aleatoriamente entre (-5, -3) o (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


# Inicializar las variables
ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}


def move(player, change):
    """Mover la posición del jugador por cambio."""
    state[player] += change


def rectangle(x, y, width, height):
    """Dibujar un rectángulo en las coordenadas (x, y) con datos dados"""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw():
    """Dibujar el juego y mueve la  pelota de Ping Pong."""
    turtle.clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    turtle.up()
    turtle.goto(x, y)
    # Dibujar la pelota
    turtle.dot(10)
    turtle.update()

    # Revisa los límites del tablero y rebota la pelota al llegar al límite.
    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        # Rebota la pelota si toca la "paleta" del jugador 1
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        # Rebota la pelota si toca la "paleta" del jugador 2
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    turtle.ontimer(draw, 50)


# Configuración inicial de la ventana de Turtle
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()

# Asigna las teclas para mover a los jugadores.
turtle.onkey(lambda: move(1, 20), 'w')
turtle.onkey(lambda: move(1, -20), 's')
turtle.onkey(lambda: move(2, 20), 'i')
turtle.onkey(lambda: move(2, -20), 'k')

# Dibuja el juego.
draw()

# Finaliza el programa cuando se cierre la ventana.
turtle.done()
