from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import hashlib
import sqlite3


class App:

	dbname = "Users.db"

	def __init__(self, root):
		self.master = root
		self.master.config(padx = 50, pady = 50)
		self.master.title("My first CRUD proyect")

		editor = Frame (self.master)
		editor.grid(row = 0, column = 0, pady = 10, sticky = 'nw')
		buttons = Frame(self.master)
		buttons.grid(row = 1, pady = 10)
		panel = Frame(self.master)
		panel.grid(row = 0, column = 1)


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
		self.inputId.config(width = 30, justify = "center")

		self.inputName = Entry(editor)
		self.inputName.grid(row = 1, column = 1, padx = 10, pady = 10)
		self.inputName.config(width = 30, justify = "center")

		self.inputLastname = Entry(editor)
		self.inputLastname.grid(row = 2, column = 1, padx = 10, pady = 10)
		self.inputLastname.config(width = 30, justify = "center")

		self.inputmail = Entry(editor)
		self.inputmail.grid(row = 3, column = 1, padx = 10, pady = 10)
		self.inputmail.config(width = 30, justify = "center")

		self.inputPass = Entry(editor)
		self.inputPass.grid(row = 4, column = 1, padx = 10, pady = 10)
		self.inputPass.config(width = 30, justify = "center", show="*")

		self.inputComent = Text(editor, width = 35, height = 10)
		self.inputComent.grid(row = 5, column = 1, padx = 10, pady = 10)
		self.inputComent.config(bd=1, selectborderwidth=1, highlightbackground = "grey", highlightcolor= "grey", highlightthickness=1)


		#----------Buttons----------

		createButton = Button (buttons, text = "Create", command = self.add_user)
		createButton.grid(row = 0, column = 0)

		readButton = Button (buttons, text = "Read", command = self.read_data)
		readButton.grid(row = 0, column = 1)

		updateButton = Button (buttons, text = "Update", command = self.update_data)
		updateButton.grid(row = 0, column = 2)

		deleteButton = Button (buttons, text = "Delete", command = self.delete_data)
		deleteButton.grid(row = 0, column = 3)

		cleanButton = Button (buttons, text = "Clean", command = self.clean_data)
		cleanButton.grid(row = 0, column = 4)

		#----------Panel----------

		self.table = ttk.Treeview(panel, height = 20, columns = ("Name", "Lastname", "mail", "Pass", "Coment"))
		self.table.grid(row = 0, column = 0)
		self.table.column('#0', width = 60)
		self.table.column('#1', width = 100)
		self.table.column('#2', width = 100)
		self.table.column('#3', width = 120)
		self.table.column('#4', width = 100)
		self.table.column('#5', width = 300)
		self.table.heading('#0', text = 'ID', anchor = CENTER)
		self.table.heading('#1', text = 'Name', anchor = CENTER)
		self.table.heading('#2', text = 'Lastname', anchor = CENTER)
		self.table.heading('#3', text = 'Mail', anchor = CENTER)
		self.table.heading('#4', text = 'Password', anchor = CENTER)
		self.table.heading('#5', text = 'Coment', anchor = CENTER)

		self.charge_data()



	#----------Functions----------

	def run_query(self, query, parametros = ()):
		with sqlite3.connect(self.dbname) as conn:
			cursor = conn.cursor()
			result = cursor.execute(query, parametros)
			conn.commit()
		return result

	def charge_data(self):
		content = self.table.get_children()
		for element in content:
			self.table.delete(element)
		#Consulta datos
		query = 'SELECT * FROM USERSDATA ORDER BY ID  DESC'
		db_rows = self.run_query(query)
		#rellenando datos
		for row in db_rows:
			self.table.insert('', 0, text = row[0], values =  (row[1], row[2], row[3], "**********", row[5]))

	def clean_data(self):
		#Cambiar por un bucle for
		self.inputId.delete(0, END)
		self.inputName.delete(0, END)
		self.inputLastname.delete(0, END)
		self.inputmail.delete(0, END)
		self.inputPass.delete(0, END)
		self.inputComent.delete(1.0, END)

	def real_mail(self):
		email = self.inputmail.get()
		match = re.match(r'([^@|\s]+@[^@]+\.[^@|\s]+)', email)
		if match:
			return True
		return False

	def hash(self):
		thepass = hashlib.sha256()
		password=str(self.inputPass.get())
		thepass.update(password.encode('utf-8'))
		return thepass

	def add_user(self):
		if len(self.inputName.get()) != 0 and len(self.inputPass.get()) != 0:
			try:
				if self.real_mail():
					thepass = self.hash()
					query = 'INSERT INTO USERSDATA VALUES (NULL, ?,?,?,?,?)'
					parametros = self.inputName.get(),self.inputLastname.get(),self.inputmail.get(),thepass.hexdigest(),self.inputComent.get(1.0, END)
					self.run_query(query, parametros)
					self.clean_data()
					self.charge_data()

				else:
					messagebox.showwarning("Wait!", "Insert a valid e-mail.")
			except Exception:
				messagebox.showwarning("Wait!", "There is already a user with that email.")
		else:
			messagebox.showwarning("Wait!", "At least put the name and the password.")
		
	def read_data(self):
		try:
			conn = sqlite3.connect("Users.db")
			cursor=conn.cursor()
			selection = str(self.table.item(self.table.selection())['text'])
			cursor.execute('SELECT * FROM USERSDATA WHERE ID =' + selection)

			theuser = cursor.fetchall()

			self.clean_data()

			for user in theuser:
				self.inputId.insert(0,user[0])
				self.inputName.insert(0,user[1])
				self.inputLastname.insert(0,user[2])
				self.inputmail.insert(0,user[3])
				self.inputPass.insert(0,user[4])
				self.inputComent.insert(1.0, user[5])

			conn.commit()

			self.charge_data()
		except:
			messagebox.showwarning("Wait!", "Select user from the right size table.")

	def update_data(self):
		if len(self.inputName.get()) != 0 and len(self.inputPass.get()) != 0:
			thepass = self.hash()
			query = 'UPDATE USERSDATA SET USER_NAME=?, LASTNAME=?, EMAIL=?, PASS=?, COMENT=?' + 'WHERE ID = ' + self.inputId.get()
			parametros = self.inputName.get(),self.inputLastname.get(),self.inputmail.get(),thepass.hexdigest(),self.inputComent.get(1.0, END)
			self.run_query(query, parametros)
			messagebox.showinfo("Great!", "The register has been successfully updated.")
			self.clean_data()
			self.charge_data()

	def delete_data(self):
		if len(self.inputId.get()) != 0:
			eliminate = messagebox.askquestion("Delete", "Do you want to delete this user?")
			if eliminate=="yes":
				query = 'DELETE FROM USERSDATA WHERE ID = ?'
				parametros = self.inputId.get()
				self.run_query(query, (parametros, ))
				self.charge_data()
				messagebox.showinfo("OK", "The user was successfully deleted.")
			else:
				messagebox.showwarning("Delete", "Select the user what you want delete.")


def main():
    root = Tk()
    Applicacion = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()