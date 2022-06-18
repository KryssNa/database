
from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("400x600")
root.title("Facebook")
root.configure(bg="#F5F5DC")

##creating database
conn=sqlite3.connect("facebook.db")
c=conn.cursor()
c.execute(""" CREATE TABLE User(
    first_name text,
    last_name text,
    address text,
    age_num integer,
    password text,
    father_name text,
    city text,
    zipcode integer
    )""")  
print("Table created succcessfully")

##To delete from records
def delete():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("DELETE from user WHERE oid = " + delete_box.get())
    print("Deleted successfully")    
    conn.commit()
    conn.close()

##To update records
def update():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    record_id=delete_box.get()
    
    c.execute("""UPDATE user SET 
            first_name=:first,
            last_name=:last,
            address=:address,
            age_num=:ages,
            password=:password,
            father_name=:f_name,
            city=:city,
            zipcode=:zipcode
    
            WHERE oid =:oid""",
             {
              "first":f_name_editor.get(),
              "last":l_name_editor.get(),
              "address":address_editor.get(),
              "ages":age_num_editor.get(),
              "password":password_editor.get(),
              "f_name":father_name_editor.get(),
              "city":city_editor.get(),
              "zipcode":zipcode_editor.get(),
              "oid":record_id
            } 
        )
    messagebox.showinfo("kryss","updated successfully")
    conn.commit()
    conn.close()

##To edit records
def edit():
    global editor
    editor=Toplevel()
    editor.title("update data")
    editor.geometry("300x400")
    editor.configure(bg="#F5F5DC")
    
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM user WHERE  oid =" + record_id)
    records = c.fetchall()
    
    global f_name_editor
    global l_name_editor
    global address_editor
    global age_num_editor
    global password_editor
    global father_name_editor
    global city_editor
    global zipcode_editor
    
    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=10)
    
    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)
    
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1)
    
    age_num_editor=Entry(editor,width=30)
    age_num_editor.grid(row=3,column=1)
    
    password_editor=Entry(editor,width=30)
    password_editor.grid(row=4,column=1)
    
    father_name_editor=Entry(editor,width=30)
    father_name_editor.grid(row=5,column=1)
    
    city_editor=Entry(editor,width=30)
    city_editor.grid(row=6,column=1)
    
    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=7,column=1)
    
    f_name_label=Label(editor,text="First Name",fg="black",bg="#F5F5DC")
    f_name_label.grid(row=0,column=0,pady=(10,0))
    
    l_name_label=Label(editor,text="Last Name",fg="black",bg="#F5F5DC")
    l_name_label.grid(row=1,column=0)
    
    address_label=Label(editor,text="Address",fg="black",bg="#F5F5DC")
    address_label.grid(row=2,column=0)
    
    age_label=Label(editor,text="Age",fg="black",bg="#F5F5DC")
    age_label.grid(row=3,column=0)
    
    password_label=Label(editor,text="Password",fg="black",bg="#F5F5DC")
    password_label.grid(row=4,column=0)
    
    fatherName_label=Label(editor,text="Father Name",fg="black",bg="#F5F5DC")
    fatherName_label.grid(row=5,column=0)
    
    city_label=Label(editor,text="City",fg="black",bg="#F5F5DC")
    city_label.grid(row=6,column=0)
    
    zipcode_label=Label(editor,text="Zip Code",fg="black",bg="#F5F5DC")
    zipcode_label.grid(row=7,column=0)
    
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        age_num_editor.insert(0,record[3])
        password_editor.insert(0,record[4])
        father_name_editor.insert(0,record[5])
        city_editor.insert(0,record[6])
        zipcode_editor.insert(0,record[7])
        
    edit_btn= Button(editor,text="save",command=update,bg="#F47F16",fg="black")
    edit_btn.grid(row=10,columnspan=2,padx=10,pady=10,ipadx=125)
    conn.commit()
    conn.close()
        
