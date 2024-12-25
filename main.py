import tkinter
from tkinter import *
import math


window = Tk()
window.title("Timer")

# ---------------------------- CONSTANTS ------------------------------- #
GRAY = "#212020"
WHITE = "#f5f5f5"
BLACK = "#0a0a0a"
YELLOW = "#ffcc33"
RED = "#f75454"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

time_running = False
current_time = WORK_MIN * 60
current_count = 0

# ---------------------------- BUTTONS MECHANISM ----------------------------- #
def reset_button_clicked():
    global time_running, current_time
    time_running = False
    current_time = WORK_MIN * 60
    canvas.itemconfig(timer_text, text="00:00")
    start.config(text="Start", command=start_button_clicked,background=BLACK, fg= WHITE)
    print("Reset button clicked")


def start_button_clicked():
    global time_running
    if not time_running:
        time_running = True
        reset.config(state="disabled",background=GRAY)
        count_down(WORK_MIN * 60)
        start.config(text="Pause", command=pause_button_clicked,background=RED,fg=BLACK)
        print("Start button clicked")


def pause_button_clicked():
    global time_running
    if time_running:
        time_running = False
        reset.config(state="normal",background=BLACK)
        start.config(text="Resume", command=resume_button_clicked,background=BLACK,fg=WHITE)
        print("Pause button clicked")

def resume_button_clicked():
    global current_count, time_running, count
    if current_count > 0:
        time_running = True
        reset.config(state="disabled", background=GRAY)
        count_down(current_count -1)
        start.config(text="Pause", command=pause_button_clicked,background=RED,fg=BLACK)
        print("Resume button clicked")

# ---------------------------- TIMER MECHANISM ------------------------------- #







# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global time_running, current_time, current_count
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=(f"{count_min}:{count_sec}"))
    if count > 0 and time_running:
        window.after(1000, count_down, count - 1)
        current_count = count
    else:
        time_running = False
        print("Countdown finished ")


# ---------------------------- UI SETUP ------------------------------- #


#IMAGE AND CANVAS
window.config(padx=0, pady=0, bg=YELLOW)
canvas = Canvas(width=400, height=330, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="cat.png")
canvas.create_image(205, 120, image=tomato, anchor="center")
timer_text = canvas.create_text(205, 300, text="00:00", fill="black", font=(FONT_NAME, 30, "bold"))

canvas.pack()

#UI buttons
reset = tkinter.Button(window, text="Reset", command=reset_button_clicked, activebackground=YELLOW, justify="left", background=BLACK, fg= "white",
                       height=1, width=8)
reset.pack(side="left", padx=20, pady=20)

start = tkinter.Button(window, text="Start", fg= "white", command=start_button_clicked, activebackground=YELLOW, background=BLACK, justify="left",
                       height=1, width=8)
start.pack(side="right", padx=20, pady=20)



window.mainloop()
