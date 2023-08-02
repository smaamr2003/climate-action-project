
import turtle

turtle.shape("turtle")
turtle.bgcolor('light blue')
turtle.speed(0)
turtle.screensize()

def sun():
    # Sun Circle
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.circle(50)
    turtle.end_fill()

    # "Wings" of the sun
    for i in range(8):
        turtle.penup()
        turtle.left(90)
        turtle.setposition(100, 130)
        turtle.forward(60)
        turtle.pendown()
        turtle.pensize(8)
        turtle.forward(15)
        turtle.penup()
        turtle.backward(75)
        turtle.right(45)
        turtle.pensize(1)


def alphabet_C():
    turtle.penup()
    turtle.left(45)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color("white")
    turtle.left(90)
    turtle.circle(10, 270)


def alphabet_O():
    # Transition from C to O
    turtle.penup()
    turtle.left(45)
    turtle.backward(3)
    turtle.right(90)
    turtle.forward(14)
    # drawing O start
    turtle.pendown()
    turtle.circle(10)


def number_two():
    # Transition from O to 2
    turtle.penup()
    turtle.forward(20)
    turtle.left(45)
    # Drawing 2 start
    turtle.pendown()
    turtle.forward(5)
    turtle.circle(5, 180)
    turtle.penup()
    turtle.right(135)
    turtle.backward(12)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(10)


def cloud(cloud_circle_radius, cloud_colour):
    turtle.begin_fill()
    turtle.color(cloud_colour)
    turtle.circle(cloud_circle_radius, 180)
    turtle.penup()
    turtle.left(90)
    turtle.forward(cloud_circle_radius / 1.5)
    turtle.right(215)
    turtle.pendown()
    turtle.circle(cloud_circle_radius + (cloud_circle_radius * (1 / 4)), 250)
    turtle.penup()
    turtle.right(215)
    turtle.forward(cloud_circle_radius / 1.5)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(cloud_circle_radius, 180)
    turtle.end_fill()


def cloud_separation_down(cloud_circle_radius):
    turtle.penup()
    turtle.forward(cloud_circle_radius * 2.5)
    turtle.right(90)
    turtle.forward((cloud_circle_radius * 2.5) - 10)
    turtle.left(90)
    turtle.forward(cloud_circle_radius * 2.5)
    turtle.pendown()


def cloud_separation_up(cloud_circle_radius):
    turtle.penup()
    turtle.forward(cloud_circle_radius * 2.5)
    turtle.left(90)
    turtle.forward((cloud_circle_radius * 2.5) - 10)
    turtle.right(90)
    turtle.forward(cloud_circle_radius * 2.5)
    turtle.pendown()


def land():
    turtle.begin_fill()
    turtle.color("light green")
    for i in range(2):
        turtle.forward(1000)
        turtle.left(90)
        turtle.forward(250)
        turtle.left(90)
    turtle.end_fill()


def tree():
    # Main branch of the tree
    turtle.begin_fill()
    turtle.color("brown")
    for i in range(2):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(80)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(35)
    turtle.pendown()
    # Leaves (semiCircles) of the tree
    turtle.begin_fill()
    turtle.color("green")
    turtle.circle(20, 180)
    turtle.right(180)
    turtle.circle(15, 180)
    turtle.right(180)
    turtle.circle(10, 180)
    turtle.forward(10)
    turtle.right(90)
    turtle.circle(15, 180)
    turtle.right(90)
    turtle.forward(10)
    turtle.circle(10, 180)
    turtle.right(180)
    turtle.circle(15, 180)
    turtle.right(180)
    turtle.circle(20, 180)
    turtle.end_fill()


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
        turtle.right(90)
        turtle.penup()
        turtle.forward(34)
        turtle.left(90)
        turtle.forward(35)
        alphabet_C()
        alphabet_O()
        number_two()
        turtle.left(90)
        turtle.penup()
        turtle.forward(72)
        turtle.right(90)
        turtle.forward(33)


def main():
    turtle.penup()
    turtle.setposition(100, 80)
    turtle.pendown()
    sun()

    turtle.penup()
    turtle.setposition(-600, -300)
    turtle.pendown()
    land()

    turtle.penup()
    turtle.setposition(-200, 120)
    turtle.pendown()
    clouds("gray")

    turtle.penup()
    turtle.setposition(-240, 155)
    turtle.pendown()
    CO2_placements()

    answer = "plant trees"
    answer_two = "plant a tree"
    while True:
        global_warming = input("What should we do to remove carbon dioxide from the atmosphere?: ")
        if global_warming.lower() == answer or global_warming.lower() == answer_two:

            turtle.penup()
            turtle.setposition(-200, -120)
            for i in range(3):
                turtle.pendown()
                tree()
                turtle.penup()
                turtle.right(90)
                turtle.forward(80)
                turtle.left(90)
                turtle.forward(120)

            turtle.penup()
            turtle.setposition(-200, 120)
            turtle.pendown()
            clouds("light blue")

            turtle.penup()
            turtle.setposition(100, 80)
            turtle.pendown()
            sun()

            break
        else:
            print("You should plant a tree.")
            print("")
    turtle.penup()
    turtle.setposition(0,0)

main()
