from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 700

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Balls breaking the walls")
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
        if pos[3] >= HEIGHT:
            canvas.delete(self.shape)
            # Create oval with coordinates x1,y1,x2,y2."""
            self.shape = canvas.create_oval(pos[0], 0, pos[2], BALL_SIZE, fill=self.color)
        if pos[1] <= 0:
            canvas.delete(self.shape)
            self.shape = canvas.create_oval(pos[0], HEIGHT, pos[2], HEIGHT - BALL_SIZE, fill=self.color)
        if pos[2] >= WIDTH:
            canvas.delete(self.shape)
            self.shape = canvas.create_oval(0, pos[1], BALL_SIZE, pos[3], fill=self.color)
        if pos[0] <= 0:
            canvas.delete(self.shape)
            self.shape = canvas.create_oval(WIDTH, pos[1], WIDTH - BALL_SIZE, pos[3], fill=self.color)


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
