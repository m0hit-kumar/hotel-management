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


instructions = 'Instructions:-' + "\n\n1) The database button allows you to see all data our hostel\n\n2) Mark attendance will allow marking attendance of the student\n\n3) Allot room button will allow you to allot attendance of student\n\n4) The edit details button will allow editing details of the users\n\n5) View Student's details allow seeing the user info\n\n6) The visitor button is to add visitor record\n\n7) Exit button help in exiting from the panel"


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


def editDetails():

    edit_screen = tk.Tk()
    edit_screen.geometry(_width+'x'+_height)
    edit_screen.configure(bg="black")

    def editData(rollno, name, guardain, department, address, mob, room, payment):

        rollno = (rollno.get())
        name = (name.get())
        guardain = (guardain.get())
        department = (department.get())
        address = (address.get())
        mob = (mob.get())
        room = (room.get())
        room = int(room)
        payment = (payment.get())
        data = getData()
        alloted_room = [i for i in data.keys()]
        if room not in alloted_room:
            tk.Label(
                edit_screen, text="Room  doesnn't exist or room is allocated yet").pack()

        else:
            dataHouse(rollno, name, department, guardain,
                      room, mob, address, payment)
            tk.Label(edit_screen, text="Data Updated successfully").pack()

    rollno = tk.StringVar(edit_screen)
    name = tk.StringVar(edit_screen)
    guardain = tk.StringVar(edit_screen)
    department = tk.StringVar(edit_screen)
    mob = tk.StringVar(edit_screen)
    address = tk.StringVar(edit_screen)
    room = tk.StringVar(edit_screen)
    payment = tk.StringVar(edit_screen)

    tk.Label(edit_screen, text="Update Data of the student",
             font="none 40 bold", fg='white', bg="black").pack(ipady=40, side=TOP)
    ttk.Separator(edit_screen, orient='horizontal').place(
        relx=0, rely=0.12, relheight=0.001, relwidth=1)
    rooms = open("room_list.txt", "r")
    data = rooms.read()
    rooms.close()
    data = ast.literal_eval(data)
    ttk.Separator(edit_screen, orient='horizontal').place(
        relx=0, rely=0.22, relheight=0.001, relwidth=1)

    tk.Label(edit_screen, text="Note: To update data you need you enter old room no. and has to renter all the details.",
             font="none 20 bold", fg='yellow', bg="black").place(relx=0.1, rely=0.14)
    tk.Label(edit_screen, text="Roll no.",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.30)
    tk.Label(edit_screen, text="Name",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.33)
    tk.Label(edit_screen, text="Guardain",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.36)
    tk.Label(edit_screen, text="Department",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.39)
    tk.Label(edit_screen, text="Address",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.42)
    tk.Label(edit_screen, text="Mobile",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.45)
    tk.Label(edit_screen, text="Room no.",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.48)
    tk.Label(edit_screen, text="Payment Status",
             font="none 10 bold", fg='white', bg="black").place(relx=0.4, rely=0.51)

    tk.Entry(edit_screen, textvariable=rollno,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.30)
    tk.Entry(edit_screen, textvariable=name,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.33)
    tk.Entry(edit_screen, textvariable=guardain,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.36)
    tk.Entry(edit_screen, textvariable=department,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.39)
    tk.Entry(edit_screen, textvariable=address,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.42)
    tk.Entry(edit_screen, textvariable=mob,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.45)
    tk.Entry(edit_screen, textvariable=room,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.48)
    tk.Entry(edit_screen, textvariable=payment,
             font="none 10 bold", bg='white', fg="black").place(relx=0.5, rely=0.51)

    user_prof = partial(editData, rollno, name, guardain,
                        department, address, mob, room, payment)

    tk.Button(edit_screen, text="Update Data", command=user_prof, width=10,  height=1,
              font="none 10 bold", bg='white', fg="black").place(relx=0.6, rely=0.71, anchor=CENTER)
    tk.Button(edit_screen, text="Cancel", command=lambda: edit_screen.destroy(), width=10,  height=1,
              font="none 10 bold", bg='white', fg="black").place(relx=0.7, rely=0.71, anchor=CENTER)


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

# <============================== add vistor record========================================>


