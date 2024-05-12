from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime



class roomdetails:
  def __init__(self,root):
    self.root=root
    self.root.title("Hotel management system")
    self.root.state('zoomed')

    self.var_floor=StringVar()
    self.var_roomno=StringVar()
    self.var_roomtype=StringVar()
    



  #title
    lbl_title=Label(self.root,text="Room Adding Department",font=("times new roman",20,"bold"),bg="black",fg="gold")
    lbl_title.place(x=0,rely=0,relheight=0.1,relwidth=1)

  #logo
    img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\logohotel.png")
    img2=img2.resize((190,95),Image.BICUBIC)
    self.photoimg2=ImageTk.PhotoImage(img2)
    

    lblimg=Label(self.root,image=self.photoimg2,relief=RIDGE,padx=0,pady=0)
    lblimg.place(relx=0,y=0,relheight=0.1,relwidth=0.1)

  #labelframe
    labelframeleft=LabelFrame(self.root,relief=RIDGE,text="New Room Add",font=("times new roman",15,"bold"))
    
    labelframeleft.place(relx=0.01,rely=0.11,relheight=0.58,relwidth=0.45)


    lbl_floor=Label(labelframeleft,text="Floor",font=("times new roman",12,"bold"))
    lbl_floor.place(relx=0,rely=0.07,relwidth=0.2)

    enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",12,"bold"))
    enty_floor.place(relx=0.2,rely=0.07,relwidth=0.25) 


    lbl_roomno=Label(labelframeleft,text="Room No",font=("times new roman",12,"bold"))
    lbl_roomno.place(relx=0,rely=0.15,relwidth=0.2)

    enty_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,font=("arial",12,"bold"))
    enty_roomno.place(relx=0.2,rely=0.15,relwidth=0.25)



    lbl_roomtype=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"))
    lbl_roomtype.place(relx=0,rely=0.23,relwidth=0.2)

    enty_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"))
    enty_roomtype.place(relx=0.2,rely=0.23,relwidth=0.25)





    btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
    btn_frame.place(relx=0,rely=0.35,relheight=0.07,relwidth=0.8)

    


    btnadd=Button(btn_frame,command=self.add_data,text="Add",font=("arial",12,"bold"),bg="black",fg="gold")
    btnadd.place(relx=0,rely=0,relheight=1,relwidth=0.25)

    btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold")
    btnupdate.place(relx=0.25,rely=0,relheight=1,relwidth=0.25)


    btndelete=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",12,"bold"),bg="black",fg="gold")
    btndelete.place(relx=0.5,rely=0,relheight=1,relwidth=0.25)


    btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold")
    btnreset.place(relx=0.75,rely=0,relheight=1,relwidth=0.25)




    labelframeright=LabelFrame(self.root,relief=RIDGE,font=("Show Room Details",12,"bold"),text="View Details")
    labelframeright.place(relx=0.5,rely=0.11,relheight=0.45,relwidth=0.47)



    scroll_x=ttk.Scrollbar(labelframeright,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(labelframeright,orient=VERTICAL)


    self.room_table=ttk.Treeview(labelframeright,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=self.room_table.xview)
    scroll_y.config(command=self.room_table.yview)



    self.room_table.heading("floor",text="Floor")
    self.room_table.heading("roomno",text="Room No")
    self.room_table.heading("roomtype",text="Room Type")
    
    

    self.room_table["show"]="headings"


    self.room_table.column("floor")
    self.room_table.column("roomno")
    self.room_table.column("roomtype")
    
    self.room_table.pack(fill=BOTH,expand=1)
    self.fetch_data()
    self.room_table.bind("<ButtonRelease-1>",self.get_cursor)



  def add_data(self):
    if self.var_floor.get()=="":
        messagebox.showerror("Error","All fields are required to be filled",parent=self.root)
      
    else:
      try:
        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into details1 values(%s,%s,%s)",(
          self.var_floor.get(),
          self.var_roomno.get(),
          self.var_roomtype.get()
          ))
      
      
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","New room added successfully",parent=self.root)
      except Exception as es:
        messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)


  def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from details1")
    rows=my_cursor.fetchall()
    #if len(rows)!=0:
    self.room_table.delete(*self.room_table.get_children())
    for i in rows:
        self.room_table.insert("",END,values=i)
    conn.commit()
    conn.close()    


  def get_cursor(self,event=""):
    cursor_row=self.room_table.focus()
    content=self.room_table.item(cursor_row)
    row=content["values"]

    self.var_floor.set(row[0]),
    self.var_roomno.set(row[1]),
    self.var_roomtype.set(row[2])



  def update(self):
    conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
    my_cursor=conn.cursor()
    my_cursor.execute("update details1 set floor=%s,roomtype=%s where roomno=%s",(
          
          
          self.var_floor.get(),
          self.var_roomtype.get(),
          self.var_roomno.get()
          
    ))
    conn.commit()
    self.fetch_data()
    conn.close()
    messagebox.showinfo("Update","Room details have been updated",parent=self.root)



  def mdelete(self):
      mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this entry",parent=self.root)
      if mdelete:
        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
        my_cursor=conn.cursor()
        query="delete from details1 where roomno=%s"
        value=(self.var_roomno.get(),)
        my_cursor.execute(query,value)
      else:
        return
    
      conn.commit()
      self.fetch_data()
      conn.close()



  def reset(self):
    self.var_floor.set(""),
    self.var_roomno.set(""),
    self.var_roomtype.set("")
   













if __name__=="__main__":
  root=Tk()
  obj=roomdetails(root)
  root.mainloop()