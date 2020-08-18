from tkinter import*
import tkinter.messagebox
import tkinter as tk
import tkinter as tkr

from tkinter import ttk
import random
import time
import datetime

import database2
import database3


def main():
    root = tk.Tk()
    app = Window1(root)


class Window1:
    def __init__(self, std):
        self.std = std


        self.std.title("Student Database Login")
        self.std.geometry("1400x750+50+0")
        self.std.config(bg ="lavender")
        self.frame = Frame(self.std, bg ="lavender")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        

      
#-------------------------

        self.lblTitle = Label(self.frame, text = "St. Francis Institution Technology", font=("georgia", 50, "bold"), bg="lavender", fg="black")
        self.lblTitle.grid(row = 1,column = 2,columnspan=2, pady=40)

        self.lblTitle = Label(self.frame, text = "Student Database Login", font=("Calibri", 27, "bold"), bg="lavender", fg="black")
        self.lblTitle.grid(row = 4,column = 2,columnspan=2, pady=40)

        self.lblTitle = Label(self.frame, text = "                ", font=("arial", 5, "bold"), bg="lavender", fg="black")
        self.lblTitle.grid(row = 5,column = 2,columnspan=2, pady=10)

#---------------------------------------------

        self.LoginFrame1= LabelFrame(self.frame, width=1300, height=600, font=("arial",20, "bold"),relief="ridge", bg="lightsteelblue", bd=8)
        self.LoginFrame1.grid(row=10, column=2,columnspan=2)

        self.LoginFrame2= LabelFrame(self.frame, width=1300, height=600, font=("arial",20, "bold"),relief="ridge", bg="lightsteelblue", bd=6)
        self.LoginFrame2.grid(row=11, column=2,columnspan=2)

#----------------------------------------

        self.lblUsername = Label(self.LoginFrame1,text =" Username ", font=("arial", 20, "bold"), bd=22, bg="lightsteelblue", fg ="midnightblue")
        self.lblUsername.grid(row=10, column=3)
        self.txtUsername= Entry(self.LoginFrame1,font=("arial", 20),bd=4, textvariable=self.Username)
        self.txtUsername.grid(row=10, column=4,padx=8)

        self.lblPassword = Label(self.LoginFrame1,text =" Password ", font=("arial", 20, "bold"), bd=22, bg="lightsteelblue", fg ="midnightblue")
        self.lblPassword.grid(row=11, column=3)
        self.txtPassword= Entry(self.LoginFrame1,font=("arial", 20),bd=4, show='*', textvariable=self.Password)
        self.txtPassword.grid(row=11, column=4,padx=8)


#---------------------------------------------

        self.btnLogin = Button( self.LoginFrame2, text = "Login", width=17, font=("arial", 15, "bold"), command = self.Login)
        self.btnLogin.grid(row=10,column=2, pady=8, padx=8)

        self.btnExit = Button( self.LoginFrame2, text = "Exit", width=17, font=("arial", 15, "bold") ,command =self.Exit)
        self.btnExit.grid(row=10,column=3 , pady=8, padx=8)


#------------------------------------------------

    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())
        if (u==str("student") and p==str(123456)):
            self.newWindow= Toplevel(self.std)
            self.app = Window2(self.newWindow)
        else:
            tkinter.messagebox.showinfo("Staff Login","Invalid Password or Username")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("Student Database Management System","Do you want to exit?")
        if self.Exit > 0:
            self.std.destroy()
        else:
            command = self.new_window
            return


#---------------------------------------------                          

    def new_window(self):
        self.newWindow = Toplevel(self.std)
        self.app = Window2(self.newWindow)
        


#***************************************************************************************************************************************************************

class Window2:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("865x500+300+100")
        self.root.config(bg="papayawhip")


#................
        MainFrame = Frame(self.root, bg="papayawhip")
        MainFrame.grid()
