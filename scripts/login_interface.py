import tkinter
from tkinter import ttk
from sqlalchemy import *
from sqlalchemy import schema, types, Table, column, String
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
metadata = schema.MetaData()
import psycopg2

class LoginInterface(ttk.Frame):
	try:
		conn=psycopg2.connect("dbname='desktopsoftware', user='root', password='master12!'")
		cur = conn.cursor()
	except:
		print ("Connection to database failed")
	def __init__(self, parent, *args, **kwargs):
		ttk.Frame.__init__(self,parent, *args, **kwargs)
		self.root=parent
		self.init_gui()
	def init_gui(self):
		self.root.title('WELCOME')
		self.grid(column=0, row=0, sticky='nsew')
		self.username = ttk.Entry(self, width=5)
		self.username.grid(column=1, row=2)
		self.password = ttk.Entry(self, width=5)
		self.password.grid(column=3, row=2)
		self.submit_button = ttk.Button(self, text='Login', command=self.login)
		self.submit_button.grid(column=0, row=3, columnspan=4)
		self.status = ttk.LabelFrame(self, text='Status',
										   height=100)
		self.status.grid(column=0, row=4, columnspan=4, sticky='nesw')

		self.status_label = ttk.Label(self.status, text='')
		self.status_label.grid(column=0, row=0)

		ttk.Label(self, text='Login').grid(column=0, row=0,
												  columnspan=4)
		ttk.Label(self, text='Username').grid(column=0, row=2,
												sticky='w')
		ttk.Label(self, text='Password').grid(column=2, row=2,
												sticky='w')

		ttk.Separator(self, orient='horizontal').grid(column=0,
													  row=1, columnspan=4, sticky='ew')


		for child in self.winfo_children():
			child.grid_configure(padx=5, pady=5)

	def login(self):
		u=str(self.username.get())
		p=str(self.password.get())
		engine = create_engine("postgresql://root:master12!@localhost:5432/desktopsoftware")
		connection=engine.connect()
		engine.echo=True
		metadata.bind = engine
		users=Table('users',metadata, autoload=True)
		def run(stmt):
			rs=stmt.execute()
			for row in rs:
				username=row.username
				password=row.password
				list=[username, password]
				success=len(list)
				break
			else:
				print("Nop")
		result=users.select(and_(users.c.username==u, users.c.password==p))
		run(result)
if __name__=='__main__':
	root=tkinter.Tk()
	LoginInterface(root)
	root.mainloop()
