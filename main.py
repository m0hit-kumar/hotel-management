from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import ast
from screeninfo import get_monitors
from functools import partial

# myfile = open("database.txt", "w+")
# myfile.close()


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


def getData():
    myfile = open("database.txt", "r")
    data = myfile.read()
    data = ast.literal_eval(data)
    return data


def pr():
    print("hi")


def table(screen, data, heading):

    print("table")
    posx = 0.01

    for i in range(len(heading)):

        h = Entry(screen, width=20, fg='blue', justify='center',
                  font=('Arial', 10, 'bold'))
        h.place(rely=0.15, relx=posx)
        h.insert(END, heading[i])
        posx = 0.08+posx

    posy = 0.18
    for i in data:
        posx = 0.01
        for j in data[i].values():
            e = Entry(screen, width=20, fg='black',
                      justify='left', font=('Arial', 10))
            e.place(rely=posy, relx=posx)
            e.insert(END, j)
            posx = 0.08+posx
        posy = posy+0.03

# <======================== mark attdendance ==============================>
 def databases = tk.Tk()
    databases.geometry(_width+'x'+_height)
    databases.configure(bg="black")
# <======================== mark attdendance ==============================>


# <============================== view database =====================================>


def viewData():
    databases = tk.Tk()
    databases.geometry(_width+'x'+_height)
    databases.configure(bg="black")
    heading = [
        "Roll no",
        "Name",
        "Guradain",
        "Department",
        "Mobile",
        "Address",
        "Room no",
        "Payment",
        "Vistor",
    ]
    tk.Label(databases, text="Database View",
             font="none 40 bold", fg='white', bg="black").pack(ipady=40, side=TOP)
    ttk.Separator(databases, orient='horizontal').place(
        relx=0, rely=0.12, relheight=0.001, relwidth=1)
    data = getData()
    print(data)
    table(databases, data, heading)

    tk.Button(databases, text="Exit", width=20, fg="red",
              command=databases.destroy).pack(side="right")


# <============================== view database =====================================>
lst_head = ["Sno.", "Name", "Place", "Age"]
lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]


def print_list(screen, data):
    Label(screen, text="List of the avalaiable room:-",
          font="none 15 bold", bg="black", fg="white").place(relx=0.01, rely=0.15)
    pos = 0.01
    for i in range(len(data)):
        pos = pos+0.02
        Label(screen, text=str(data[i])).place(
            relx=pos, rely=0.2, width=20, anchor=CENTER)


# <========================== Allot room window start ==============================================>


