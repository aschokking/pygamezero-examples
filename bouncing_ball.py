ball = Actor('ball')
ball.dx = 10
ball.dy = 5

def draw():
    screen.clear()
    ball.draw()

def update():
    ball.x += ball.dx
    if ball.right > screen.width or ball.left < 0:
        ball.dx *= -1
    ball.y += ball.dy
    if ball.bottom > screen.height or ball.top < 0:
        ball.dy *= -1