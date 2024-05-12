from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime
from time import time



class roombooking:
  def __init__(self,root):
    self.root=root
    self.root.title("Admin")
    self.root.state('zoomed')


    img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\bed.jpg")
    img1=img1.resize((600,330),Image.BICUBIC)
    self.photoimg1=ImageTk.PhotoImage(img1)

    lblimg=Label(self.root,image=self.photoimg1,relief=RIDGE)
    lblimg.place(relx=0.6,rely=0.11,relheight=0.39,relwidth=0.34)




    self.var_contact=StringVar()
    self.var_checkin=StringVar()
    self.var_checkout=StringVar()
    self.var_roomtype=StringVar()
    self.var_roomavailable=StringVar()
    self.var_meal=StringVar()
    self.var_noofdays=StringVar()
    self.var_paidtax=StringVar()
    self.var_actualtotal=StringVar()
    self.var_total=StringVar()
    self.var_room=StringVar()
    







  #title
    lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold")
    lbl_title.place(x=0,rely=0,relheight=0.1,relwidth=1)

  #logo
    img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\logohotel.png")
    img2=img2.resize((190,95),Image.BICUBIC)
    self.photoimg2=ImageTk.PhotoImage(img2)
    

    lblimg=Label(self.root,image=self.photoimg2,relief=RIDGE,padx=0,pady=0)
    lblimg.place(relx=0,y=0,relheight=0.1,relwidth=0.1)

  #labelframe
    labelframeleft=LabelFrame(self.root,relief=RIDGE,text="Room booking details",font=("times new roman",15,"bold"))
    
    labelframeleft.place(relx=0.01,rely=0.13,relheight=0.85,relwidth=0.3)

  

  #labels and entry

    lbl_cust_contact=Label(labelframeleft,text="Contact",font=("times new roman",12,"bold"))
    lbl_cust_contact.place(relx=0,rely=0.07,relwidth=0.2)

    enty_contact=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_contact)
    enty_contact.place(relx=0.2,rely=0.07,relwidth=0.5)

    btn_fetch=Button(labelframeleft,command=self.fetch_contact,text="Fetch data",bg="black",fg="gold",font=("times new roman",12,"bold"))

    btn_fetch.place(relx=0.74,relwidth=0.25,rely=0.07,relheight=0.039)

    checkin=Label(labelframeleft,text="Check in",font=("times new roman",12,"bold"))
    checkin.place(relx=0,rely=0.14,relwidth=0.2)

    txtcheckin=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_checkin)
    txtcheckin.place(relx=0.2,rely=0.14,relwidth=0.75)



    checkout=Label(labelframeleft,text="Check out",font=("times new roman",12,"bold"))
    checkout.place(relx=0,rely=0.21,relwidth=0.2)

    txtcheckout=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_checkout)
    txtcheckout.place(relx=0.2,rely=0.21,relwidth=0.75)


    



    lbl_roomtype=Label(labelframeleft,text="Room type",font=("times new roman",12,"bold"))
    lbl_roomtype.place(relx=0,rely=0.28,relwidth=0.2)



    

    combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),state="readonly")
    combo_roomtype["value"]=("Single","Double","Luxury")
    combo_roomtype.current(0)
    combo_roomtype.place(relx=0.2,rely=0.28,relwidth=0.75)

    



    lbl_available=Label(labelframeleft,text="Rooms",font=("times new roman",12,"bold"))
    lbl_available.place(relx=0,rely=0.35,relwidth=0.2)


    conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
    my_cursor=conn.cursor()
    my_cursor.execute("select roomno from details1")
    rows=my_cursor.fetchall()
    
    combo_room=ttk.Combobox(labelframeleft,textvariable=self.var_room,font=("arial",12,"bold"),state="readonly")
    combo_room["value"]=rows
    combo_room.current(0)
    combo_room.place(relx=0.2,rely=0.35,relwidth=0.75)

    


    




    lbl_meal=Label(labelframeleft,text="Meal",font=("times new roman",12,"bold"))
    lbl_meal.place(relx=0,rely=0.42,relwidth=0.2)

    #enty_meal=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_meal)
    #enty_meal.place(relx=0.2,rely=0.42,relwidth=0.75)


    combo_meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),state="readonly")
    combo_meal["value"]=("Breakfast","Lunch","Dinner")
    combo_meal.current(0)
    combo_meal.place(relx=0.2,rely=0.42,relwidth=0.75)




    lbl_days=Label(labelframeleft,text="Days",font=("times new roman",12,"bold"))
    lbl_days.place(relx=0,rely=0.49,relwidth=0.2)

    enty_days=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_noofdays)
    enty_days.place(relx=0.2,rely=0.49,relwidth=0.75)
    

    



    lbl_tax=Label(labelframeleft,text="Paid Tax",font=("times new roman",12,"bold"))
    lbl_tax.place(relx=0,rely=0.56,relwidth=0.2)

    enty_tax=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_paidtax)
    enty_tax.place(relx=0.2,rely=0.56,relwidth=0.75)





    lbl_cp=Label(labelframeleft,text="Room tariff",font=("times new roman",12,"bold"))
    lbl_cp.place(relx=0,rely=0.63,relwidth=0.2)

    enty_cp=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_actualtotal)
    enty_cp.place(relx=0.2,rely=0.63,relwidth=0.75)






    lbl_total=Label(labelframeleft,text="Total cost",font=("times new roman",12,"bold"))
    lbl_total.place(relx=0,rely=0.7,relwidth=0.2)

    enty_total=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_total)
    enty_total.place(relx=0.2,rely=0.7,relwidth=0.75)



    btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
    btn_frame.place(relx=0,rely=0.88,relheight=0.07,relwidth=1)

    btn_bill=Button(labelframeleft,text="Bill",command=self.totalcost,font=("arial",12,"bold"),bg="black",fg="gold")

    btn_bill.place(relx=0,rely=0.78,relwidth=0.25)

    

    btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold")
    btnadd.place(relx=0,rely=0,relheight=1,relwidth=0.25)

    btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold")
    btnupdate.place(relx=0.25,rely=0,relheight=1,relwidth=0.25)


    btndelete=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",12,"bold"),bg="black",fg="gold")
    btndelete.place(relx=0.5,rely=0,relheight=1,relwidth=0.25)


    btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold")
    btnreset.place(relx=0.75,rely=0,relheight=1,relwidth=0.25)



    labelframeright=LabelFrame(self.root,relief=RIDGE,font=("times new roman",12,"bold"),text="View Details")
    labelframeright.place(relx=0.33,rely=0.5,relheight=0.45,relwidth=0.67)



    details_table=Frame(labelframeright,bd=2,relief=RIDGE)
    details_table.place(relx=0.035,rely=0.05,relheight=0.85,relwidth=0.93)

    scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

    
    self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=self.room_table.xview)
    scroll_y.config(command=self.room_table.yview)

    self.room_table.heading("contact",text="Contact")
    self.room_table.heading("checkin",text="Check-in")
    self.room_table.heading("checkout",text="Check-out")
    self.room_table.heading("roomtype",text="Room type")
    self.room_table.heading("roomavailable",text="Room No")
    self.room_table.heading("meal",text="Meal")
    self.room_table.heading("noofdays",text="NoOfDays")
    

    self.room_table["show"]="headings"


    self.room_table.column("contact")
    self.room_table.column("checkin")
    self.room_table.column("checkout")
    self.room_table.column("roomtype")
    self.room_table.column("roomavailable")
    self.room_table.column("meal")
    self.room_table.column("noofdays")  
    self.room_table.pack(fill=BOTH,expand=1)
    self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
    self.fetch_data()



  def add_data(self):
    if self.var_contact.get()=="":
        messagebox.showerror("Error","All fields are required to be filled",parent=self.root)
      
    else:
      try:
        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into room2 values(%s,%s,%s,%s,%s,%s,%s)",(
          self.var_contact.get(),
          self.var_checkin.get(),
          self.var_checkout.get(),
          self.var_roomtype.get(),
          self.var_roomavailable.get(),
          self.var_meal.get(),
          self.var_noofdays.get()
          ))
      
      
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Room has been booked",parent=self.root)
      except Exception as es:
        messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)





  def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from room2")
    rows=my_cursor.fetchall()
    #if len(rows)!=0:
    self.room_table.delete(*self.room_table.get_children())
    for i in rows:
        self.room_table.insert("",END,values=i)
    conn.commit()
    conn.close()







  def fetch_contact(self):
    if self.var_contact.get()=="":
      messagebox.showerror("Error","Please enter a contact number",parent=self.root)

    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
      my_cursor=conn.cursor()
      query=("select Name from customer1 where Mobile=%s")
      value=(self.var_contact.get(),)
      print(self.var_contact)
      my_cursor.execute(query,value)

      row=my_cursor.fetchone()
      

      if row==None:
        messagebox.showerror("Error","This number was not found")
      else:
        conn.commit()
        conn.close()

        showdata=Frame(self.root,bd=2,relief=RIDGE,padx=2)
        showdata.place(relx=0.35,rely=0.15,relheight=0.33,relwidth=0.2)

        lblname=Label(showdata,text="Name:",font=("arial",12,"bold"))
        lblname.place(relx=0.1,rely=0.1,relwidth=0.2)

        lblname1=Label(showdata,text=row,font=("arial",12,"bold"))
        lblname1.place(relx=0.3,rely=0.1)

        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
        my_cursor=conn.cursor()
        query=("select Gender from customer1 where Mobile=%s")
        value=(self.var_contact.get(),)
        print(self.var_contact)
        my_cursor.execute(query,value)

        row=my_cursor.fetchone()

        lblgender=Label(showdata,text="Gender:",font=("arial",12,"bold"))
        lblgender.place(relx=0.1,rely=0.2,relwidth=0.2)

        lblgender1=Label(showdata,text=row,font=("arial",12,"bold"))
        lblgender1.place(relx=0.3,rely=0.2)



        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
        my_cursor=conn.cursor()
        query=("select Email from customer1 where Mobile=%s")
        value=(self.var_contact.get(),)
      
        my_cursor.execute(query,value)

        row=my_cursor.fetchone()

        lblmail=Label(showdata,text="Email:",font=("arial",12,"bold"))
        lblmail.place(relx=0.1,rely=0.3,relwidth=0.2)

        lblmail1=Label(showdata,text=row,font=("arial",12,"bold"))
        lblmail1.place(relx=0.3,rely=0.3)

        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
        my_cursor=conn.cursor()
        query=("select Nationality from customer1 where Mobile=%s")
        value=(self.var_contact.get(),)
        
        my_cursor.execute(query,value)

        row3=my_cursor.fetchone()

        lblnat=Label(showdata,text="Nationality:",font=("arial",12,"bold"))
        lblnat.place(relx=0.1,rely=0.4,relwidth=0.3)

        lblnat1=Label(showdata,text=row3,font=("arial",12,"bold"))
        lblnat1.place(relx=0.4,rely=0.4)





        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
        my_cursor=conn.cursor()
        query=("select Address from customer1 where Mobile=%s")
        value=(self.var_contact.get(),)
        
        my_cursor.execute(query,value)

        row4=my_cursor.fetchone()

        lbladd=Label(showdata,text="Address:",font=("arial",12,"bold"))
        lbladd.place(relx=0.1,rely=0.5,relwidth=0.24)

        lbladd1=Label(showdata,text=row4,font=("arial",12,"bold"))
        lbladd1.place(relx=0.35,rely=0.5)

        

  def get_cursor(self,event=""):
    cursor_row=self.room_table.focus()
    content=self.room_table.item(cursor_row)
    row=content["values"]

    self.var_contact.set(row[0]),
    self.var_checkin.set(row[1]),
    self.var_checkout.set(row[2]),
    self.var_roomtype.set(row[3]),
    self.var_roomavailable.set(row[4]),
    self.var_meal.set(row[5]),
    self.var_noofdays.set(row[6])   



  def update(self):
    conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
    my_cursor=conn.cursor()
    my_cursor.execute("update room2 set checkin=%s,checkout=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
          
          
          self.var_checkin.get(),
          self.var_checkout.get(),
          self.var_roomtype.get(),
          self.var_roomavailable.get(),
          self.var_meal.get(),
          self.var_noofdays.get(),
          self.var_contact.get()
    ))
    conn.commit()
    self.fetch_data()
    conn.close()
    messagebox.showinfo("Update","Customer details have been updated",parent=self.root)



  def mdelete(self):
      mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
      if mdelete:
        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema1")
        my_cursor=conn.cursor()
        query="delete from room2 where contact=%s"
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
      else:
        return
    
      conn.commit()
      self.fetch_data()
      conn.close()


  def reset(self):
    self.var_contact.set(""),
    self.var_checkin.set(""),
    
    self.var_checkout.set(""),
    self.var_roomtype.set(""),
    self.var_roomavailable.set(""),
    self.var_paidtax.set(""),
    self.var_actualtotal.set(""),
    self.var_total.set(""),
    
    
    self.var_noofdays.set("")  


  
  def totalcost(self):
    indate=self.var_checkin.get()
    outdate=self.var_checkout.get()
    indate=datetime.strptime(indate,"%d/%m/%y")
    outdate=datetime.strptime(outdate,"%d/%m/%y")

    self.var_noofdays.set(abs(outdate-indate).days)

    if self.var_roomtype.get()=="Single":
      q1=float(300)
      q2=float(700)
      q3=float(self.var_noofdays.get())
      q4=float(q1+q2)
      q5=float(q3+q4)
      tax="Rs."+str("%.2f"%((q5)*0.1))
      st="Rs."+str("%.2f"%((q5)))
      tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
      self.var_paidtax.set(tax)
      self.var_actualtotal.set(st)
      self.var_total.set(tt)

    elif self.var_roomtype.get()=="Double":
      q1=float(500)
      q2=float(800)
      q3=float(self.var_noofdays.get())
      q4=float(q1+q2)
      q5=float(q3+q4)
      tax="Rs."+str("%.2f"%((q5)*0.1))
      st="Rs."+str("%.2f"%((q5)))
      tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
      self.var_paidtax.set(tax)
      self.var_actualtotal.set(st)
      self.var_total.set(tt)

    else:
      q1=float(800)
      q2=float(950)
      q3=float(self.var_noofdays.get())
      q4=float(q1+q2)
      q5=float(q3+q4)
      tax="Rs."+str("%.2f"%((q5)*0.1))
      st="Rs."+str("%.2f"%((q5)))
      tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
      self.var_paidtax.set(tax)
      self.var_actualtotal.set(st)
      self.var_total.set(tt)




      


    
    
    
    


  

    
 






if __name__=="__main__":
  root=Tk()
  obj=roombooking(root)
  root.mainloop()