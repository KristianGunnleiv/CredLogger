import tkinter as tk
import sqlite3



main = tk.Tk()
main.geometry("300x100")
main.title("CredLogger V1.")

global service
global username
global password

#service = tk.StringVar()
#username = tk.StringVar()
#password = tk.StringVar()

#top = tk.Frame(main)
#top.pack()
#bottom = tk.Frame(main)
#bottom.pack()


#tk.Label(top, text = "Service: ").grid(row=0, column=0)
#tk.Entry(top, textvariable=service).grid(row=0, column=1)

#tk.Label(top, text = "Username: ").grid(row=1, column=0)
#tk.Entry(top, textvariable=username).grid(row=1, column=1)

#tk.Label(top, text = "Password: ").grid(row=2, column=0)
#tk.Entry(top, textvariable=password).grid(row=2, column=1)

#tk.Button(bottom, text="Submit", command=f).pack()


main.mainloop()
    