#.........
        TitFrame2 = Frame(MainFrame, bg="papayawhip", relief = RIDGE)
        TitFrame2.pack(side=TOP)
        
        TitFrame = Frame(MainFrame, padx=8, pady=8, bg="papayawhip", relief = RIDGE)
        TitFrame.pack(side=TOP)

        TitFrame1 = Frame(MainFrame,  bg="papayawhip", relief = RIDGE)
        TitFrame1.pack(side=TOP)

        self.lblTit = Label(TitFrame1 ,font=('Arial', 14,'bold'), text="  www.sfiteng.org  ",bg="ghostwhite")
        self.lblTit.grid()
        self.lblTit = Label(TitFrame1 ,font=('Arial', 25,'bold'), text="       ",bg="papayawhip")
        self.lblTit.grid()
        self.lblTit = Label(TitFrame2 ,font=('arial', 0), text="    ",bg="papayawhip")
        self.lblTit.grid()
#..........

        self.lblTit = Label(TitFrame ,font=('Times New Roman', 35,'bold'), fg="maroon",text="  Student Database Management System  ",bg="papayawhip")
        self.lblTit.grid()

        ButtonFrame1 = Frame(MainFrame, width=300, height=70, padx=18, pady=10, bg="papayawhip", relief = RIDGE)
        ButtonFrame1.pack(side=BOTTOM)
        self.lblTit = Label(ButtonFrame1,font=('Arial', 14,'bold'),text="PAYMENT DETAILS:",bg="papayawhip")
        self.lblTit.grid()
        
        ButtonFrame = Frame(MainFrame, width=300, height=70, padx=18, pady=10, bg="papayawhip", relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        self.lblTit = Label(ButtonFrame ,font=('Arial', 14,'bold'), text="STUDENT DETAILS:",bg="papayawhip")
        self.lblTit.grid()
        
        
        
        
        
#----------------------------
        self.btnAddDate = Button(ButtonFrame,text="Add ", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue",command=self.addD)
        self.btnAddDate.grid(row=1, column=0,padx=4,pady=4)

        self.btnDisplayDate = Button(ButtonFrame,text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=self.DisplayD)
        self.btnDisplayDate.grid(row=1, column=2,padx=4,pady=4)

        self.btnAdd1Date = Button(ButtonFrame1,text="Add", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=self.addD2)
        self.btnAdd1Date.grid(row=1, column=0, padx=4,pady=4)


        self.btnDisplay1Date = Button(ButtonFrame1,text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=self.DisplayD2)
        self.btnDisplay1Date.grid(row=1, column=1,padx=4,pady=4)
#---------------------------------
    def addD(self):
        self.newWindow= Toplevel(self.root)
        self.app = Addwindow(self.newWindow)

    def new_window(self):
        self.newWindow = Toplevel(self.std)
        self.app = Window2(self.newWindow)


    def DisplayD(self):
        self.newWindow= Toplevel(self.root)
        self.app = Displaywindow(self.newWindow)

    def new_window(self):
        self.newWindow = Toplevel(self.std)
        self.app = Window2(self.newWindow)


    def addD2(self):
        self.newWindow= Toplevel(self.root)
        self.app = Addwindow2(self.newWindow)

    def new_window(self):
        self.newWindow = Toplevel(self.std)
        self.app = Window2(self.newWindow)


    def DisplayD2(self):
        self.newWindow= Toplevel(self.root)
        self.app = Displaywindow2(self.newWindow)

    def new_window(self):
        self.newWindow = Toplevel(self.std)
        self.app = Window2(self.newWindow)
    
    
    
#****************************************************************************************************************************************************
        
class Addwindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add")
        self.root.geometry("1300x700+85+0")
        self.root.config(bg="ghostwhite")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        #Age = StringVar()
        Gender = StringVar()
        Address= StringVar()
        Mobile = StringVar()


        #===============================Function=======================        
        def checked():
            message="Male"
            message+=Gender.get()

            self.txtGen.delete(0,END)
            self.txtGen.insert(0,message)
            
        def checkedf():
            message="Female"
            message+=Gender.get()

            self.txtGen.delete(0,END)
            self.txtGen.insert(0,message)
#...............................................
       
        def check1():
            message="EXTC"
            message+=Address.get()

            self.txtAdd.delete(0,END)
            self.txtAdd.insert(0,message)
            
        def check2():
            message="CMPN"
            message+=Address.get()

            self.txtAdd.delete(0,END)
            self.txtAdd.insert(0,message)

    
        def check3():
            message="IT"
            message+=Address.get()

            self.txtAdd.delete(0,END)
            self.txtAdd.insert(0,message)

        def check4():
            message="Mech"
            message+=Address.get()

            self.txtAdd.delete(0,END)
            self.txtAdd.insert(0,message)
        
 #..................................................             

        


        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtSna.delete(0,END)
            self.txtDob.delete(0,END)
            #self.txtAge.delete(0,END)
            self.txtGen.delete(0,END)
            self.txtAdd.delete(0,END)
            self.txtMob.delete(0,END)

        def addData():
            if(len(StdID.get())!=0):
                database2.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(),  Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)    
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Gender.get(), Address.get(), Mobile.get()))



        def DisplayData():
            studentlist.delete(0,END)
            for row in database2.viewData():
                studentlist.insert(END, row, str(""))
                                       

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END,sd[3])
            self.txtDob.delete(0,END)
            self.txtDob.insert(END,sd[4])
            #self.txtAge.delete(0,END)
            #self.txtAge.insert(END,sd[5])
            self.txtGen.delete(0,END)
            self.txtGen.insert(END,sd[5])
            self.txtAdd.delete(0,END)
            self.txtAdd.insert(END,sd[6])
            self.txtMob.delete(0,END)
            self.txtMob.insert(END,sd[7])
                              


        def DeleteData():
            if(len(StdID.get())!=0):
                database2.deleteRec(sd[0])
                clearData()
                DisplayData()
                

        def searchDatabase():
            studentlist.delete(0,END) 
            for row in database2.searchData(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Gender.get(), Address.get(), Mobile.get()):
                studentlist.insert(END, row, str(""))


        def update():
            if(len(StdID.get())!=0):
                database2.deleteRec(sd[0])
            if(len(StdID.get())!=0):
                database2.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)                      
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(),  Gender.get(), Address.get(), Mobile.get()))



