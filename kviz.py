from tkinter import*

class Kviz():

    def __init__(self, master):
        self.platno = Canvas(master, width=1000, height=800)
        self.platno.pack()

root = Tk()
root.title('Kviz')
app = Kviz(root)
root.mainloop()