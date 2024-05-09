from turtle import *
import math 

def crystal1(size,color='white'):
    penup()
    forward(size/2)
    pendown()
    left(135)
    forward(size)
    left(90)
    forward(size)
    left(45)
    forward(size*3)
    left(90)
    forward(math.sqrt(size*size*2))
    left(90)
    forward(size*3)
    left(90)
    forward(math.sqrt(size*size*2))
    right(135)
    forward(size)
    right(100)
    forward(size*0.899)
    right(35)
    forward(size*3)
    penup()
    right(90)
    forward(size)
    right(90)
    pendown()
    forward(size*3)
    right(35)
    forward(size*0.9)
    penup()
    right(145)
    forward(size*3.7)
    left(90)
    pendown()
    fillcolor(color)
    begin_fill()
    forward(size/2)
    left(90)
    forward(size*3)
    left(90)
    forward(size)
    left(90)
    forward(size*3)
    left(90)
    forward(size)
    end_fill()
    left(90)
    forward(size*3)
    right(90)
    fillcolor(color)
    begin_fill()
    forward(size*0.19)
    left(136)
    forward(size)
    left(170)
    forward(size*0.87)
    left(55)
    forward(size*0.2)
    end_fill()
    left(179)
    forward(size*1.2)
    fillcolor(color)
    begin_fill()
    forward(size*0.2)
    right(134)
    forward(size)
    right(168)
    forward(size*0.86)
    right(66)
    forward(size*0.3)
    end_fill()
    penup()
    left(145)
    forward(size*2)
    right(48)
    forward(size*1.7)

def crystal2(size,color='white'):
    forward(size/2)
    left(135)
    forward(size*0.7)
    left(135)
    forward(size*2.5)
    left(90)
    forward(size/2)
    left(90)
    forward(size*2)
    left(90)
    fillcolor(color)
    begin_fill()
    forward(size*0.2)
    right(59)
    forward(size*0.6)
    right(165)
    forward(size*0.76)
    right(135)
    forward(size*0.2)
    end_fill()



crystal2(100,'yellow')
done()