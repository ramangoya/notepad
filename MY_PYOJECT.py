from tkinter  import *
from tkinter import ttk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
from tkinter import filedialog
import csv

root=Tk()
root.geometry("1390x1299")
root.config(bg="skyblue")
list2=["Name_string","Father_Name_string","Age_string","Address_string","Number_string","combobox_gender","combobox_district"]

def sql():
    global con
    con=sqlite3.connect("Student_DataBase.db")
    cursor=con.cursor()
    Name_string=name_entry.get()
    Father_Name_string=fname_entry.get()
    Age_string=Aname_entry.get()
    Number_string=Nname_entry.get()
    Address_string=aname_entry.get()
    combobox_gender=combobox.get()
    combobox_district=combobox_d.get()
    list1=[Name_string,Father_Name_string,Age_string,Address_string,Number_string,combobox_gender,combobox_district]
    try:
        cursor.execute("CREATE TABLE student(name text,fathername text,age integer,phone integer,address text,gender text,destrict text)")
    except:
        pass
    cursor.execute("INSERT INTO student(name,fathername,age,phone,address,gender,destrict)VALUES(?,?,?,?,?,?,?)",list1)
    con.commit()
    messagebox.showinfo("INFROMETION","DATA SUBMITTED")
    cursor = con.cursor()
    cursor.execute("select *from student")
    var = cursor.fetchall()
    f = open("student.csv","w",newline="")
    obj = csv.writer(f)
    obj.writerow(list2)
    for i in var:
        obj.writerow(i)



dict1={}

