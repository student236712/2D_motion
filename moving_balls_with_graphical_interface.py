import tkinter as tk
import moving_balls


def show_balls_animation():
    moving_balls.show_animation(e1.get(), e2.get(), variable.get(), balls_behaviour_variants)


def close_windows():
    moving_balls.close()
    master.quit()



master = tk.Tk()

tk.Label(master,
         text="Balls size").grid(row=0)
tk.Label(master,
         text="Balls amount").grid(row=1)
tk.Label(master,
         text="Balls behaviour").grid(row=2)
variable = tk.StringVar(master)
variable.set("Select from list")  # default value

balls_behaviour_variants = ["Bouncing", "Breaking walls", "Collisions"]
w = tk.OptionMenu(master, variable, *balls_behaviour_variants)
e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
w.grid(row=2, column=1)
master.title("Balls parameters")
master.geometry("500x400-500-500")

tk.Button(master,
          text='Quit',
          command=close_windows).grid(row=3,
                                      column=0,
                                      sticky=tk.W,
                                      pady=4)
tk.Button(master,
          text='Show', command=show_balls_animation).grid(row=3,
                                                          column=1,
                                                          sticky=tk.W,
                                                          pady=4)

tk.mainloop()
