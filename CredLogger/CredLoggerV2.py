
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Denne koden eies av Kristian Gunnleiv I Gardastovu Sørensen,  #
# og kan ikke selges uten avtale med ham. Hvis du bryter dette, #
# kommer han og dreper deg mens du sover. Denne koden er utgitt #
# under ©GNU open source license 2020. Dette er ihvertfall ikke #
# en falsk lisens. Alle filer i dette prosjektet underfaller    #
# kopirettighetene ovenfor!                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #




import tkinter as tk
import sqlite3 as sql
from sqlFunc import *

conn = sql.connect("profiles.db")
cursor = conn.cursor()
MainWnd = tk.Tk()
MainWnd.geometry("165x50")
func = SqlFunc("profiles.db")

cursor.execute("CREATE TABLE IF NOT EXISTS brukerdata(service TEXT NOT NULL UNIQUE, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL UNIQUE);")

def get_profiles_callback():
    getProfWnd = tk.Toplevel()
    
    username = tk.StringVar()
    service = tk.StringVar()
    password = tk.StringVar()
    output = ""

    
    errormsg = tk.Message(getProfWnd, text="""Get profiles by combination of one, or more of the fields below""").grid(row=0, column=0, rowspan=1, columnspan=3)
    
    tk.Label(getProfWnd, text="Username: ").grid(row=2,column=0)
    tk.Entry(getProfWnd, textvariable=username).grid(row=2,column=1,columnspan=2)
    
    tk.Label(getProfWnd, text="Service: ").grid(row=3,column=0)
    tk.Entry(getProfWnd, textvariable=service).grid(row=3,column=1,columnspan=2)
    
    tk.Label(getProfWnd, text="password: ").grid(row=4,column=0)
    tk.Entry(getProfWnd, textvariable=password).grid(row=4,column=1, columnspan=2)

    tk.Label(text=output)

    tk.Button(getProfWnd, text="Get profile(s)", command=lambda:func.getInNotNull("brukerdata", service=service.get(), username=username.get(), password=password.get())).grid(row=5,column=1)

def add_profiles_callback():
    addProfWnd = tk.Toplevel(MainWnd)
    
    service = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()
    
    tk.Message(addProfWnd, text="Enter service password and username. All fields required! No special signs like '(' or '/' will break the program.").grid(row=0,column=0,columnspan=3)

    tk.Label(addProfWnd, text="Service: ").grid(row=1,column=0)
    tk.Entry(addProfWnd, textvariable=service).grid(row=1,column=1,columnspan=2)
    
    tk.Label(addProfWnd, text="Username: ").grid(row=2,column=0)
    tk.Entry(addProfWnd).grid(row=2,column=1,columnspan=2)
    
    tk.Label(addProfWnd, text="Password: ").grid(row=3,column=0)
    tk.Entry(addProfWnd).grid(row=3,column=1,columnspan=2)

    def Submit_callback():
        cursor.execute("INSERT INTO brukerdata VALUES (, ?, ?)", (service.get(), username.get(), password.get()))
        conn.commit()
    
    tk.Button(addProfWnd, text="Add", command=Submit_callback).grid(row=4,column=1)
    
    
tk.Button(MainWnd, text="Get profile(s)", height=3, width=11, command= get_profiles_callback).pack(side="left")
tk.Button(MainWnd, text="Add profile(s)", height=3, width=11, command= add_profiles_callback).pack(side="left")

MainWnd.mainloop()
cursor.execute("SELECT * FROM brukerdata")
print(cursor.fetchall())
conn.close()


