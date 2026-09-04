import sqlite3 as a
mydb=a.connect('MEDICALSTORE.db')
mycursor=mydb.cursor()
mycursor.execute('create table if not exists medicine(m_id integer primary key , name varchar(50), brand_name varchar(50), price decimal(7,2), availability char(10))')
mycursor.execute('create table if not exists employee(e_id integer primary key , name varchar(50),  salary decimal(7,2), age integer)')
mycursor.execute('create table if not exists cart(order_id integer primary key , name varchar(50), brand_name varchar(50), price decimal(7,2))')
mydb.commit()

def connection():
    import sqlite3 as a
    mycursor=mydb.cursor()
    mycursor.execute('select * from medicine')
connection()

def employee():
    ans='y'
    while ans in 'yY':
        a=int(input('ENTER EMPLOYEE ID : '))
        b=input('ENTER EMPLOYEE NAME : ')
        f=float(input('ENTER SALARY : '))
        g=int(input('ENTER THE AGE : '))
        mycursor.execute("insert into employee values({0},'{1}','{2}',{3}) ".format(a,b,f,g))
        mydb.commit()
        print("*****DATA ENTERED*****")
        ans=input(' DO YOU WANT TO ADD MORE OR NOT? (YES/NO) ')
        if ans not in 'yY':
            option()

def edemp():
    ans='y'
    while ans in 'yY':
        print('1. SALARY \n2. NAME ')
        opt=int(input('ENTER THE COLOUMN YOU WANT TO EDIT INFORMATION INTO : '))
        if opt==1:
            p=input('ENTER THE EMPLOYEE ID INTO WHICH YOU WANT TO EDIT : ')
            n=float(input('ENTER THE NEW SALARY : '))
            mycursor.execute("update employee set salary ='{}' where e_id={} ".format(n,p))
            mydb.commit()
            print('*******SALARY UPDATED*******')
        if opt==2:
            a=input('ENTER THE EMPLOYEE ID INTO WHICH YOU WANT TO EDIT : ')
            b=input('ENTER THE NAME : ')
            mycursor.execute("update employee set name='{}' where e_id={} ".format(b,a))
            mydb.commit()
            print('*******NAME UPDATED*******')
            ans=input(' DO YOU WANT TO EDIT MORE OR NOT? (YES/NO) ')
            if ans not in 'yY':
                option()
    
def addmd():
    
    ans='y'
    while ans in 'yY':
        a=int(input('ENTER THE SERIAL NUMBER : '))
        b=input('ENTER THE MEDICINE NAME : ')
        c=input('ENTER THE MEDICINE BRAND NAME : ')
        f=float(input('ENTER THE PRICE : '))
        g=input('ENTER THE AVAILABILITY : ')
        mycursor.execute("insert into medicine values({0},'{1}','{2}',{3},'{4}')".format(a,b,c,f,g))
        mydb.commit()
        print("*****DATA ENTERED*****")
        ans=input(' DO YOU WANT TO ADD MORE OR NOT? (YES/NO) ')
        if ans not in 'yY':
            option()
        
def editmd():
    
    ans='y'
    while ans in 'yY':
        print('1. PRICE \n2. AVAILABILITY ')
        opt=int(input('ENTER THE COLOUMN YOU WANT TO EDIT INFORMATION INTO : '))
        if opt==1:
            n=input('ENTER THE MEDICINE ID INTO WHICH YOU WANT TO EDIT : ')
            p=float(input('ENTER THE NEW PRICE : '))
            mycursor.execute("update medicine set price={} where m_id={} ".format(p,n))
            mydb.commit()
            print('*******PRICE UPDATED*******')
        if opt==2:
            a=input('ENTER THE MEDICINE ID INTO WHICH YOU WANT TO EDIT : ')
            b=input('ENTER THE AVAILABILITY : ')
            mycursor.execute("update medicine set availability='{}' where m_id={} ".format(b,a))
            mydb.commit()
            print('*******AVAILABILITY UPDATED*******')
            ans=input(' DO YOU WANT TO EDIT MORE OR NOT? (YES/NO) ')
            if ans not in 'yY':
                option()

