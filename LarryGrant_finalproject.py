from ipaddress import collapse_addresses
from tkinter import *
import tkinter.font as font
from turtle import width
from PIL import Image, ImageTk
import sqlite3
import random
import uuid

root = Tk()
root.title('Checkin App')
root.geometry("500x500")
root.iconbitmap("tkd.ico")

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
    
    select_id = fname.get()

    c.execute("UPDATE students SET classes = classes + 1 WHERE fname = '" + select_id + "'")

    c.execute("SELECT * from students WHERE fname LIKE :fname",
        {

            'fname': select_id
        }
    )
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records[0]:
        print_records += str(record) + "\n"
    
    query_label = Label(root, text="Student Info")
    query_label.grid(row=8,column=0)
    output.config(state="normal")
    output.insert(0.0,print_records)
    output.config(state="disabled")
    ty = Tk()
    ty.iconbitmap("tytkd.ico")

    

    def exit2():
        fname.delete(0,END)
        lname.delete(0,END)
        output.config(state="normal")
        output.delete(0.0,END)
        output.config(state="disabled")
        ty.destroy()
        
     #Adds text to say thank you   
    thankyou_label = Label(ty,font=("Arial", 48),text="Thank you for checking in")
    thankyou_label.grid(row=0, column=1)
      #Create close button2
    myFont = font.Font(size=98, weight='bold')
    tyclose_btn= Button(ty,text="Exit",command=exit2,borderwidth=0,height=10,width=100)
    tyclose_btn['font'] = myFont
    tyclose_btn.grid(row=1, column=1)
    

    #close DB
    conn.commit()

    #close Connection
    conn.close()


    
#Create submit function
def submit():
    #Create DB
    conn = sqlite3.connect('checkin.db')

    #Create Cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO students VALUES(:fname, :lname, :classes)",
            {   'fname': fname.get(),
                'lname': lname.get(),
                'classes': "1"

            }
    )

    fname.delete(0,END)
    lname.delete(0,END)

    #close DB
    conn.commit()

    #close Connection
    conn.close()


def cls():
    fname.delete(0,END)
    lname.delete(0,END)
    output.config(state="normal")
    output.delete(0.0,END)
    output.config(state="disabled")

#Clears the main Screen after Checkin
root.protocol("WM_DELETE_WINDOW", cls) 

#Create close button2
close = PhotoImage(file='exitbutton.png')
close_btn= Button(root, image=close,command= exit,borderwidth=0,height=50,width=100)
close_btn.grid(row=11, column=1,columnspan=6)
    


def exit():
    root.destroy()




  


#Create Boxes
fname = Entry(root, width=30)
fname.grid(row=0, column=1)
lname = Entry(root, width=30)
lname.grid(row=1, column=1)
output = (Text(root, width=45, height=15 ))
output.grid(row=9,column=0, columnspan=3)



#Create Labels
fname_label = Label(root, text="First Name")
fname_label.grid(row=0, column=0)
lname_label = Label(root, text="Last Name")
lname_label.grid(row=1, column=0)
exit_label = Label(root,text="Exit Program")
exit_label.grid(row=10, column=1,columnspan=6)


#Create close button
close = PhotoImage(file='exitbutton.png')
close_btn= Button(root, image=close,command= exit,borderwidth=0,height=50,width=100)
close_btn.grid(row=11, column=1,columnspan=6)
    


#Create New Student Button
new_student = Button(root, text="New Student", command=submit)
new_student.grid(row=6, column=1,)

#Create Checkin Button
checkin = Button(root, text="Checkin", command=checkin)
checkin.grid(row=6, column=0,)

#Create Checkin Button
cls = Button(root, text="Clear Screen", command=cls)
cls.grid(row=6, column=2,)




#close DB
conn.commit()

#close Connection
conn.close()

root.mainloop()