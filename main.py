from tkinter import *
import random
import time

global entry

# Tk window creation
master = Tk()
master.title("Speed Type Test")
master.geometry("800x500+550+200")
master.config(bg="black")


# Title
title = Label(master, text="Typing Speed Test", font=("Comic Sans MS", 32), fg="white", bg="black")
title.place(x=200, y=25)


# Generate random sentence
def random_sent():
    global sentence
    with open('responses/sentences.txt', 'r') as f:
        content = f.read()
        sentences = content.splitlines()
        sentence = random.choice(sentences)
        random_sentence = Label(master, text=f"{sentence}", fg="white", font=("calibri", 17), bg="black")
        random_sentence.place(x=50, y=150, width=700, height=40)


# Display random sentence
r_sentence = Label(master, bg="black", textvariable=random_sent, fg="white")

# User entry box
entry = Entry(master, font=("calibri", 16), bg="black", fg="white", highlightbackground="green",
              highlightcolor="green", highlightthickness=3, insertbackground="white")
entry.place(x=50, y=220, width=700, height=50)


def start():
    global started
    # starts the clock
    started = time.time()
    # Grabs and displays random sentence
    random_sent()
    # Destroys previous button
    print("Started. Click ENTER to Stop.")
    # STOP! BUTTON
    button = Button(master, text="STOP!", font="calibri, 18", fg="white",
                    command=lambda: [button.place_forget(), check_entry()])
    button.place(x=350, y=325, width=100)
    button.config(bg="red")
    master.bind("<Return>", check_entry)


# START/STOP Button
button = Button(master, text="START", font="calibri, 18", fg="white", command=lambda: [button.place_forget(), start()])
button.place(x=350, y=325, width=100)
button.config(bg="green")


# Processes STOP and displays START button
def stop(event=None):
    global total
    # delete user entry once submitted
    entry.delete(0, 'end')
    # ends the clock
    end = time.time()
    # total time rounded 3 dp
    total = end - started
    total_rounded = round(total, 3)
    # Display WPM
    words_per_minute()

    print("Stopped. Hit START to go again.")

    # Clock stopped display START! button
    button = Button(master, text="START", font="calibri, 18", fg="white",
                                command=lambda: [button.place_forget(), start(), total_time.place_forget(),
                                                 wpm.place_forget(), response.place_forget()])
    button.place(x=350, y=325, width=100)
    button.config(bg="green")
    total_time = Label(master, text=f"TIME: {total_rounded}s", fg="lightgrey", bg="black",
                                font="calibri 18")
    response = Label(master, text=f"Well Done!", fg="green", font=("calibri", 18), bg="black")
    response.place(x=342, y=280)
    total_time.place(x=330, y=440)


# Display incorrect entry message
def incorrect_input():
    global response
    with open('responses/incorrect.txt', 'r') as f:
        content = f.read()
        fails = content.splitlines()
        fail = random.choice(fails)
        response = Label(master, text=f"{fail}", fg="#ff3300", font=("calibri", 18), bg="black")
        response.place(x=250, y=400)
        button = Button(master, text="START", font="calibri, 18", fg="white",
                        command=lambda: [button.place_forget(), response.place_forget(), start()])
        button.place(x=350, y=325, width=100)
        button.config(bg="green")


# Check user entry to determine what results are shown
def check_entry(event=None):
    user_input = entry.get()
    if sentence == user_input:
        stop()
    else:
        incorrect_input()


# Calculate WPM
def words_per_minute():
    global wpm
    keystrokes = len(sentence)
    words_per_min = round(keystrokes * 60) / total / 5
    wpm_rounded = int(words_per_min)
    wpm = Label(master, text=f"WPM: {wpm_rounded}", fg="lightgrey", font=("calibri", 18), bg="black")
    wpm.place(x=350, y=400)


master.mainloop()
