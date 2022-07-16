from tkinter import *

def table():
    global tableFrame
    tableFrame.destroy()
    tableFrame = Frame(root)   
    tableFrame.grid(row=2, pady=10, padx=10)
    try:
        lable = Label(tableFrame, text=f"Table of: {int(tableVal.get())}", font="lucida 25 bold", fg="red")
        lable.grid(row=3, column=2)
        for i in range(10):
            table_v = (i+1)*int(tableVal.get())
            table_l = Label(tableFrame, text=f"{int(tableVal.get())} X {int(i+1)} = {table_v}", font="lucida 20 bold", fg='blue', pady=5)
            table_l.grid(row=4+i, column=2)
    except Exception as e:
        table_l = Label(tableFrame, text="Only Numbers are allowed",font="lucida 20 bold", fg="blue", pady=5)
        table_l.grid(row=4, column=2)
    

# GUI STARTS HERE
root = Tk()
root.title("Jocefyneroot - MyTable")
root.geometry("470x600")
root.minsize(470, 300)

# Creating variable for get user input
tableVal = StringVar()
frm = Frame(root) # Creating a frame to add input field and button in a row
frm.grid(pady=10, padx=10)

# Creating a Entry For Take input
tableEntry = Entry(frm, textvariable=tableVal, width=30, font="lucida 15 bold")
tableEntry.grid(row=1, column=2, padx=10)

# Creating a Button
Button(frm, text="Get Table", fg="white", bg="blue", font="lucida 11 bold", command=table).grid(row=1, column=3)

tableFrame = Frame(root)
tableFrame.grid(row=2, pady=10, padx=10)


# GUI ENDS HERE
root.mainloop()
