from turtle import Turtle
DATA_FILE_NAME = 'data.txt'
class ScoreBoard(Turtle):

    def __init__(self, height: int):
        super().__init__()
        self.hideturtle()
        self.penup()
        top_y = height // 2 - 15
        self.goto(0, top_y)
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.color("white")
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 8, "bold"),)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_high_score(self):
        with open(DATA_FILE_NAME) as file:
            self.high_score = int(file.read())

    def write_high_score(self):
        with open(DATA_FILE_NAME, mode="w") as file:
            file.write(str(self.high_score))