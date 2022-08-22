import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple']

# No of racers
def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter no. of racers between ( 2 - 10 ): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Oops invalid input. Please try again...')
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("No. of racers are not in the range (2 - 10 ). Try Again...")

# Initilizing turtle screen
def init_screen():
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title("Turtle Race!")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        x = -WIDTH // 2 + spacingx * (i+1)
        y = -HEIGHT//2 + 20
        racer.setpos(x, y)
        racer.pendown()
        racer.left(90)
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT//2 - 20:
                return colors[turtles.index(racer)]    


def main():
    racers = get_number_of_racers()
    init_screen()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    return race(colors)

winner = main()
print("Winner: ", winner)
