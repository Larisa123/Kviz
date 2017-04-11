from tkinter import*

class Kviz():

    def __init__(self, master):
        self.prikaziZacetnoOkno()


    def prikaziZacetnoOkno(self):
        top_frame = Frame(root)
        top_frame.pack()
        text = Text(top_frame, width = 40, height=2, spacing1 = 15)
        text.insert(INSERT, "Izberi področje:")

        text.config(state=DISABLED)
        text.pack()

        buttonGeo = Button(top_frame, text="Geografija", command=prikaziGeografijo).pack(fill=X)
        buttonMat = Button(top_frame, text="Matematika").pack(fill=X)

    def prikaziGeografijo(self):



root = Tk()
root.title('Kviz')
app = Kviz(root)
root.mainloop()

