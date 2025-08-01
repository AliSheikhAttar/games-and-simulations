from vpython import *
from physutil import *
import math

def create_scene(theta):
    inclinedPlane = box(pos = vector(1,0,0) , size= vector(2,0.02,0.2), color = color.green , opacity = 0.3)
    inclinedPlane.rotate(angle=theta , origin= vector(0,0,0), axis = vector(0,0,1))
    cart1 = box(size= vector(0.2,0.06,0.06), color = color.yellow )
    cart2 = box(size= vector(0.4,0.1,0.06), color = color.blue )
    cart3 = box(size= vector(0.8,0.16,0.06), color = color.red )

    cart1.pos = vector(1.9,0.3,0.08)
    cart1.m1 = 0.5
    cart1.F1 = vector(0,0,0)
    cart1.v1 = vector(0,0,0)
    cart1.rotate(angle=theta, origin = vector(0,0,0), axis=vector(0,0,1))  

    cart2.pos = vector(1.9,0.22,0.08)
    cart2.m2 = 1
    cart2.F2 = vector(0,0,0)
    cart2.v2 = vector(0,0,0)
    cart2.rotate(angle=theta, origin = vector(0,0,0), axis=vector(0,0,1))  
    
    cart3.pos = vector(1.9,0.09,0.08)
    cart3.m3 = 1.5
    cart3.F3 = vector(0,0,0)
    cart3.v3 = vector(0,0,0)
    cart3.rotate(angle=theta, origin = vector(0,0,0), axis=vector(0,0,1))        


    return inclinedPlane, cart1, cart2, cart3

def calc_forces(cart1, cart2, cart3, g, ip):
    cart1.F1 = norm(ip.axis)
    cart1.F1.mag = cart1.m1 * g * sin(theta)
    cart2.F2 = norm(ip.axis)
    cart2.F2.mag = cart2.m2 * g * sin(theta)
    cart3.F3 = norm(ip.axis)
    cart3.F3.mag = cart3.m3 * g * sin(theta)

def update_cart_pos_on_plane(cart1, cart2, cart3, dt):
    cart1.v1 = cart1.v1 + (cart1.F1/cart1.m1) * dt
    cart1.pos = cart1.pos + cart1.v1 * dt
    cart2.v2 = cart2.v2 + (cart2.F2/cart2.m2) * dt
    cart2.pos = cart2.pos + cart2.v2 * dt
    cart3.v3 = cart3.v3 + (cart3.F3/cart3.m3) * dt
    cart3.pos = cart3.pos + cart3.v3 * dt

def update_cart_pos_off_plane(cart1, cart2, cart3, dt, gv, theta):    
    cart1.v1 = cart1.v1 + gv * dt
    cart1.pos = cart1.pos + cart1.v1 * dt
    cart2.v2 = cart2.v2 + gv * dt
    cart2.pos = cart2.pos + cart2.v2 * dt
    cart3.v3 = cart3.v3 + gv * dt
    cart3.pos = cart3.pos + cart3.v3 * dt

theta = math.pi/8
inclined_plane, cart1, cart2, cart3 = create_scene(theta)

dt = 0.005
t = 0
g = -9.8
gv = vector(0,g,0)
plot1 = PhysGraph(3,title='graph for cart 1',xlabel='time',ylabel='a,v,x')
plot2 = PhysGraph(3,title='graph for cart 2',xlabel='time',ylabel='a,v,x')
plot3 = PhysGraph(3,title='graph for cart 3',xlabel='time',ylabel='a,v,x')

calc_forces(cart1, cart2, cart3, g, inclined_plane)

while t < 3:
    rate(100)
    if cart1.pos.y > 0 and cart1.pos.x > 0 and cart2.pos.y > 0 and cart2.pos.x > 0 and cart3.pos.y > 0 and cart3.pos.x > 0:
        update_cart_pos_on_plane(cart1, cart2, cart3, dt)
    else:
        update_cart_pos_off_plane(cart1, cart2, cart3, dt, gv, theta)

    # the result have 3 plots!
    t = t + dt
    plot1.plot(t, mag(cart1.v1), cart1.F1.mag/cart1.m1, mag(cart1.pos))
    plot2.plot(t, mag(cart2.v2), cart2.F2.mag/cart2.m2, mag(cart2.pos))
    plot3.plot(t, mag(cart3.v3), cart3.F3.mag/cart3.m3, mag(cart3.pos))