from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import ast
from screeninfo import get_monitors


_width = 0
_height = 0
# Function to get screen size
for i in get_monitors():
    _width = str(i.width)
    _height = str(i.height)


instructions = 'Instructions:-' + "\n\n1)Database btuuon allow you to see all data our hostel\n\n2)Marl attdemdace wull allow to mark attdenace of the student\n\n3) allot room button will allow you to allot atdance of student\n\n4) Edit details button will allow to edit details of the users\n\n5)View Students details allow to se the user info\n\n6)vistor button is to add vistor record\n\n7) exit button help in exiting from the panel"


def exitWindow(window1):
    notice = tk.Tk("Admin Portal")
    notice.geometry("600x200")
    notice.eval('tk::PlaceWindow . center')

    def destroy_all():
        window1.destroy()
        notice.destroy()

    notice.title("exit")
    notice.config(bg="black")
    tk.Label(notice, text="Do you really want to exit?", font="none 20 bold",
             bg="black", fg="red").grid(ipady=20, ipadx=10)
    tk.Button(notice, text="Yes", command=destroy_all).grid(
        column=1, row=6, ipadx=10)
    tk.Button(notice, text="NO", command=notice.destroy).grid(
        row=6, column=3, ipadx=10)


def pr():
    print("hi")


lst_head = ["Sno.", "Name", "Place", "Age"]
lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]


def table(screen, data, heading):
    for i in range(len(heading)):
        e = Entry(screen, width=20, fg='black')
        e.place(ipadx=10, ipady=10,
                row=2, column=80+i)
        e.insert(END, heading[i])

    for i in range(len(data)):
        for j in range(len(data[0])):
            e = Entry(screen, width=20, fg='blue')
            e.place(ipadx=10, ipady=10,
                    row=i+10, column=j+80)
            e.insert(END, lst[i][j])


def print_list(screen, data):
    print(data)
    Label(screen, text="List of the avalaiable room:-",
          font="none 15 bold", bg="black", fg="white").place(relx=0.01, rely=0.15)
    pos = 0.01
    for i in range(len(data)):
        pos = pos+0.02
        Label(screen, text=str(data[i])).place(
            relx=pos, rely=0.2, width=20, anchor=CENTER)


def allot_room():
    room_allot = tk.Tk()
    room_allot.geometry(_width+'x'+_height)
    room_allot.configure(bg="black")
    tk.Label(room_allot, text="Allot Room to the student",
             font="none 40 bold", fg='white', bg="black").pack(ipady=40, side=TOP)
    ttk.Separator(room_allot, orient='horizontal').place(
        relx=0, rely=0.12, relheight=0.001, relwidth=1)
    rooms = open("rooms.txt", "r")
    data = rooms.read()
    rooms.close()
    data = ast.literal_eval(data)
    print_list(room_allot, data)


# <================================ Menu Screen/Main Screen Start=====================================>
menu = tk.Tk()
menu.geometry(_width+'x'+_height)
menu.title("Dashboard")
menu.configure(bg='black')
heading = tk.Label(menu, text="Welcome to the Hostel Managment Panel !!",
                   font="none 40 bold", fg='white', bg="black").pack(ipady=40, side=TOP)
separator = ttk.Separator(menu, orient='horizontal').place(
    relx=0, rely=0.12, relheight=0.001, relwidth=1)
separator = ttk.Separator(menu, orient='vertical').place(
    relx=0.1, rely=0.12, relwidth=0.001, relheight=1)
tk.Button(menu, text="Database", command=pr, width=20,
          height=5).place(relx=0.05, rely=0.19, anchor=CENTER)
tk.Button(menu, text="Mark Attdedance", command=pr, width=20,
          height=5).place(relx=0.05, rely=0.30, anchor=CENTER)
tk.Button(menu, text="Allot Room", command=allot_room, width=20,
          height=5).place(relx=0.05, rely=0.41, anchor=CENTER)
tk.Button(menu, text="Edit Details", command=pr, width=20,
          height=5).place(relx=0.05, rely=0.52, anchor=CENTER)
tk.Button(menu, text="View Student Details", command=pr, width=20,
          height=5).place(relx=0.05, rely=0.63, anchor=CENTER)
tk.Button(menu, text="Vistors", command=pr, width=20,
          height=5).place(relx=0.05, rely=0.74, anchor=CENTER)
tk.Button(menu, text="Exit", command=lambda: exitWindow(menu), width=20, fg="red",
          height=5).place(relx=0.05, rely=0.85, anchor=CENTER)
tk.Label(menu, text=instructions,
         font="none 20 bold", fg='white', bg="black", justify=LEFT).place(relx=0.15, rely=0.19)

# <=================================================== Main Screen End========================================>


# table(menu, lst, lst_head)

menu.mainloop()
