from tkinter import *

window = Tk()
window.title("Interest calculator")
window.geometry("380x400")
window.configure(bg="#18db13")

def calculate_interest():
    principle = float(principle_entry.get())
    time = float(time_entry.get())
    rate = float(rate_entry.get())
    interest = (principle*rate*time)/100
    interest = round(interest,2)
    name = username.get()
    result_label.destroy()

    output_message = Label(result_frame,text = name+", your interest is"+str(interest), bg="#1db373", font=("Calibri",12), width=40)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label = Label(window,text="PRINCIPLE CALCULATOR", fg="black", bg="#12bd18",font=("Calibri", 20), bd=5)
app_label.place(x=50,y=20)

name_label = Label(window,text="your name!>:(", fg="black", bg="#12bd18",font=("Calibri", 14), bd=1)
name_label.place(x=20,y=90)

username = Entry(window,text="",width=22, bd=2)
username.place(x=150,y=92)

principle_label = Label(window,text="Enter principle", fg="black", bg="#12bd18",font=("Calibri", 14), bd=1)
principle_label.place(x=20,y=140)

rate_label = Label(window,text="Enter rate", fg="black", bg="#12bd18",font=("Calibri", 14), bd=1)
rate_label.place(x=20,y=185)

time_label = Label(window,text="Enter Time", fg="black", bg="#12bd18",font=("Calibri", 14), bd=1)
time_label.place(x=20,y=230)

principle_entry = Entry(window,text="",width=15, bd=2)
principle_entry.place(x=150,y=142)

rate_entry = Entry(window,text="",width=15, bd=2)
rate_entry.place(x=150,y=185)

time_entry = Entry(window,text="",width=15, bd=2)
time_entry.place(x=150,y=230)

calculate_button = Button(window,text = "CALCULATE", fg="#1245be", bg="#1db162", bd=4, command=calculate_interest)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window,text="Result", bg="#ed8173", font=("Calibri",12))
result_frame.pack(padx= 20, pady=20)
result_frame.place(x=20,y=300)

result_label = Label(window,text="", bg="#ed8173", font=("Calibri",12), width=30)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()

