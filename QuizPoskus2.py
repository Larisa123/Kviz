from tkinter import *
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class Quiz(Tk):
    frames = {}
    current_question_number = 0
    points = 0

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self, width=600, height=150) # to je frame, ki nima na sebi nič, na njega zlagama nove
        container.pack(side="top", fill="both", expand=True)

        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0, weight=1)

        self.frames[0] = StartPage(container, self)

        for i in range(1,11):
            question = Question(container, self, i)
            self.frames[i] = question
            #question.grid(row=0, column=0, sticky="nsew")

        self.show_frame()

    def show_frame(self):
        if self.current_question_number <= 10:
            frame = self.frames.get(self.current_question_number, None)
            if frame != None:
                print("Frame {} sem tkraisal".format(self.current_question_number))
                frame.tkraise()
            else: print("Nekaj se je zalomilo. Vprasanja {} ni bilo mogoče naložiti".format(self.current_question_number))
            self.current_question_number += 1

class StartPage(Frame): # podeduje metode in lastnosti razreda
    def __init__(self, parent, quiz_reference): #self je container - vse se bo nalagalo na container
        Frame.__init__(self, parent)
        self.contParent = parent # parent je container iz Quiza, self.parent je torej Frame (container je objekt tipa Frame)
        self.quiz_reference = quiz_reference

        self.show_frame()


    def show_frame(self):
        text = Text(self.contParent, font=LARGE_FONT)
        text.insert(INSERT, "Izberi področje:")

        text.config(state=DISABLED)  # uporabnik ne more spreminjati texta v text polju
        text.pack()

        buttonGeo = ttk.Button(self.contParent, text="Geografija", command=self.quiz_reference.show_frame).pack(fill=X)
        # buttonMat = ttk.Button(widgetMaster, text="Matematika", command=Quiz.show_frame).pack(fill=X)

class Question(Frame):
    number = 0
    question = ""
    correct_answer = 0
    possible_answers = []
    chosen_answer = ""
    is_confirm_button_showing = False


    def __init__(self, parent, quiz_reference, number): #ko imama stevilko, poiscema vprasanje, odgovor in mozne odgovore iz datoteke
        Frame.__init__(self, parent)
        self.contParent = parent
        self.quiz_reference = quiz_reference

        # definirat morema kaj je vprasanje od objekta vprasanje, kaj so mozni odgovori in kaj pravilen odgovor

        self.number = number
        self.question = "Kako si?"
        self.correct_answer = "Vredu"
        self.possible_answers = ["Vredu", "Slabo", "Utrujeno"]


    def show_frame(self):
        self.show_the_question()
        self.show_possible_answers()

    def show_the_question(self):
        text = Text(self.contParent)
        text.insert(INSERT, self.question)
        text.pack()

    def show_possible_answers(self):
        var = StringVar()
        for possible_answer in self.possible_answers:
            R = Radiobutton(self.contParent, text=possible_answer, variable=var, value=possible_answer,
                            command=lambda: self.set_chosen_answer(var))
            # Ko uporabnik izbere odgovor, se mu prikaze gumb za potrditev,
            # ko stisne nanj se preveri pravilnost izbire
            R.pack()

    def set_chosen_answer(self, selected_answer):
        if self.is_confirm_button_showing == False: self.show_confirm_button()
        self.chosen_answer = selected_answer

    def show_confirm_button(self):
        confirm_button = ttk.Button(self.contParent, text="Potrdi izbiro",
                                    command=self.check_the_answer).pack(fill=X)
        self.is_confirm_button_showing = True

    def check_the_answer(self):
        if self.chosen_answer == self.correct_answer: self.points += 1

        #poklici show_frame da nalozi novo vprasanje

app = Quiz()
app.mainloop()