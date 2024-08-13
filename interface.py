from tkinter import * 

root = Tk()

class Interface():
    def __init__ (self):
        self.root = root
        self.tela()
        self.root.mainloop()  # Chame mainloop() por último
        
    def tela(self):
        self.root.title("Prolog consult")
        
    def frames(self):
        self.farme_l = Frame(self.root)
        self.farme_r = Frame(self.root)
        
        
Interface()
