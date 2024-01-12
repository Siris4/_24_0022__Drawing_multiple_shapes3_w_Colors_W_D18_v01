
from turtle import Turtle, Screen
import random

turtle = Turtle()

full_cycle = 360

colors_list = ['orange red', 'slate blue', 'crimson', 'purple', 'yellow', 'lime green', 'black']


# TODO 1: Triangle
# sides = 3
# counter = 0

def draw_shapes_just_enter_side_quantity(sides):
    for _ in range(sides):
        turtle.forward(64)
        turtle.right(full_cycle/sides)

for side_quantity_loop_per_shape in range(3, 11):
    turtle.color(random.choice(colors_list))
    draw_shapes_just_enter_side_quantity(side_quantity_loop_per_shape)


#TODO 2: Square

#TODO 3: Pentagon

# sides = 5
# for loop in range(sides):
#     turtle.forward(64)
#     turtle.right(full_cycle/sides)


#TODO 4: Hexagon

# sides = 6
# for loop in range(sides):
#     turtle.forward(64)
#     turtle.right(full_cycle/sides)

#TODO 5: Heptagon

# sides = 7
# for loop in range(sides):
#     turtle.forward(64)
#     turtle.right(full_cycle/sides)

#TODO 6: Octagon

# sides = 8
# for loop in range(sides):
#     turtle.forward(64)
#     turtle.right(full_cycle/sides)

#TODO 7: Nonagon

# sides = 9
# for loop in range(sides):
#     turtle.forward(64)
#     turtle.right(full_cycle/sides)

#TODO 8: Decagon

# sides = 10
# for loop in range(sides):
#     turtle.forward(64)
#     turtle.right(full_cycle/sides)





screen = Screen()
screen.exitonclick()