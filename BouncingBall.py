#first change after syncing to local mac repo and commiting within visual code studio - just this comment
#second change made after loading into V
#import needed libraries   
import turtle
from turtle import *
import random

#Define constants
#changed 400 to 300 to make it easier to test and see 
RIGHT_EDGE= 300
LEFT_EDGE = -300
BOTTOM_EDGE = -300
TOP_EDGE = 300

GRAVITY = .1
DAMPING = .8
FRICTION = .02

#This function will update the location of the ball
def moveBall():
    global xVel, yVel

    #update the postiion of the ball
    x = ball.xcor()
    if xVel != 0: # we have not stopped rolling due to friction
        ball.setx(x + xVel)
        
    y = ball.ycor()
    if yVel!=0: #if it's 0 we are not bouncing, we are rolling
        #changed gravity from - to + so now the ball goes up instead of down 
        yVel = yVel + GRAVITY   #only y is impacted by gravity
        ball.sety(y + yVel)
    else:   # friction comes into play while rolling which impacts xVel
        if (xVel>0):  xVel = xVel-FRICTION
        if (xVel<0):  xVel = xVel+FRICTION
        if abs(xVel)>.005:  #we are still rolling
            # print(xVel) - debug
            pass
        else:  # we are done - ball stopped bouncing and then stopped rolling
            exit()

    #Check for collisons and reverse the direction if so
    #if the ball hits right edge or the left edge then it changes from a color in a list from "colors2".
    #if the ball hits the top or bottom edge then it changes from a color in a list from "colors1". 
    if (x >= RIGHT_EDGE):
        xVel *= -1
        ball.color(random.choice(colors2))
        if xVel!=0:
            ball.setx(x + xVel-5)

    if (x <= LEFT_EDGE):
        xVel *= -1
        ball.color(random.choice(colors2))
        if xVel!=0:
            ball.setx(x + xVel+5)
   
    if (y <= BOTTOM_EDGE+5):
        yVel *= -1
        ball.color(random.choice(colors1)) 
        if yVel>2:
            ball.sety(y + yVel+5)
        else:
            yVel=0

    if (y >= TOP_EDGE):
        yVel *= -1
        yVel = yVel * DAMPING #damping effect
        #changed damping to top edge
        ball.color(random.choice(colors1))
        if yVel!=0:
            ball.sety(y + yVel-5)
        else:
            yVel=0


def spacebar():
    global RIGHT_EDGE, LEFT_EDGE, BOTTOM_EDGE, TOP_EDGE
    if RIGHT_EDGE==300:
        RIGHT_EDGE= 175
        
    if LEFT_EDGE==-300: 
        LEFT_EDGE=-175
        
    if BOTTOM_EDGE==-300:
        BOTTOM_EDGE =-175
        
    if TOP_EDGE==300:
        TOP_EDGE=175
        
    print("space") 
#


#lists used to change color of the ball
colors1 = ["chocolate", "skyblue", "yellow"]
colors2 = ["brown","blue", "red"]

#Global variables
screen = Screen() 
screen.bgcolor("green")

ball = Turtle()
ball.clear()
ball.penup()

ball.shape("circle")
ball.color("blue")
ball.position()
ball.speed(0)
ball.setheading(40)

#Define initial position and speed of the ball
ball.setx(100)
ball.sety(200)
xVel = 5
yVel = 3

screen.tracer(0) #turn off auto screen updates to make it faster


while True:
    moveBall()
    turtle.onkey(spacebar, "space") 
    turtle.listen() 
    screen.update()

