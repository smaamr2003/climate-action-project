"""
This is a simple visual graphics program about creating awareness about global
warming, specifically talking about planting trees to remove excess
carbon dioxide from the atmosphere. This was created for the presentation
of the speaking session of IOELL Virtual 2023, which was conducted by GEIST
International Foundation. Even though it is not perfect as a program, but at
least it is an attempt by a new Python learner who wants to explore even greater
things about this language and eventually build up on that. It is actually
designed for the young generation to get a lesson on how to prepare ourselves
in defending a natural calamity like global warming, but just a visual way to
actually get the idea on how simple an effort we can take to tackle this
calamity, and what actually happens when we plant trees.

FOR THE INSTRUCTOR OF THE CLASS:

This program first of all gives a light blue background, then draws a sun and
land. Then it draws 6 clouds of grey color, and writes CO2 on top of the clouds.

After that, in the box below the canvas, there should come a question, asking
"What should we do to remove carbon dioxide from the atmosphere?: "To this, the
students will answer either "plant trees" OR "plant a tree". Any answer other
than that will ask the same question repeatedly until the code receives its
desired answer. After the answer, the code will draw 3 trees, and then remove
the clouds and redraw the sun (Redraw the sun because part of sun gets wiped
out due to removing clouds in the process).

(N.B.: They can type either in capital letters or in small letters, but the
input should be only these two: "plant trees" OR "plant a tree")

Contact: smaamr2003@gmail.com

"""

import turtle

turtle.shape("circle")
turtle.bgcolor('light blue')
turtle.speed(0)


def sun():
    # Sun Circle
    begin_fill()
    color("yellow")
    circle(50)
    end_fill()

    # "Wings" of the sun
    for i in range(8):
        penup()
        left(90)
        setposition(100, 130)
        forward(60)
        pendown()
        pensize(8)
        forward(15)
        penup()
        backward(75)
        right(45)
        pensize(1)


def alphabet_C():
    penup()
    left(45)
    pendown()
    pensize(2)
    color("white")
    left(90)
    circle(10, 270)


def alphabet_O():
    # Transition from C to O
    penup()
    left(45)
    backward(3)
    right(90)
    forward(14)
    # drawing O start
    pendown()
    circle(10)


def number_two():
    # Transition from O to 2
    penup()
    forward(20)
    left(45)
    # Drawing 2 start
    pendown()
    forward(5)
    circle(5, 180)
    penup()
    right(135)
    backward(12)
    right(90)
    pendown()
    forward(10)


def cloud(cloud_circle_radius, cloud_colour):
    begin_fill()
    color(cloud_colour)
    circle(cloud_circle_radius, 180)
    penup()
    left(90)
    forward(cloud_circle_radius / 1.5)
    right(215)
    pendown()
    circle(cloud_circle_radius + (cloud_circle_radius * (1 / 4)), 250)
    penup()
    right(215)
    forward(cloud_circle_radius / 1.5)
    left(90)
    pendown()
    circle(cloud_circle_radius, 180)
    end_fill()


def cloud_separation_down(cloud_circle_radius):
    penup()
    forward(cloud_circle_radius * 2)
    right(90)
    forward((cloud_circle_radius * 2) - 10)
    left(90)
    forward(cloud_circle_radius * 2)
    pendown()


def cloud_separation_up(cloud_circle_radius):
    penup()
    forward(cloud_circle_radius * 2)
    left(90)
    forward((cloud_circle_radius * 2) - 10)
    right(90)
    forward(cloud_circle_radius * 2)
    pendown()


def land():
    begin_fill()
    color("light green")
    for i in range(2):
        forward(400)
        left(90)
        forward(150)
        left(90)
    end_fill()


def tree():
    # Main branch of the tree
    begin_fill()
    color("brown")
    for i in range(2):
        forward(20)
        left(90)
        forward(80)
        left(90)
    end_fill()
    penup()
    left(90)
    forward(80)
    right(90)
    forward(35)
    pendown()
    # Leaves (semiCircles) of the tree
    begin_fill()
    color("green")
    circle(20, 180)
    right(180)
    circle(15, 180)
    right(180)
    circle(10, 180)
    forward(10)
    right(90)
    circle(15, 180)
    right(90)
    forward(10)
    circle(10, 180)
    right(180)
    circle(15, 180)
    right(180)
    circle(20, 180)
    end_fill()


def clouds(cloud_colour):
    cloud_circle_radius = 25
    for i in range(3):
        cloud(cloud_circle_radius, cloud_colour)
        cloud_separation_down(cloud_circle_radius)
        cloud(cloud_circle_radius, cloud_colour)
        cloud_separation_up(cloud_circle_radius)


def CO2_placements():
    for i in range(3):
        alphabet_C()
        alphabet_O()
        number_two()
        right(90)
        penup()
        forward(20)
        left(90)
        forward(15)
        alphabet_C()
        alphabet_O()
        number_two()
        left(90)
        penup()
        forward(55)
        right(90)
        forward(20)


def main():
    penup()
    setposition(100, 80)
    pendown()
    sun()

    penup()
    setposition(-200, -200)
    pendown()
    land()

    penup()
    setposition(-120, 120)
    pendown()
    clouds("gray")

    penup()
    setposition(-145, 155)
    pendown()
    CO2_placements()

    answer = "plant trees"
    answer_two = "plant a tree"
    while True:
        global_warming = input("What should we do to remove carbon dioxide from the atmosphere?: ")
        if global_warming.lower() == answer or global_warming.lower() == answer_two:

            penup()
            setposition(-150, -120)
            for i in range(3):
                pendown()
                tree()
                penup()
                right(90)
                forward(80)
                left(90)
                forward(120)

            penup()
            setposition(-120, 120)
            pendown()
            clouds("light blue")

            penup()
            setposition(100, 80)
            pendown()
            sun()

            break
        else:
            print("You should plant a tree.")
            print("")


main()