from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 700

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Ball breaking the walls")
canvas.pack()

BALL_SIZE = 35
BALL_COLOUR = "steel blue"
start_X_1_position = random.randrange(0, WIDTH - BALL_SIZE)
start_Y_1_position = random.randrange(0, HEIGHT - BALL_SIZE)

ball = canvas.create_oval(start_X_1_position, start_Y_1_position, start_X_1_position + BALL_SIZE,
                          start_Y_1_position + BALL_SIZE, fill=BALL_COLOUR)
xspeed = random.randrange(-12, 12, 3)
yspeed = random.randrange(-12, 12, 3)

while True:
    canvas.move(ball, xspeed, yspeed)
    # pos = [left,top,right,bottom]
    pos = canvas.coords(ball)
    if pos[3] >= HEIGHT:
        canvas.delete(ball)
        # Create oval with coordinates x1,y1,x2,y2."""
        ball = canvas.create_oval(pos[0], 0, pos[2], BALL_SIZE, fill=BALL_COLOUR)
    if pos[1] <= 0:
        canvas.delete(ball)
        ball = canvas.create_oval(pos[0], HEIGHT, pos[2], HEIGHT - BALL_SIZE, fill=BALL_COLOUR)
    if pos[2] >= WIDTH:
        canvas.delete(ball)
        ball = canvas.create_oval(0, pos[1], BALL_SIZE, pos[3], fill=BALL_COLOUR)
    if pos[0] <= 0:
        canvas.delete(ball)
        ball = canvas.create_oval(WIDTH, pos[1], WIDTH - BALL_SIZE, pos[3], fill=BALL_COLOUR)
    tk.update()
    time.sleep(0.01)

tk.mainloop()
