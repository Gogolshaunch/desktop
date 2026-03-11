from tkinter import *
import random
window = Tk()
window.configure(bg="white")
window.geometry("800x400")
window.title("Rolling The Dices Game")
window.resizable(0, 0)


def one():
    dice_dots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    a = random.choice(dice_dots)
    label.configure(text=f'{a}')
    label.pack()


def two():
    dice_dots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    a = random.choice(dice_dots)
    s = random.choice(dice_dots)
    label.configure(text=f'{a}{s}')
    label.pack()


def three():
    dice_dots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    a = random.choice(dice_dots)
    s = random.choice(dice_dots)
    d = random.choice(dice_dots)
    label.configure(text=f'{a}{s}{d}')
    label.pack()


def pvp():
    dice_dots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    a = random.choice(dice_dots)
    s = random.choice(dice_dots)
    label6 = Label(window, text='Игрок 1')
    label7 = Label(window, text='Игрок 2')
    label6.place(x=210, y=70)
    label7.place(x=550, y=70)
    label.configure(text=f'{a} {s}')
    label.pack()


label = Label(window, font=("times", 250), bg="white", fg="yellow")
label2 = Label(window, text='Сколько костей будете кидать?')
button1 = Button(window, text="1", font=20, bg="grey",
                     bd=2, command=one, height=2, width=4)
button2 = Button(window, text="2",font=20, bg="grey",
                     bd=2, command=two, height=2, width=4)
button3 = Button(window, text="3", font=20, bg="grey",
                     bd=2, command=three, height=2, width=4)
button4 = Button(window, text="Соревнование двух игроков", font=20, bg="grey",
                     bd=2, command=pvp, height=1)
label2.pack()
button1.place(x=40, y=25)
button2.place(x=380, y=25)
button3.place(x=700, y=25)
button4.place(x=280, y=350)

window.mainloop()
