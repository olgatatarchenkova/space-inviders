from turtle import Turtle

ENEMY_BULLETSPEED = 20


class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed(0)

    def move(self, enemies, enemyspeed):
        x = self.xcor()
        x += enemyspeed
        self.setx(x)


class Ebullet(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.shapesize(0.5, 0.5)
        self.setheading(270)

    def fire(self, enemy):
        # Move the bullet to just below the enemy
        x = enemy.xcor()
        y = enemy.ycor() - 10
        self.setposition(x, y)
        self.showturtle()

    def move_bullet(self):
        y = self.ycor()
        y -= ENEMY_BULLETSPEED
        self.sety(y)
