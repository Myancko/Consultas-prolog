import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog

# Configurar o Prolog
prolog_file = "cute.pl"
prolog = Prolog()
prolog.consult(prolog_file)

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("She is Cute?")
        self.create_widgets()

    def create_widgets(self):

        self.search_button = tk.Button(self.root, text="Pesquisar", command=self.search_girl)
        self.search_button.pack(pady=10)


        self.list_button = tk.Button(self.root, text="Listar Garotas", command=self.list_girls)
        self.list_button.pack(pady=10)


        self.cute_button = tk.Button(self.root, text="É Fofa", command=self.girl_cute)
        self.cute_button.pack(pady=10)

        self.beautiful_button = tk.Button(self.root, text="É Bonita", command=self.girl_beautiful)
        self.beautiful_button.pack(pady=10)
        
        self.smart_and_beautiful = tk.Button(self.root, text="É Bonita e esperta", command=self.is_smart_and_beautiful)
        self.smart_and_beautiful.pack(pady=10)
        
        self.custom_search_buttom =  tk.Button(self.root, text=">>> Enviar comando prolog <<<", command=self.custom_search)
        self.custom_search_buttom.pack(pady=10, padx=10)
        
        self.name_label = tk.Label(self.root, text="Digite o nome da garota:")
        self.name_label.pack(pady=5)
        
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)
        
        self.quit_button = tk.Button(self.root, text="Sair", command=self.root.quit)
        self.quit_button.pack(pady=10)

    def custom_search(self):
        name = self.name_entry.get()
        query = self.name_entry.get()
        result = prolog.query(f"{query}")
        result_list = list(result)

        print(result, '<<<')
        if result:
            
            if len(result_list) > 0:
                messagebox.showinfo(f"Resultado ->", f"{result_list}")
            else :
                messagebox.showinfo("Resultado", "True")
        else:
            messagebox.showinfo("GG")
    
    def search_girl(self):
        name = self.name_entry.get()
        query = f"girl('{name}')"
        result = list(prolog.query(query))
        print(result, '<<<')
        if result:
            messagebox.showinfo("Resultado", f"{name} foi encontrada.")
        else:
            messagebox.showinfo("Resultado", f"{name} não foi encontrada.")
            
    def is_smart_and_beautiful(self):
        name = self.name_entry.get()
        query = f"is_smart_and_beautiful('{name}')"
        result = list(prolog.query(query))
        if result:
            messagebox.showinfo("Resultado", f"{name} é bonia e esperta")
        else:
            messagebox.showinfo("Resultado", f"{name} não é bonita ou esperta.")

    def girl_cute(self):
        name = self.name_entry.get()
        query = f"is_cute('{name}')"
        result = list(prolog.query(query))
        if result:
            messagebox.showinfo("Resultado", f"{name} é fofa.")
        else:
            messagebox.showinfo("Resultado", f"{name} não é fofa.")

    def girl_beautiful(self):
        name = self.name_entry.get()
        query = f"is_beautifil('{name}')"
        result = list(prolog.query(query))
        if result:
            messagebox.showinfo("Resultado", f"{name} é bonita.")
        else:
            messagebox.showinfo("Resultado", f"{name} não é bonita.")

    def list_girls(self):
        girls = list(prolog.query("girl(X)"))
        girls_list = "\n".join(girl['X'] for girl in girls)
        messagebox.showinfo("Lista de Garotas", girls_list)

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
