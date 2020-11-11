from tkinter import *
import random
import time
import numpy as np

WIDTH = 1200
HEIGHT = 1000

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Balls 2D motion")
canvas.pack()


class Ball:
    def __init__(self, start_x_1_position, start_y_1_position, color, size):
        self.color = color
        self.size = size
        self.shape = canvas.create_oval(start_x_1_position, start_y_1_position, start_x_1_position + size,
                                        start_y_1_position + size, fill=color)
        self.xspeed = random.randrange(-10, 10)
        self.yspeed = random.randrange(-10, 10)

    def move_with_breaking_walls(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT:
            canvas.delete(self.shape)
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

    def move_with_bouncing(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

    def move_with_collision(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        for ball in balls:
            distance_between_balls_centres = np.sqrt(
                np.power(
                    (canvas.coords(ball.shape)[0] + canvas.coords(ball.shape)[2]) / 2 - (canvas.coords(self.shape)[0] +
                                                                                         canvas.coords(self.shape)[
                                                                                             2]) / 2,
                    2) + np.power(
                    (canvas.coords(ball.shape)[1] + canvas.coords(ball.shape)[3]) / 2 - (canvas.coords(self.shape)[1] +
                                                                                         canvas.coords(self.shape)[
                                                                                             3]) / 2,
                    2))

            if ball != self and distance_between_balls_centres <= (ball.size + self.size) / 2:
                two_balls_size = self.size + ball.size
                x_speed_after_collision = (self.xspeed*self.size + ball.xspeed*ball.size) / two_balls_size
                y_speed_after_collision = (self.yspeed*self.size + ball.yspeed*ball.size) / two_balls_size
                canvas.delete(ball.shape)
                balls.remove(ball)
                canvas.delete(self.shape)
                self.size = two_balls_size
                self.shape = canvas.create_oval(pos[0], pos[1], pos[0] + self.size, pos[1] + self.size)
                self.xspeed = x_speed_after_collision
                self.yspeed = y_speed_after_collision
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed


BALL_SIZE = 20
balls = []
balls.append(Ball(random.randrange(0, WIDTH - BALL_SIZE), random.randrange(0, HEIGHT - BALL_SIZE), "steel blue",
                  BALL_SIZE))
balls.append(Ball(random.randrange(0, WIDTH - BALL_SIZE), random.randrange(0, HEIGHT - BALL_SIZE), "maroon", BALL_SIZE))
balls.append(
    Ball(random.randrange(0, WIDTH - BALL_SIZE), random.randrange(0, HEIGHT - BALL_SIZE), "salmon1", BALL_SIZE))
balls.append(
    Ball(random.randrange(0, WIDTH - BALL_SIZE), random.randrange(0, HEIGHT - BALL_SIZE), "black", BALL_SIZE))
balls.append(
    Ball(random.randrange(0, WIDTH - BALL_SIZE), random.randrange(0, HEIGHT - BALL_SIZE), "red", BALL_SIZE))
balls.append(
    Ball(random.randrange(0, WIDTH - BALL_SIZE), random.randrange(0, HEIGHT - BALL_SIZE), "grey", BALL_SIZE))
while True:
    for ball in balls:
        ball.move_with_collision()

    tk.update()
    time.sleep(0.01)

tk.mainloop()
