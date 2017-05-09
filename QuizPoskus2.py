from tkinter import *
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class Quiz(Tk):
    #containerFrame = []
    frames = {}
    current_question_number = 0

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self, height=50, width=90) # to je frame, ki nima na sebi nič, na njega zlagama nove
        #self.containerFrame.append(container)
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
            else: print("Frame {} ni v seznamu".format(self.current_question_number))
            self.current_question_number += 1

class StartPage(Frame): # podeduje metode in lastnosti razreda
    def __init__(self, parent, container):
        Frame.__init__(self, parent) # klic, ki ga inicializira v starsevski razred
        text = Text(parent, width=40, height=2, spacing1=15)
        text.insert(INSERT, "Izberi področje:")

        text.config(state=DISABLED) # uporabnik ne more spreminjati texta v text polju
        text.pack()

        #container = Quiz.containerFrame[0]
        buttonGeo = ttk.Button(parent, text="Geografija", command=Quiz.show_frame(Quiz)).pack(fill=X)
        buttonMat = ttk.Button(parent, text="Matematika", command=Quiz.show_frame(Quiz)).pack(fill=X)

class Question(Frame):
    def __init__(self, parent, container, number): #ko imama stevilko, poiscema vprasanje, odgovor in mozne odgovore iz datoteke
        Frame.__init__(self, parent)

        # definirat morema kaj je vprasanje od objekta vprasanje, kaj so mozni odgovori in kaj pravilen odgovor

        self.number = number
        self.question = "Kako si?"
        self.correct_answer = "Vredu"
        self.possible_answers = (self.question, "Vredu", "Slabo", "Utrujeno")

        for possible_answer in self.possible_answers:
            text = Text(parent, width=40, height=2, spacing1=15)
            text.insert(INSERT, possible_answer)

            text.config(state=DISABLED)  # uporabnik ne more spreminjati texta v text polju
            text.pack()

        confirm_button = ttk.Button(self, text="Potrdi izbiro").pack(fill=X)

app = Quiz()
app.mainloop()