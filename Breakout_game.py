import turtle
from turtle import *
import random
import time
import math
def get_random_directions():
    angle = random.random()* -1 * math.pi
    length = 5
    dx = math.sin(angle) * length
    dy = math.cos(angle) * length * -1

    return dx, dy

def init_blocks():
    x_list = [-340, -230, -120, -10, 100, 210, 320]
    y_list = [280, 255, 230, 205, 180, 155, 130]
    colors = ['red', 'blue', 'green', 'cyan', 'purple','yellow', 'orange']
    blocks=[]
    for x in x_list:
        for y in y_list:
            b = Turtle()
            b.shape('square')
            b.shapesize(stretch_len=5, stretch_wid=1)
            b.color(random.choice(colors))
            b.up()
            b.goto(x,y)
            blocks.append(b)

    return blocks

def init_game():
    win=Screen()
    win.setup(width=800, height=600)
    win.bgcolor('black')
    win.tracer(0)
    win.title('Breakout Game')
    win.listen()
    win.onkey(paddle_right, 'Right')
    win.onkey(paddle_left, 'Left')

    paddle = turtle.Turtle()
    paddle.shape('square')
    paddle.shapesize(stretch_len=5, stretch_wid=1)
    paddle.color('white')
    paddle.up()
    paddle.goto(0,-270)
    
    ball=turtle.Turtle()
    ball.shape('circle')
    ball.color('white')

    ball.dx, ball.dy = get_random_directions()

    ball.up()
    blocks = init_blocks()
    return win, paddle, ball, blocks, pen

def move_ball(b):
    x,y=b.pos()
    b.setpos(x+b.dx, y+b.dy)

def paddle_right():
    x,y= paddle.pos()
    if x<350:
        paddle.setpos(x+80,y)

def paddle_left():
    x,y= paddle.pos()
    if x> -350:
        paddle.setpos(x-80,y)

def check_paddle(paddle, ball):
    px, py = paddle.pos()
    bx, by = ball.pos()
    if by-10 <= py+10 and by-10>=py-10:
        if bx-10 <= px+50 and bx+10>=px-50:
            ball.dy *= -1

def border_check(ball):
    if ball.ycor()>280:
        ball.dy *= -1
    if ball.xcor()>380 or ball.xcor()< -380:
        ball.dx *=-1

def is_close(block, ball):
    blockx, blocky = block.pos()
    ballx, bally = ball.pos()
    if (blockx-50<=ballx <= blockx+50) and (blocky-10<=bally<=blocky+10):
        return True
    return False


def check_blocks(blocks, ball, score, pen):
    for b in blocks:
        if is_close(b,ball):
            b.hideturtle()
            b.goto(-1000,1000)
            pen.clear()
            pen.write(f'score: {score} ', align='center', font=('Courier', 24 , 'normal') )
    return score

def check_game_over(ball):
    _,y= ball.pos()
    if y<-400 or len(blocks)==0 :
        pen.clear()
        pen.goto(0,0)
        pen.write(f'Game Over\nscore : {score}', align='center', font=('Courier', 24 , 'normal'))
        return True
    return False


win, paddle, ball, blocks, pen = init_game()

score=0
is_game_over = False
while not is_game_over:
    is_game_over = check_game_over(ball)
    time.sleep(0.02)
    win.update()
    move_ball(ball)
    border_check(ball)
    check_paddle(paddle,ball)
    score = check_blocks(blocks, ball, score, pen)
done()