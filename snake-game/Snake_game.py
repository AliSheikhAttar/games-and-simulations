import turtle
import random
import time





def init_screen():
    game_screen = turtle.Screen()
    game_screen.bgcolor('blue')
    game_screen.setup(width=600, height=600)
    game_screen.tracer(0)
    return game_screen

def snake_food():
    food= turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,90)
    return food

def snake_head():
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"
    return head


def scorre():
    sc = turtle.Turtle()
    sc.speed(0)
    sc.shape("square")
    sc.color("yellow")
    sc.penup()
    sc.hideturtle()
    sc.goto(-290,270)
    sc.write("score: 0", align = "left", font=("ds-digital", 19, "normal"))
    return sc


def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def moving():
    game_screen.listen()
    game_screen.onkeypress(go_up, "Up")
    game_screen.onkeypress(go_down, "Down")
    game_screen.onkeypress(go_left, "Left")
    game_screen.onkeypress(go_right, "Right")

game_screen = init_screen()
head = snake_head()
sc = scorre()
food = snake_food()
moving()
score = 0
body = []
level = 0.1
while True:
    game_screen.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction = "stop"


        for x in body:
            x.goto(500,500) 
        body.clear()

        score = "game over"
        level = 0.1

        sc.goto(0,0)
        sc.penup()
        sc.clear()
        sc.write(" {}".format(score), align="center",font=("ds-digital", 50, "normal"))
        time.sleep(2)
        sc.clear()
        score = 0
        sc.goto(-290, 270)
        sc.write("score: {}".format(score), align="Left",font=("ds-digital", 19, "normal"))
        sc.penup()
        food.goto(0,90)


    if head.distance(food) <21:
        x= random.choice(["red", "purple", "yellow", "black", "green", "white", "cyan"])
        xx = random.randint(-290,290)
        yy = random.randint(-290,290)
        food.goto(xx,yy)
        snake_body = turtle.Turtle()
        snake_body.speed(0)
        snake_body.shape("square")
        snake_body.color(x)
        snake_body.penup()
        body.append(snake_body)

        score += 1
        level -=0.001

        sc.clear()
        sc.write("score: {}  ".format(score), align="Left", font=("ds-digital", 19, "normal")) 

    for i in range(len(body)-1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)

    if len(body)>0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    move()

    for t in body:
        if t.distance(head)<20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"


            for x in body:
                x.goto(500,500) 
            body.clear()

            score = "game over"
            level = 0.1

            sc.goto(0,0)
            sc.penup()
            sc.clear()
            sc.write(" {}".format(score), align="center", font=("ds-digital", 50, "normal"))
            time.sleep(2)
            sc.clear()
            score = 0  
            sc.goto(-290,270)
            sc.write("score: {}".format(score), align="Left", font=("ds-digital", 19, "normal"))
            sc.penup()
            food.goto(0,90)

    time.sleep(level)  