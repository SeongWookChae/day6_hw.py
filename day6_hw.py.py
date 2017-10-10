#drawing python logo
import turtle as t

#setting for drawing
t.speed(0)
t.up()
t.lt(90)
t.fd(70)
t.down()
t.rt(90)

#drawing the logo of the left side
t.color("steelblue")
t.pensize(5)

t.begin_fill() #filling steelblue color
t.fd(60)
for x in range(29): #curve
    t.fd(3)
    t.lt(3.141592)
t.rt(1) #correction of angle
t.fd(70)
for x in range(28): #more gentle curve
    t.fd(4)
    t.lt(3.141592)
t.lt(2) #correction of angle
t.fd(90)
for x in range(28): #more gentle curve
    t.fd(4)
    t.lt(3.141592)
t.fd(30)
t.lt(92) #correction of angle
t.fd(120)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(180)
for x in range(29): #curve
    t.fd(3)
    t.lt(3.141592)
t.right(1) #correction of angle
t.fd(100)
for x in range(28): #more gentle curve
    t.fd(4)
    t.lt(3.141592)
t.lt(2) #correction of angle
t.fd(50)
t.lt(90)
t.lt(1) #correction of angle
t.fd(90)
for x in range(29): #curve
    t.fd(3)
    t.rt(3.141592)
t.fd(70)
t.end_fill() #filling royalblue color

#drawing symbol of eye
t.up() #displacing turtle without t.color
t.lt(90)
t.fd(160)
t.lt(90)
t.fd(80)
t.down()
t.color("white") #filling white color in the symbol of eye
t.begin_fill()
t.circle(20)
t.end_fill()



#displacing turtle for drawing logo of the right side
t.up()
t.lt(90)
t.fd(190)
t.lt(90)
t.fd(110)
t.down()



#drawing the logo of the right side
t.color("gold") #setting for drawing
t.pensize(5)

t.begin_fill() #filling steelblue color
t.rt(180)
t.fd(60)
for x in range(29): #curve
    t.fd(3)
    t.lt(3.141592)
t.rt(1) #correction of angle
t.fd(70)
for x in range(28): #more gentle curve
    t.fd(4)
    t.lt(3.141592)
t.lt(2) #correction of angle
t.fd(90)
for x in range(28): #more gentle curve
    t.fd(4)
    t.lt(3.141592)
t.fd(30)
t.lt(92) #correction of angle
t.fd(120)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(180)
for x in range(29): #curve
    t.fd(3)
    t.lt(3.141592)
t.right(1) #correction of angle
t.fd(100)
for x in range(28): #more gentle curve
    t.fd(4)
    t.lt(3.141592)
t.lt(2) #correction of angle
t.fd(50)
t.lt(90)
t.lt(1) #correction of angle
t.fd(90)
for x in range(29): #curve
    t.fd(3)
    t.rt(3.141592)
t.fd(70)
t.end_fill() #filling royalblue color

#drawing symbol of eye
t.up() #displacing turtle without t.color
t.lt(90)
t.fd(160)
t.lt(90)
t.fd(80)
t.down()
t.color("white") #filling white color in the symbol of eye
t.begin_fill()
t.circle(20)
t.end_fill()



#displacing turtle for appearing ' I LOVE PYTHON ' without t.color
t.up()
t.rt(180)
t.fd(120)
t.lt(90)
t.fd(160)


#drawing letter "I love python"
t.color("gray")
t.write("' I LOVE PYTHON '", False, "center", ("", 60))
#this instruction is referred to teaching ppt pg.122

