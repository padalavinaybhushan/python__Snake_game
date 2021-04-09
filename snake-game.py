import turtle as t
import  random as r
import time as ti

t.bgcolor('yellow')

#we require fpur turtles

snake = t.Turtle()
leaf = t.Turtle()

score = t.Turtle()

#defining initial condition for each turtle

snake.shape('square')
snake.speed(0)
snake.penup()
snake.hideturtle()

leaf_shape= ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed(0)
leaf.hideturtle()

gtext = False
gtext = t.Turtle()
gtext1 = t.Turtle()
gtext.write('press space to start',align='center',font=('Arial',18,'bold'))
gtext.hideturtle()
x1 = (t.window_width() / 2) - 380
y1 = (t.window_height()/ 2) - 50
gtext1.penup()
gtext1.setpos(x1, y1)
gtext1.write('Designed by vinay bhushan',align='center',font=('Arial',8,'bold'))
gtext1.hideturtle()

score.speed(0)
score.hideturtle()

def outside_window():
    left_wall = -t.window_width()/2
    right_wall  = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = snake.pos()
    outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
    return outside

def place_leaf():
    leaf.hideturtle()
    leaf.setx(r.randint(-200,200))
    leaf.sety(r.randint(-200,200))
    leaf.showturtle()

def game_over():
    snake.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('game over ',align='center',font=('Arial',18,'bold'))

def display_score(cu_score):
    score.clear()
    score.penup()
    x = (t.window_width()/2)-50
    y = (t.window_height()/2)-50
    score.setpos(x, y)
    score.write(str(cu_score),align='right',font=('Arial',18,'bold'))


def start_game():
    global game_started
    if game_started :
        return
    game_started = True
    s = 0
    gtext.clear()

    snake_speed=2
    snake_len=3
    snake.shapesize(1,snake_len,1)
    snake.showturtle()
    display_score(s)
    place_leaf()

    while True:
        snake.forward(snake_speed)
        if snake.distance(leaf) < 20:
            place_leaf()
            snake_len = snake_len+1
            snake.shapesize(1,snake_len,1)
            snake_speed = snake_speed+1
            s = s+10
            display_score(s)
        if outside_window():
            game_over()
            break


def move_up():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def move_down():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def move_left():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def move_right():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)


game_started = False
t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()

#for output

ti.sleep(10)
t.hideturtle()
