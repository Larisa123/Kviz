from tkinter import *

LARGE_FONT = ("Verdana", 12)

class Quiz(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self, height=50, width=90) # to je frame, ki nima na sebi nič, na njega zlagama nove
        # frame s pomočjo vgrajene funkcije tkraise

        container.pack() # se prikaže

        self.frames = {} # tu not imama vse frame (slovar oblike Razred tipa Frame : frame) - startPage in vprasanja
        start_page_frame = StartPage(container, self) # inicializirama zacetni frame
        self.frames[StartPage] = start_page_frame
        # shranima razred od zacetnega okna v slovar, njegova vrednost je inicializiran frame z napisi itd.

        self.show_frame(StartPage) #najina metoda


    def show_subject(self):
        pass

    def show_frame(self, cont):
        frame = self.frames[cont] # poišče start_page_frame kot vrednost StartPage razreda v slovarju
        frame.tkraise()

class StartPage(Frame): # podeduje metode in lastnosti razreda
    def __init__(self, parent, controller): #kje uporabljama controller?
        Frame.__init__(self, parent) # klic, ki ga inicializira v starsevski razred
        text = Text(width=40, height=2, spacing1=15)
        text.insert(INSERT, "Izberi področje:")

        text.config(state=DISABLED) # uporabnik ne more spreminjati texta v text polju
        text.pack()

        buttonGeo = Button(text="Geografija", command=Quiz.show_subject(Quiz)).pack(fill=X)
        buttonMat = Button(text="Matematika", command=Quiz.show_subject(Quiz)).pack(fill=X)



app = Quiz()
app.mainloop()

