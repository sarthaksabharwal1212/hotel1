from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


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
          self.var_pass.get(),
          
          ))
      
      
        
      conn.commit()
      conn.close()
      messagebox.showinfo("Success","Registration successful",parent=self.root)

      












if __name__=="__main__":
  root=Tk()
  obj=registerclass(root)
  root.mainloop() 