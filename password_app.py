from tkinter import *
import pyperclip
import string,random


def copy():
    random = passwordField.get()
    pyperclip.copy(random)


def generate():
    small = string.ascii_lowercase
    capital = string.ascii_uppercase
    num = string.digits
    special = string.punctuation

    all = small + capital + num + special

    password_length = int(length_Box.get())

    if choice.get() ==1:
        passwordField.insert(0,random.sample(small,password_length))
    elif choice.get() ==2:
        passwordField.insert(0,random.sample(capital,password_length))

    elif choice.get() ==3:
        passwordField.insert(0,random.sample(all,password_length))


root = Tk()
root.resizable(0,0)
root.config(bg='gray20')
choice = IntVar()
Font=('arial',13,'bold')
passwordLabel = Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid()
weakradioButton = Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=10)
MediumradioButton = Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
MediumradioButton.grid(pady=10)
StrongradioButton = Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
StrongradioButton.grid(pady=10)

lengthLabel = Label(root,text='Password Length',font=Font,bg='gray20',fg='white')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root,from_=5,to_=8,width = 5, font =Font)
length_Box.grid(pady=5)

generateButton= Button(root,text='Generate',font=Font,command=generate)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=5)


copyButton= Button(root,text='Copy Text',font=Font,command = copy)
copyButton.grid(pady=5)


root.mainloop()
