from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from register import registerclass
import mysql.connector
from cust_win import cust
from room import roombooking
from details import roomdetails





def main():
  win=Tk()
  app=loginclass(win)
  win.mainloop()
  


class loginclass:
  def __init__(self,root):
    self.root=root
    self.root.title("Login")
    self.root.state('zoomed')


    self.var_email=StringVar()
    self.var_password=StringVar()
    
    



  #1ST IMAGE
    img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
    img1=img1.resize((1650,1000),Image.BICUBIC)
    self.photoimg1=ImageTk.PhotoImage(img1)
    

    lblimg=Label(self.root,image=self.photoimg1,relief=RIDGE)
    lblimg.place(relx=0,y=0,relheight=1,relwidth=1)


    frame=Frame(self.root,bg="black")
    frame.place(relx=0.42,rely=0.24,relheight=0.52,relwidth=0.2)

    # img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\LoginIconAppl.png")
    # img2=img2.resize((130,120),Image.BICUBIC)
    # self.photoimg2=ImageTk.PhotoImage(img2)
    

    # lblimg=Label(frame,image=self.photoimg2,borderwidth=0)
    # lblimg.place(relx=0.35,rely=0.1,relheight=0.25,relwidth=0.3)

    get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
    get_str.place(relx=0.22,rely=0.02)



    username=Label(frame,text="Email",font=("times new roman",20),fg="white",bg="black")
    username.place(relx=0.03,rely=0.2,relheight=0.05,relwidth=0.4)

    enty_user=ttk.Entry(frame,textvariable=self.var_email,font=("arial",12,"bold"))
    enty_user.place(relx=0.03,rely=0.28)

    password=Label(frame,text="Password",font=("times new roman",20),fg="white",bg="black")
    password.place(relx=0.03,rely=0.4,relheight=0.05,relwidth=0.4)

    enty_password=ttk.Entry(frame,textvariable=self.var_password,font=("arial",12,"bold"))
    enty_password.place(relx=0.03,rely=0.5)

    loginbtn=Button(frame,text="Login",font=("times new roman",20),fg="white",bg="red",command=self.login)
    loginbtn.place(relx=0.05,rely=0.6,relheight=0.08)

    newuser_btn=Button(frame,text="New user? Sign up here",command=self.registerclass,font=("times new roman",10),fg="white",bg="black",bd=0)
    newuser_btn.place(relx=0.05,rely=0.75)


  def login(self):
    if self.var_email.get()=="" or self.var_password.get()=="":
      messagebox.showerror("Error","All fields are required to be filled")
    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from register where email=%s and password=%s",(
        self.var_email.get(),
        self.var_password.get()
      ))
      
      row=my_cursor.fetchone()
      if row==None:
        messagebox.showerror("Error","Invalid username or password")
      else:
        self.new_window=Toplevel(self.root)
        self.app=hotelmanagementsystem(self.new_window)
    conn.commit()
    conn.close()
  

  




  def registerclass(self):
    self.newwindow=Toplevel(self.root)
    self.app=registerclass(self.newwindow)



class registerclass:
  def __init__(self,root):
    self.root=root
    self.root.title("Register")
    self.root.state('zoomed')




    self.var_pass=StringVar()
    self.var_fname=StringVar()
    self.var_lname=StringVar()
    self.var_cpass=StringVar()
    self.var_email=StringVar()
    self.var_contact=StringVar()



  #1ST IMAGE
    img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
    img1=img1.resize((1650,1000),Image.BICUBIC)
    self.photoimg1=ImageTk.PhotoImage(img1)
    

    lblimg=Label(self.root,image=self.photoimg1,relief=RIDGE)
    lblimg.place(relx=0,y=0,relheight=1,relwidth=1)


    frame=Frame(self.root,bg="White")
    frame.place(relx=0.3,rely=0.25,relheight=0.5,relwidth=0.43)

    register_label=Label(frame,text="Register",font=("times new roman",20),fg="green",bg="white")
    register_label.place(relx=0.1,rely=0.1)

    fname_label=Label(frame,text="First Name",font=("times new roman",17),fg="black",bg="white")
    fname_label.place(relx=0.1,rely=0.25)

    enty_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("arial",12,"bold"))
    enty_fname.place(relx=0.1,rely=0.35)


    lname_label=Label(frame,text="Last Name",font=("times new roman",17),fg="black",bg="white")
    lname_label.place(relx=0.6,rely=0.25)


    enty_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("arial",12,"bold"))
    enty_lname.place(relx=0.6,rely=0.35)



    email_label=Label(frame,text="Email",font=("times new roman",17),fg="black",bg="white")
    email_label.place(relx=0.1,rely=0.45)

    enty_email=ttk.Entry(frame,textvariable=self.var_email,font=("arial",12,"bold"))
    enty_email.place(relx=0.1,rely=0.55)


    contact_label=Label(frame,text="Contact",font=("times new roman",17),fg="black",bg="white")
    contact_label.place(relx=0.6,rely=0.45)


    enty_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("arial",12,"bold"))
    enty_contact.place(relx=0.6,rely=0.55)



    pass_label=Label(frame,text="Password",font=("times new roman",17),fg="black",bg="white")
    pass_label.place(relx=0.1,rely=0.65)

    enty_email=ttk.Entry(frame,textvariable=self.var_pass,font=("arial",12,"bold"))
    enty_email.place(relx=0.1,rely=0.75)


    cpass_label=Label(frame,text="Confirm Password",font=("times new roman",17),fg="black",bg="white")
    cpass_label.place(relx=0.6,rely=0.65)


    enty_cpass=ttk.Entry(frame,textvariable=self.var_cpass,font=("arial",12,"bold"))
    enty_cpass.place(relx=0.6,rely=0.75)



    register_btn=Button(frame,text="Register",command=self.register_data,font=("times new roman",20),fg="white",bg="red")
    register_btn.place(relx=0.1,rely=0.85,relheight=0.09)



  def register_data(self):
    if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_pass.get()=="" or self.var_cpass.get()=="":
      messagebox.showerror("Error","All fields are required to be filled",parent=self.root)
    elif self.var_pass.get()!=self.var_cpass.get():
      messagebox.showerror("Error","Password and Confirm password must be same",parent=self.root)

    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
      my_cursor=conn.cursor()
      query="select * from register where email=%s"
      value=(self.var_email.get(),)
      my_cursor.execute(query,value)
      row=my_cursor.fetchone()
      if row!=None:
        messagebox.showerror("Error","User already exists",parent=self.root)
      else:
        my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",(
          self.var_fname.get(),
          self.var_lname.get(),
          self.var_email.get(),
          self.var_contact.get(),
          self.var_pass.get()
          
          ))
      
      
        
      conn.commit()
      conn.close()
      messagebox.showinfo("Success","Registration successful",parent=self.root)
      self.root.destroy()







  



