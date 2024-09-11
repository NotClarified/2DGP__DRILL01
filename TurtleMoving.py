import turtle

turtle.shape('turtle')
move_distance = 50

# 각 방향키에 맞추어 50씩 이동

def move_up():
    turtle.setheading(90)
    turtle.forward(move_distance)
    turtle.stamp()

def move_down():
    turtle.setheading(270)
    turtle.forward(move_distance)
    turtle.stamp()

def move_left():
    turtle.setheading(180)
    turtle.forward(move_distance)
    turtle.stamp()

def move_right():
    turtle.setheading(0)
    turtle.forward(move_distance)
    turtle.stamp()

def reset_position():
    turtle.reset()

# 함수 호출
turtle.listen() 
turtle.onkey(move_up, "w")
turtle.onkey(move_down, "s")
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(reset_position, "Escape")

#터틀 실행
turtle.mainloop()  
