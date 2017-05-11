from tkinter import *
from tkinter import ttk
import random

class Quiz(Tk):
    frames = {}
    number_of_questions = 3
    question_count = 0
    number_of_all_questions = 15 # per subject in SUBJECTdata.txt
    points = 0 # number of points user gets for answering the question correctly

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.initialize_container_frame()
        self.initialize_start_page()

    def initialize_container_frame(self):
        self.container = Frame(self)  # to je frame, ki nima na sebi nič, na njega zlagama nove
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        # default weight je 0, kar pomeni da bo ta imel najvecji prostor ko spremenimo velikost - zaenkrat nima veze ker je sam
        self.container.grid_columnconfigure(0, weight=1)

    def initialize_start_page(self):
        start_page = StartPage(self.container, self)
        start_page.grid(row=0, column=0, sticky="nsew")
        self.frames[0] = start_page
        self.show_frame()

    def show_frame(self):
        if self.question_count <= self.number_of_questions:
            frame = self.frames.get(self.question_count, None) # da slucajno ne pride do zrusitve programa
            if frame != None: frame.tkraise() # naloži nov frame - vprašanje
            else: print("Nekaj se je zalomilo. Vprasanja {} ni bilo mogoče naložiti".format(self.current_question_number))
            self.question_count += 1
        else: self.show_result_frame()

    def set_subject(self, subject):
        self.create_random_questions(subject)
        self.show_frame()

    def create_random_questions(self, subject):
        random_question_numbers = []
        table_of_possible_question_numbers = list(range(1, self.number_of_all_questions + 1)) # iti more od 1 do vkljucno stevila

        # tu samo dolocimo random stevilke vprasanj, stevilka pomeni vrstica v dokumentu:
        while len(random_question_numbers) < self.number_of_questions:
            rand_number = random.choice(table_of_possible_question_numbers)
            random_question_numbers.append(rand_number)

            if rand_number in table_of_possible_question_numbers: table_of_possible_question_numbers.remove(rand_number)
            else: print("Pri določanju tvojih vprašanj se je zalomilo.") # spet da slucajno ne pride do zrusitve

        # nalozimo dejanska vprasanja, prikazemo zaenkrat se nobenega:
        question_count = 1 # to ni lastnost metode self.question_count, ampak nova spremenljivka
        for number in random_question_numbers:
            question = Question(self.container, self, subject, number)
            self.frames[question_count] = question
            question_count += 1
            question.grid(row=0, column=0, sticky="nsew")

    def show_result_frame(self):
        result_page = ResultPage(self.container, self)
        result_page.grid(row=0, column=0, sticky="nsew")
        result_page.tkraise()

        # ponastavimo rezultate, ce bo slucajno igral ponovno:
        self.question_count = 0
        self.points = 0
        self.destroy_previous_frames() # da se nam spomin ne zabase

    def destroy_previous_frames(self):
        for frame in self.frames.values():
            frame.destroy()
        self.frames = {}

    def increase_points(self):
        self.points += 1



class StartPage(Frame): # podeduje metode in lastnosti razreda
    def __init__(self, parent, quiz_reference): #self je container - vse se bo nalagalo na container
        Frame.__init__(self, parent)
        self.quiz_reference = quiz_reference

        self.show_frame()

    def show_frame(self):
        Label(self, text="Izberi področje:").pack(pady=15, padx=10)

        buttonGeo = ttk.Button(self, text="Geografija", command= lambda: self.quiz_reference.set_subject("GEO")).pack(fill=X)
        buttonMat = ttk.Button(self, text="Matematika", command= lambda: self.quiz_reference.set_subject("MAT")).pack(fill=X)
        # lambda uporabimo, da lahko podamo parameter in ob tem ne sprožimo klica funkcije


class Question(Frame):
    question = ""
    correct_answer = 0
    possible_answers = []
    chosen_answer = ""
    is_confirm_button_showing = False


    def __init__(self, parent, quiz_reference, subject, number): #ko imama stevilko, poiscema vprasanje, odgovor in mozne odgovore iz datoteke
        Frame.__init__(self, parent)
        self.quiz_reference = quiz_reference
        self.subject = subject
        self.number = number
        self.get_data()

        self.show_frame_widgets()

    def show_frame_widgets(self):
        self.show_the_question()
        self.show_possible_answers()

    def show_the_question(self):
        Label(self, text=self.question).pack(pady=15, padx=10)

    def show_possible_answers(self):
        var = StringVar()
        for possible_answer in self.possible_answers:
            R = Radiobutton(self, text=possible_answer, variable=var, value=possible_answer,
                            command=lambda: self.set_chosen_answer(var.get()))
            # Ko uporabnik izbere odgovor, se mu prikaze gumb za potrditev, ko stisne nanj se preveri pravilnost izbire
            R.pack()

    def set_chosen_answer(self, selected_answer):
        if self.is_confirm_button_showing == False: self.show_confirm_button()
        self.chosen_answer = selected_answer

    def show_confirm_button(self):
        confirm_button = ttk.Button(self, text="Potrdi izbiro",
                                    command=self.check_the_answer).pack(fill=X)
        self.is_confirm_button_showing = True

    def check_the_answer(self):
        if self.chosen_answer == self.correct_answer: self.quiz_reference.increase_points()
        self.quiz_reference.show_frame()
        #poklici show_frame da nalozi novo vprasanje

    def get_data(self):
        data = self.subject + "data.txt"

        with open(data, "r") as file:
            lines = [line.strip() for line in file]
            currentLine = lines[self.number]
            # zapisano v obliki Vprasanje;odg1:odg2:odg3;odgovorPravilen
            data = currentLine.split(";")
            self.question = data[0]
            self.correct_answer = data[2]
            self.possible_answers = data[1].split(":");


class ResultPage(Frame):
    def __init__(self, parent, quiz_reference): #ko imama stevilko, poiscema vprasanje, odgovor in mozne odgovore iz datoteke
        Frame.__init__(self, parent)
        self.quiz_reference = quiz_reference
        self.show_frame_widgets()

    def show_frame_widgets(self):
        Label(self, text="Tvoj rezultat je: {}/{} točk!".
              format(self.quiz_reference.points, self.quiz_reference.number_of_questions)).pack(pady=15, padx=10)

        # sporocilo glede na rezultat:
        user_points = self.quiz_reference.points
        all_points = self.quiz_reference.number_of_questions
        if user_points in range(all_points//2+1, all_points//4): message = "Tvoje znanje je zadovoljivo."
        else: message = "Bravo, tvoje znanje je izjemno!!!" if user_points == all_points else "Treba bo vaditi!"
        Label(self, text=message).pack(pady=15, padx=10)

        ttk.Button(self, text="Igraj ponovno!", command=self.quiz_reference.initialize_start_page).pack(fill=X)

app = Quiz()
app.mainloop()