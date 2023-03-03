from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title('Loginpage')
        self.root.geometry("1920x1080+100+50")
        #Bg_Image
        self.bg=ImageTk.PhotoImage(file="C:\\Users\\Prajot Awale\Desktop\\Mini Project\\login.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Login_Framel
        Frame_login=Frame(self.root,bg="White")
        Frame_login.place(x=500,y=248,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),bg="white").place(x=90,y=30)
        desc=Label(Frame_login, text="Doctor Login Area", font=("Goudy old style", 15, "bold"), bg="white").place(x=90, y=100)

        lbl_user= Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=140)
        self.txt_user=Entry(Frame_login,font=("time new roman",15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("time new roman", 15), bg="lightgray",show="*")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        Login_btn = Button(self.root, command=self.login_function, text="Login", fg="White",bg="Black", font=("times new roman", 20)).place(x=665, y=570,width=180, height=40)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.txt_pass.get()!="Doctor" or self.txt_user.get()!="Doctor@gmail.com":
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
        else:
            root.destroy()
            from Main_layout import Database




root=Tk()
obj=Login(root)
root.mainloop()