class hotelmanagementsystem:
  def __init__(self,root):
    self.root=root
    self.root.title("Hotel management system")
    self.root.state('zoomed')
  #1ST IMAGE
    img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\myh.jpg")
    img1=img1.resize((1250,210),Image.BICUBIC)
    self.photoimg1=ImageTk.PhotoImage(img1)
    

    lblimg=Label(self.root,image=self.photoimg1,relief=RIDGE)
    lblimg.place(relx=0.2,y=0,relheight=0.25,relwidth=0.8)
  #LOGO
    img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\logohotel.png")
    img2=img2.resize((350,230),Image.BICUBIC)
    self.photoimg2=ImageTk.PhotoImage(img2)
    

    lblimg=Label(self.root,image=self.photoimg2,relief=RIDGE)
    lblimg.place(relx=0,y=0,relheight=0.25,relwidth=0.2)

  #title
    lbl_title=Label(self.root,text="Hotel Management System",font=("times new roman",40,"bold"),bg="black",fg="gold")
    lbl_title.place(x=0,rely=0.25,relheight=0.1,relwidth=1)

  #main frame
    main_frame=Frame(self.root,bd=4,relief=RIDGE)
    main_frame.place(x=0,rely=0.35,relwidth=1,relheight=0.65)

  #menu
    #lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold")
    #lbl_menu.place(relx=0,rely=0,relwidth=0.15,relheight=0.09)

  #btn frame
    btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
    btn_frame.place(relx=0,rely=0,relwidth=0.15,relheight=0.59)

    cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,font=("times new roman",20,"bold"),bg="black",fg="gold")
    cust_btn.place(relx=0,rely=0,relwidth=1,relheight=0.25)

    room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,font=("times new roman",20,"bold"),bg="black",fg="gold")
    room_btn.place(relx=0,rely=0.25,relwidth=1,relheight=0.25)

    details_btn=Button(btn_frame,command=self.roomdetails,text="ADMIN",font=("times new roman",20,"bold"),bg="black",fg="gold")
    details_btn.place(relx=0,rely=0.5,relwidth=1,relheight=0.25)

    #report_btn=Button(btn_frame,text="REPORT",font=("times new roman",20,"bold"),bg="black",fg="gold")
    #report_btn.place(relx=0,rely=0.6,relwidth=1,relheight=0.2)

    logout_btn=Button(btn_frame,command=self.logout,text="LOGOUT",font=("times new roman",20,"bold"),bg="black",fg="gold")
    logout_btn.place(relx=0,rely=0.75,relwidth=1,relheight=0.25)


    img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\hotel1.png")
    img3=img3.resize((1350,330),Image.BICUBIC)
    self.photoimg3=ImageTk.PhotoImage(img3)
    

    lblimg=Label(main_frame,image=self.photoimg3,relief=RIDGE)
    lblimg.place(relx=0.15,rely=0,relheight=0.59,relwidth=0.85)

    img4=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\room1.jpg")
    img4=img4.resize((600,330),Image.BICUBIC)
    self.photoimg4=ImageTk.PhotoImage(img4)
    

    lblimg=Label(main_frame,image=self.photoimg4,relief=RIDGE)
    lblimg.place(relx=0,rely=0.59,relheight=0.41,relwidth=0.33)

    img5=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\room2.jpg")
    img5=img5.resize((600,330),Image.BICUBIC)
    self.photoimg5=ImageTk.PhotoImage(img5)
    

    lblimg=Label(main_frame,image=self.photoimg5,relief=RIDGE)
    lblimg.place(relx=0.33,rely=0.59,relheight=0.41,relwidth=0.33)


    img6=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\room3.jpg")
    img6=img6.resize((600,330),Image.BICUBIC)
    self.photoimg6=ImageTk.PhotoImage(img6)
    

    lblimg=Label(main_frame,image=self.photoimg6,relief=RIDGE)
    lblimg.place(relx=0.66,rely=0.59,relheight=0.41,relwidth=0.34)

  def cust_details(self):
    self.newwindow=Toplevel(self.root)
    self.app=cust(self.newwindow)

  def roombooking(self):
    self.newwindow=Toplevel(self.root)
    self.app=roombooking(self.newwindow)

  def roomdetails(self):
    self.newwindow=Toplevel(self.root)
    self.app=roomdetails(self.newwindow)
  def logout(self):
    self.root.destroy()


        



if __name__=="__main__":
  main()
  