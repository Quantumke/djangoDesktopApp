import tkinter
from tkinter import ttk
from sqlalchemy import *
from sqlalchemy import schema, types, Table, column, String
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
metadata = schema.MetaData()
import psycopg2

LARGE_FONT= ("Verdana", 12)


class GuiInit(tkinter.Tk):

    def __init__(self, *args, **kwargs):

        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        self.login_gui()
    def login_gui(self):
        # self.root.title('WELCOME')
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
        u = str(self.username.get())
        p = str(self.password.get())
        engine = create_engine("postgresql://root:master12!@localhost:5432/desktopsoftware")
        connection = engine.connect()
        engine.echo = True
        metadata.bind = engine
        users = Table('users', metadata, autoload=True)
        def destroy_window(parent, self):
            parent.destroy()
            self.destroy()

        def run(stmt):
            rs = stmt.execute()
            for row in rs:
                username = row.username
                password = row.password
                list = [username, password]
                success = len(list)
                Session = sessionmaker(bind=engine)
                session = Session()
                self.status_label['text'] = "Login successful!"
                self.submit_button['command'] = destroy_window(self,self)
                break
            else:
                self.status_label['text'] = "Wrong username or password"
        result = users.select(and_(users.c.username == u, users.c.password == p))
        run(result)


class PageOne(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(LoginPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.homegui()
    def homegui(self):
        self.grid(column=0, row=0, sticky='nsew')
        self.username=ttk.Entry(self, width=5)



app = GuiInit()
app.mainloop()
