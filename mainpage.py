from tkinter import*
from PIL import Image,ImageTk
from cust_win import cust
from room import roombooking
from details import roomdetails


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

    logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,font=("times new roman",20,"bold"),bg="black",fg="gold")
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
  root=Tk()
  obj=hotelmanagementsystem(root)
  root.mainloop() 