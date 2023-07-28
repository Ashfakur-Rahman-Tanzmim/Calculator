from tkinter import *
import math

windows = Tk()
windows.title("Calculator")
def calc():
    if input1.get()=="":
        return " "
    else:
        try:
            if "√" in str(input1.get()):
                n=str(input1.get()).replace("√","")
                return math.sqrt(eval(n))
            if "root" in str(input1.get()):
                n=str(input1.get()).replace("root","")
                return math.sqrt(eval(n))
            
            return eval(input1.get())

        except ZeroDivisionError:
            return "Can't Divide by zero"
        except ValueError :
            return "Input a vaid argument"
        except SyntaxError and NameError:
            return "Syntax Error"

def click():
    output["text"]="Result: "+str(calc())


    
button =Button(windows,text="Output",fg="black",command=click)
button.place(relx=0.5, rely=0.5, anchor="center")



label =Label(windows,text="Calculator",fg="black",font=("Times New Roman",16))
label.place(relx=0.5,y=10,anchor="center")
input1= Entry(windows,text="This is Entry Widget",fg="black",bd=1,bg="white")
input1.place(relx=0.5,rely=0.7,anchor="center",height=35,width=200)

output = Label(windows,text="Hello! How are you? I am a calculator.",fg="black",bd=1,bg="white",borderwidth=2,relief='solid',padx=3,pady=3,width=40,height=5)
output.place(relx=0.5,rely=0.3,anchor="center")
result = Label(windows,text="Result:",fg="black",font=("Times New Roman",16))
result.place(x=30,y=70)



#...............main activasion
windows.geometry("400x500")
windows.minsize(400,500)
windows.maxsize(400,500)
windows.mainloop()
