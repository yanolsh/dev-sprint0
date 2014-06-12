# Polygon excercise from Week 0

# Name:Yan Olshevskyy
import math

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()
bob.delay=0				



# This is where you put code to move bob
def square(turtle, length):
	for i in range(4):
		fd(turtle, length)
		rt(turtle)

#square()
def line(turtle, n, length, angle):
	for i in range(n):
		fd(turtle, length)
		rt(turtle, angle)


def polygon(turtle, length, n):
	for i in range(n):
		fd(turtle, length)
		rt(turtle, 360/n)

#polygon(bob,50, 5)
def arc(turtle, radius, theta):
  
    arc_length = 2 * math.pi * radius * abs(theta) / 360
    n = int(arc_length / 4) + 1
    s_length = arc_length / n
    s_angle = float(theta) / n

    lt(turtle, s_angle/2)
    line(turtle,n, s_length, s_angle)
    rt(turtle, s_angle/2)

def circle(turtle, radius):
	arc(turtle, radius, 360)



circle(bob,100)



wait_for_user()					