def dltmd():
    
    ans='y'
    while ans in 'yY':
        n=input('ENTER THE MEDICINE ID WHICH YOU WANT TO DELETE : ')
        mycursor.execute("delete from medicine where m_id={} ".format(n))
        mydb.commit()
        print("*******RECORD DELETED******")
        ans=input(' DO YOU WANT TO DELETE MORE OR NOT? (YES/NO) ')
        if ans not in 'yY':
            option()

        
def chpr():
    
    ans='y'
    while ans in 'yY':
        n=input('ENTER THE MEDICINE ID WHOSE PRICE YOU WANT TO SEE : ')
        price=mycursor.execute("select price from medicine where m_id={} ".format(n))
        ans=input(' DO YOU WANT TO CHECK MORE OR NOT? (YES/NO) ')
        if ans not in 'yY':
            option()
            
def ordermedicine():
    ans='y'
    while ans in 'yY':
        a=int(input('ENTER THE ORDER ID : '))
        b=input('ENTER THE MEDICINE NAME : ')
        c=input('ENTER THE MEDICINE BRAND NAME : ')
        f=float(input('ENTER THE PRICE : '))
        mycursor.execute("insert into cart values({0},'{1}','{2}',{3}) ".format(a,b,c,f))
        mydb.commit()
        ans=input(' DO YOU WANT TO ORDER MORE OR NOT? (YES/NO) ')
        if ans not in 'yY':
            print("*****ORDER SUCCESSFULLY PLACED*****")
            option()
    
def enquiry():
    
    ans='y'
    while ans in 'yY':
        n=input('ENTER THE MEDICINE NAME ABOUT WHICH YOU WANT TO ENQUIRE : ')
        avail=mycursor.execute("select availability from medicine where name='{}' ".format(n))
        mydb.commit()
        print(avail)
        ans=input(' DO YOU WANT TO ENQUIRE MORE OR NOT? (YES/NO) ')
        if ans not in 'yY':
            option()
        
def helpdesk():
    
    ans='y'
    while ans in 'yY':
        n=input('ENTER THE MEDICINE NAME WHOSE BRAND NAME YOU WANT TO KNOW  : ')
        brand=mycursor.execute("select brand_name from medicine where name='{}' ".format(n))
        mydb.commit()
        print(brand)
        ans=input(' DO YOU WANT TO KNOW MORE OR NOT? (YES/NO) ')
        if ans not in 'yY':
            option()


def option():
    print('\n')
    print('1. ADD EMPLOYEE DETAILS \n2. EDIT EMPLOYEE DETAILS \n3. ADD MEDICINE DETAILS \n4. EDIT MEDICINE DETAILS \n5. DELETE MEDICINE DETAILS \n6. CHECK PRICE \n7. ORDER MEDICINE \n8. ENQUIRY \n9. HELPDESK \n10. EXIT ')
    print('\n')
    opt=int(input('ENTER THE OPTION YOU WANT TO ACCESS : '))
    if opt==1: 
        employee()
    elif opt==2:
        edemp()
    elif opt==3:
        addmd()
    elif opt==4:
        editmd()
    elif opt==5:
        dltmd()
    elif opt==6:
        chpr()
    elif opt==7:
        ordermedicine()
    elif opt==8:
        enquiry()
    elif opt==9:
        helpdesk()
    elif opt==10:
        exit()
    else:
        print('PLEASE ENTER VALID OPTION ')

def signin():
    print ('*******          MEDICAL STORE          *******')
    pas=input("ENTER THE PASSWORD TO ACCESS THE SOFTWARE : ")
    if pas=='med123':
        option()
    else:
        print('1. ENTER PASSWORD AGAIN \n 2. FORGET PASSWORD ')
    while True:
        opt=int(input("ENTER THE OPTION : "))
        if opt==1:
            pas=input("ENTER THE PASSWORD TO ACCESS THE SOFTWARE : ")
            if pas=='med123':
                    option()
        else:
            pa=input('ENTER THE NEW PASSWORD : ')
            pas=pa
            break
    
    pas=input("ENTER THE PASSWORD TO ACCESS THE SOFTWARE : ")
    if pas==pas:
        option()

signin()
'''
import mysql.connector as a
mydb=a.connect(host='localhost',user='root',passwd='5283',database='MEDICALSTORE')
mycursor=mydb.cursor()
mycursor.execute('drop table employee')
mycursor.execute('drop table medicine')
mycursor.execute('drop table cart')
mydb.commit()
'''


