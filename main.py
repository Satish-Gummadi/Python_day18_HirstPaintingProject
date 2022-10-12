# color checker : https://www.w3schools.com/colors/colors_rgb.asp

import turtle
from turtle import Turtle, Screen
import random
import colorgram

# colors = colorgram.extract('spot_painting_ss.JPG', 100)
# color_set = []
#
# for i in colors:
#     color_set.append((i.rgb.r,i.rgb.g,i.rgb.b))
# print(color_set)

# after obtaining color_list as below from above program result, we will comment out the above program

color_list = [(204, 162, 88), (58, 88, 128), (140, 92, 44), (220, 207, 112), (134, 174, 198), (136, 27, 50),
              (153, 51, 84), (46, 55, 101), (170, 158, 43), (132, 187, 145), (81, 21, 43), (37, 44, 67),
              (190, 140, 161), (184, 94, 108), (89, 115, 175), (58, 40, 33), (88, 155, 96), (79, 154, 163),
              (56, 125, 122), (194, 84, 71), (163, 202, 216), (45, 74, 76), (221, 176, 188), (169, 206, 163),
              (76, 74, 45), (46, 74, 72), (219, 182, 168), (180, 188, 212), (142, 38, 36), (43, 64, 63)]

# my code

turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed(0)
tim.setheading(135)
tim.forward(280)
tim.setheading(0)
paint_size = 10     # variables
dot_size = 22       # variables
dot_spacing = 40    # variables

for i in range(0, paint_size):
    for j in range(0, paint_size):
        tim_color = random.choice(color_list)
        tim.dot(dot_size,tim_color)
        tim.forward(dot_spacing)
    tim.right(90)
    tim.forward(dot_spacing)
    tim.right(90)
    tim.forward(dot_spacing * paint_size)
    tim.right(180)


screen = Screen()
screen.exitonclick()