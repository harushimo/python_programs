#!/usr/bin/python

import turtle

def create_window ():
	window = turtle.Screen()
	window.bgcolor("green")
	draw_H()
	draw_V()
	window.exitonclick()

def draw_H ():
	turtle.Turtle()
	turtle.shape("turtle")
	turtle.color("yellow")
	turtle.speed(2)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.backward(200)
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(100)
	turtle.backward(200)

def draw_V ():
	test = turtle.Turtle()
	test.shape("turtle")
	test.color("red")
	test.speed(2)
	test.pu()
	test.forward(150)
	test.pu()
	test.left(90)
	test.pu()
	test.forward(100)
	test.pd()
	test.right(150)
	test.forward(250)
	test.left(120)
	test.forward(250)


create_window()
