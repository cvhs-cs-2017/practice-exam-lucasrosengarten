""" Create a Turtle, name it, make it BLUE and draw a Smiley Face"""
import turtle
wn = turtle.Screen()
smiles = turtle.Turtle()

smiles.color("blue")
smiles.penup()
smiles.goto(-75,150)
smiles.pendown()
smiles.circle(10)     #eye one

smiles.penup()
smiles.goto(75,150)
smiles.pendown()
smiles.circle(10)     #eye two

smiles.penup()
smiles.goto(0,0)
smiles.pendown()
smiles.circle(100,90)   #right smile

smiles.penup()           
smiles.goto(0,0)
smiles.pendown()
smiles.circle(-100,90)
