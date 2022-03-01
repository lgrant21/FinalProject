from ipaddress import collapse_addresses
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import random
import uuid

root = Tk()
root.title('Checkin App')
root.geometry("500x500")

#Create DB
conn = sqlite3.connect('checkin.db')

#Create Cursor
c = conn.cursor()

#Create Table
'''
c.execute("""CREATE TABLE students (sid int,
                fname text,
                lname text,
                classes int,
)
"""")

'''

def checkin():

    #Create DB
    conn = sqlite3.connect('checkin.db')

    #Create Cursor
    c = conn.cursor()

    c.execute("SELECT *, fname From students")
    records = c.fetchall()
    for row in c.fetchall():
        print(row[1])
        print(row[2])
        print(row[3])
    print(records)
    print_records = ''
    for record in records[0]:
        print_records += str(record) + "\n"

    query_label = Label(root, text="Student Info")
    query_label.grid(row=8,column=0)
    query_data = Label(root, text=print_records)
    query_data.grid(row=9,column=0)



    
#Create submit function
def submit():
    #Create DB
    conn = sqlite3.connect('checkin.db')

    #Create Cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO students VALUES(:fname, :lname, :classes, :sid)",
            {   'sid': str(uuid.uuid4()).replace('-',''), 
                'fname': fname.get(),
                'lname': lname.get(),
                'classes': "1"

            }
    )

    #close DB
    conn.commit()

    #close Connection
    conn.close()



#Create Boxes
fname = Entry(root, width=30)
fname.grid(row=0, column=1)
lname = Entry(root, width=30)
lname.grid(row=1, column=1)
classes = Entry(root, width=30)
classes.grid(row=2, column=1)

#Create Labels
fname_label = Label(root, text="First Name")
fname_label.grid(row=0, column=0)
lname_label = Label(root, text="Last Name")
lname_label.grid(row=1, column=0)
classes_label = Label(root, text="Classes Attended")
classes_label.grid(row=2, column=0)


#Create New Student Button
new_student = Button(root, text="New Student", command=submit)
new_student.grid(row=6, column=1,)

#Create Checkin Button
checkin = Button(root, text="Checkin", command=checkin)
checkin.grid(row=6, column=0,)





#close DB
conn.commit()

#close Connection
conn.close()

root.mainloop()