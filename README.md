# recursive_spiral
from turtle import *
from math import *
colormode(255)
def spiral_function(num, angle, r, g, b, rr, gg, bb):
    turn_angle = 360/num
    size = sin(radians(turn_angle/2))*10*2
    while True:
        tup = pencolor()
        pencolor(color_rotate(tup[0], tup[1], tup[2],rr, gg, bb))
        draw_shape(size, num, turn_angle)
        rt(angle)
        size *= 1.05


def draw_shape(size, num, turn_angle):
    count = 0
    speed(7)
    while count < num:
        fd(size)
        rt(turn_angle)
        count += 1



def color_rotate(r, g, b, rr, gg, bb):
    def check_color(x, xx):
        if x < xx:
            x += 5
            if x > xx:
                x = xx
        else:
            x -= 5
            if x < xx:
                x = xx
        return x
    r = check_color(r, rr)
    g = check_color(g, gg)
    b = check_color(b, bb)
    return (r, g, b)



spiral_function(4, 10, 227, 66, 52, 255, 232, 131)
