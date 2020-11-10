from tkinter import *
import random
import time


def screen():
    global r
    global button

    master.title("Speed Type Test")
    master.geometry("800x500+550+200")
    master.config(bg="black")

    # Top (t) frame
    t = Frame(master, width=800, height=100, bg="black")
    t.pack(pady=10, padx=10)
    # Propagate tells frame to not let its children determine it's size
    t.pack_propagate(0)

    title = Label(t, text="Typing Speed Test", font=("Comic Sans MS", 32), fg="white", bg="black")
    title.pack(pady=15)

    m = Frame(master, width=800, height=50, bg="black")
    m.pack(pady=10, padx=10)
    m.propagate(0)

    r_sentence = Label(m, textvariable=random_sent, bg="black")
    r_sentence.pack()

    # Entry frame
    entry_frame = Frame(master, width=800, height=50, bg="black",
                        highlightbackground="green", highlightcolor="green", highlightthickness=3)
    entry_frame.pack(padx=15, pady=15)
    entry_frame.propagate(0)
    entry = Entry(entry_frame, font=("calibri", 16), bg="black", fg="white",
                  insertbackground="white")
    entry.pack(expand=TRUE, fill=BOTH)
    entry.focus_set()

    # Bottom (b) frame
    b = Frame(master, height=50, width=800, bg="black")
    b.pack()
    b.pack_propagate(0)

    # Default equal/incorrect input labels
    response = Label(b, fg="#ff3300", font=("calibri", 18), bg="black", width=100)

    # Frame that holds START/STOP
    go_frame = Frame(master, width=800, height=70, bg="black")
    go_frame.bind("<Return>", started)
    go_frame.pack()
    go_frame.propagate(0)

    # START Button
    button = Button(go_frame, text="START", font="calibri, 18", command=started, fg="white")
    button.pack(side=TOP, pady=10)
    button.config(bg="green")

    # Results Frame
    r = Frame(master, width=800, height=100, bg="black")
    r.pack()
    r.propagate(0)


# generate a random sentence
def random_sent():
    global total_words
    global r_sentence
    global sentence

    with open('sentences.txt', 'r') as f:
        r_sentence.destroy()
        content = f.read()
        sentences = content.splitlines()
        sentence = random.choice(sentences)
        r_sentence = Label(m, text=f"{sentence}", fg="white", font=("calibri", 18), bg="black")
        r_sentence.pack()

        # generate a mis-match sentence


def incorrect_info():
    global fail
    global response

    response.destroy()

    with open('incorrect.txt', 'r') as f:
        content = f.read()
        fails = content.splitlines()
        fail = random.choice(fails)
        response = Label(b, text=f"{fail}", fg="#ff3300", font=("calibri", 18), bg="black")
        response.pack()


# calculate and return words per minute
def words_per_minute():

    keystrokes = len(sentence)
    words_per_min = round(keystrokes * 60) / total / 5
    wpm_rounded = int(words_per_min)
    wpm = Label(r, text=f"WPM: {wpm_rounded}", fg="lightgrey", font=("calibri", 18), bg="black")
    wpm.pack()


    # Processes STOP and also displays start button
def stop(event=None):
    global end
    global entry
    global total
    global total_time

    u_entry()
    # delete user entry once submitted
    entry.delete(0, 'end')
    # destroys previous button
    button.destroy()
    # ends the clock
    end = time.time()
    # total time rounded 3 dp
    total = end-start
    total_rounded = round(total, 3)

    print("Stopped. Hit START to go again.")

    # START! BUTTON
    button = Button(go_frame, text="START", font="calibri, 18", command=reset_all, fg="white",
                            width=10)
    button.pack(side=TOP, pady=10)
    button.config(bg="green")
    total_time = Label(r, text=f"TIME: {total_rounded}s", fg="lightgrey", bg="black",
                                        font="calibri 18")
    total_time.pack()
    words_per_minute()

def reset_all():
    # reset all results
    total_time.destroy()
    response.destroy()
    wpm.destroy()
    # Run started
    started()

def u_entry():
    u_input = entry.get()
    if sentence == u_input:
        response.destroy()
        response = Label(b, text=f"Well Done!", fg="green", font=("calibri", 18), bg="black")
        response.pack()
    else:
        incorrect_info()


def started():
    global start
    # starts the clock
    start = time.time()
    # Grabs random sentence
    random_sent()
    # Destroys previous button
    button.destroy()
    print("Started. Click ENTER to Stop.")
    # STOP! BUTTON
    button = Button(go_frame, text="STOP!", font="calibri, 18", command=stop, fg="white", width=10)
    button.pack(side=TOP, pady=10)
    button.config(bg="red")
    master.bind("<Return>", stop)

    # Default equal/incorrect input labels
    """response = Label(b, fg="#ff3300", font=("calibri", 18), bg="black", width=100)

    # Frame that holds START/STOP
    go_frame = Frame(master, width=800, height=70, bg="black")
    go_frame.bind("<Return>", started)
    go_frame.pack()
    go_frame.propagate(0)

    # START Button
    button = Button(go_frame, text="START", font="calibri, 18", command=started, fg="white")
    button.pack(side=TOP, pady=10)
    button.config(bg="green")

    # Results Frame
    r = Frame(master, width=800, height=100, bg="black")
    r.pack()
    r.propagate(0)"""


master = Tk()
screen()
master.mainloop()