#================================Frame=========================
        MainFrame = Frame(self.root, bg="ghostwhite")
        MainFrame.grid()
#.........
        TitFrame2 = Frame(MainFrame, bg="ghostwhite", relief = RIDGE)
        TitFrame2.pack(side=TOP)
#.........        
        TitFrame = Frame(MainFrame, bd=6, padx=54, pady=8, bg="lavender", relief = RIDGE)
        TitFrame.pack(side=TOP)

        TitFrame1 = Frame(MainFrame,  bg="ghostwhite", relief = RIDGE)
        TitFrame1.pack(side=TOP)
#..........
       
        self.lblTit = Label(TitFrame2 ,font=('arial', 10), text="    ",bg="ghostwhite")
        self.lblTit.grid()

        self.lblTit = Label(TitFrame1 ,font=('arial', 10), text="    ",bg="ghostwhite")
        self.lblTit.grid()
#..........

        self.lblTit = Label(TitFrame ,font=('Times New Roman', 25,'bold'), fg="midnightblue",text="  STUDENT DETAILS  ",bg="lavender")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame,  width=1350, height=70, padx=18, pady=10, bg="ghostwhite", relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)
#...............
        DataFrame = Frame(MainFrame, width=1300,height=16, bg="ghostwhite", relief = RIDGE)
        DataFrame.pack(side=BOTTOM)
#..................                
        DataFrame = Frame(MainFrame, bd=3, width=1300,height=400, padx=14, pady=14, bg="lavender", relief = RIDGE)
        DataFrame.pack(side=BOTTOM)
        


        DataFrameLEFT = LabelFrame(DataFrame, bd=8, width=1000, height=650, padx=20,pady=20, bg="lavender", relief = RIDGE)
        DataFrameLEFT.pack(side=LEFT)
#..................
        DataFrameRIGHT = LabelFrame(DataFrame, width=25,height=300, bg="lavender", relief = RIDGE, font=('georgia', 16),fg ='saddlebrown' , text="*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*")
        DataFrameRIGHT.pack(side=LEFT)
