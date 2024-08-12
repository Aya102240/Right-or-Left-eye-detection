# Import the required Libraries
from tkinter import *
from tkinter import ttk
from Right_Left import enterData, visulize, accuracy
# Create an instance of tkinter frame
win= Tk()

# Set the geometry of tkinter frame
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry(f"{width}x{height}")
global y

x = Label(win,text="x-axis").place(x=550,y=40)
y = Label(win,text="y-axis").place(x=550,y=65)
w = Label(win,text="width").place(x=550,y=90)
h = Label(win,text="height").place(x=550,y=115)

# Initialize a label to display the user Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

# Create an entry widget to accept user Input
entry1= Entry(win, width= 20)
entry1.focus_set()
entry1.pack(pady=3)
# Create an entry widget to accept user Input
entry2= Entry(win, width= 20)
entry2.pack(pady=3)
# Create an entry widget to accept user Input
entry3= Entry(win, width= 20)
entry3.pack(pady=3)
# Create an entry widget to accept user Input
entry4= Entry(win, width= 20)
entry4.pack(pady=3)

def result():
   new1 = int(entry1.get())
   new2 = int(entry2.get())
   new3 = int(entry3.get())
   new4 = int(entry4.get())
   new5  = int(new3)*int(new4)
   new_out = enterData(new1, new2, new5)

   if  new_out == 0:
      print("left")
      y = "left"
      return y
   else:
      print("right")
      y = "right"
      return y

def display_text():
   string= result()
   label.configure(text=string)


# Create a button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

# Create button for visulization
ttk.Button(win, text= "Visulization?",width= 20, command= visulize).pack(pady=20)

acc = accuracy()
label=Label(win, text=f"Accuracy: {acc:.2f}", font=("Courier 22 bold"))
label.pack()

win.mainloop()