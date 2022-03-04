import turtle

wn = turtle.Screen()

wn.bgcolor("light green")#Write the color as light green

turtle.color("blue")#Write the color as blue

def sqrfunc(size,speed):#Pass the value size and speed
    for i in range(4):
        (size, speed) = (size + 5, speed + 5)
        (turtle.speed(speed))#Use the variable speed
        turtle.fd(size)#Use the variable name
        turtle.left(90)

sqrfunc(6, 2)
sqrfunc(26, 5)
sqrfunc(46, 7)
sqrfunc(66, 10)
sqrfunc(86, 15)
sqrfunc(106, 20)
sqrfunc(116,30)#Fill in the values as 116,30
sqrfunc(136,40)#Fill in the values as 136,40
