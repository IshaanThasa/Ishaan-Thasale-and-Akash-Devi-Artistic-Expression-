import turtle
import random

# set up the screen
screen = turtle.Screen()
screen.title("Encouragement Card")
screen.bgcolor("navy")
screen.setup(600, 500)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ask the user for their name
name = input("What is your name? ")

# if they left it blank just use Friend
if name == "":
    name = "Friend"
else:
    name = name.strip().title()

# list of encouraging messages
messages = [
    "You are stronger than you think!",
    "Keep going, you got this!",
    "You make the world a better place!",
    "Believe in yourself!",
    "You are capable of amazing things!"
]

# list of colors
colors = ["red", "orange", "yellow", "lime green", "cyan", "violet", "hot pink"]

# draws a star at a given position
def draw_star(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# draws the border around the card
def draw_border():
    t.penup()
    t.goto(-270, 220)
    t.pendown()
    t.pensize(5)
    sides = [540, 440, 540, 440]
    for i in range(4):
        t.color(colors[i])
        t.forward(sides[i])
        t.right(90)

# writes the name letter by letter each in a different color
def draw_name(name):
    start_x = -(len(name) * 25) // 2
    for i in range(len(name)):
        letter = name[i].upper()
        color = colors[i % len(colors)]
        t.penup()
        t.goto(start_x + i * 25, 20)
        t.color(color)
        t.write(letter, font=("Arial", 24, "bold"))

# draws a firework burst at a given position
def draw_firework(x, y, color):
    t.pensize(2)
    for i in range(12):
        t.penup()
        t.goto(x, y)
        t.setheading(i * 30)
        t.pendown()
        t.color(color)
        t.forward(40)
        t.dot(6)

# launches one firework per letter in the name
def launch_fireworks(name):
    positions = [(-200, 150), (200, 150), (-200, -120), (200, -120), (0, 160)]
    for i in range(len(name)):
        if i < len(positions):
            x, y = positions[i]
        else:
            x = random.randint(-200, 200)
            y = random.randint(-150, 150)
        color = colors[i % len(colors)]
        draw_firework(x, y, color)

# draws small stars in the corners for decoration
def draw_background_stars():
    star_spots = [(-220, 180), (220, 180), (-220, -160), (220, -160), (0, 190), (-100, -170), (100, -170)]
    for i in range(len(star_spots)):
        x, y = star_spots[i]
        draw_star(x, y, 10, colors[i % len(colors)])

# build the card
draw_background_stars()
draw_border()

message = random.choice(messages)

t.penup()
t.goto(0, 150)
t.color("gold")
t.write("A Message For You", align="center", font=("Arial", 16, "bold"))

draw_name(name)

t.penup()
t.goto(0, -20)
t.color("white")
t.write(message, align="center", font=("Arial", 13, "italic"))

launch_fireworks(name)

t.penup()
t.goto(0, -200)
t.color("light blue")
t.write("Computing for Change - Community Card", align="center", font=("Arial", 10, "normal"))

# fires a firework wherever you click
def on_click(x, y):
    color = random.choice(colors)
    draw_firework(x, y, color)
    if abs(x) < 80 and abs(y) < 80:
        draw_firework(x + 20, y + 20, random.choice(colors))

screen.onclick(on_click)
screen.mainloop()