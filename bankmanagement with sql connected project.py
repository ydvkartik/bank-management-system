#SOURCE CODE FOR BANKING TRANSACTIONS
print("****BANK TRANSACTION****")
import datetime
#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="kartik",passwd="kartik")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
#creating required tables 
mycursor.execute("create table if not exists bank_master(acno char(20) primary key,name varchar(30),city char(20),mobileno char(10),balance float(9))")
mycursor.execute("create table if not exists banktrans(acno char (20),amount float(9),date date ,ttype char(1),foreign key (acno) references bank_master(acno))")
mydb.commit()
while(True):
    
    print("1=Create account")
    print("2=Deposit money")
    print("3=Withdraw money")
    print("4=Display account")
    print("5=Exit")
    ch=int(input("Enter your choice:"))
    
#PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
    if(ch==1):
        print("All information prompted are mandatory to be filled")
        acno=str(input("Enter account number:"))
        name=input("Enter name(limit 35 characters):")
        city=str(input("Enter city name:"))
        mn=str(input("Enter mobile no.:"))
        balance=0
        mycursor.execute("insert into bank_master values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"')")
        mydb.commit()
        print("Account is successfully created!!!")
        
#PROCEDURE FOR UPDATIONG DETAILS AFTER THE DEPOSITION OF MONEY BY THE APPLICANT
    elif(ch==2):
        acno=str(input("Enter account number:"))
        dp=float(input("Enter amount to be deposited:"))
        date=str(datetime.datetime.now())
        ttype="d"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(dp)+"','"+date+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where acno='"+acno+"'")
        mydb.commit()
        print("money has been deposited successully!!!")
#PROCEDURE FOR UPDATING THE DETAILS OF ACCOUNT AFTER THE WITHDRAWL OF MONEY BY THE APPLICANT

    elif(ch==3):
        acno=str(input("Enter account number:"))
        wd=float(input("Enter amount to be withdrawn:"))
        date=str(datetime.datetime.now())
        ttype="w"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(wd)+"','"+date+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
        mydb.commit()

#PROCEDURE FOR DISPLAYING THE ACCOUNT OF THE ACCOUNT HOLDER AFTER HE/SHE ENTERS HIS/HER ACCOUNT NUMBER
    elif(ch==4):
        acno=str(input("Enter account number:"))
        mycursor.execute("select * from bank_master where acno='"+acno+"'")
        for i in mycursor:
            print(i)
    else:
        break
        
        
