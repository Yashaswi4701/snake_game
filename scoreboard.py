from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.sety(280)
        self.score = 0
        self.hideturtle()
        self.write(arg=f"Scoreboard={self.score}", move=False, align='center', font=('Arial', 15, 'normal'))



    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Scoreboard={self.score}", move=False, align='center', font=('Arial', 15, 'normal'))

    def game_over(self):
        self.color('white')
        self.sety(0)
        self.write(f"Game Over",move=False,align='center',font=('Arial',25,'normal'))
