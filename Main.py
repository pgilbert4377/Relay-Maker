import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
import itertools

con = sqlite3.connect("Main.db")
cur = con.cursor()

"""
cur.execute("CREATE TABLE eightu(swimmerID INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,lname TEXT NOT NULL,free_time DECIMAL(5,2),back_time DECIMAL(5,2),breast_time DECIMAL(5,2),fly_time DECIMAL(5,2),absent INTEGER)")
cur.execute("CREATE TABLE ninetenmale(swimmerID INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,lname TEXT NOT NULL,free_time DECIMAL(5,2),back_time DECIMAL(5,2),breast_time DECIMAL(5,2),fly_time DECIMAL(5,2),absent INTEGER)")
cur.execute("CREATE TABLE ninetenfemale(swimmerID INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,lname TEXT NOT NULL,free_time DECIMAL(5,2),back_time DECIMAL(5,2),breast_time DECIMAL(5,2),fly_time DECIMAL(5,2),absent INTEGER)")
cur.execute("CREATE TABLE elfmale(swimmerID INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,lname TEXT NOT NULL,free_time DECIMAL(5,2),back_time DECIMAL(5,2),breast_time DECIMAL(5,2),fly_time DECIMAL(5,2),absent INTEGER)")
cur.execute("CREATE TABLE elffemale(swimmerID INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,lname TEXT NOT NULL,free_time DECIMAL(5,2),back_time DECIMAL(5,2),breast_time DECIMAL(5,2),fly_time DECIMAL(5,2),absent INTEGER)")
cur.execute("CREATE TABLE trecemale(swimmerID INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,lname TEXT NOT NULL,free_time DECIMAL(5,2),back_time DECIMAL(5,2),breast_time DECIMAL(5,2),fly_time DECIMAL(5,2),absent INTEGER)")
cur.execute("CREATE TABLE trecefemale(swimmerID INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,lname TEXT NOT NULL,free_time DECIMAL(5,2),back_time DECIMAL(5,2),breast_time DECIMAL(5,2),fly_time DECIMAL(5,2),absent INTEGER)")
cur.execute("CREATE TABLE quincemale(swimmerID INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,lname TEXT NOT NULL,free_time DECIMAL(5,2),back_time DECIMAL(5,2),breast_time DECIMAL(5,2),fly_time DECIMAL(5,2),absent INTEGER)")
cur.execute("CREATE TABLE quincefemale(swimmerID INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,lname TEXT NOT NULL,free_time DECIMAL(5,2),back_time DECIMAL(5,2),breast_time DECIMAL(5,2),fly_time DECIMAL(5,2),absent INTEGER)")
#"""

def tableNamer(a,g):
    tbl  = ''
    if a == '8&U':
        tbl += 'eightu'
    elif a == '9-10':
        if g == 'Male':
            tbl += 'ninetenmale'
        else:
            tbl += 'ninetenfemale'
    elif a == '11-12':
        if g == 'Male':
            tbl += 'elfmale'
        else:
            tbl += 'elffemale'
    elif a == '13-14':
        if g == 'Male':
            tbl += 'trecemale'
        else:
            tbl += 'trecefemale'
    else:
        if g == 'Male':
            tbl += 'quincemale'
        else:
            tbl += 'quincefemale'
    return tbl

def reset_absences():
    s = "UPDATE eightu SET absent = 0"
    cur.execute(s)
    s = "UPDATE ninetenmale SET absent = 0"
    cur.execute(s)
    s = "UPDATE ninetenfemale SET absent = 0"
    cur.execute(s)
    s = "UPDATE elfmale SET absent = 0"
    cur.execute(s)
    s = "UPDATE elffemale SET absent = 0"
    cur.execute(s)
    s = "UPDATE trecemale SET absent = 0"
    cur.execute(s)
    s = "UPDATE trecefemale SET absent = 0"
    cur.execute(s)
    s = "UPDATE quincemale SET absent = 0"
    cur.execute(s)
    s = "UPDATE quincefemale SET absent = 0"
    cur.execute(s)
    con.commit()
    