##To show data 
def query():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("SELECT *,oid FROM user")
    
    records=c.fetchall()
    print(records)
    
    print_records=''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' '+ str(record[3])+ ' ' + '\t'+str(record[8])+"\n" 
    
    query_label=Label(root,text=print_records,fg="black",bg="#F5F5DC")
    query_label.grid(row=11,column=0,columnspan=2)
    
    conn.commit()
    conn.close()

##To submit
def submit():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("INSERT INTO user values(:first_name, :last_name, :address ,:age, :password, :father_name,:city, :zipcode)",{
        "first_name":first_name.get(),
        "last_name":last_name.get(),
        "address":address.get(),
        "age":age_num.get(),
        "password":password.get(),
        "father_name":father_name.get(),
        "city":city.get(),
        "zipcode":zipcode.get()
        } )
    
    messagebox.showinfo("kryss", "Inserted successfully")
    conn.commit()
    conn.close()

##creating entry to insert data
first_name= Entry(root, width=20)
first_name.grid(row=0,column=1,pady=10)

last_name=Entry(root,width=20)
last_name.grid(row=1,column=1,pady=5)

address=Entry(root,width=20)
address.grid(row=2,column=1,pady=5)

age_num=Entry(root,width=20)
age_num.grid(row=3,column=1,pady=5)

password=Entry(root,width=20)
password.grid(row=4,column=1,pady=5)

father_name=Entry(root,width=20)
father_name.grid(row=5,column=1,pady=5)

city=Entry(root,width=20)
city.grid(row=6,column=1,pady=5)

zipcode=Entry(root,width=20)
zipcode.grid(row=7,column=1,pady=5)

delete_box=Entry(root,width=20)
delete_box.grid(row=12,column=1,pady=5)

##creating  label(color:light goldenrod)
label_f_name=Label(root,text="First Name:",fg="black",bg="#F5F5DC")
label_f_name.grid(row=0,column=0,pady=5)

label_l_name=Label(root,text="Last Name:",fg="black",bg="#F5F5DC")
label_l_name.grid(row=1,column=0,pady=5)

label_address=Label(root,text="Address:",fg="black",bg="#F5F5DC")
label_address.grid(row=2,column=0,pady=5)


label_age=Label(root,text="Age:",fg="black",bg="#F5F5DC")
label_age.grid(row=3,column=0,pady=5)

label_pass=Label(root,text="Password:",fg="black",bg="#F5F5DC")
label_pass.grid(row=4,column=0,pady=5)

label_father_name=Label(root,text="Father Name:",fg="black",bg="#F5F5DC")
label_father_name.grid(row=5,column=0,pady=5)

label_city=Label(root,text="City:",fg="black",bg="#F5F5DC")
label_city.grid(row=6,column=0,pady=5)

label_zipcode=Label(root,text="Zip code:",fg="black",bg="#F5F5DC")
label_zipcode.grid(row=7,column=0,pady=5)

delete_label=Label(root,text="Table No.",fg="black",bg="#F5F5DC")
delete_label.grid(row=12,column=0,pady=5)


##for button ,color(orange red)
btn=Button(root,text="Submit",command=submit,bg="#F47F16",fg="black")
btn.grid(row=10,column=1,pady=5,padx=10,ipadx=20)

query_btn=Button(root, text="Show Records",command=query,bg="#F47F16",fg="black")
query_btn.grid(row=17,column=0,columnspan=2,padx=30,pady=10,ipadx=90)

edit_btn=Button(root,text="Update",command=edit,bg="#F47F16",fg="black")
edit_btn.grid(row=15,column=0,columnspan=2,padx=30,pady=10,ipadx=107)

delete_btn=Button(root,text="Delete",command=delete,bg="#F47F16",fg="black")
delete_btn.grid(row=14,column=0,columnspan=2,padx=30,pady=10,ipadx=110)


conn.commit()
conn.close()
root.mainloop()