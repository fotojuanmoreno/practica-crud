from tkinter import *
import sqlite3
from tkinter import messagebox


class App:

	dbname = "Users.db"

	def __init__(self, root):
		self.master = root
		self.master.title("My first CRUD proyect")

		editor = Frame (self.master)
		editor.grid(row = 0, column = 0, pady = 10, sticky = 'nw')
		buttons = Frame(self.master)
		buttons.grid(row = 1, pady = 10)


		#----------Labels----------
		
		idLabel = Label(editor, text = "Id:")
		idLabel.grid(row = 0, column = 0, sticky ="e")

		nameLabel = Label(editor, text = "Name:")
		nameLabel.grid(row = 1, column = 0, sticky ="e")

		lastnameLabel = Label(editor, text = "Lastname:")
		lastnameLabel.grid(row = 2, column = 0, sticky ="e")

		mailLabel = Label(editor, text = "e-mail:")
		mailLabel.grid(row = 3, column = 0, sticky ="e")

		passLabel = Label(editor, text = "Password:")
		passLabel.grid(row = 4, column = 0, sticky ="e")

		comentLabel = Label(editor, text = "Coment:")
		comentLabel.grid(row = 5, column = 0, sticky ="e")

		#----------Inputs----------

		inputId=StringVar()
		inputName=StringVar()
		inputLastname=StringVar()
		inputmail=StringVar()
		inputPass=StringVar()

		self.inputId = Entry(editor)
		self.inputId.grid(row = 0, column = 1, padx = 10, pady = 10)
		self.inputId.config(width = 30)

		self.inputName = Entry(editor)
		self.inputName.grid(row = 1, column = 1, padx = 10, pady = 10)
		self.inputName.config(width = 30)

		self.inputLastname = Entry(editor)
		self.inputLastname.grid(row = 2, column = 1, padx = 10, pady = 10)
		self.inputLastname.config(width = 30)

		self.inputmail = Entry(editor)
		self.inputmail.grid(row = 3, column = 1, padx = 10, pady = 10)
		self.inputmail.config(width = 30)

		self.inputPass = Entry(editor)
		self.inputPass.grid(row = 4, column = 1, padx = 10, pady = 10)
		self.inputPass.config(width = 30)

		self.inputComent = Text(editor, width = 35, height = 10)
		self.inputComent.grid(row = 5, column = 1, padx = 10, pady = 10)
		self.inputComent.config(bd=1, selectborderwidth=1, highlightbackground = "grey", highlightcolor= "grey", highlightthickness=1)


		#----------Buttons----------

		createButton = Button (buttons, text = "Create", command = self.add_user)
		createButton.grid(row = 0, column = 0)

		readButton = Button (buttons, text = "Read")
		readButton.grid(row = 0, column = 1)

		updateButton = Button (buttons, text = "Update")
		updateButton.grid(row = 0, column = 2)

		deleteButton = Button (buttons, text = "Delete")
		deleteButton.grid(row = 0, column = 3)

	#----------Functions----------

	def run_query(self, query, parametros = ()):
		with sqlite3.connect(self.dbname) as conn:
			cursor = conn.cursor()
			result = cursor.execute(query, parametros)
			conn.commit()
		return result

	def clean_data(self):
		#Cambiar por un bucle for
		self.inputId.delete(0, END)
		self.inputName.delete(0, END)
		self.inputLastname.delete(0, END)
		self.inputmail.delete(0, END)
		self.inputPass.delete(0, END)
		self.inputComent.delete(1.0, END)

	def add_user(self):
		if len(self.inputName.get()) != 0 and len(self.inputPass.get()) != 0:
			query = 'INSERT INTO USERSDATA VALUES (NULL, ?,?,?,?,?)'
			parametros = self.inputName.get(),self.inputLastname.get(),self.inputmail.get(),self.inputPass.get(),self.inputComent.get(1.0, END)
			self.run_query(query, parametros)
			self.clean_data()
			#self.dameDatos()
		else:
			messagebox.showwarning("Wait!", "At least put the name and the password.")




def main():
    root = Tk()
    Applicacion = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()