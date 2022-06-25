from tkinter import *
import time
import threading
import random
import ctypes
import pygame.mixer

ctypes.windll.shcore.SetProcessDpiAwareness(1)

app = Tk()
app.title('math games')
app.config(bg='#181b1f')
app.geometry('700x500')
timer_first_condition = True
timer_second_condition = True


pygame.mixer.init()


def right_answer():
    pygame.mixer.music.load('right answer.mp3')
    pygame.mixer.music.play(0)


def wrong_answer():
    pygame.mixer.music.load('wrong answer.mp3')
    pygame.mixer.music.play(0)


def timer():
    global timer_first_condition, timer_second_condition, s
    mil_sec = 0
    sec = 0
    m = 0
    hour = 0
    while True:
        if timer_first_condition:
            if mil_sec < 9:
                mil_sec += 1
                time.sleep(.1)
                str(hour)
                str(m)
                str(sec)
                str(mil_sec)
                a = f'{hour}:{m}:{sec}:{mil_sec}0'
                timer_label.configure(text=a)
            else:
                mil_sec = 0
                sec += 1
                time.sleep(.1)
                str(hour)
                str(m)
                str(sec)
                str(mil_sec)
                print(sec)
                a = f'{hour}:{m}:{sec}:{mil_sec}0'
                timer_label.configure(text=a)
            if sec != 59 and mil_sec == 9:
                mil_sec = 0
                sec += 1
                time.sleep(.1)
                str(hour)
                str(m)
                str(sec)
                str(mil_sec)
                a = f'{hour}:{m}:{sec}:{mil_sec}0'
                timer_label.configure(text=a)
            if sec == 59 and mil_sec == 9:
                mil_sec = 0
                sec = 0
                m += 1
                str(hour)
                str(m)
                str(sec)
                str(mil_sec)
                a = f'{hour}:{m}:{sec}:{mil_sec}0'
                timer_label.configure(text=a)
            if m == 59 and sec == 59 and mil_sec == 9:
                mil_sec = 0
                sec = 0
                m = 0
                hour += 1
                str(hour)
                str(m)
                str(sec)
                str(mil_sec)
                a = f'{hour}:{m}:{sec}:{mil_sec}0'
                timer_label.configure(text=a)
            if not timer_first_condition and timer_second_condition:
                mil_sec = 0
                sec = 0
                m = 0
                hour = 0
                a = f'{hour}:{m}:{sec}:{mil_sec}0'
                timer_label.configure(text=a)
                timer_first_condition = True
            if not timer_first_condition and not timer_second_condition:
                a = f'{hour}:{m}:{sec}:{mil_sec}0'
                timer_label.configure(text=a)
                mil_sec = 0
                sec = 0
                m = 0
                hour = 0


t = threading.Thread(target=timer, daemon=True)
start_points = 0
points = 0
starts = 0
starting_times = 0


def start():
    global start_points, points, timer_first_condition, starts, timer_second_condition
    label6.config(text=':)')
    timer_first_condition = True
    timer_second_condition = True
    start_points = 0
    points = 0
    points_label.config(text=f'{points}/5')
    answer_entry.delete(0, END)
    cal(event=False)
    if starts != 0:
        starts = 1
        timer_first_condition = False
        timer_second_condition = True

    if starts == 0:
        starts += 1
        t.start()
    app.bind("<Return>", cal)


def math_game():
    global r, x, y
    number_list = [2, 3, 4, 5, 6, 7, 8, 9]
    if start_points == 1:
        x = random.choice(number_list)
        y = random.choice(number_list)
        r = x + y
    if start_points == 2:
        x = random.choice(number_list)
        y = random.choice(number_list)
        if x > y:
            r = x - y
        if x == y:
            r = x - y
        if x < y:
            r = y - x
    if start_points == 3:
        x = random.choice(number_list)
        y = random.choice(number_list)
        r = x * y
    if start_points == 4:
        x = random.choice(number_list)
        y = random.choice(number_list)
        r = x * y
    if start_points == 5:
        x = random.choice(number_list)
        y = random.choice(number_list)
        r = x * y


def cal(event):
    global start_points, timer_first_condition, points, timer_second_condition
    try:
        answer = int(answer_entry.get())
        if type(answer) == int:
            start_points += 1

    except ValueError:
        if start_points == 0:
            start_points += 1

        else:
            return label6.config(text='numbers only :)')
    if start_points == 1:
        math_game()
        question_label.config(text=f'{x} + {y} = ')
    if start_points == 2:
        answer = int(answer_entry.get())
        if r == answer:
            points += 1
            right_answer()
        else:wrong_answer()
        points_label.config(text=f'{points}/5')
        math_game()
        if x > y:
            question_label.config(text=f'{x} - {y} = ')
        if x == y:
            question_label.config(text=f'{x} - {y} = ')
        if x < y:
            question_label.config(text=f'{y} - {x} = ')
        answer_entry.delete(0, END)
    if start_points == 3:
        answer = int(answer_entry.get())
        if r == answer:
            points += 1
            right_answer()
        else:
            wrong_answer()
        points_label.config(text=f'{points}/5')
        math_game()
        question_label.config(text=f'{x} x {y} = ')
        answer_entry.delete(0, END)
    if start_points == 4:
        answer = int(answer_entry.get())
        if r == answer:
            points += 1
            right_answer()
        else:
            wrong_answer()
        points_label.config(text=f'{points}/5')
        math_game()
        question_label.config(text=f'{x} x {y} = ')
        answer_entry.delete(0, END)
    if start_points == 5:
        answer = int(answer_entry.get())
        if r == answer:
            points += 1
            right_answer()
        else:
            wrong_answer()
        points_label.config(text=f'{points}/5')
        math_game()
        question_label.config(text=f'{x} x {y} = ')
        answer_entry.delete(0, END)
    if start_points == 6:
        answer = int(answer_entry.get())
        if r == answer:
            points += 1
            right_answer()
        else:wrong_answer()
        points_label.config(text=f'{points}/5')
        answer_entry.delete(0, END)

        timer_first_condition = False
        timer_second_condition = False
        question_label.config(text='you finished all the questions !!', font=15)


font_color = '#7FFF4D'
credit_label = Label(app, text='developer: @dev_iQ8', fg=font_color, bg='#181b1f')
timer_label = Label(app, text='00:00:00:00', fg=font_color, bg='#181b1f')
time_label = Label(app, text='Timer', fg=font_color, bg='#181b1f')
points_label = Label(app, text='Points', fg=font_color, bg='#181b1f')
question_label = Label(app, text='question', fg=font_color, font=29, bg='#181b1f')
start_button = Button(app, text='Start', fg=font_color, bg='#181b1f', command=start)
answer_entry = Entry(app, width=30, )
label6 = Label(app, text=' press start :)', bd=1, relief=SUNKEN, anchor=E, bg='#181b1f', fg=font_color)

timer_label.place(relx=0.2, rely=0.15, anchor=CENTER)
time_label.place(relx=0.2, rely=0.1, anchor=CENTER)
question_label.place(relx=0.5, rely=0.1, anchor=CENTER)
points_label.place(relx=0.8, rely=0.1, anchor=CENTER)
start_button.pack()
credit_label.place(relx=0.5, rely=0.9, anchor=CENTER)
answer_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
label6.pack(fill=X, side=BOTTOM, ipady=4)


answer_entry.focus_set()
app.mainloop()