def update_time():
    text.delete('1.0',END)
    a = swimmer_age_entry.get()
    g = swimmer_gender_entry.get()
    f = swimmer_fname_entry.get()
    l = swimmer_lname_entry.get()
    stroke = stroke_entry.get().lower()
    time = float(time_entry.get())
    t = tableNamer(a,g)
    s = "SELECT * FROM " + str(t) + " WHERE fname = '" + str(f) + "' AND lname = '" + str(l) + "'"
    res = cur.execute(s)
    if res.fetchone() is None:
        s = "INSERT INTO " + str(t) + " (fname,lname,free_time,back_time,breast_time,fly_time,absent) VALUES('" + str(f) + "','" + str(l) + "',999.99,999.99,999.99,999.99,0)"
        cur.execute(s)
    s = "SELECT " + str(stroke) + "_time FROM " + str(t) + " WHERE fname = '" + str(f) + "' AND lname = '" + str(l) + "'"
    res = cur.execute(s)
    comp = res.fetchone()[0]
    if float(comp) > time:
        s = "UPDATE " + str(t) + " SET " + str(stroke) + "_time = " + str(time) + " WHERE fname = '" + str(f) + "' AND lname = '" + str(l) + "'"
        cur.execute(s)
    s = "SELECT fname,lname,free_time,back_time,breast_time,fly_time FROM " + str(t) + " WHERE fname = '" + str(f) + "' AND lname = '" + str(l) + "'"
    res = cur.execute(s)
    rows = res.fetchall()
    for row in rows:
        fname,lname,free_time,back_time,breast_time,fly_time = row
        sentence = f"{fname} {lname} - Free: {free_time}, Back: {back_time}, Breast: {breast_time}, Fly: {fly_time}"
    text.insert(END,sentence)
    con.commit()

def absence_input():
    text.delete('1.0',END)
    ab = int(absent_entry.get())
    a = swimmer_age_entry.get()
    g = swimmer_gender_entry.get()
    f = swimmer_fname_entry.get()
    l = swimmer_lname_entry.get()
    t = tableNamer(a,g)
    s = "UPDATE " + str(t) + " SET absent = " + str(ab) + " WHERE fname = '" + str(f) + "' AND lname = '" + str(l) + "'"
    cur.execute(s)
    if ab == 1:
        out = "absent"
    else:
        out = "present"
    text.insert(END,str(f) + " " + str(l) + " is marked as " + out)
    con.commit()
    
def make_relay():
    text.delete('1.0',END)
    tab = ['eightu','ninetenmale','ninetenfemale','elfmale','elffemale','trecemale','trecefemale','quincemale','quincefemale']
    min_combos = []
    for i in range(9):
        free_times=[]
        back_times=[]
        breast_times=[]
        fly_times=[]
        s = "SELECT swimmerID,fname,lname,free_time FROM " + str(tab[i]) + " WHERE absent = 0"
        res = cur.execute(s)
        times = res.fetchall()
        for row in times:
            free_times.append([str(f"{row[1]} {row[2]}"),float(f"{row[3]}")])
        s = "SELECT swimmerID,fname,lname,back_time FROM " + str(tab[i]) + " WHERE absent = 0"
        res = cur.execute(s)
        times = res.fetchall()
        for row in times:
            back_times.append([str(f"{row[1]} {row[2]}"),float(f"{row[3]}")])
        s = "SELECT swimmerID,fname,lname,breast_time FROM " + str(tab[i]) + " WHERE absent = 0"
        res = cur.execute(s)
        times = res.fetchall()
        for row in times:
            breast_times.append([str(f"{row[1]} {row[2]}"),float(f"{row[3]}")])
        s = "SELECT swimmerID,fname,lname,fly_time FROM " + str(tab[i]) + " WHERE absent = 0"
        res = cur.execute(s)
        times = res.fetchall()
        for row in times:
            fly_times.append([str(f"{row[1]} {row[2]}"),float(f"{row[3]}")])
        s = "SELECT COUNT(swimmerID) FROM " + str(tab[i]) + " WHERE absent = 0"
        res = cur.execute(s)
        count = res.fetchone()[0]
        print(count)
        min_total = float('inf')
        free = 0
        back = 0
        breast = 0
        fly = 0
        if count < 4:
            min_combos.append(f"There are not enough swimmers in {ageGroups2[i]} for a relay.")
        else:
            for indices in itertools.permutations(range(count),4):
                w,x,y,z = indices
                if tab[i] == 'ninetenmale' or tab[i] == 'ninetenfemale':
                    total = free_times[w][1] + back_times[x][1] + breast_times[y][1] + fly_times[z][1] + fly_times[z][1]
                else:
                    total = free_times[w][1] + back_times[x][1] + breast_times[y][1] + fly_times[z][1]
                if total < min_total:
                    min_total = total
                    free = w
                    back = x
                    breast = y
                    fly = z
            min_combos.append(f"{ageGroups2[i]} | Back: {back_times[back][0]}, Breast: {breast_times[breast][0]}, Fly: {fly_times[fly][0]}, Free: {free_times[free][0]}")
            print(f"{min_total:.2f}")
            #print(free_times)
    text.insert(END,min_combos[0] + "\n" + min_combos[1] + "\n" + min_combos[2] + "\n" + min_combos[3] + "\n" + min_combos[4] + "\n" + min_combos[5] + "\n" + min_combos[6] + "\n" + min_combos[7] + "\n" + min_combos[8])
    