#...............

        DataFrameRIGHT = LabelFrame(DataFrame, bd=5, width=450,height=300, padx=31, pady=3, bg="lavender", relief = RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)

#=======================Labels and entries================================
        
        self.lblStdID = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="Student PID:", padx=2, pady=2, bg="lavender")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=StdID,bd=2, width=35)
        self.txtStdID.grid(row=0, column=1, sticky=W)

        self.lblfna = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="First Name:", padx=2, pady=2, bg="lavender")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=Firstname,bd=2, width=35)
        self.txtfna.grid(row=1, column=1, sticky=W)

        self.lblSna = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="Last Name:", padx=2, pady=2, bg="lavender")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=Surname,bd=2, width=35)
        self.txtSna.grid(row=2, column=1, sticky=W)

        self.lblDob = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="Date of Birth:", padx=2, pady=2, bg="lavender")
        self.lblDob.grid(row=3, column=0, sticky=W)
        self.txtDob = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=DoB,bd=2, width=35)
        self.txtDob.grid(row=3, column=1, sticky=W)
        '''
        self.lblAge = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="Age:", padx=2, pady=2, bg="lavender")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=Age, bd=2,width=35)
        self.txtAge.grid(row=4, column=1, sticky=W)
        '''
#=---------------------
       
        self.lblGen = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="Gender:", padx=2, pady=2, bg="lavender")
        self.lblGen.grid(row=5, column=0, sticky=W)
        
        self.checkGen = Radiobutton(DataFrameLEFT,text="Male",variable=Gender ,command=checked,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.checkGen.grid(row=5,column=0,columnspan=8)
      
        self.checkGen = Radiobutton(DataFrameLEFT,text="Female",variable=Gender, command=checkedf,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.checkGen.grid(row=5,column=1,columnspan=20)
        self.txtGen = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=Gender,bd=2, width=9)
        self.txtGen.grid(row=5, column=1, sticky=W)

       
#-------------------------

        
#--------------------------------
        self.lblAdd = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="Department:", padx=2, pady=2, bg="lavender")
        self.lblAdd.grid(row=6, column=0, sticky=W)
       
        self.ckAdd = Radiobutton(DataFrameLEFT,text="EXTC",variable=Address ,command=check1,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.ckAdd.grid(row=6,column=0,columnspan=8)
      
        self.ckAdd = Radiobutton(DataFrameLEFT,text="CMPN",variable=Address, command=check2,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.ckAdd.grid(row=6,column=1,columnspan=6)

        self.ckAdd = Radiobutton(DataFrameLEFT,text="IT",variable=Address, command=check3,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.ckAdd.grid(row=7,column=0,columnspan=2)

        self.ckAdd = Radiobutton(DataFrameLEFT,text="Mechanics",variable=Address, command=check4,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.ckAdd.grid(row=7,column=1,columnspan=8)
        
        
        self.txtAdd = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=Address,bd=2, width=9)
        self.txtAdd.grid(row=6, column=1, sticky=W)

#------------------------------------------
        

        

        self.lblMob = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="Mobile No.:", padx=2, pady=2, bg="lavender")
        self.lblMob.grid(row=9, column=0, sticky=W)
        self.txtMob = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=Mobile,bd=2, width=35)
        self.txtMob.grid(row=9, column=1, sticky=W)

#=============================listbox & Scrollbar Widge=====================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=45, height=17, font=('dubai', 13, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)


        

#===================Button Widget=============================================
                        
        self.btnAddDate = Button(ButtonFrame,text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=addData)
        self.btnAddDate.grid(row=1, column=0,padx=4,pady=4)

        self.btnDisplayDate = Button(ButtonFrame,text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=DisplayData)
        self.btnDisplayDate.grid(row=1, column=1,padx=4,pady=4)

        self.btnUpdateDate = Button(ButtonFrame,text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=update)
        self.btnUpdateDate.grid(row=1, column=2, padx=4,pady=4)

        self.btnSearchDate = Button(ButtonFrame,text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=searchDatabase)
        self.btnSearchDate.grid(row=1, column=3, padx=4,pady=4)

        self.btnClearDate = Button(ButtonFrame,text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=clearData)
        self.btnClearDate.grid(row=2, column=1, padx=4,pady=4)

        self.btnDeleteDate = Button(ButtonFrame,text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=DeleteData)
        self.btnDeleteDate.grid(row=2, column=2,padx=4,pady=4)

        
        







#*****************************************************************************************************************************************************************************************************
class Displaywindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Display")
        self.root.geometry("1550x600+0+0")
        self.root.config(bg="ghostwhite")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        #Age = StringVar()
        Gender = StringVar()
        Address= StringVar()
        Mobile = StringVar()

    


        def DisplayData():
            
            for row in database2.viewData():
                studentlist.insert(END, row, str("   "))
                #print(row)
                self.tree.insert("",tk.END,values=row)
                

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END,sd[3])
            self.txtDob.delete(0,END)
            self.txtDob.insert(END,sd[4])
            #self.txtAge.delete(0,END)
            #self.txtAge.insert(END,sd[5])
            self.txtGen.delete(0,END)
            self.txtGen.insert(END,sd[6])
            self.txtAdd.delete(0,END)
            self.txtAdd.insert(END,sd[7])
            self.txtMob.delete(0,END)
            self.txtMob.insert(END,sd[8])

            