def addVistor():
    vistor_screen = tk.Tk()
    vistor_screen.geometry("700x300")
    vistor_screen.configure(bg="black")

    def vistMe(rollno, vistor):
        rollno = (rollno.get())
        vistor = (vistor.get())
        print(rollno)
        data = getData()
        marked = False
        for i in data:
            if data[i]['rollno'] == rollno:
                data[i]['attdendance'] += 1
                data[i]['vistors'] = vistor
                tk.Label(vistor_screen, text="Vistor data updated").pack(
                    side="top")
                marked = True
            myfile = open("database.txt", "w")
            myfile.write(str(data))
            myfile.close()

        if marked == False:
            tk.Label(vistor_screen, text="Roll no doesnt exist").pack(
                side="bottom")

    rollno = tk.StringVar(vistor_screen)
    vistor = tk.StringVar(vistor_screen)

    tk.Label(vistor_screen, text="Mark attdendance", justify=LEFT,
             font="none 20 bold", fg='white', bg="black").pack(padx=10, pady=20, anchor="w")
    vistorcheckin = partial(vistMe, rollno, vistor)
    tk.Label(vistor_screen, text="Enter Roll no.:", fg='white', bg="black",
             font="none 10").place(relx=0, rely=0.5)
    tk.Label(vistor_screen, text="Vistor Name:", fg='white', bg="black",
             font="none 10").place(relx=0, rely=0.7)
    tk.Entry(vistor_screen, width=40, textvariable=rollno).place(
        relx=0.4, rely=0.5)
    tk.Entry(vistor_screen, width=40, textvariable=vistor).place(
        relx=0.4, rely=0.7)
    tk.Button(vistor_screen, text="Add Vistor",
              command=vistorcheckin).place(relx=0.5, rely=0.9)
    tk.Button(vistor_screen, text="Exit", fg="red",
              command=vistor_screen.destroy).place(relx=0.75, rely=0.9)


# <==============================add vistor record==============================================>
# <======================== mark attdendance ==============================>


def attend():
    attdendance = tk.Tk()
    attdendance.geometry("600x200")
    attdendance.configure(bg="black")

    def mark(rollno):
        rollno = (rollno.get())
        print(rollno)
        data = getData()
        marked = False
        for i in data:
            if data[i]['rollno'] == rollno:
                data[i]['attdendance'] += 1
                tk.Label(attdendance, text="Attdendance marked").pack(
                    side="bottom")
                marked = True
            myfile = open("database.txt", "w")
            myfile.write(str(data))
            myfile.close()

        if marked == False:
            tk.Label(attdendance, text="Roll no doesnt exist").pack(
                side="bottom")

    rollno = tk.StringVar(attdendance)

    tk.Label(attdendance, text="Mark attdendance", justify=LEFT,
             font="none 20 bold", fg='white', bg="black").pack(padx=10, pady=20, anchor="w")
    markeME = partial(mark, rollno)

    tk.Label(attdendance, text="Enter Roll no.", fg='white', bg="black",
             font="none 10").place(relx=0, rely=0.5)
    tk.Entry(attdendance, width=40, textvariable=rollno).place(
        relx=0.4, rely=0.5)
    tk.Button(attdendance, text="Mark Attdedance",
              command=markeME).place(relx=0.5, rely=0.7)
    tk.Button(attdendance, text="Exit", fg="red",
              command=attdendance.destroy).place(relx=0.75, rely=0.7)


# <======================== mark attdendance ==============================>


# <========================== View Student Details=================================>

def viewDetails():

    studInfo = tk.Tk()
    studInfo.geometry(_width+'x'+_height)
    studInfo.configure(bg="black")

    def studData(rollno, heading):
        rollno = (rollno.get())
        data = getData()
        stuProf = [data[i]
                   for i in data if data[i]["rollno"] == rollno]
        stuProf = [stuProf[0][i] for i in stuProf[0]]
        print(stuProf)
        posx = 0.01
        for i in range(len(heading)):
            h = Entry(studInfo, width=20, fg='blue', justify='center',
                      font=('Arial', 10, 'bold'))
            e = Entry(studInfo, width=20, fg='black', justify='center',
                      font=('Arial', 10))
            e.place(rely=0.2, relx=posx)
            e.insert(END, heading[i])
            h.place(rely=0.25, relx=posx)
            h.insert(END, stuProf[i])
            posx = 0.1+posx

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
        'attdendance'
    ]
    rollno = tk.StringVar(studInfo)
    getStudInfo = partial(studData, rollno, heading)
    tk.Label(studInfo, text="Student Profile",
             font="none 40 bold", fg='white', bg="black").pack(ipady=40, side=TOP)
    ttk.Separator(studInfo, orient='horizontal').place(
        relx=0, rely=0.12, relheight=0.001, relwidth=1)
    tk.Label(studInfo, text="Enter the Roll no of the student",
             bg="black", fg="white", width=50, font="none 15 bold").pack(side="top")
    tk.Entry(studInfo, textvariable=rollno,
             bg="white", fg="black", width=20).pack()
    tk.Button(studInfo, text="Exit", width=20, fg="red",
              command=studInfo.destroy).pack(side="right")
    tk.Button(studInfo, text="Get Info", width=20, fg="black",
              command=getStudInfo).pack(side="right")

