from turtle import Screen, Turtle
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVING_BLOCKS = 20
# screen = Screen()
# screen.setup(600, 600)
# screen.bgcolor('pink')
# screen.title("My Snake Game")
# screen.tracer(0)

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle()
            new_segment.color(COLORS[i])
            new_segment.shape('square')
            new_segment.penup()
            new_segment.goto(INITIAL_POSITIONS[i])
            self.segments.append(new_segment)
            #self.snake_head = self.segments[0]
            # print(self.segments)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVING_BLOCKS)

    def increase_snake_size(self):

        new_segment = Turtle()
        new_segment.color('green')
        new_segment.shape('square')
        new_segment.penup()
        self.segments.append(new_segment)
        self.move()

    # s1=Snake()
    # s1.move()

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def snake_self_collision(self):
        for seg in self.segments[1:]:
            if self.snake_head.distance(seg) < 15:
                return True

    #def snake_collision_with_wall(self):
        # self.snake_head.xcor()>280 or self.snake_head.xcor()<-280 or self.snake_head.ycor()>280 or self.snake_head.ycor<-280:
        # True
