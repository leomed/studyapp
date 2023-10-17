from tkinter import *
import pygame

import math

RED = "#E73365B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

reps = 0

check_reps = []

pygame.mixer.init()

window = Tk()
window.title("Pomodoro Simpson")
window.config()



def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    timer_title.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

def start_timer():

    global reps
    global check_reps
    reps +=1
    check_reps.append(reps)

    work_sec = WORK_MIN * 60
    short_breack_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        pygame.mixer.music.load("trasero.mp3")
        pygame.mixer.music.play()
        count_down(long_break_sec)

        timer_title = Label(text="Long Break", font=("Fixedsys", 30), fg="red")
        timer_title.config(padx=40, bg=YELLOW)
        timer_title.grid(column=2, row=1)

    elif reps % 2 == 0:
        window.attributes('-topmost' , 1)
        pygame.mixer.music.load("homerosound.mp3")
        pygame.mixer.music.play()
        timer_title = Label(text="Short Break", font=("Fixedsys", 30), fg="red")
        timer_title.config(padx=40, bg=YELLOW)
        timer_title.grid(column=2, row=1)

        count_down(short_breack_sec)
    else:

        pygame.mixer.music.load("homerocerebro.mp3")
        pygame.mixer.music.play()
        count_down(work_sec)




def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    """This is dymanic tiping in the if we are using a int but then 00 its a string"""
    if count_sec == 0:
        count_sec = "00"

    elif count_sec < 10:
        count_sec = f"0{count}"
    #How to change something in a canvas,text_timer is a variable
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    #This if prevents to go to negative numbers in the loop
    if count > 0:
        global timer
        """AFTER allows to do a loop in a GUI"""
        """count-1 is the input"""
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
            check_mark.config(text=mark)














"""How to use an image in tkinter"""
canvas = Canvas(width=400,height=400, bg="Black", highlightthickness=0)

homero_img = PhotoImage(file="asd.png")

canvas.create_image(150,330, image=homero_img)

text_timer = canvas.create_text(290,110, text="00:00" , font=("Fixedsys", 40), fill="grey")

canvas.grid(column=2, row=2)


timer_title = Label(text="Timer", font=("Fixedsys", 30) ,fg="green")
timer_title.config(padx=40, bg=YELLOW)
timer_title.grid(column=2,row=1)




start_btn = Button(text="Start", font="Fixedsys" , bg="YELLOW", highlightthickness=0, command=start_timer)
start_btn.grid(column=1, row=3)

reset_btn = Button(text="Reset" ,font="Fixedsys", bg="yellow", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=3,row=3)



check_mark = Label( font=(20))
check_mark.grid(column=2, row=4)


#Event Driven
window.mainloop()

