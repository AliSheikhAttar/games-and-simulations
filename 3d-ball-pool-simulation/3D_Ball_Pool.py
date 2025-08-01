from vpython import *
import random
import time

def make_balls(n,d):
    balls=[]
    for i in range(n):
        x=  random.randint(-d ,d)
        y=  random.randint(-d,d)
        z=  random.randint(-d,d)
        c = random.choice([color.green, color.cyan, color.blue, color.black])
        center = vector(x,y,z)
        b = sphere(pos=center, radius=0.5, color=c)
        b.velocity = vector(random.random()*2-1,random.random()*2-1,random.random()*2-1)
        balls.append(b)
    return balls

def make_floor1():  
    f1 = box(pos=vector(0,-10,0), size=vector(20,1,20), color=color.blue)
    return f1

def make_floor2():  
    f2 = box(pos=vector(0,10,0), size=vector(20,1,20), color=color.blue)
    return f2
def make_floor3():  
    f3 = box(pos=vector(10,0,0), size=vector(1,20,20), color=color.blue)
    return f3
def make_floor4():  
    f4 = box(pos=vector(-10,0,0), size=vector(1,20,20), color=color.blue)
    return f4
def make_floor5():  
    f5 = box(pos=vector(0,0,-10), size=vector(20,20,1), color=color.blue)
    return f5

def move_balls(balls, dt):
    for b in balls:
        b.pos = b.pos +b.velocity *dt

def handle_floor(balls):
    for b in balls:
        if b.pos.y <= -9 and b.velocity.y <0:
            b.velocity.y = -1*b.velocity.y
        elif b.pos.y >= 9  and b.velocity.y >0:
            b.velocity.y = -1*b.velocity.y
        elif b.pos.x <= -9 and b.velocity.x <0:
            b.velocity.x = -1*b.velocity.x
        elif b.pos.x >= 9  and b.velocity.x >0:
            b.velocity.x = -1*b.velocity.x
        elif b.pos.z <= -9 and b.velocity.z <0:
            b.velocity.z = -1*b.velocity.z
        elif b.pos.z >= 9  and b.velocity.z >0:
            b.velocity.z = -1*b.velocity.z
def distance_balls(b,g):
    distance=(abs(b.pos.x-g.pos.x)**2+abs(b.pos.y-g.pos.y)**2+(abs(b.pos.z-g.pos.z))**2)**0.5
    return distance

def handle_balls(balls):
    for b in balls:
        for g in balls:
            if b != g and 0.98 < distance_balls(b,g) < 1:
                b.color = color.red
                g.color = color.red
                if distance_balls(b,g)>1:
                    b.velocity = -1*b.velocity
                    g.velocity = -1*g.velocity


balls = make_balls(20,5)
ff1 = make_floor1()
ff2 = make_floor2()
ff3 = make_floor3()
ff4 = make_floor4()
ff5 = make_floor5()

dt = 0.01
t = 0

def game_over(balls):
    for b in balls:
        if b.color != color.red :
            return False
    return True

def clean_game(balls,ff1,ff2,ff3,ff4,ff5):
    for b in balls:
        b.hideturtule()
        b.goto(1000,1000)
    ff1.hideturtle()
    ff1.goto(1000,1000)
    ff2.hideturtle()
    ff2.goto(1000,1000)
    ff1.hideturtle()
    ff3.goto(1000,1000)
    ff3.hideturtle()
    ff1.goto(1000,1000)
    ff4.hideturtle()
    ff4.goto(1000,1000)
    ff5.hideturtle()
    ff5.goto(1000,1000)

while True:
    gameisover = False
    while not gameisover:
        gameisover = game_over(balls)
        rate(1000)
        move_balls(balls, dt)
        handle_floor(balls)
        handle_balls(balls)

    time.sleep(1)
    clean_game(balls,ff1,ff2,ff3,ff4,ff5)

done()