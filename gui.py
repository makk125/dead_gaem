from tkinter import *
from tkinter import messagebox
import random
import math

first_number = 0
second_number = 0
third_number = 0
fourth_number = 0
start_timer = None
num = 120
user_guess = []


def click_one():
    global user_guess
    user_guess.append(1)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_two():
    global user_guess
    user_guess.append(2)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_three():
    global user_guess
    user_guess.append(3)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_four():
    global user_guess
    user_guess.append(4)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_five():
    global user_guess
    user_guess.append(5)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_six():
    global user_guess
    user_guess.append(6)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_seven():
    global user_guess
    user_guess.append(7)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_eight():
    global user_guess
    user_guess.append(8)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_nine():
    global user_guess
    user_guess.append(9)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_zero():
    global user_guess
    user_guess.append(0)
    canvas.itemconfig(bomb_start_text, text=user_guess)


def click_asterisk():
    global user_guess
    global first_number
    global second_number
    global third_number
    global fourth_number
    global num
    bomb_timer(num)

    canvas.itemconfig(bomb_text, text="",)
    canvas.itemconfig(bomb_start_text, text="Guess the 4 pin code to defuse the bomb!", fill = "black")
    canvas.itemconfig(timer_text, fill = "red")
    user_guess = []

    first_number = random.randint(1, 9)
    second_number = random.randint(0, 9)
    third_number = random.randint(0, 9)
    fourth_number = random.randint(0, 9)


def click_hashtag():
    global user_guess
    global start_timer

    counter = 0
    if user_guess[0] == first_number:
        counter += 1
    if user_guess[1] == second_number:
        counter += 1
    if user_guess[2] == third_number:
        counter += 1
    if user_guess[3] == fourth_number:
        counter += 1
    if counter == 4:
        canvas.itemconfig(bomb_start_text, text=f"You got it  right! the number is "
                                                f"{user_guess[0]}{user_guess[1]}{user_guess[2]}{user_guess[3]}")
        my_window.after_cancel(start_timer)
        canvas.itemconfig(timer_text, text="00:00", fill = "green")
        button_one.config(state = 'disabled')
        button_two.config(state='disabled')
        button_three.config(state='disabled')
        button_four.config(state='disabled')
        button_five.config(state='disabled')
        button_six.config(state='disabled')
        button_seven.config(state='disabled')
        button_eight.config(state='disabled')
        button_nine.config(state='disabled')
        button_zero.config(state='disabled')
        button_hashtag.config(state='disabled')


    else:
        canvas.itemconfig(bomb_start_text, text=f"You got {counter} correct number.")
        user_guess = []


def click_info():
    messagebox.showinfo(title='How to play the game', message="You have 2 minutes to decode the password or else the "
                                                              "bomb will explode. You have unlimited tries but if "
                                                              "you ran out of time it's game over. After each game if "
                                                              "you want to play again click the asterisk '*' button. "
                                                              "Thank you and have fun.")

def bomb_timer(num):
    global start_timer

    count_min = math.floor(num / 60)
    count_sec = num % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if num > 0:
        start_timer = my_window.after(1000, bomb_timer, num - 1)
    else:
        canvas.itemconfig(bomb_start_text, text="Game Over!! Terrorist wins!", fill = 'red')
        button_one.config(state='disabled')
        button_two.config(state='disabled')
        button_three.config(state='disabled')
        button_four.config(state='disabled')
        button_five.config(state='disabled')
        button_six.config(state='disabled')
        button_seven.config(state='disabled')
        button_eight.config(state='disabled')
        button_nine.config(state='disabled')
        button_zero.config(state='disabled')
        button_hashtag.config(state='disabled')



my_window = Tk()
my_window.title("Guess the Password")

canvas = Canvas(width=420, height=560, highlightthickness=0)
bomb_image = PhotoImage(file='images/bomb2.png')
bomb = canvas.create_image(210, 280, image=bomb_image)
canvas.grid()
bomb_text = canvas.create_text(225, 165, width=150, text="Click * to start the game!")
bomb_start_text = canvas.create_text(235,165, width = 150, text = '')
timer_text = canvas.create_text(165,150, text = '', fill = 'red')

one_image = PhotoImage(file="images/one.png")
button_one = Button(image=one_image, highlightthickness=0, command=click_one)
button_one.place(relx=.38, rely=.545)

two_image = PhotoImage(file="images/two.png")
button_two = Button(image=two_image, highlightthickness=0, command=click_two)
button_two.place(relx=.46, rely=.545)

three_image = PhotoImage(file="images/three.png")
button_three = Button(image=three_image, highlightthickness=0, command=click_three)
button_three.place(relx=.55, rely=.545)

four_image = PhotoImage(file="images/four.png")
button_four = Button(image=four_image, highlightthickness=0, command=click_four)
button_four.place(relx=.38, rely=.605)

five_image = PhotoImage(file="images/five.png")
button_five = Button(image=five_image, highlightthickness=0, command=click_five)
button_five.place(relx=.46, rely=.605)

six_image = PhotoImage(file="images/six.png")
button_six = Button(image=six_image, highlightthickness=0, command=click_six)
button_six.place(relx=.55, rely=.605)

seven_image = PhotoImage(file="images/seven.png")
button_seven = Button(image=seven_image, highlightthickness=0, command=click_seven)
button_seven.place(relx=.38, rely=.67)

eight_image = PhotoImage(file="images/eight.png")
button_eight = Button(image=eight_image, highlightthickness=0, command=click_eight)
button_eight.place(relx=.46, rely=.67)

nine_image = PhotoImage(file="images/nine.png")
button_nine = Button(image=nine_image, highlightthickness=0, command=click_nine)
button_nine.place(relx=.55, rely=.67)

zero_image = PhotoImage(file="images/zero.png")
button_zero = Button(image=zero_image, highlightthickness=0, command=click_zero)
button_zero.place(relx=.46, rely=.73)

hashtag_image = PhotoImage(file="images/clear.png")
button_hashtag = Button(image=hashtag_image, highlightthickness=0, command=click_hashtag)
button_hashtag.place(relx=.55, rely=.73)

asterisk_image = PhotoImage(file="images/asterisk.png")
button_asterisk = Button(image=asterisk_image, highlightthickness=0, command=click_asterisk)
button_asterisk.place(relx=.38, rely=.73)

info_button = Button(text="Click for more information.", highlightthickness=0, bg="green", command=click_info)
info_button.place(relx=.33, rely=.83)

my_window.mainloop()
