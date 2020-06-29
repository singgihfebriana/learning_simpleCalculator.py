from tkinter import*

#Making_Calculator

class Simply_Calc:
    def __init__(self,master):
        self.master=master
        master.title("Calc")
        master.geometry("313x376+1000+100")

        #Output_display_numbers

        self.display_number=Entry(master,width=35,borderwidth=5)
        self.display_number.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


        #Button_numbers
        self.number1=Button(master,text="1",padx=40,pady=20,command=lambda:self.button_click(1))
        self.number2=Button(master,text="2",padx=40,pady=20,command=lambda:self.button_click(2))
        self.number3=Button(master,text="3",padx=40,pady=20,command=lambda:self.button_click(3))
        self.number4=Button(master,text="4",padx=40,pady=20,command=lambda:self.button_click(4))
        self.number5=Button(master,text="5",padx=40,pady=20,command=lambda:self.button_click(5))
        self.number6=Button(master,text="6",padx=40,pady=20,command=lambda:self.button_click(6))
        self.number7=Button(master,text="7",padx=40,pady=20,command=lambda:self.button_click(7))
        self.number8=Button(master,text="8",padx=40,pady=20,command=lambda:self.button_click(8))
        self.number9=Button(master,text="9",padx=40,pady=20,command=lambda:self.button_click(9))
        self.number0=Button(master,text="0",padx=40,pady=20,command=lambda:self.button_click(0))

        #button_function
        self.button_clear=Button(master,text="Clear",padx=80,pady=20,command=self.button_clear)
        self.button_add=Button(master,text="+",padx=39,pady=20,command=self.button_add)
        self.button_equal=Button(master,text="=",padx=91,pady=20,command=self.button_equal)


        #Positioning button dan entry

        self.number1.grid(row=3,column=0)
        self.number2.grid(row=3,column=1)
        self.number3.grid(row=3,column=2)

        self.number4.grid(row=2,column=0)
        self.number5.grid(row=2,column=1)
        self.number6.grid(row=2,column=2)

        self.number7.grid(row=1,column=0)
        self.number8.grid(row=1,column=1)
        self.number9.grid(row=1,column=2)

        self.number0.grid(row=4,column=0)

        self.button_add.grid(row=5,column=0)
        self.button_clear.grid(row=4,column=1,columnspan=2)
        self.button_equal.grid(row=5,column=1,columnspan=2)

        #function or processing program

    def button_click(self,number):
        self.current=self.display_number.get()
        self.display_number.delete(0,END)
        self.display_number.insert(0,str(self.current)+str(number))

    def button_clear(self):
        self.display_number.delete(0,END)

    def button_add(self):
        self.first_number=self.display_number.get()
        global f_num
        f_num=int(self.first_number)
        self.display_number.delete(0,END)

    def button_equal(self):
        self.second_number=self.display_number.get()
        self.display_number.delete(0,END)
        self.display_number.insert(0,f_num+int(self.second_number))


root=Tk()
objectof_cals=Simply_Calc(root)
root.mainloop()
