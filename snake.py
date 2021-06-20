from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_new_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[seg_num - 1].xcor()
            y_new = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_new, y_new)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.move()
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_new_segment(self, position):
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_new_segment(self.segments[-1].position())