# <=============================View Student Details================================>


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
        'attdendance'
    ]
    tk.Label(databases, text="Database View",
             font="none 40 bold", fg='white', bg="black").pack(ipady=40, side=TOP)
    ttk.Separator(databases, orient='horizontal').place(
        relx=0, rely=0.12, relheight=0.001, relwidth=1)
    data = getData()
    # print(data)
    table(databases, data, heading)

    tk.Button(databases, text="Exit", width=20, fg="red",
              command=databases.destroy).pack(side="right")


# <============================== view database =====================================>


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

# <============================ Leave Hostel Room=========================================>


def leaveHostel():
    leaveScreen = tk.Tk()
    leaveScreen.geometry("600x200")
    leaveScreen.configure(bg="black")

    def del_data(roomNo):
        roomNo = (roomNo.get())
        roomNo = int(roomNo)
        print(roomNo)
        data = getData()
        removed_value = data.pop(1, 0)

        if removed_value == 0:
            tk.Label(leaveScreen, text="Data doesn't Exist").pack(
                side="bottom")
        else:
            myfile = open("database.txt", "w")
            myfile.write(str(data))
            myfile.close()
            room_list = open("room_list.txt", "r")
            rooms = room_list.read()
            room_list.close()
            rooms = ast.literal_eval(rooms)
            rooms.append(roomNo)
            new_rooms_list = open("room_list.txt", "w")
            new_rooms_list.write(str(rooms))
            new_rooms_list.close()

            tk.Label(leaveScreen, text="Data Updated successfully").pack(
                side="bottom")

    roomNo = tk.StringVar(leaveScreen)

    tk.Label(leaveScreen, text="Mark attdendance", justify=LEFT,
             font="none 20 bold", fg='white', bg="black").pack(padx=10, pady=20, anchor="w")
    checkOut = partial(del_data, roomNo)

    tk.Label(leaveScreen, text="Enter Room no.", fg='white', bg="black",
             font="none 10").place(relx=0, rely=0.5)
    tk.Entry(leaveScreen, width=40, textvariable=roomNo).place(
        relx=0.4, rely=0.5)
    tk.Button(leaveScreen, text="Leave Room",
              command=checkOut).place(relx=0.5, rely=0.7)
    tk.Button(leaveScreen, text="Exit", fg="red",
              command=leaveScreen.destroy).place(relx=0.75, rely=0.7)


# <============================ Leave Hostel Room =========================================>


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
          height=4).place(relx=0.05, rely=0.19, anchor=CENTER)
tk.Button(menu, text="Mark Attdedance", command=attend, width=20,
          height=4).place(relx=0.05, rely=0.29, anchor=CENTER)
tk.Button(menu, text="Allot Room", command=allot_room, width=20,
          height=4).place(relx=0.05, rely=0.39, anchor=CENTER)
tk.Button(menu, text="Edit Details", command=editDetails, width=20,
          height=4).place(relx=0.05, rely=0.49, anchor=CENTER)
tk.Button(menu, text="View Student Details", command=viewDetails, width=20,
          height=4).place(relx=0.05, rely=0.59, anchor=CENTER)
tk.Button(menu, text="Vistors", command=addVistor, width=20,
          height=4).place(relx=0.05, rely=0.69, anchor=CENTER)
tk.Button(menu, text="Leave Hostel", command=leaveHostel, width=20, fg="black",
          height=4).place(relx=0.05, rely=0.79, anchor=CENTER)
tk.Button(menu, text="Exit", command=lambda: exitWindow(menu), width=20, fg="red",
          height=4).place(relx=0.05, rely=0.89, anchor=CENTER)
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
        stud[room]["attdendance"] = 0

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
        stud[room]["attdendance"] = 0

        database.close()
        database = open("database.txt", "w")
        print("$$$$$$$$")
        database.write(str(stud))
        database.close()


menu.mainloop()
