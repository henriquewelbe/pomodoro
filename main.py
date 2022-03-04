from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ''
timer = '0'
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, marks
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0
    marks = ''
    checkbox.config(text=marks)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text='Work', fg=GREEN)
        countdown(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global marks, reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            if marks != '✔ ✔ ✔ ✔ ':
                marks += '✔ '
                checkbox.config(text=marks)
            else:
                marks = ''
                checkbox.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 48))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 32, 'bold'))
canvas.grid(row=1, column=1)

start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

checkbox = Label(fg=GREEN, bg=YELLOW)
checkbox.grid(row=3, column=1)

window.mainloop()
