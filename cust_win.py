from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox



class cust:
  def __init__(self,root):
    self.root=root
    self.root.title("Hotel management system")
    self.root.state('zoomed')


  #variables
    self.var_ref=StringVar()
    x=random.randint(1000,9999)
    self.var_ref.set(str(x))

    self.var_name=StringVar()
    self.var_gender=StringVar()
    self.var_post=StringVar()
    self.var_mobile=StringVar()
    self.var_email=StringVar()
    self.var_nationality=StringVar()
    self.var_idproof=StringVar()
    self.var_idnum=StringVar()
    self.var_address=StringVar()




  #title
    lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold")
    lbl_title.place(x=0,rely=0,relheight=0.1,relwidth=1)
  #LOGO
    img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\1633410403702hotel-images\hotel images\logohotel.png")
    img2=img2.resize((190,95),Image.BICUBIC)
    self.photoimg2=ImageTk.PhotoImage(img2)
    

    lblimg=Label(self.root,image=self.photoimg2,relief=RIDGE,padx=0,pady=0)
    lblimg.place(relx=0,y=0,relheight=0.1,relwidth=0.1)


  #labelframe
    labelframeleft=LabelFrame(self.root,relief=RIDGE,text="Customer_Details",font=("times new roman",15,"bold"))
    
    labelframeleft.place(relx=0.01,rely=0.13,relheight=0.85,relwidth=0.36)

    #labels and entry

    lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"))
    lbl_cust_ref.place(relx=0,rely=0.08,relwidth=0.2)

    enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("arial",12,"bold"),state="readonly")
    enty_ref.place(relx=0.2,rely=0.08)



    lbl_cust_name=Label(labelframeleft,text="Customer Name",font=("times new roman",12,"bold"))
    lbl_cust_name.place(relx=0,rely=0.16,relwidth=0.2)

    enty_name=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("arial",12,"bold"))
    enty_name.place(relx=0.2,rely=0.16)



    lbl_gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold"))
    lbl_gender.place(relx=0,rely=0.24,relwidth=0.2)


    combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),state="readonly")
    combo_gender["value"]=("Male","Female")
    combo_gender.current(0)
    combo_gender.place(relx=0.2,rely=0.24)



    lblpostcode=Label(labelframeleft,text="Postcode",font=("times new roman",12,"bold"))
    lblpostcode.place(relx=0,rely=0.32,relwidth=0.2)

    enty_post=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",12,"bold"))
    enty_post.place(relx=0.2,rely=0.32)



    lblmobile=Label(labelframeleft,text="Mobile",font=("times new roman",12,"bold"))
    lblmobile.place(relx=0,rely=0.40,relwidth=0.2)

    enty_mobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",12,"bold"))
    enty_mobile.place(relx=0.2,rely=0.40)




    lblemail=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"))
    lblemail.place(relx=0,rely=0.48,relwidth=0.2)

    enty_email=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",12,"bold"))
    enty_email.place(relx=0.2,rely=0.48)



    lblnat=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold"))
    lblnat.place(relx=0,rely=0.56,relwidth=0.2)


    combonat=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),state="readonly")
    combonat["value"]=("Indian","Foreign")
    combonat.current(0)
    combonat.place(relx=0.2,rely=0.56)

    



    lblidproof=Label(labelframeleft,text="ID Proof Type",font=("times new roman",12,"bold"))
    lblidproof.place(relx=0,rely=0.64,relwidth=0.2)

    comboid=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),state="readonly")
    comboid["value"]=("Aadhar","Passport","Voter Id","Driving License")
    comboid.current(0)
    comboid.place(relx=0.2,rely=0.64)





    lblidnum=Label(labelframeleft,text="ID Number",font=("times new roman",12,"bold"))
    lblidnum.place(relx=0,rely=0.72,relwidth=0.2)

    enty_idnum=ttk.Entry(labelframeleft,textvariable=self.var_idnum,font=("arial",12,"bold"))
    enty_idnum.place(relx=0.2,rely=0.72)






    lbladress=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"))
    lbladress.place(relx=0,rely=0.8,relwidth=0.2)

    enty_address=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",12,"bold"))
    enty_address.place(relx=0.2,rely=0.8)


    btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
    btn_frame.place(relx=0.1,rely=0.88,relheight=0.07,relwidth=0.8)

    btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold")
    btnadd.place(relx=0,rely=0,relheight=1,relwidth=0.25)

    btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold")
    btnupdate.place(relx=0.25,rely=0,relheight=1,relwidth=0.25)


    btndelete=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",12,"bold"),bg="black",fg="gold")
    btndelete.place(relx=0.5,rely=0,relheight=1,relwidth=0.25)


    btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold")
    btnreset.place(relx=0.75,rely=0,relheight=1,relwidth=0.25)




  #right frame
    labelframeright=LabelFrame(self.root,relief=RIDGE,font=("times new roman",12,"bold"),text="View Details")
    labelframeright.place(relx=0.4,rely=0.13,relheight=0.85,relwidth=0.58)

    #lblsearch=Label(labelframeright,font=("times new roman",13,"bold"),text="SearchBy")
    #lblsearch.place(relx=0,rely=0,relheight=0.06,relwidth=0.1)
    #self.search_var=StringVar()
    #combosearch=ttk.Combobox(labelframeright,textvariable=self.search_var,font=("arial",13,"bold"),state="readonly")
    #combosearch["value"]=("Mobile","Reference Number")
    #combosearch.current(0)
    #combosearch.place(relx=0.1,rely=0.01,relwidth=0.18)

    #self.text_search=StringVar()
    #enty_search=ttk.Entry(labelframeright,textvariable=self.text_search,font=("arial",12,"bold"))
    #enty_search.place(relx=0.29,rely=0.01,relwidth=0.18)


    #btnsearch=Button(labelframeright,command=self.search,text="Search",font=("arial",12,"bold"),bg="black",fg="gold")
    #btnsearch.place(relx=0.48,rely=0.01,relwidth=0.18,relheight=0.04)

    #btnshow=Button(labelframeright,text="Update",font=("arial",12,"bold"),bg="black",fg="gold")
    #btnshow.place(relx=0.25,rely=0,relheight=0.01,relwidth=0.25)


    #data table

    details_table=Frame(labelframeright,bd=2,relief=RIDGE)
    details_table.place(relx=0.035,rely=0.05,relheight=0.7,relwidth=0.93)

    scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

    
    self.cust_details_table=ttk.Treeview(details_table,column=("ref","name","gender","post","mobile","email","Nationality","Idproof","Idnumber","Address"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=self.cust_details_table.xview)
    scroll_y.config(command=self.cust_details_table.yview)

    self.cust_details_table.heading("ref",text="Reference")
    self.cust_details_table.heading("name",text="Name")
    self.cust_details_table.heading("gender",text="Gender")
    self.cust_details_table.heading("post",text="Post Code")
    self.cust_details_table.heading("mobile",text="Mobile")
    self.cust_details_table.heading("email",text="Email")
    self.cust_details_table.heading("Nationality",text="Nationality")
    self.cust_details_table.heading("Idproof",text="Idproof")
    self.cust_details_table.heading("Idnumber",text="Id Number")
    self.cust_details_table.heading("Address",text="Address")

    self.cust_details_table["show"]="headings"


    self.cust_details_table.column("ref")
    self.cust_details_table.column("name")
    self.cust_details_table.column("gender")
    self.cust_details_table.column("post")
    self.cust_details_table.column("mobile")
    self.cust_details_table.column("email")
    self.cust_details_table.column("Nationality")
    self.cust_details_table.column("Idproof")
    self.cust_details_table.column("Idnumber")
    self.cust_details_table.column("Address")



    self.cust_details_table.pack(fill=BOTH,expand=1)
    self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
    self.fetch_data()

  def add_data(self):
    if self.var_name.get()=="":
        messagebox.showerror("Error","All fields are required to be filled",parent=self.root)
      
    else:
      try:
        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into customer1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
          self.var_ref.get(),
          self.var_name.get(),
          self.var_gender.get(),
          self.var_post.get(),
          self.var_mobile.get(),
          self.var_email.get(),
          self.var_nationality.get(),
          self.var_idproof.get(),
          self.var_idnum.get(),
          self.var_address.get()))
      
      
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Customer has been added",parent=self.root)
      except Exception as es:
        messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)


  def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from customer1")
    rows=my_cursor.fetchall()
    #if len(rows)!=0:
    self.cust_details_table.delete(*self.cust_details_table.get_children())
    for i in rows:
      self.cust_details_table.insert("",END,values=i)
    conn.commit()
    conn.close()


  def get_cursor(self,event=""):
    cursor_row=self.cust_details_table.focus()
    content=self.cust_details_table.item(cursor_row)
    row=content["values"]

    self.var_ref.set(row[0]),
    self.var_name.set(row[1]),
    self.var_gender.set(row[2]),
    self.var_post.set(row[3]),
    self.var_mobile.set(row[4]),
    self.var_email.set(row[5]),
    self.var_nationality.set(row[6]),
    self.var_idproof.set(row[7]),
    self.var_idnum.set(row[8]),
    self.var_address.set(row[9])





  def update(self):
    conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
    my_cursor=conn.cursor()
    my_cursor.execute("update customer1 set Name=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where reference=%s",(
          
          self.var_name.get(),
          self.var_gender.get(),
          self.var_post.get(),
          self.var_mobile.get(),
          self.var_email.get(),
          self.var_nationality.get(),
          self.var_idproof.get(),
          self.var_idnum.get(),
          self.var_address.get(),
          self.var_ref.get()
    ))
    conn.commit()
    self.fetch_data()
    conn.close()
    messagebox.showinfo("Update","Customer details have been updated",parent=self.root)

    







  def mdelete(self):
      mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
      if mdelete:
        conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
        my_cursor=conn.cursor()
        query="delete from customer1 where reference=%s"
        value=(self.var_ref.get(),)
        my_cursor.execute(query,value)
      else:
        return
    
      conn.commit()
      self.fetch_data()
      conn.close()


  def reset(self):
    self.var_ref.set(""),
    self.var_name.set(""),
    
    self.var_post.set(""),
    self.var_mobile.set(""),
    self.var_email.set(""),
    
    
    self.var_idnum.set(""),
    self.var_address.set("")
    x=random.randint(1000,9999)
    self.var_ref.set(str(x))

  #def search(self):
    #conn=mysql.connector.connect(host="localhost",user="root",password="rssba0102",database="new_schema")
    #my_cursor=conn.cursor()

    #my_cursor.execute("select * from customer1 where "+str(self.search_var.get())+"LIKE'%"+str(self.text_search.get())+"%'")

    #rows=my_cursor.fetchall()
    #if len(rows)!=0:
    #self.cust_details_table.delete(*self.cust_details_table.get_children())
      #for i in rows:    
        #self.cust_details_table.insert("",END,values=i)
      #conn.commit()
    #conn.close()









if __name__=="__main__":
  root=Tk()
  obj=cust(root)
  root.mainloop()