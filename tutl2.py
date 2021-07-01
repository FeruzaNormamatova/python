import turtle 
screen = turtle.Screen()
t = turtle.Turtle()
w = turtle.Screen()
screen.colormode()
turtle.colormode(1)
w.clear()
w.bgcolor("#ffffff")
dist2 = input("please enter density: ")
#turtle.tracer()
#speed = turtle.Speed()
density = input("please enter density: ")
dist = 1
for i in range(250):
	t.fd(dist)
	screen.colormode(50)
	t.width(density)
	t.rt(50)
	t.rt(250)
	t.pencolor('#FF0000')
	dist += int(dist2)
	print(dist)
	t.speed(0)
turtle.update()
w.exitonclick()





