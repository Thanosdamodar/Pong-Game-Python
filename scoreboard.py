from turtle import  Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.update_score()

    def r_score(self):
        self.right_score += 1


    def l_score(self):
        self.left_score += 1

    def update_score(self):
        self.clear()
        self.write(f"{self.left_score}  {self.right_score}", False, "center", ("Courier", 50, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Courier", 70, "bold"))
        self.goto(0, -60)
        self.write(f"Left - {self.left_score}\nRight - {self.right_score}", False, "center", ("Courier", 20, "normal"))