#---------------------------
        MainFrame = Frame(self.root, bg="ghostwhite")
        MainFrame.grid()
#.........
        TitFrame2 = Frame(MainFrame, bg="ghostwhite", relief = RIDGE)
        TitFrame2.pack(side=TOP)
#.........        
        TitFrame = Frame(MainFrame, bd=6, padx=54, pady=8, bg="lavender", relief = RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame ,font=('Times New Roman', 35,'bold'), fg="midnightblue",text="  Student Details  ",bg="lavender")
        self.lblTit.grid()

        
        DataFrame = Frame(MainFrame, width=1300,height=16, bg="ghostwhite", relief = RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameRIGHT = LabelFrame(DataFrame, bd=5, width=2000,height=300, bg="lavender", relief = RIDGE)
        DataFrameRIGHT.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, width=100, height=70, padx=18, pady=10, bg="ghostwhite", relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        #--------------------

        self.btnDisplayDate = Button(ButtonFrame,text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=DisplayData)
        self.btnDisplayDate.grid(row=0, column=2,padx=4,pady=4)


        
        
        
        self.tree= ttk.Treeview(DataFrameRIGHT, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8"), show='headings')
        self.tree.grid(row=0, column=2)
        self.tree.heading("#1", text="Sr.No")
        self.tree.heading('#2', text='PID')
        self.tree.heading("#3", text="FIRST NAME")
        self.tree.heading("#4", text="LAST NAME")
        self.tree.heading('#5', text='DOB')
        self.tree.heading('#6', text='GENDER')
        self.tree.heading('#7', text='DEPARTMENT')
        self.tree.heading('#8', text='MOBILE ')
        
        #self.tree.pack()

        
        
        


        #=============================listbox & Scrollbar Widge=====================
        
        scrollbar = Scrollbar(DataFrameRIGHT)
        #scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=1000, height=100, font=('dubai', 15, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect >>', StudentRec)
        #studentlist.grid(row=0, column=0, padx=8)
        #scrollbar.config(command = studentlist.yview)

        
#*********************************************************************************************************************************************************************************************
class Addwindow2:
    def __init__(self, root):

        CSem = ["Choose semester","I","II","III","IV","V","VI","VII","VIII"]
        
        self.root = root
        self.root.title("Add Payment Details:")
        self.root.geometry("1250x800+85+0")
        self.root.config(bg="ghostwhite")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Semester = tkr.StringVar()
        Payment = StringVar()
        Status = StringVar()

        Semester.set(CSem[0])
        

        #===============================Function=======================        
        def checked():
            message="Cash"
            message+=Payment.get()

            self.txtPay.delete(0,END)
            self.txtPay.insert(0,message)
            
        def checkedf():
            message="Check"
            message+=Payment.get()

            self.txtPay.delete(0,END)
            self.txtPay.insert(0,message)
#...............................................
       
        def check1():
            message="Paid"
            message+=Status.get()

            self.txtSts.delete(0,END)
            self.txtSts.insert(0,message)
            
        def check2():
            message="Unpaid"
            message+=Status.get()

            self.txtSts.delete(0,END)
            self.txtSts.insert(0,message)

    
        
 #..................................................             

        


        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtSna.delete(0,END)
            self.txtSem.delete(0,END)
            self.txtPay.delete(0,END)
            self.txtSts.delete(0,END)
            
        def addData():
            if(len(StdID.get())!=0):
                database3.addStdRec(StdID.get(), Firstname.get(), Surname.get(), Semester.get(), Payment.get(), Status.get())
                studentlist.delete(0,END)    
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), Semester.get(), Payment.get(), Status.get()))



        def DisplayData():
            studentlist.delete(0,END)
            for row in database3.viewData():
                studentlist.insert(END, row, str(""))
                                       

        def StudentRec(event):
            global Sd
            searchStd = studentlist.curselection()[0]
            Sd = studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,Sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,Sd[2])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END,Sd[3])
            self.txtSem.delete(0,END)
            self.txtSem.insert(END,Sd[4])
            self.txtPay.delete(0,END)
            self.txtPay.insert(END,Sd[5])
            self.txtSts.delete(0,END)
            self.txtSts.insert(END,Sd[6])
            


        def DeleteData():
            if(len(StdID.get())!=0):
                database3.deleteRec(Sd[0])
                clearData()
                DisplayData()
                

        def searchDatabase():
            studentlist.delete(0,END) 
            for row in database3.searchData(StdID.get(), Firstname.get(), Surname.get(),Semester.get(), Payment.get(), Status.get() ):
                studentlist.insert(END, row, str(""))


        def update():
            if(len(StdID.get())!=0):
                database3.deleteRec(Sd[0])
            if(len(StdID.get())!=0):
                database3.addStdRec(StdID.get(), Firstname.get(), Surname.get(), Semester.get(), Payment.get(), Status.get())
                studentlist.delete(0,END)                      
                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), Semester.get(), Payment.get(), Status.get()))