def Edit():
    def delate():
        nameentry.delete(0,END)
        fatherentry.delete(0,END)
        AGEentry.delete(0,END)
        PHONEentry.delete(0,END)
        ADDRESSentry.delete(0,END)
        GENDERcombobox.delete(0,END)
        DISTRICTcombobox_d.delete(0,END)
        
    def show():
        con=sqlite3.connect("Student_DataBase.db")
        cursor=con.cursor()
        s=searchentry.get()
        cursor.execute("select * from student where name=?",[s])
        row=cursor.fetchall()
        print(row)
        for i in row:
            if s in i:
                var1=i[0]
                var2=i[1]
                var3=i[2]
                var4=i[3]
                var5=i[4]
                var6=i[5]
                var7=i[6]
            else:
                var1=0
                var2=0
                var3=0
                var4=0
                var5=0
                var6=0
                var7=0
                
            print(i)
        

        nameentry.insert(0,var1)
        fatherentry.insert(1,var2)
        AGEentry.insert(2,var3)
        PHONEentry.insert(3,var4)
        ADDRESSentry.insert(4,var5)
        GENDERcombobox.set(var6)
        DISTRICTcombobox_d.set(var7)

        
        
    def Exit():
        close=messagebox.askyesno("INFROMETION","ARE YOU REALLY.... EXIT")
        if close>0:
            window.destroy()


    def update1():
                con=sqlite3.connect("Student_DataBase.db")
                cursor=con.cursor()
                s=searchentry.get()
                cursor.execute("select * from student where name=?",[s])
                row=cursor.fetchall()
                Name_string=nameentry.get()
                Father_Name_string=fatherentry.get()
                Age_string=AGEentry.get()
                Number_string=PHONEentry.get()
                Address_string=ADDRESSentry.get()
                combobox_gender=GENDERcombobox.get()
                combobox_district=DISTRICTcombobox_d.get()
                cursor.execute("update student set name=? where name=?",(Name_string,s))
                cursor.execute("update student set fathername =? where name=?",(Father_Name_string,s))
                cursor.execute("update student set age= ? where name=?",(Age_string,s))
                cursor.execute("update student set phone= ? where name=?",(Number_string,s))
                cursor.execute("update student set address= ? where name=?",(Address_string,s))
                cursor.execute("update student set gender= ? where name=?",(combobox_gender,s))
                cursor.execute("update student set destrict= ? where name=?",(combobox_district,s))
                print('updated')
                con.commit()
                

        
    window=Tk()
    window.geometry("1390x1299")
    window.config(bg="skyblue")
    #variable for Edit window
    searchVariable=StringVar()
    nameVariable=StringVar()
    fatherVariable=StringVar()
    ageVariable=StringVar()
    phoneVariable=StringVar()
    addressVariable=StringVar()
    genderVariable=StringVar()
    districtVariable=StringVar()
    





    
    mainFrame=Frame(window,width=1300,bg="skyblue",height=800)
    mainFrame.pack()
    
    titleFrame=Frame(mainFrame,width=100,bg="yellow",height=100)
    titleFrame.pack(side=TOP)
    
    titleLabel=Label(titleFrame,text="SHOW DATA WINDOW",font=("Arial",25,"bold"),bg="steelblue1")
    titleLabel.pack()



    searchFrame=LabelFrame(mainFrame,text="search",width=500,height=700,bg="steelblue1",font=("Arial",25,"bold"))
    searchFrame.pack(side=LEFT)
    
    searchlabel=Label(searchFrame,text="NAME",font=("Arial",25,"bold"),bg="steelblue1")
    searchlabel.grid(row=0,column=0)
    searchentry=Entry(searchFrame,width=45,bd=7,font=("arial",10,"bold"),textvariable=searchVariable)
    searchentry.grid(row=0,column=1)
    searchbutton=Button(searchFrame,text="SEARCH",width=15,bd=5,font=("Arial",10,"bold"),command=show)
    searchbutton.grid(row=2,column=0)

    
    bodyFrame=Frame(mainFrame,width=1200,height=700,bg="skyblue")
    bodyFrame.pack(side=RIGHT)


    
    #this is a label for name
    namelabel=Label(bodyFrame,text="NAME",font=("Arial",25,"bold"),bg="skyblue")
    namelabel.grid(row=0,column=0)
    nameentry=Entry(bodyFrame,width=45,bd=7,font=("arial",10,"bold"),textvariable=nameVariable)
    nameentry.grid(row=0,column=1)
    #this is a label for father's name
    fatherlabel=Label(bodyFrame,text="FATHER'S NAME",font=("Arial",25,"bold"),bg="skyblue")
    fatherlabel.grid(row=2,column=0)
    fatherentry=Entry(bodyFrame,width=45,bd=7,font=("arial",10,"bold"),textvariable=fatherVariable)
    fatherentry.grid(row=2,column=1)
    #this is a label for Age
    AGElabel=Label(bodyFrame,text="AGE",font=("Arial",25,"bold"),bg="skyblue")
    AGElabel.grid(row=3,column=0)
    AGEentry=Entry(bodyFrame,width=45,bd=7,font=("arial",10,"bold"),textvariable=ageVariable)
    AGEentry.grid(row=3,column=1)
    #this is a label for name
    ADDRESSlabel=Label(bodyFrame,text="PHONE ",font=("Arial",25,"bold"),bg="skyblue")
    ADDRESSlabel.grid(row=4,column=0)
    ADDRESSentry=Entry(bodyFrame,width=45,bd=7,font=("arial",10,"bold"),textvariable=addressVariable)
    ADDRESSentry.grid(row=4,column=1)
    #this is a label for phone
    PHONElabel=Label(bodyFrame,text="ADDRESS",font=("Arial",25,"bold"),bg="skyblue")
    PHONElabel.grid(row=5,column=0)
    PHONEentry=Entry(bodyFrame,width=45,bd=7,font=("arial",10,"bold"),textvariable=phoneVariable)
    PHONEentry.grid(row=5,column=1)
    #this is a label for GENDER
    GENDERlable=Label(bodyFrame,text="GENDER",font=("arial",25,"bold"),bd=3,bg="skyblue",pady=10)
    GENDERlable.grid(row=6,column=0)


    GENDERcombobox=ttk.Combobox(bodyFrame,values=["Male","Female","Other"],width=35,font=("arial",10,"bold"),textvariable=genderVariable)
    GENDERcombobox.grid(row=6,column=1)
    #this is a label for district
    DISTRICTcombobox_district=Label(bodyFrame,text="DISTRICT",font=("arial",25,"bold"),bg="skyblue")
    DISTRICTcombobox_district.grid(row=7,column=0)
    DISTRICTlist3=["Agra","Aligarh","Allahabad","Ambedkar Nagar","Amethi","Amroha","Auraiya""Azamgarh","Bagpat""Bahraich","Ballia","Balrampur","Banda","Barabanki","Bareilly","Basti","Bhadohi","Bijnor","Budaun","Bulandshahr","Chandauli","Chitrakoot","Deoria","Etah","Etawah","Faizabad","Farrukhabad","Fatehpur","FirozabadGautam Buddh Nagar","Ghaziabad""Ghazipur""Gonda""Gorakhpur","Hamirpur","Hapur","Hardoi","Hathras","Jalaun","Jaunpur","Jhansi","Kannauj","Kanpur Dehat","Kanpur Nagar","KasganjKaushambi","Kushinagar","Lakhimpur Kheri","Lalitpur","LucknowMaharajganj""Mahoba","Mainpuri","Mathura","Mau","Meerut","Mirzapur","Moradabad","Muzaffarnagar","Pilibhit","Pratapgarh""Raebareli""Rampur","Saharanpur","Sambhal","Sant Kabir Nagar","Shahjahanpur","Shamli[18]","Shravasti","Siddharthnagar","Sitapur","Sonbhadra","Sultanpur","Unnao","Varanasi"]
    DISTRICTcombobox_d=ttk.Combobox(bodyFrame,values=list3,width=35,font=("arial",10,"bold"),textvariable=districtVariable)
    DISTRICTcombobox_d.grid(row=7,column=1,padx=10)
        
