from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from train import Train
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\NEWUSER\Find me\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\loginBg1.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#FFFFFF")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\NEWUSER\Find me\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\log1.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#FFFFFF")
        lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="black",bg="#FFFFFF")
        get_str.place(x=140,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="black",bg="#FFFFFF")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",10))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="#FFFFFF")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",10))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="black",activebackground="white")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="#FFFFFF",activeforeground="black",activebackground="#FFFFFF")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="#FFFFFF",activeforeground="black",activebackground="#FFFFFF")
        loginbtn.place(x=90,y=370,width=50,height=20)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            conn = mysql.connector.connect(username='root', password='ars3124hussain',host='localhost',database='face_recognition',port=3306)# messagebox.showerror("Error","Please Check Username or Password !")
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='ars3124hussain',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)

                conn.commit()
                conn.close()
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='ars3124hussain',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="black",bg="white")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",12),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="black",bg="white")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",12))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",12))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",12),bd=0,relief=RIDGE,fg="black",bg="silver",activeforeground="white",activebackground="black")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face deteion system====================

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\NEWUSER\Find me\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\back.png")
        img=img.resize((1366,160),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\NEWUSER\Find me\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\back3.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Attendance Managment System",font=("verdana",25,"bold"),bg="white",fg="black")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\NEWUSER\Find me\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\user.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Students",cursor="hand2",font=("tahoma",13),bg="white",fg="black")
        std_b1_1.place(x=250,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\NEWUSER\Find me\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",13),bg="white",fg="black")
        det_b1_1.place(x=480,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\NEWUSER\Find me\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\att.png")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",13),bg="white",fg="black")
        att_b1_1.place(x=710,y=280,width=180,height=45)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"C:\Users\NEWUSER\Find me\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\dat.png")
        tra_img_btn=tra_img_btn.resize((180,180),Image.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=940,y=100,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Data",cursor="hand2",font=("tahoma",13),bg="white",fg="black")
        tra_b1_1.place(x=940,y=280,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def open_img(self):
        os.startfile("dataset")
    
  




if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()