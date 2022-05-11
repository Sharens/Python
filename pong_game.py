#Nail Pong
 
import turtle
 
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height=600)
wn.tracer(0)
 
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=4, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
 
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=4, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)
 
 
#Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1
 
#Function Up A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
#Function Down A
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
 
#Function Up B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
#Function Down B
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
 
#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
 
#Main game loop
while True:
    wn.update()
 
    #Move of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
 
    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
 
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
 
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
 
    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
 
    #right paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
 
