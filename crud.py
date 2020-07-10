from tkinter import *

class App:
	def __init__(self, root):
		self.master = root
		self.master.title("Prueba CRUD con ventana que muestra los contenidos")

		editor = Frame (self.master)
		editor.grid(row = 0, column = 0, pady = 10, sticky = 'nw')
		buttons = Frame(self.master)
		buttons.grid(row = 1, pady = 10)


		#----------Labels----------
		
		idLabel = Label(editor, text = "Id:")
		idLabel.grid(row = 0, column = 0)

		nameLabel = Label(editor, text = "Name:")
		nameLabel.grid(row = 1, column = 0)

		lastnameLabel = Label(editor, text = "Lastname:")
		lastnameLabel.grid(row = 2, column = 0)

		mailLabel = Label(editor, text = "e-mail:")
		mailLabel.grid(row = 3, column = 0)

		passLabel = Label(editor, text = "Password:")
		passLabel.grid(row = 4, column = 0)

		comentLabel = Label(editor, text = "Coment:")
		comentLabel.grid(row = 5, column = 0)

		#----------Inputs----------

		inputId = Entry(editor)
		inputId.grid(row = 0, column = 1)

		inputName = Entry(editor)
		inputName.grid(row = 1, column = 1)

		inputLastname = Entry(editor)
		inputLastname.grid(row = 2, column = 1)

		inputmail = Entry(editor)
		inputmail.grid(row = 3, column = 1)

		inputPass = Entry(editor)
		inputPass.grid(row = 4, column = 1)

		inputComent = Entry(editor)
		inputComent.grid(row = 5, column = 1)

		#----------Buttons----------

		createButton = Button (buttons, text = "Create")
		createButton.grid(row = 0, column = 0)

		readButton = Button (buttons, text = "Read")
		readButton.grid(row = 0, column = 1)

		updateButton = Button (buttons, text = "Update")
		updateButton.grid(row = 0, column = 2)

		deleteButton = Button (buttons, text = "Delete")
		deleteButton.grid(row = 0, column = 3)



def main():
    root = Tk()
    Applicacion = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()