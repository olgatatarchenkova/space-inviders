from turtle import Turtle


class BorderPen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(-300, -300)
        self.pendown()
        self.pensize(3)
        for _ in range(4):
            self.fd(600)
            self.lt(90)


class ScorePen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(-290, 270)


class LivesPen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(200, 270)


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(0, 0)
