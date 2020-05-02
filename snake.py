import turtle 
import time
import random


delay =0.1
score =0
high_score =0

wn=turtle.Screen()
wn.title("Snake Game by AnasBaig")
wn.bgcolor('black')
wn.setup(width=600 ,height =600)
wn.tracer(0) #turns of screen update

#snake head
head =turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0,0)
head.direction ='Stop'

#Food
food =turtle.Turtle()
colors=random.choice(['red','blue','green'])
shapes =random.choice(['square','triangle','circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

segements =[]
pen =turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score:0   High Score: 0",align ="center",font=("arial",24,"bold"))


def goup():
	if head.direction != "down":
		head.direction ="up"
def godown():
	if head.direction !="up":
		head.direction ="down"
def goleft():
	if head.direction !="right":
		head.direction="left"
def goright():
	if head.direction !="left":
		head.direction ="right"

def move():
	if head.direction == "up":
		y=head.ycor()
		head.sety(y+20)
	if head.direction == "down":
		y=head.ycor()
		head.sety(y-20)
	if head.direction == "left":
		x=head.xcor()
		head.setx(x-20)
	if head.direction == "right":
		x=head.xcor()
		head.setx(x + 20)


wn.listen()
wn.onkeypress(goup,"w")
wn.onkeypress(godown,"s")
wn.onkeypress(goleft,"a")
wn.onkeypress(goright,"d")


while True:
	wn.update()
	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
		time.sleep(1)
		head.goto(0,0)
		head.direction ="Stop"
		colors =random.choice(['red','blue','green'])
		shapes =random.choice(['square','circle'])
		for segement in segements:
			segement.goto(1000,1000)
		segement.clear()
		score=0
		delay =0.1
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score,high_score),align='center',font=('arial',24,'bold'))
	if  head.distance(food)<20:
		x=random.randint(-270,270)
		y=random.randint(-270,270)
		food.goto(x,y)

		new_segement =turtle.Turtle()
		new_segement.speed(0)
		new_segement.shape("square")
		new_segement.color("lightgreen")
		new_segement.penup()
		segements.append(new_segement)
		delay -= 0.001
		score += 10
		if score > high_score:
			high_score =score
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=('arial',24,'bold'))
	#move the end segemnt first in reverse order	
	for i in range(len(segements)-1, 0, -1):
		x=segements[i-1].xcor()
		y=segements[i-1].ycor()
		segements[i].goto(x,y)
	#move segment 0 to where the head is 
	if len(segements)>0:
		x=head.xcor()
		y=head.ycor()
		segements[0].goto(x,y)
	move()
	for segement in segements:
		if segement.distance(head)<20:
			time.sleep(1)
			head.goto(0,0)
			head.direction ="Stop"
			colors =random.choice(['red','blue','green'])
			shapes=random.choice(['square','circle'])
			for segement in segements:
				segement.goto(1000,1000)
			segements.clear()

			score =0
			delay =0.1
			pen.clear()
			pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=('arial',24,'bold'))
	time.sleep(delay)

wn.mainloop()
