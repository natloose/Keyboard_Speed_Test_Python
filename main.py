from tkinter import *
import random
import time


class Home:
    def __init__(self, master):
        self.master = master
        self.master.title("Speed Type Test")
        self.master.geometry("800x500+550+200")
        self.master.config(bg="black")

        # Top (t) frame
        self.t = Frame(master, width=800, height=100, bg="black")
        self.t.pack(pady=10, padx=10)
        # propagate tells frame to not let its children determine it's size
        self.t.pack_propagate(0)

        self.title = Label(self.t, text="Typing Speed Test", font=("Comic Sans MS", 32), fg="white", bg="black")
        self.title.pack(pady=15)

        # generate a random sentence
        def random_sent():
            global sentence
            global total_words

            with open('sentences.txt', 'r') as f:
                self.r_sentence.destroy()
                content = f.read()
                sentences = content.splitlines()
                sentence = random.choice(sentences)
                self.r_sentence = Label(self.m, text=f"{sentence}", fg="white", font=("calibri", 18), bg="black")
                self.r_sentence.pack()

        # generate a mis-match sentence
        def incorrect_info():
            global fail
            self.response.destroy()

            with open('incorrect.txt', 'r') as f:
                self.content = f.read()
                fails = self.content.splitlines()
                fail = random.choice(fails)
                self.response = Label(self.b, text=f"{fail}", fg="#ff3300", font=("calibri", 18), bg="black")
                self.response.pack()

        # calculate and return words per minute
        def words_per_minute():
            keystrokes = len(sentence)
            words_per_min = round(keystrokes * 60) / total / 5
            wpm_rounded = int(words_per_min)
            self.wpm = Label(self.r, text=f"WPM: {wpm_rounded}", fg="lightgrey", font=("calibri", 18), bg="black")
            self.wpm.pack()

        self.m = Frame(self.master, width=800, height=50, bg="black")
        self.m.pack(pady=10, padx=10)
        self.m.propagate(0)

        self.r_sentence = Label(self.m, textvariable=random_sent, bg="black")
        self.r_sentence.pack()

        # entry frame
        self.entry_frame = Frame(self.master, width=800, height=50, bg="black",
                                 highlightbackground="green", highlightcolor="green", highlightthickness=3)
        self.entry_frame.pack(padx=15, pady=15)
        self.entry_frame.propagate(0)
        self.entry = Entry(self.entry_frame, font=("calibri", 16), bg="black", fg="white",
                           insertbackground="white")
        self.entry.pack(expand=TRUE, fill=BOTH)
        self.entry.focus_set()

        # Bottom (b) frame
        self.b = Frame(self.master, height=50, width=800, bg="black")
        self.b.pack()
        self.b.pack_propagate(0)

        # Processes STOP and also displays start button
        def stop(event=None):
            global end
            global total
            u_entry()
            # delete user entry once submitted
            self.entry.delete(0, 'end')
            # destroys previous button
            self.button.destroy()
            # ends the clock
            end = time.time()
            # total time rounded 3 dp
            total = end-start
            total_rounded = round(total, 3)

            print("Stopped. Hit START to go again.")

            # START! BUTTON
            self.button = Button(self.go_frame, text="START", font="calibri, 18", command=reset_all, fg="white",
                                 width=10)
            self.button.pack(side=TOP, pady=10)
            self.button.config(bg="green")
            self.total_time = Label(self.r, text=f"TIME: {total_rounded}s", fg="lightgrey", bg="black",
                                    font="calibri 18")
            self.total_time.pack()
            words_per_minute()

        def reset_all():
            # reset all results
            self.total_time.destroy()
            self.response.destroy()
            self.wpm.destroy()
            # Run started
            started()

        def u_entry():
            u_input = self.entry.get()
            if sentence == u_input:
                self.response.destroy()
                self.response = Label(self.b, text=f"Well Done!", fg="green", font=("calibri", 18), bg="black")
                self.response.pack()
            else:
                incorrect_info()

        def started():
            global start
            # starts the clock
            start = time.time()
            # Grabs random sentence
            random_sent()
            # Destroys previous button
            self.button.destroy()
            print("Started. Click ENTER to Stop.")
            # STOP! BUTTON
            self.button = Button(self.go_frame, text="STOP!", font="calibri, 18", command=stop, fg="white", width=10)
            self.button.pack(side=TOP, pady=10)
            self.button.config(bg="red")
            self.master.bind("<Return>", stop)

        # Default equal/incorrect input labels
        self.response = Label(self.b, fg="#ff3300", font=("calibri", 18), bg="black", width=100)

        # Frame that holds START/STOP
        self.go_frame = Frame(self.master, width=800, height=70, bg="black")
        self.go_frame.bind("<Return>", started)
        self.go_frame.pack()
        self.go_frame.propagate(0)

        # START Button
        self.button = Button(self.go_frame, text="START", font="calibri, 18", command=started, fg="white")
        self.button.pack(side=TOP, pady=10)
        self.button.config(bg="green")

        # Results Frame
        self.r = Frame(self.master, width=800, height=100, bg="black")
        self.r.pack()
        self.r.propagate(0)


root = Tk()
h = Home(root)
root.mainloop()
