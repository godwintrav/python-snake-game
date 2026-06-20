from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body: list[Turtle] = []
        self.__init_snake()
        self.head = self.body[0]

    def __init_snake(self):
        for i in range(0, 3):
            pos = (0, 0)
            if i > 0:
                previous_pos = self.body[i - 1].pos()
                pos = ((previous_pos[0] - 10), 0)
            self.add_segment(pos)

    def reset(self):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body.clear()
        self.__init_snake()
        self.head = self.body[0]

    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.setpos(position)
        self.body.append(turtle)

    def extend(self):
        self.add_segment(self.body[-1].position())


    def move(self):
        for part_num in range((len(self.body) - 1), 0, -1):
            previous_pos = self.body[part_num - 1].pos()
            self.body[part_num].setpos(previous_pos[0], previous_pos[1])
        self.body[0].forward(MOVE_DISTANCE)
        # self.set_snake_within_screen() USED TO ALLOW THE SNAKE MOVE BETWEEN SCREENS SO IF IT REACHES THE END IT COMES OUT OF THE OTHER SIDE

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # USED TO ALLOW THE SNAKE MOVE BETWEEN SCREENS SO IF IT REACHES THE END IT COMES OUT OF THE OTHER SIDE
    def set_snake_within_screen(self):
        end_pos = self.head.pos()
        print(end_pos)
        if self.head.heading() == RIGHT and end_pos[0] >= 300:
            self.head.setpos(-300, end_pos[1])
        if self.head.heading() == LEFT and end_pos[0] <= -300:
            self.head.setpos(300, end_pos[1])
        if self.head.heading() == UP and end_pos[1] >= 300:
            self.head.setpos(end_pos[0], -300)
        if self.head.heading() == DOWN and end_pos[1] <= -300:
            self.head.setpos(end_pos[0], 300)