#================================Frame=========================
        MainFrame = Frame(self.root, bg="ghostwhite")
        MainFrame.grid()
#.........
        TitFrame2 = Frame(MainFrame, bg="ghostwhite", relief = RIDGE)
        TitFrame2.pack(side=TOP)
#.........        
        TitFrame = Frame(MainFrame, bd=6, padx=54, pady=8, bg="lavender", relief = RIDGE)
        TitFrame.pack(side=TOP)

        TitFrame1 = Frame(MainFrame, bg="ghostwhite", relief = RIDGE)
        TitFrame1.pack(side=TOP)

       
#..........
        
        self.lblTit = Label(TitFrame2 ,font=('arial', 0), text="    ",bg="ghostwhite")
        self.lblTit.grid()
#..........

        self.lblTit = Label(TitFrame ,font=('Times New Roman', 25,'bold'), fg="midnightblue",text="  PAYMENT DETAILS:  ",bg="lavender")
        self.lblTit.grid()

        
#...............
        DataFrame = Frame(MainFrame, width=1300,height=16,bd=2, bg="ghostwhite", relief = RIDGE)
        DataFrame.pack(side=BOTTOM)
#..................

        
        DataFrame = Frame(MainFrame, bd=3, width=1300,height=400, padx=14, pady=14, bg="lavender", relief = RIDGE)
        DataFrame.pack(side=BOTTOM)


        
#..................
        DataFrameLEFT = LabelFrame(TitFrame1, width=1000,bd=6, height=650, padx=50 ,pady=50, bg="lavender", relief = RIDGE)
        DataFrameLEFT.pack(side=LEFT)

        ButtonFrame = Frame(TitFrame1, width=1350, height=70, padx=18, pady=10, bg="ghostwhite", relief = RIDGE)
        ButtonFrame.pack(side=RIGHT)

        

        
