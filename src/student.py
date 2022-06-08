
from tkinter import Tk, Canvas, Label, Frame, Entry, Button, W, E, Listbox, END
import psycopg2


# Config db
db = psycopg2
conection = db.connect(
    host='localhost',
    user='postgres',
    password='1234',
    database='postgres',
    port=5432
)
cursor = conection.cursor()

root = Tk()
root.title('Giot tkinter and postgresSql app')

# Funciones
def saveStudent(name, age, address):
    print(f'{name}, {age}, {address}')
    query = '''INSERT INTO students(name, age, address) VALUES(%s, %s, %s)'''
    cursor.execute(query,(name, age, address))
    print('datos insertados')
    conection.commit()
    displayStudents()

def displayStudents():
    query = '''SELECT * FROM students'''
    cursor.execute(query)
    
    row = cursor.fetchall()

    LB = Listbox(frame, width=20, height=15)
    LB.grid(row=10, columnspan=4,sticky=W+E)

    for i in row:
        LB.insert(END, i)    
    
    conection.commit()





# Canvas
canvas = Canvas(root, width=500, height=500)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Add a student')
label.grid(row=0, column=1)

# Name inputs

label = Label(frame, text='Name')
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# Age inputs
label = Label(frame, text='Age')
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# Address inputs
label = Label(frame, text='Address')
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)
# Button add
button = Button(frame, text='Add', command=lambda: saveStudent(
    entry_name.get(), entry_age.get(), entry_address.get())
    )
button.grid(row=4, column=1, sticky=W+E)


# Search 
label = Label(frame, text='Search')
label.grid(row=5, column=0)

# Search label
label = Label(frame, text='Search By ID')
label.grid(row=6, column=0)

# Search input
idSearch = Entry(frame)
idSearch.grid(row=6, column=1)

"""
"""
def filterStudents(row):
    LB = Listbox(frame, width=20, height=1)
    LB.grid(row=9, columnspan=4,sticky=W+E)
    LB.insert(END, row)

def searchID(id):
    query = '''SELECT * FROM students WHERE id = %s'''
    cursor.execute(query, (id))
    
    row = cursor.fetchone()
    print(row)

    filterStudents(row)

    conection.commit()
    print(id)

"""
"""
# Search button
button = Button(frame, text='Search', command=lambda:searchID(idSearch.get()))
button.grid(row=6, column=2, sticky=W+E)

# Actualiza los datos
displayStudents()
#Mantiene el programa en ejecucion
root.mainloop()


# print('Hello World')
