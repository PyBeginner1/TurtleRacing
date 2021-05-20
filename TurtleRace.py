import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red','orange','yellow','brown', 'black','pink', 'white', 'purple', 'violet']

def get_racers():
    racers = 0
    while True:
        racers = input("Enter number of racers (2-10): ")
        if racers.isdigit():
            #int format
            racers = int(racers)
        else:
            print("Invalid Input. Try Again!!!")
            continue


        if 2 <= racers <= 10:
            return racers
        else:
            print('Number range is invalid. Try Again!!!')


#racing
def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            #move individual turtles randomly from 1px to 20 px & vice versa
            distance = random.randrange(1, 20)
            racer.forward(distance)

            #pos check if its reached checkpoint
            x, y = racer.pos()      #each turtle pos
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


#create turtle
def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)               #ex: if colors = 4. 400 / 5= 80. (colors + 1) is done so that they dont fall into the border
    #enumerate gives index(i) & value(color)
    for i, color in enumerate(colors):      #ex ---> i = 0, color = white
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.speed(2)
        #make it face upward
        racer.left(90)
        #turtle is in center so we keep peen up(no drawing of line)
        racer.penup()
        #set pos
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 30 )  #x, y co-ordinates
        racer.pendown()
        turtles.append(racer)

    return turtles



#turtle screen
def init_turtle():
    # turtle window
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')




racers = get_racers()
init_turtle()

#shuffle COLORS
random.shuffle(COLORS)
#pick a color for each turtle
colors = COLORS[:racers]

winner = race(colors)
print('The winner is the turtle with color:' ,winner)
time.sleep(10)






''' Practice Stuff
#create & move turtle
racer = turtle.Turtle()
#speed of the turtle
racer.speed(1)
#creating shape for turtle
racer.shape('turtle')
racer.color('orange')
#no line is created along the path of turtle
racer.penup()
racer.forward(100)      #moves forward in pixels
racer.right(45)         #right & left is the degree of the turn
racer.forward(90)
racer.right(90)
racer.forward(90)
racer.right(90)
racer.forward(90)
racer.backward(90)
racer.pendown()
racer.forward(90)
racer.forward(90)



racer2 = turtle.Turtle()
#speed of the turtle
racer2.speed(1)
#creating shape for turtle
racer2.shape('turtle')
racer.color('red')
#no line is created along the path of turtle
racer2.penup()
racer.forward(100)      #moves forward in pixels
racer.right(45)         #right & left is the degree of the turn
racer.forward(90)
racer.right(90)
racer.forward(90)
racer.right(90)
racer.forward(90)
racer.backward(90)
racer.pendown()
racer.forward(90)
racer.forward(90)
'''








