from turtle import *
from math import *
colormode(255)
bgcolor(65, 64, 66)
def spiral_function(num, angle, r, g, b, rr, gg, bb):
    turn_angle = 360/num
    size = sin(radians(turn_angle/2))*10*2
    pencolor(r, g, b)
    while True:
        tup = pencolor()
        width(2)
        pencolor(color_rotate(tup[0], tup[1], tup[2],rr, gg, bb))
        draw_shape(size, num, turn_angle)
        rt(angle)
        size *= 1.05


def draw_shape(size, num, turn_angle):
    count = 0
    speed(10)
    while count < num:
        fd(size)
        rt(turn_angle)
        count += 1



def color_rotate(r, g, b, rr, gg, bb):
    def check_color(x, xx):
        if x < xx:
            x += 2
            if x > xx:
                x = int(xx)
        else:
            x -= 2
            if x < xx:
                x = int(xx)
        return int(x)
    r = check_color(r, rr)
    g = check_color(g, gg)
    b = check_color(b, bb)
    return (r, g, b)

spiral_function(6, 15, 227, 66, 52, 255, 232, 131)