#...............

        DataFrameRIGHT = LabelFrame(DataFrame, width=90,height=10,bd=4, bg="lavender", relief = RIDGE)
        DataFrameRIGHT.pack(side=BOTTOM)
        

#=======================Labels and entries================================
        
        self.lblStdID = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 20,'bold'),text="Student PID:", padx=2, pady=2, bg="lavender")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 20),textvariable=StdID,bd=2, width=35)
        self.txtStdID.grid(row=0, column=1, sticky=W)

        self.lblfna = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 20,'bold'),text="First Name:", padx=2, pady=2, bg="lavender")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 20),textvariable=Firstname,bd=2, width=35)
        self.txtfna.grid(row=1, column=1, sticky=W)

        self.lblSna = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 20,'bold'),text="Last Name:", padx=2, pady=2, bg="lavender")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 20),textvariable=Surname,bd=2, width=35)
        self.txtSna.grid(row=2, column=1, sticky=W)

        
    
        self.lblSem = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 20,'bold'),text="Semester:", padx=2, pady=2, bg="lavender")
        self.lblSem.grid(row=4, column=0, sticky=W)
        self.sem = tkr.OptionMenu(DataFrameLEFT ,Semester,*CSem)
        self.sem.config(font=("Bahnschrift SemiCondensed",12),width=12)
        self.sem.grid(row=4, column=1)
        self.txtSem = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 17),textvariable=Semester, bd=2,width=11)
        self.txtSem.grid(row=4, column=1, sticky=W)

        
#=---------------------
       
        self.lblPay = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="Payment Mode:", padx=2, pady=2, bg="lavender")
        self.lblPay.grid(row=5, column=0, sticky=W)
        
        self.checkPay = Radiobutton(DataFrameLEFT,text="Cash",variable=Payment ,command=checked,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.checkPay.grid(row=5,column=0,columnspan=12)
      
        self.checkPay = Radiobutton(DataFrameLEFT,text="Check",variable=Payment, command=checkedf,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.checkPay.grid(row=5,column=1,columnspan=20)
        self.txtPay = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=Payment,bd=2, width=8)
        self.txtPay.grid(row=5, column=1, sticky=W)

       
#-------------------------

        
#--------------------------------
        self.lblSts = Label(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19,'bold'),text="Status:", padx=2, pady=2, bg="lavender")
        self.lblSts.grid(row=6, column=0, sticky=W)
       
        self.ckSts = Radiobutton(DataFrameLEFT,text="Paid",variable=Status ,command=check1,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.ckSts.grid(row=6,column=0,columnspan=8)
      
        self.ckSts = Radiobutton(DataFrameLEFT,text="Unpaid",variable=Status, command=check2,font=('Bahnschrift SemiCondensed', 13),bg="lavender")
        self.ckSts.grid(row=6,column=1,columnspan=6)

        
        
        self.txtSts = Entry(DataFrameLEFT ,font=('Bahnschrift SemiCondensed', 19),textvariable=Status,bd=2, width=8)
        self.txtSts.grid(row=6, column=1, sticky=W)

#------------------------------------------
        

#=============================listbox & Scrollbar Widge=====================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=90, height=10, font=('dubai', 13, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)


        

#===================Button Widget=============================================
                        
        self.btnAddDate = Button(ButtonFrame,text="Add New", font=('arial', 18, 'bold'), height=1, width=9, bd=6,bg="lavender",fg="midnightblue", command=addData)
        self.btnAddDate.grid(row=0, column=0,padx=4,pady=4)

        self.btnDisplayDate = Button(ButtonFrame,text="Display", font=('arial', 18, 'bold'), height=1, width=9, bd=6,bg="lavender",fg="midnightblue", command=DisplayData)
        self.btnDisplayDate.grid(row=1, column=0,padx=4,pady=4)

        self.btnUpdateDate = Button(ButtonFrame,text="Update", font=('arial', 18, 'bold'), height=1, width=9, bd=6,bg="lavender",fg="midnightblue", command=update)
        self.btnUpdateDate.grid(row=2, column=0, padx=4,pady=4)

        self.btnSearchDate = Button(ButtonFrame,text="Search", font=('arial', 18, 'bold'), height=1, width=9, bd=6,bg="lavender",fg="midnightblue", command=searchDatabase)
        self.btnSearchDate.grid(row=3, column=0, padx=4,pady=4)

        self.btnClearDate = Button(ButtonFrame,text="Clear", font=('arial', 18, 'bold'), height=1, width=9, bd=6,bg="lavender",fg="midnightblue", command=clearData)
        self.btnClearDate.grid(row=4, column=0, padx=4,pady=4)

        self.btnDeleteDate = Button(ButtonFrame,text="Delete", font=('arial',18, 'bold'), height=1, width=9, bd=6,bg="lavender",fg="midnightblue", command=DeleteData)
        self.btnDeleteDate.grid(row=5, column=0,padx=4,pady=4)

        
        


        
        

 
#*********************************************************************************************************************************************************************************************
class Displaywindow2:
    def __init__(self, root):
        self.root = root
        self.root.title("Display Payment Details:")
        self.root.geometry("1430x600+30+20")
        self.root.config(bg="ghostwhite")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Semester = StringVar()
        Payment = StringVar()
        Status = StringVar()

    


        def DisplayData():
            
            for row in database3.viewData():
                studentlist.insert(END, row, str("   "))
               
                self.tree.insert("",tk.END,values=row)
                

        def StudentRec(event):
            global Sd
            searchStd = studentlist.curselection()[0]
            Sd = studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,Sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,Sd[2])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END,Sd[3])
            self.txtSem.delete(0,END)
            self.txtSem.insert(END,Sd[4])
            self.txtPay.delete(0,END)
            self.txtPay.insert(END,Sd[5])
            self.txtSts.delete(0,END)
            self.txtSts.insert(END,Sd[6])
            