#label for button


    clear_button=Button(bodyFrame,text="CLEAR",width=15,bd=5,font=("Arial",10,"bold"),command=delate)
    clear_button.grid(row=8,column=0)

    edit_button=Button(bodyFrame,text="UPDATE",width=15,bd=5,font=("Arial",10,"bold"),command=update1)
    edit_button.grid(row=8,column=1)

    EXIT_button=Button(bodyFrame,text="EXIT",width=15,bd=5,font=("Arial",10,"bold"),command=Exit)
    EXIT_button.grid(row=8,column=2)



    
    window.mainloop()


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------










 
root_Name=StringVar()
root_Father_Name=StringVar()
root_Age=StringVar()
root_Number=StringVar()
root_Address=StringVar()
root_combobox_gender=StringVar()
combobox_state=StringVar()
combobox_district=StringVar()
filetruck=StringVar()



def clear():
    name_entry.delete(0,END)
    fname_entry.delete(0,END)
    Aname_entry.delete(0,END)
    Nname_entry.delete(0,END)
    aname_entry.delete(0,END)
    combobox.delete(0,END)
    combobox_d.delete(0,END)

def ima():
    name=filedialog.askopenfilename()
    filetruck.set(name)
    '''
    img=ImageTk.PhotoImage(Image.open(name))
    canvas.create_image(100,90,image=img)
    '''
    canvas = Canvas(bodyFrame,width=100, height=80,)
    canvas.grid(row=1,column=5)
    image = ImageTk.PhotoImage(file=name)
    canvas.create_image(50, 40, image=image, anchor=NW)


def Exit1():
        close=messagebox.askyesno("INFROMETION","ARE YOU REALLY.... EXIT")
        if close>0:
            root.destroy()


    



scroll=Scrollbar(root, orient=VERTICAL) 
scroll.pack(side=RIGHT, fill=Y)

mainFrame=Frame(root,bg="skyblue")
mainFrame.pack()
#scrollbar = Scrollbar(mainFrame) 
#scrollbar.pack( side = RIGHT, fill = Y ) 

titleFrame=Frame(mainFrame,width=1000,bg="skyblue")
titleFrame.pack(side=TOP)

title=Label(titleFrame,text="STUDENT DATABASE",font=("itelic",20,"bold"),padx=50,pady=10,bg="skyblue")
title.grid()

bodyFrame=Frame(mainFrame,bg="skyblue",width=1500)
bodyFrame.pack(side=TOP)

name_lable=Label(bodyFrame,text="STUDENT NAME: ",font=("arial",10,"bold"),bg="skyblue",pady=10)
name_lable.grid(row=0,column=0)
name_entry=Entry(bodyFrame,width=40,bd=4,textvariable=root_Name)
name_entry.grid(row=0,column=2)

name_father_lable=Label(bodyFrame,text="FATHER'S NAME: ",font=("arial",10,"bold"),bd=3,bg="skyblue",pady=10)
name_father_lable.grid(row=1,column=0)
fname_entry=Entry(bodyFrame,width=40,bd=4,textvariable=root_Father_Name)
fname_entry.grid(row=1,column=2,padx=10)

age_lable=Label(bodyFrame,text="STUDENT AGE",font=("arial",10,"bold"),bd=3,bg="skyblue",pady=10)
age_lable.grid(row=2,column=0)
Aname_entry=Entry(bodyFrame,width=40,bd=4,textvariable=root_Age)
Aname_entry.grid(row=2,column=2,padx=10)

