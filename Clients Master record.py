from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox



class Master:
    def __init__(self,root):
        self.root=root
        self.root.title("Client Management System")
        self.root.geometry("1900x750+0+0")

        title=Label(self.root,text="Client Management System",bd=10,relief=GROOVE,font=("Cambria",30,"bold"),bg="black",fg="white")
        title.pack(side=TOP,fill=X)

        #================All Variables===============#
        self.Record_var=StringVar()
        self.name_var=StringVar()
        self.speciality_tag_var=StringVar()
        self.regn_var=StringVar()
        self.phone_var=StringVar()
        self.mobile_var=StringVar()
        self.email_var=StringVar()
        self.address_var=StringVar()
        self.Hospital_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()



#=============Manage frame=============#

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=20,y=101,width=550,height=690)

        m_title=Label(Manage_Frame,text="Manage Clients",bg="black",fg="white",font=("Book Antiqua",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_rec=Label(Manage_Frame,text="Record No. :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_rec.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_Rec=Entry(Manage_Frame,textvariable=self.Record_var,font=("Book Antiqua",14,"bold"),bd=5,relief=GROOVE).grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Full Name :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("Book Antiqua",14,"bold"),bd=5,relief=GROOVE).grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_speciality_tag=Label(Manage_Frame,text="Speciality Tag :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_speciality_tag.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_speciality_tag=Entry(Manage_Frame,textvariable=self.speciality_tag_var,font=("Book Antiqua",14,"bold"),bd=5,relief=GROOVE).grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_regn=Label(Manage_Frame,text="Regn no. :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_regn.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        txt_Regn=Entry(Manage_Frame,textvariable=self.regn_var,font=("Book Antiqua",14,"bold"),bd=5,relief=GROOVE).grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_phone=Label(Manage_Frame,text="Phone no. :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_phone.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_phone=Entry(Manage_Frame,textvariable=self.phone_var,font=("Book Antiqua",14,"bold"),bd=5,relief=GROOVE).grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_mobile=Label(Manage_Frame,text="Mobile No. :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_mobile.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_mobile=Entry(Manage_Frame,textvariable=self.mobile_var,font=("Book Antiqua",14,"bold"),bd=5,relief=GROOVE).grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_Frame,text="Email Id :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_email.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("Book Antiqua",14,"bold"),bd=5,relief=GROOVE).grid(row=7,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_address.grid(row=8,column=0,pady=10,padx=20,sticky="w")
        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("Book Antiqua",10))
        self.txt_address.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        lbl_Hospital=Label(Manage_Frame,text="Hospital name :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_Hospital.grid(row=9,column=0,pady=10,padx=20,sticky="w")
        txt_Hospital=Entry(Manage_Frame,textvariable=self.Hospital_var,font=("Book Antiqua",14,"bold"),bd=5,relief=GROOVE).grid(row=9,column=1,pady=10,padx=20,sticky="w")

        #====================Button Frame===================#

        btn_frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_frame.place(x=20,y=620,width=411)

        Addbtn=Button(btn_frame,text="ADD",width=10,command=self.add_Clientsystem).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


        
#=============Detail frame=============#


        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Detail_Frame.place(x=600,y=100,width=900,height=690)

        lbl_search=Label(Detail_Frame,text="Search By :",bg="black",fg="white",font=("Book Antiqua",17,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("Book Antiqua",13,"bold"),state='readonly')
        combo_search['values']=("Record","Name","mobile")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("Book Antiqua",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show all",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

  #========================Table Frame=========================#
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="black")
        Table_Frame.place(x=10,y=70,width=760,height=600)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Client_table=ttk.Treeview(Table_Frame,columns=("record","name","speciality_tag","regn","phone","mobile","email","address","hospital"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Client_table.xview)
        scroll_y.config(command=self.Client_table.yview)
        self.Client_table.heading("record",text="Record No.")
        self.Client_table.heading("name",text="Full name")
        self.Client_table.heading("speciality_tag",text="speciality tag")
        self.Client_table.heading("regn",text="Regn No.")
        self.Client_table.heading("phone",text="Phone No.")
        self.Client_table.heading("mobile",text="Mobile No.")
        self.Client_table.heading("email",text="Email Id")
        self.Client_table.heading("address",text="Address")
        self.Client_table.heading("hospital",text="Hospital name")
        self.Client_table['show']='headings'
        self.Client_table.column("record",width=100)
        self.Client_table.column("name",width=120)
        self.Client_table.column("speciality_tag",width=100)
        self.Client_table.column("regn",width=100)
        self.Client_table.column("phone",width=100)
        self.Client_table.column("mobile",width=100)
        self.Client_table.column("email",width=100)
        self.Client_table.column("address",width=150)
        self.Client_table.column("hospital",width=100)
        self.Client_table.pack(fill=BOTH,expand=1)
        self.Client_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        

    def add_Clientsystem(self):
            if self.Record_var.get()=="" or self.name_var.get()=="":
                    messagebox.showerror("Error","All fields are required!!!")
            else:
                    con=pymysql.connect(host="localhost",user="root",password="",database="clientsystem")
                    cur=con.cursor()
                    cur.execute("insert into clientsystem values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Record_var.get(),
                                                                                              self.name_var.get(),
                                                                                              self.speciality_tag_var.get(),
                                                                                              self.regn_var.get(),
                                                                                              self.phone_var.get(),
                                                                                              self.mobile_var.get(),
                                                                                              self.email_var.get(),
                                                                                              self.txt_address.get('1.0',END),
                                                                                              self.Hospital_var.get()
                                                                                              ))
            
                    con.commit()
                    self.fetch_data()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="clientsystem")
            cur=con.cursor()
            cur.execute("select * from clientsystem")
            rows=cur.fetchall()
            if len(rows)!=0:
                    self.Client_table.delete(*self.Client_table.get_children())
                    for row in rows:
                            self.Client_table.insert('',END,values=row)
                    con.commit()
            con.close()                
            
    def clear(self):
            self.Record_var.set("")
            self.name_var.set("")
            self.speciality_tag_var.set("")
            self.regn_var.set("")
            self.phone_var.set("")
            self.mobile_var.set("")
            self.email_var.set("")
            self.txt_address.delete("1.0",END)
            self.Hospital_var.set("")

    def get_cursor(self,ev):
            cursor_row=self.Client_table.focus()
            contents=self.Client_table.item(cursor_row)
            row=contents['values']
            self.Record_var.set(row[0])
            self.name_var.set(row[1])
            self.speciality_tag_var.set(row[2])
            self.regn_var.set(row[3])
            self.phone_var.set(row[4])
            self.mobile_var.set(row[5])
            self.email_var.set(row[6])
            self.txt_address.delete("1.0",END)
            self.txt_address.insert(END,row[7])
            self.Hospital_var.set(row[8])

    def update_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="clientsystem")
            cur=con.cursor()
            cur.execute("update clientsystem set name=%s,speciality_tag=%s,regn=%s,phone=%s,mobile=%s,email=%s,address=%s,Hospital=%s where Record=%s",(
                                                                                                                          self.name_var.get(),
                                                                                                                          self.speciality_tag_var.get(),
                                                                                                                          self.regn_var.get(),
                                                                                                                          self.phone_var.get(),
                                                                                                                          self.mobile_var.get(),
                                                                                                                          self.email_var.get(),
                                                                                                                          self.txt_address.get('1.0',END),
                                                                                                                          self.Hospital_var.get(),
                                                                                                                          self.Record_var.get()
                                                                                                                          ))
            
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()

    def delete_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="clientsystem")
            cur=con.cursor()
            cur.execute("delete from clientsystem where Record=%s",self.Record_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
           
    def search_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="clientsystem")
            cur=con.cursor()
            cur.execute("select * from clientsystem where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                    self.Client_table.delete(*self.Client_table.get_children())
                    for row in rows:
                            self.Client_table.insert('',END,values=row)
                    con.commit()
            con.close()            
            



root=Tk()
ob=Master(root)
root.mainloop()
