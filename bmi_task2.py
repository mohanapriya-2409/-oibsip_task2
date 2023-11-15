import tkinter as tk
from tkinter import Label, Entry, Radiobutton, Button, Frame
import matplotlib.pyplot as plt

def reset():
    age.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')
    var.set(0)  # Reset gender radio buttons

def bodymass():
    kg = float(weight_tf.get())
    m = float(height_tf.get())
    m = m / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 2)
    bmi_categories = ""
    if bmi < 18.5:
        bmi_categories = "Underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_categories = "Normal"
    elif 25 <= bmi < 29.9:
        bmi_categories = "Overweight"
    elif bmi >= 29.9:
        bmi_categories = "Obesity"

    custom_message = tk.Toplevel()
    custom_message.title("BMI Categories")
    custom_message.geometry("300x150")  # Set the desired size here

    label = Label(custom_message, text=f"BMI = {bmi} is {bmi_categories}")
    label.pack(padx=20, pady=30)

    ok_button = Button(custom_message, text="OK", command=custom_message.destroy)
    ok_button.pack(pady=10)

    # Plot graph using Matplotlib
    categories = ['Your BMI', 'Normal', 'Overweight', 'Obesity', 'Severe Obesity']
    bmi_values = [bmi, 22, 25, 29, 33]

    plt.figure(figsize=(6, 4))
    plt.bar(categories, bmi_values, color=['purple', 'green', 'yellow', 'red', 'orange'])
    plt.xlabel('BMI Categories')
    plt.ylabel('BMI Values')
    plt.title('BMI Categories Chart')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

window = tk.Tk()
window.title("BMI CALCULATOR")
window.config(bg="aqua")
window.geometry('1000x750')

frame = Frame(
    window,
    padx=100,
    pady=75,
    bg="yellow"
)
frame.pack(expand=True)

var = tk.IntVar()  # Initialize the variable for gender selection

age_lb = Label(frame, text="ENTER YOUR AGE :")
age_lb.grid(row=1, column=1)
age = Entry(frame)
age.grid(row=1, column=2, pady=5)

gen = Label(frame, text='Select Gender')
gen.grid(row=2, column=1)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=5)

male = Radiobutton(frame2, text='Male', variable=var, value=1)
male.pack(side=tk.LEFT)
female = Radiobutton(frame2, text='Female', variable=var, value=2)
female.pack(side=tk.RIGHT)

height_lb = Label(frame, text="Enter Height (cm):")
height_lb.grid(row=3, column=1)
weight_lb = Label(frame, text="Enter Weight (kg):")
weight_lb.grid(row=4, column=1)

height_tf = Entry(frame)
height_tf.grid(row=3, column=2, pady=5)
weight_tf = Entry(frame)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3, text='Calculate', command=bodymass)
cal_btn.pack(side=tk.LEFT)
reset_btn = Button(frame3, text='Reset', command=reset)
reset_btn.pack(side=tk.LEFT)
exit_btn = Button(frame3, text='Exit', command=lambda: window.destroy())
exit_btn.pack(side=tk.RIGHT)

window.mainloop()

