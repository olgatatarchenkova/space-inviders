import turtle
import random
from player import *
from enemy import *
from board import *

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw the border
border_pen = BorderPen()

# Initialize game variables
score = 0
lives = 3

# Create score display
score_pen = ScorePen()
score_string = "Score: {}".format(score)
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

# Create lives display
lives_pen = LivesPen()
lives_string = "Lives: {}".format(lives)
lives_pen.write(lives_string, False, align="left", font=("Arial", 14, "normal"))

# Create the player turtle
player = Player()

# Create the player's bullet
bullet = Pbullet()

# Create the enemy
enemy_rows = 5
enemy_cols = 11
enemies = []

for row in range(enemy_rows):
    for col in range(enemy_cols):
        enemy = Enemy()
        x = -200 + col * 40
        y = 250 - row * 40
        enemy.setposition(x, y)
        enemies.append(enemy)
        enemy.showturtle()

enemyspeed = 2

# Create the enemy's bullet
enemy_bullet = Ebullet()
enemy_bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"


def fire_bullet():
    # Declare bulletstate as a global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        bullet.fire(player)


def fire_enemy_bullet():
    # Choose a random enemy to fire a bullet
    enemy = random.choice(enemies)
    enemy_bullet.fire(enemy)


def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 20:
        return True
    else:
        return False


# Create keyboard bindings
turtle.listen()
turtle.onkey(player.move_left, "Left")
turtle.onkey(player.move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Game over
game = GameOver()
game_string = "Game Over!"

game_over = False

# Main game loop
while not game_over:
    # Move the player
    x = player.xcor()
    if x < -280:
        x = -280
    elif x > 280:
        x = 280
    player.setx(x)

    # Move the enemy
    for enemy in enemies:
        enemy.move(enemies, enemyspeed)

        # Move the enemy back and down
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        # Check for collision between the bullet and the enemy
        if is_collision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            enemy.hideturtle()
            enemies.remove(enemy)
            # Update the score
            score += 10
            score_string = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        # Check for collision between the player and the enemy
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            game_over = True
            game.write(game_string, False, align="center", font=("Arial", 14, "normal"))
            break

        # Check if the enemy reaches the bottom of the screen
        if enemy.ycor() < -260:
            player.hideturtle()
            game_over = True
            game.write(game_string, False, align="center", font=("Arial", 14, "normal"))
            break

    # Move the bullet
    if bulletstate == "fire":
        bullet.move_bullet()

    # Check if the bullet reaches the top of the screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    # Move the enemy's bullet
    if enemy_bullet.isvisible():
        enemy_bullet.move_bullet()

    if enemy_bullet.ycor() < -275:
        enemy_bullet.hideturtle()

    # Check if the enemy's bullet hits the player
    if is_collision(player, enemy_bullet):
        enemy_bullet.hideturtle()
        lives -= 1
        lives_string = "Lives: {}".format(lives)
        lives_pen.clear()
        lives_pen.write(lives_string, False, align="left", font=("Arial", 14, "normal"))

        if lives == 0:
            player.hideturtle()
            game_over = True
            game.write(game_string, False, align="center", font=("Arial", 14, "normal"))
            break

    # Check if all enemies are defeated
    if len(enemies) == 0:
        # Increase the game difficulty
        enemyspeed *= 1.2
        enemy_bulletspeed *= 1.2

        # Create a new wave of enemies
        for row in range(enemy_rows):
            for col in range(enemy_cols):
                enemy = Enemy()
                x = -200 + col * 40
                y = 250 - (row + 1) * 40
                enemy.setposition(x, y)
                enemies.append(enemy)
                enemy.showturtle()

    # Randomly fire enemy bullets
    if not enemy_bullet.isvisible() and len(enemies) > 3:
        # if random.randint(0, 100) < 10:  # was 2
        fire_enemy_bullet()

wn.mainloop()
