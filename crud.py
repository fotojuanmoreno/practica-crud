from tkinter import *

class App:
	def __init__(self, root):
		self.master = root
		self.master.title("Prueba CRUD con ventana que muestra los contenidos")

def main():
    root = Tk()
    Applicacion = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()