ageGroups = ['8&U','9-10','11-12','13-14','15-18']
ageGroups2 = ['8&U','9-10 Boys','9-10 Girls','11-12 Boys','11-12 Girls','13-14 Boys','13-14 Girls','15-18 Boys','15-18 Girls']
events = ['Free','Back','Breast','Fly']
yn = ["Yes","No"]
mf = ["Male","Female"]

root = tk.Tk()
root.title("Swimmer Time Input")

frame = tk.Frame(root)
frame.pack()

frame_label = tk.Label(frame,text="Fill in the boxes with the information")
frame_label.grid(row=0,column=0,columnspan=2)

swimmer_frame = tk.LabelFrame(frame,text="Swimmer Information")
swimmer_frame.grid(row=1,column=0,columnspan=2,sticky="news")

swimmer_fname_label = tk.Label(swimmer_frame,text="First Name")
swimmer_fname_label.grid(row=0,column=0)
swimmer_fname_entry = tk.Entry(swimmer_frame)
swimmer_fname_entry.grid(row=1,column=0)

swimmer_lname_label = tk.Label(swimmer_frame,text="Last Name")
swimmer_lname_label.grid(row=0,column=1)
swimmer_lname_entry = tk.Entry(swimmer_frame)
swimmer_lname_entry.grid(row=1,column=1)

swimmer_age_label = tk.Label(swimmer_frame,text="Age Group")
swimmer_age_label.grid(row=0,column=2)
swimmer_age_entry = ttk.Combobox(swimmer_frame,values=ageGroups)
swimmer_age_entry.grid(row=1,column=2)

swimmer_gender_label = tk.Label(swimmer_frame,text="Gender")
swimmer_gender_label.grid(row=0,column=3)
swimmer_gender_entry = ttk.Combobox(swimmer_frame,values=mf)
swimmer_gender_entry.grid(row=1,column=3)

for widget in swimmer_frame.winfo_children():
    widget.grid_configure(padx=15,pady=5)

event_frame = tk.LabelFrame(frame,text="Event Information")
event_frame.grid(row=2,column=0,columnspan=2,sticky="ew")

event_frame.columnconfigure(0,weight=1)
event_frame.columnconfigure(1,weight=1)
event_frame.columnconfigure(2,weight=1)
event_frame.columnconfigure(3,weight=1)

stroke_entry = ttk.Combobox(event_frame,values=events)
stroke_entry.grid(row=0,column=0,sticky="news")
time_entry = tk.Entry(event_frame)
time_entry.grid(row=0,column=3,sticky="news")

button1 = tk.Button(event_frame,text="Update Time",command=update_time)
button1.grid(row=3,column=0,columnspan=4,sticky="ew")
    
for widget in event_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)
    
absent_frame = tk.LabelFrame(frame,text="Attendance Information")
absent_frame.grid(row=3,column=0,columnspan=2,sticky="ew")

absent_frame.columnconfigure(0, weight=1)
absent_frame.columnconfigure(1, weight=1)

absence_label = tk.Label(absent_frame,text="Absent?")
absence_label.grid(row=0,column=0,sticky="w")
absent_entry = tk.IntVar(value=0)
absence_entry = tk.Checkbutton(absent_frame,variable=absent_entry,onvalue=1,offvalue=0)
absence_entry.grid(row=0,column=1,sticky="w")
button2 = tk.Button(absent_frame,text="Update Absence",command=absence_input)
button2.grid(row=1,column=0,columnspan=2,sticky="ew")
button3 = tk.Button(absent_frame,text="Reset Absences",command=reset_absences)
button3.grid(row=2,column=0,columnspan=2,sticky="ew")



create_frame = tk.LabelFrame(frame,text="Create Relay")
create_frame.grid(row=4,column=0,columnspan=2,sticky="news")

create_frame.columnconfigure(0,weight=1)
create_frame.columnconfigure(1,weight=1)

button4 = tk.Button(create_frame,text="Generate Relays",command=make_relay)
button4.grid(row=2,column=0,columnspan=2,sticky="ew")

text = Text(frame)
text.grid(row=5,column=1,rowspan=5)

for widget in frame.winfo_children():
    widget.grid_configure(padx=20,pady=5)

root.mainloop()