phone_lable=Label(bodyFrame,text="PHONE NUMBER",font=("arial",10,"bold"),bd=3,bg="skyblue",pady=10)
phone_lable.grid(row=3,column=0)
Nname_entry=Entry(bodyFrame,width=40,bd=4,textvariable=root_Number)
Nname_entry.grid(row=3,column=2,padx=10)

address_lable=Label(bodyFrame,text="ADDRESS",font=("arial",10,"bold"),bd=3,bg="skyblue")
address_lable.grid(row=4,column=0)
aname_entry=Entry(bodyFrame,width=40,bd=4,textvariable=root_Address)
aname_entry.grid(row=4,column=2,padx=10,pady=10)

Gender_lable=Label(bodyFrame,text="GENDER",font=("arial",10,"bold"),bd=3,bg="skyblue",pady=10)
Gender_lable.grid(row=5,column=0)


combobox=ttk.Combobox(bodyFrame,values=["Male","Female","Other"],width=35,textvariable=root_combobox_gender)
combobox.grid(row=5,column=2)

image=Button(bodyFrame,text="Open",font=("arial",10,"bold"),bd=3,command=ima)
image.grid(row=1,column=4)
image_truck=Entry(bodyFrame,width=45,textvariable=filetruck)
image_truck.grid(row=2,column=4)
#-----------------------------------------------------------------------------------

combobox_district=Label(bodyFrame,text="District",font=("arial",10,"bold"),bg="skyblue")
combobox_district.grid(row=7,column=0)

list3=["Agra","Aligarh","Allahabad","Ambedkar Nagar","Amethi","Amroha","Auraiya""Azamgarh","Bagpat""Bahraich","Ballia","Balrampur","Banda","Barabanki","Bareilly","Basti","Bhadohi","Bijnor","Budaun","Bulandshahr","Chandauli","Chitrakoot","Deoria","Etah","Etawah","Faizabad","Farrukhabad","Fatehpur","FirozabadGautam Buddh Nagar","Ghaziabad""Ghazipur""Gonda""Gorakhpur","Hamirpur","Hapur","Hardoi","Hathras","Jalaun","Jaunpur","Jhansi","Kannauj","Kanpur Dehat","Kanpur Nagar","KasganjKaushambi","Kushinagar","Lakhimpur Kheri","Lalitpur","LucknowMaharajganj""Mahoba","Mainpuri","Mathura","Mau","Meerut","Mirzapur","Moradabad","Muzaffarnagar","Pilibhit","Pratapgarh""Raebareli""Rampur","Saharanpur","Sambhal","Sant Kabir Nagar","Shahjahanpur","Shamli[18]","Shravasti","Siddharthnagar","Sitapur","Sonbhadra","Sultanpur","Unnao","Varanasi"]



combobox_d=ttk.Combobox(bodyFrame,values=list3,width=35,textvariable=combobox_district)
combobox_d.grid(row=7,column=2,padx=10)




#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

address_lable=Label(bodyFrame,text="                     ",font=("arial",10,"bold"),bd=3,bg="skyblue",pady=20)
address_lable.grid(row=0,column=3)

address_lable=Label(bodyFrame,text="",font=("arial",10,"bold"),bd=3,bg="skyblue",pady=20)
address_lable.grid(row=11,column=0)


address_lable=Label(bodyFrame,text="",font=("arial",10,"bold"),bd=3,bg="skyblue",pady=20)
address_lable.grid(row=12,column=0)
#==================================================================================
#==================================================================================
#==================================================================================

BottamFrame=Frame(mainFrame,bg="red",width=400)
BottamFrame.pack(side=BOTTOM)

submit_button=Button(BottamFrame,text="SUBMIT",width=15,bd=5,font=("Arial",10,"bold"),command=sql)
submit_button.grid(row=0,column=0)

clear_button=Button(BottamFrame,text="CLEAR",width=15,bd=5,font=("Arial",10,"bold"),command=clear)
clear_button.grid(row=0,column=1)

edit_button=Button(BottamFrame,text="EDIT",width=15,bd=5,font=("Arial",10,"bold"),command=Edit)
edit_button.grid(row=0,column=2)

EXIT_button=Button(BottamFrame,text="EXIT",width=15,bd=5,font=("Arial",10,"bold"),command=Exit1)
EXIT_button.grid(row=0,column=3)

root.mainloop()

