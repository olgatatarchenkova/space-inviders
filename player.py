from turtle import Turtle

PLAYERSPEED = 15
BULLETSPEED = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("blue")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)
        self.showturtle()

    # Move the player left and right
    def move_left(self):
        x = self.xcor()
        x -= PLAYERSPEED
        if x < -280:
            x = -280
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += PLAYERSPEED
        if x > 280:
            x = 280
        self.setx(x)


class Pbullet(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.shapesize(0.5, 0.5)
        self.setheading(90)

    def fire(self, player):
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        self.setposition(x, y)
        self.showturtle()

    def move_bullet(self):
        y = self.ycor()
        y += BULLETSPEED
        self.sety(y)
