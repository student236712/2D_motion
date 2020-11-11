from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 700

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Bouncing balls")
canvas.pack()

BALL_SIZE = 35
BALL_COLOUR = "steel blue"
start_X_1_position = random.randrange(0, WIDTH - BALL_SIZE)
start_Y_1_position = random.randrange(0, HEIGHT - BALL_SIZE)


class Ball:
    def __init__(self, start_x_1_position, start_y_1_position, color, size):
        self.color = color
        self.shape = canvas.create_oval(start_x_1_position, start_y_1_position, start_x_1_position + size,
                                        start_y_1_position + size, fill=color)
        self.xspeed = random.randrange(-10, 10)
        self.yspeed = random.randrange(-10, 10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed


BALL_SIZE = 35

balls = []
balls.append(Ball(random.randrange(0, WIDTH - BALL_SIZE), random.randrange(0, HEIGHT - BALL_SIZE), "steel blue",
                  BALL_SIZE))
balls.append(Ball(random.randrange(0, WIDTH - BALL_SIZE), random.randrange(0, HEIGHT - BALL_SIZE), "maroon", BALL_SIZE))
balls.append(Ball(random.randrange(0, WIDTH - BALL_SIZE), random.randrange(0, HEIGHT - BALL_SIZE), "salmon1", BALL_SIZE))

while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