def allot_room():

    room_allot = tk.Tk()
    room_allot.geometry(_width+'x'+_height)
    room_allot.configure(bg="black")

    def allotTheRoom(rollno, name, guardain, department, address, mob, room, payment):

        rollno = (rollno.get())
        name = (name.get())
        guardain = (guardain.get())
        department = (department.get())
        address = (address.get())
        mob = (mob.get())
        room = (room.get())
        room = int(room)
        payment = (payment.get())

        room_list = open("room_list.txt", "r")
        available_rooms = room_list.read()
        room_list.close()
        available_rooms = ast.literal_eval(available_rooms)
        if room not in available_rooms:
            tk.Label(
                room_allot, text="Room not exist or room not available at a moment").pack()

        else:
            room_list = open("room_list.txt", "w")
            available_rooms.remove(room)
            room_list.write(str(available_rooms))
            room_list.close()
            dataHouse(rollno, name, department, guardain,
                      room, mob, address, payment)
            tk.Label(room_allot, text="Room no" + str(room) +
                     "is alloted successfully to" + name + "of rollno" + str(rollno)).pack()

    rollno = tk.StringVar(room_allot)
    name = tk.StringVar(room_allot)
    guardain = tk.StringVar(room_allot)
    department = tk.StringVar(room_allot)
    mob = tk.StringVar(room_allot)
    address = tk.StringVar(room_allot)
    room = tk.StringVar(room_allot)
    payment = tk.StringVar(room_allot)

    tk.Label(room_allot, text="Allot Room to the student",
             font="none 40 bold", fg='white', bg="black").pack(ipady=40, side=TOP)
    ttk.Separator(room_allot, orient='horizontal').place(
        relx=0, rely=0.12, relheight=0.001, relwidth=1)
    rooms = open("room_list.txt", "r")
    data = rooms.read()
    rooms.close()
    data = ast.literal_eval(data)
    print_list(room_allot, data)
    ttk.Separator(room_allot, orient='horizontal').place(
        relx=0, rely=0.22, relheight=0.001, relwidth=1)
    tk.Label(room_allot, text="Roll no.",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.30)
    tk.Label(room_allot, text="Name",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.33)
    tk.Label(room_allot, text="Guardain",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.36)
    tk.Label(room_allot, text="Department",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.39)
    tk.Label(room_allot, text="Address",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.42)
    tk.Label(room_allot, text="Mobile",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.45)
    tk.Label(room_allot, text="Room no.",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.48)
    tk.Label(room_allot, text="Payment Status",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.51)

    tk.Entry(room_allot, textvariable=rollno,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.30)
    tk.Entry(room_allot, textvariable=name,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.33)
    tk.Entry(room_allot, textvariable=guardain,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.36)
    tk.Entry(room_allot, textvariable=department,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.39)
    tk.Entry(room_allot, textvariable=address,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.42)
    tk.Entry(room_allot, textvariable=mob,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.45)
    tk.Entry(room_allot, textvariable=room,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.48)
    tk.Entry(room_allot, textvariable=payment,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.51)

    user_prof = partial(allotTheRoom, rollno, name, guardain,
                        department, address, mob, room, payment)

    tk.Button(room_allot, text="Allot", command=user_prof, width=10,  height=1,
              font="none 10 bold", bg='white', fg="black").place(relx=0.6, rely=0.71, anchor=CENTER)
    tk.Button(room_allot, text="Cancel", command=lambda: room_allot.destroy(), width=10,  height=1,
              font="none 10 bold", bg='white', fg="black").place(relx=0.7, rely=0.71, anchor=CENTER)


# <======================== Allot room window end ==============================================>
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
tk.Button(menu, text="Database", command=viewData, width=20,
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

stud = {}


def dataHouse(rollno, name, department, guardain, room, mob, address, payment):
    stud = {}
    print(rollno, name, department, guardain, room, mob, address, payment)

    database = open("database.txt", "r+")
    print(database)
    user = database.read()
    print("user", user)

    if user != '':
        stud = ast.literal_eval(user)
        print(stud)
        stud[room] = {}
        stud[room]["rollno"] = rollno
        stud[room]["name"] = name
        stud[room]["guardain"] = guardain
        stud[room]["department"] = department
        stud[room]["mob"] = mob
        stud[room]["address"] = address
        stud[room]["room"] = room
        stud[room]["payment"] = payment
        stud[room]["vistors"] = ""
        database.close()
        database = open("database.txt", "w")
        print("$$$$$$$$", stud)
        database.write(str(stud))
        database.close()

    else:
        database.close()
        database = open("database.txt", "w")
        database.write(str(stud))
        database.close()
        database = open("database.txt", "r")
        user = database.read()
        stud = ast.literal_eval(user)
        stud[room] = {}
        stud[room]["rollno"] = rollno
        stud[room]["name"] = name
        stud[room]["guardain"] = guardain
        stud[room]["department"] = department
        stud[room]["mob"] = mob
        stud[room]["address"] = address
        stud[room]["room"] = room
        stud[room]["payment"] = payment
        stud[room]["vistors"] = ""
        database.close()
        database = open("database.txt", "w")
        print("$$$$$$$$")
        database.write(str(stud))
        database.close()


menu.mainloop()