#---------------------------
        MainFrame = Frame(self.root, bg="ghostwhite")
        MainFrame.grid()
#.........
        TitFrame2 = Frame(MainFrame, bg="ghostwhite", relief = RIDGE)
        TitFrame2.pack(side=TOP)
#.........        
        TitFrame = Frame(MainFrame, bd=6, padx=54, pady=8, bg="lavender", relief = RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame ,font=('Times New Roman', 35,'bold'), fg="midnightblue",text="  Payment Details  ",bg="lavender")
        self.lblTit.grid()

        
        DataFrame = Frame(MainFrame, width=1300,height=100, bg="ghostwhite", relief = RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameRIGHT = LabelFrame(DataFrame, bd=5, width=2000,height=300, bg="lavender", relief = RIDGE)
        DataFrameRIGHT.pack(side=BOTTOM)

        ButtonFrame = Frame(DataFrame, width=100, height=100, padx=18, pady=10, bg="ghostwhite", relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        #--------------------

        self.btnDisplayDate = Button(ButtonFrame,text="Display", font=('arial', 18, 'bold'), height=1, width=10, bd=6,bg="lavender",fg="midnightblue", command=DisplayData)
        self.btnDisplayDate.grid(row=0, column=2,padx=4,pady=4)


        
        
        
        self.tree= ttk.Treeview(DataFrameRIGHT, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"), show='headings')
        self.tree.grid(row=0, column=0)
        self.tree.heading("#1", text="Sr.No")
        self.tree.heading('#2', text='PID')
        self.tree.heading("#3", text="FIRST NAME")
        self.tree.heading("#4", text="LAST NAME")
        self.tree.heading('#5', text='SEMESTER')
        self.tree.heading('#6', text='PAYMENT MODE')
        self.tree.heading('#7', text='STATUS')
        
        
        

        
        
        


        #=============================listbox & Scrollbar Widge=====================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=1000, height=100, font=('dubai', 20, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect >>', StudentRec)
        
        scrollbar.config(command = studentlist.yview)


        
#===============================================================================================================================================================================================
if __name__=='__main__':
    main()
        
