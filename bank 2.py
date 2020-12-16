import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='123',database='online')
cursor=db.cursor()
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
ctr=0
bank=0
while bank==0:
    print(color.UNDERLINE +color.RED+'<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>')
    print(color.YELLOW+ '       WELCOME TO HACKERS BANK    ')
    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
    print(color.CYAN+ 'Press 1 To  Log in')
    print('Press 2 To  Register a new bank account')
    print('Press 3 To  Delete your account')
    print('Press 4 To  Report a Bug')
    print('Press 5 To  Rate our Project')
    print('Press 6 For About us')
    print('Press 7 To  Check for Updates' +color.END)
    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
    choice=int(input(color.GREEN+ "Option :- " +color.END))
    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
    if choice==1:
        def welcome_message():
            print(color.UNDERLINE +color.RED+'<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>')
            print(color.YELLOW+ '       WELCOME TO HACKERS BANK    ')
            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
        

        def login():
            while True:
                us=input("Enter your username :- ")
                p=input("Enter your password :-")
                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                value=(us,p)
                query="select * from customers where username=%s and pas=%s"
                cursor.execute(query,(value))
                data_login=cursor.fetchall()
                if len(data_login)!=0:
                    globals()['ctr']=1
                    break
                else:
                    print('LOGIN UNSUCCSESSFUL')
                    print("USERNAME OR PASSWORD IS WRONG")
                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)

            return data_login

        def interface():
            welcome_message()
            b=login()
            if globals()['ctr']==1:
                i=b[0][0]
                name=b[0][2]
                print("LOGIN SUCCESSFUL")
                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                c=1
                while c==1:
                    print(color.CYAN+ 'Press 1 to  deposit money')
                    print('Press 2 to  withdraw money')
                    print('Press 3 to  Transfer money')
                    print('Press 4 to  do kyc')
                    print('Press 5 to  check balance')
                    print('Press 6 to  Pay Bills of Accessories ')
                    print('Press 7 to  Log Out' +color.END)
                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                    ch=int(input(color.GREEN+ "Option :- " +color.END))
                    if ch==1:
                        money_deposit=int(input('Amount to be deposited :- '))
                        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        cursor.execute('update customers set balance=balance+%s where sno=%s',(money_deposit,i))
                        db.commit()
                        q='select balance from customers where sno=%s and username=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            print("Updated Balance :- ",x)
                            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                    
                    elif ch==2:
                        q='select balance from customers where sno=%s and username=%s'
                        cursor.execute(q,(i,name))
                        b=cursor.fetchall()
                        b=b[0]
                        for row in b:
                            cn=int(row)
                            print("Your Current Balance: ",row)
                        money_withdrawn=int(input('Amount to be withdrawn :- '))
                        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        cursor.execute("update customers set balance=balance-%s where sno='%s'",(money_withdrawn,i))
                        db.commit()
                        q='select balance from customers where sno=%s and username=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            print("New Balance :- ",x)
                            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                    
                    elif ch==3:
                        q='select balance from customers where sno=%s and username=%s'
                        cursor.execute(q,(i,name))
                        b=cursor.fetchall()
                        b=b[0]
                        for row in b:
                            cn=int(row)
                            print("Your Current Balance: ",row)
                            while True:
                                def transfer():
                                    cursor.execute('update customers set balance=balance-%s where sno=%s',(money_transfer,i))
                                    print("Transfer Succesfull")
                                    db.commit()
                                    q='select balance from customers where sno=%s and username=%s'
                                    cursor.execute(q,(i,name))
                                    a=cursor.fetchall()
                                    a=a[0]
                                    for x in a:
                                        print("New Balance :- ",x)
                                        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                        
                                money_transfer=int(input("Enter ammount to be Transfer: "))
                                if money_transfer<=cn:
                                    print()
                                elif money_transfer>cn:
                                    print("you dont have sufficent money")
                                    break
                                else:
                                    print("please provide valid information")
                                    break
                                ac=int(input("Enter Receiver Acc. No:"))
                                ab=str(ac)
                                an=len(ab)
                                if an==8:
                                    print()
                                else:
                                    print("Please Provide the Valid A/C No")
                                    break
                                n=input("enter Receiver Name: ")
                                print()
                                yn=input("Are You Sure you want to transfer(yes/ no): ")
                                if yn=='yes' or yn=='Yes':
                                    transfer()
                                    
                                elif yn=='no' or yn=='No':
                                    print("Transfering Cancel")
                                else:
                                    print("Transfering Cancel due to invalid inforamtion")
                                break
                            break
             
                    elif ch==4:
                        q='select kyc from customers where sno=%s and username=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            condition=x
                        if condition=='false':
                            print(color.CYAN+ 'For KYC you need to provide details from one of these government id')
                            print('Press 1 for Citizenship')
                            print('Press 2 for Passport')
                            print('Press 3 for Pan Card')
                            print('Press 4 for Driving License')
                            print('Press 5 To Back' +color.END)
                            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                            cho=int(input("Enter your choice :- "))
                            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                            if cho==1:
                                ad=int(input("Citizenship Number :- "))
                                cursor.execute('update customers set kyc="true" where sno=%s and username=%s',(i,name))
                                db.commit()
                                print("KYC Done")
                            elif cho==2:
                                vi=int(input("Passport Number :- "))
                                cursor.execute('update customers set kyc="true" where sno=%s and username=%s',(i,name))
                                db.commit()
                                print("KYC Done")
                            elif cho==3:
                                pc=int(input("Pan Card Number :- "))
                                cursor.execute('update customers set kyc="true" where sno=%s and username=%s',(i,name))
                                db.commit()
                                print("KYC Done")
                            elif cho==4:
                                dl=int(input("Driving License Number :- "))
                                cursor.execute('update customers set kyc="true" where sno=%s and username=%s',(i,name))
                                db.commit()
                                print("KYC Done")
                            elif cho==5:
                                c==1
                            else:
                                print('Wrong Choice')
                        else:
                            print('KYC Already Done')
                        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                    elif ch==5:
                        q='select balance from customers where sno=%s and username=%s'
                        cursor.execute(q,(i,name))
                        a=cursor.fetchall()
                        a=a[0]
                        for x in a:
                            print("Balance :- ",x)
                            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                            break
                    elif ch==6:
                        print(color.CYAN+ 'Press 1 To  Pay Electricity Bill')
                        print('Press 2 To  Pay Water Bill')
                        print('Press 3 To  Pay Internet Bill')
                        print('Press 4 To  Pay Landline Phone Bill')
                        print('Press 5 To  Pay TV Bill')
                        print('Press 6 To  Recharge Phone')
                        print('Press 7 To  Back' +color.END)
                        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        opt=int(input(color.GREEN+ "Option :- " +color.END))
                        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        if opt==1:
                            cursor.execute('select sno from customers where sno=%s and username=%s',(i,name))
                            a=cursor.fetchall()
                            a=a[0]
                            for x in a:
                                id=x 
                            cadd=input("Enter Your City Address: ")
                            hadd=input("Enter Your Home Address: ")
                            hom=input("Enter Your House No: ")
                            amt=int(input("Enter Ammount To Pay: "))
                            co=input("Are You Sure?(yes/no): ")
                            if co=='yes' or co=='Yes':
                                cursor.execute("update ele set Ammount_Paid=%s where id=%s",(amt,id))
                                db.commit()
                                q='insert into ele values(%s,%s,%s,%s,%s,curdate())'
                                value=(id,cadd,hadd,hom,amt)
                                cursor.execute(q,value)
                                db.commit()
                                while True:
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    print(color.GREEN+ "   Electricity Bill Successfully Paid" +color.END)
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    break
                            else:
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                print("Transcation Canceled")
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        elif opt==2:
                            cursor.execute('select sno from customers where sno=%s and username=%s',(i,name))
                            a=cursor.fetchall()
                            a=a[0]
                            for x in a:
                                id=x
                            cadd=input("Enter Your City Address: ")
                            hadd=input("Enter Your Home Address: ")
                            hom=input("Enter Your House No: ")
                            amt=int(input("Enter Ammount To Pay: "))
                            co=input("Are You Sure?(yes/no): ")
                            if co=='yes' or co=='Yes':
                                cursor.execute("update water set Ammount_Paid=%s where id=%s",(amt,id))
                                db.commit()
                                q='insert into water values(%s,%s,%s,%s,%s,curdate())'
                                value=(id,cadd,hadd,hom,amt)
                                cursor.execute(q,value)
                                db.commit()
                                while True:
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    print(color.GREEN+ "   Water Bill Successfully Paid" +color.END)
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    break
                            else:
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                print(color.GREEN+ "   Transcation Cancel" +color.END)
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        elif opt==3:
                            cursor.execute('select sno from customers where sno=%s and username=%s',(i,name))
                            a=cursor.fetchall()
                            a=a[0]
                            for x in a:
                                id=x
                            isp=input("Enter Your ISP Name: ")
                            usr=input("Enter Your Username: ")
                            amt=int(input("Enter Ammount To Pay: "))
                            co=input("Are You Sure?(yes/no): ")
                            if co=='yes' or co=='Yes':
                                cursor.execute("update internet set Ammount_Paid=%s where id=%s",(amt,id))
                                db.commit()
                                q='insert into internet values(%s,%s,%s,%s,curdate())'
                                value=(id,isp,usr,amt)
                                cursor.execute(q,value)
                                db.commit()
                                while True:
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    print(color.GREEN+ "   Internet Bill Successfully Paid" +color.END)
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    break
                            else:
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                print(color.GREEN+ "   Transcation Cancel" +color.END)
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        elif opt==4:
                            cursor.execute('select sno from customers where sno=%s and username=%s',(i,name))
                            a=cursor.fetchall()
                            a=a[0]
                            for x in a:
                                id=x
                            land=input("Enter Your Landline Phone Number: ")
                            amt=int(input("Enter Ammount To Pay: "))
                            co=input("Are You Sure?(yes/no): ")
                            if co=='yes' or co=='Yes':
                                cursor.execute("update landline set Ammount_Paid=%s where id=%s",(amt,id))
                                db.commit()
                                q='insert into landline values(%s,%s,%s,curdate())'
                                value=(id,land,amt)
                                cursor.execute(q,value)
                                db.commit()
                                while True:
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    print(color.GREEN+ "  LandLine Phone Bill Successfully Paid" +color.END)
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    break
                            else:
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                print(color.GREEN+ "   Transcation Cancel" +color.END)
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        elif opt==5:
                            cursor.execute('select sno from customers where sno=%s and username=%s',(i,name))
                            a=cursor.fetchall()
                            a=a[0]
                            for x in a:
                                id=x
                            sbn=input("Enter Your Setup Box Number: ")
                            hadd=input("Enter Your Home Address: ")
                            hom=input("Enter Your House No: ")
                            amt=int(input("Enter Ammount To Pay: "))
                            co=input("Are You Sure?(yes/no): ")
                            if co=='yes' or co=='Yes':
                                cursor.execute("update tv set Ammount_Paid=%s where id=%s",(amt,id))
                                db.commit()
                                q='insert into tv values(%s,%s,%s,%s,%s,curdate())'
                                value=(id,sbn,hadd,hom,amt)
                                cursor.execute(q,value)
                                db.commit()
                                while True:
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    print(color.GREEN+ "  TV Bill Successfully Paid" +color.END)
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    break
                            else:
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                print(color.GREEN+ "   Transcation Cancel" +color.END)
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        elif opt==6:
                            cursor.execute('select sno from customers where sno=%s and username=%s',(i,name))
                            a=cursor.fetchall()
                            a=a[0]
                            for x in a:
                                id=x
                            spn=input("Enter Your Sim-Card Company Name: ")
                            pn=input("Enter Your Phone Number: ")
                            amt=int(input("Enter Ammount To Recharge: "))
                            co=input("Are You Sure?(yes/no): ")
                            if co=='yes' or co=='Yes':
                                cursor.execute("update recharge set Ammount_Paid=%s where id=%s",(amt,id))
                                db.commit()
                                q='insert into recharge values(%s,%s,%s,%s,curdate())'
                                value=(id,spn,pn,amt)
                                cursor.execute(q,value)
                                db.commit()
                                while True:
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    print(color.GREEN+ "  Phone Successfully Recharge" +color.END)
                                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                    break
                            else:
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                                print(color.GREEN+ "   Transcation Cancel" +color.END)
                                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        elif opt==7:
                            ch==6
                    
                        else:
                            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                            print(color.GREEN+ "   Provide Valid Information" +color.END)
                            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)  
                    elif ch==7:
                        break
                    else:
                        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                        print("Wrong Option ")
                        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)

        interface()
    elif choice==2:
        q='select count(*) from customers'
        cursor.execute(q)
        a=cursor.fetchall()
        a=a[0]
        for x in a:
            sno=x
        sno+=1
        print('Fill these details to register your account ')
        name=input("Enter your name :- ")
        username=input('Enter your username :- ')
        pas=input('Enter your password :- ')
        balance=float(input('Enter your balance :- '))
        DOB=input('Enter your DOB(YYYY-MM-DD in A.D) :- ')
        gender=input('Enter your gender (M/F) :- ')
        contact=int(input("Enter Contact Number:- "))
        addr=input("Enter City address:- ")
        addr2=input("Enter Street address:-")
        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
        kyc='false'
        query="insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value=(sno,name,username,pas,balance,DOB,gender,kyc,contact,addr,addr2)
        cursor.execute(query,value)
        while True:
            print("You have Succesfully Registered an account. Now You can Login")
            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            break
        db.commit()
    
    elif choice==3:
        us=input("Enter your username :- ")
        p=int(input("Enter your password :-"))
        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
        value=(us,p)
        query="select * from customers where username=%s and pas=%s"
        cursor.execute(query,value)
        data_login=cursor.fetchall()
        cursor.execute('delete from customers where sno=%s and username=%s',(data_login[0][0],data_login[0][2]))
        while True:
            print("Account Succesfully Deleted.")
            print("Now say Goodbye to all your money because it is ours Now.")
            print("Thank You")
            break
        db.commit()
    elif choice==4:
        bug=input("Describe Your Problem in more than 30 characters: ")
        error=len(bug)
        if error>30:
            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            print("Thanks for Your Help. We will look at your problem, if there is bug we will fix it as soon as possible.Stay Tuned")
        else:
            print("You have to describe your problem in more than 30 Characters. so that it will be easier for us to fix the problem")
        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
    elif choice==5:
        print(color.CYAN+ "what do you rate our project?")
        print("1- Bad")
        print("2- Good")
        print("3- Very Good")
        print("4- Excellent")
        print("5- Outstanding")
        print("6- Extra-Oridinary" +color.END)
        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
        fb=int(input("Option:- "))
        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
        if fb<7:
            print("Thanks for You Feedback!!!")
            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
        else:
            print("please Submit a Valid Feedback")
            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
    elif choice==6:
        print(color.YELLOW+ "Welcome to Hackers Bank")
        print("Developed by 3 Humans on Earth: Manjit, Banty & Santosh")
        print("All Rights Reserved® Copyright© 2020-2021" +color.END)
    elif choice==7:
        print(color.PURPLE+ 'You are up to date. Current Version 7.5.3' +color.END)
    elif choice==75321:
        while True: 
            print(color.YELLOW+ '      ACCESS GRANTED AS ADMIN' +color.END)
            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            print(color.CYAN+ 'Press 1 to see the creating table codes' )
            print('Press 2 to see the total ammount of money in bank')
            print('Press 3 to see the no. of peoples who have created an account')
            print('Press 4 to see the no. of males')
            print('Press 5 to see the no. of females')
            print('Press 6 to log out' +color.END)
            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            op=int(input('OPTION: '))
            print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            if op==1:
                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
                print('''create table customers(sno int(100) primary key auto_increment,
                name varchar(100),
                username varchar(100),
                pas varchar(100),
                balance varchar(100),
                age varchar(100),
                gender varchar(100),
                kyc varchar(100))''')
                print('''create table ele(id int(100),
                city_address varchar(255),
                home_address varchar(255),
                house_no varchar(255),
                ammount_paid varchar(255),
                paid_on date)''')
                print('''create table internet(id int(100),
                ISP_Name varchar(255),
                username varchar(255),
                ammount_paid varchar(255),
                paid_on date''')
                print('''create table landline(id int(100),
                phone_no int(255),
                ammount_paid varchar(255),
                paid_on date)''')
                print('''create table recharge(id int(100),
                sim_card varchar(255),
                phone_no varchar(255),
                ammount_paid varchar(255),
                paid_on date)''')
                print('''create table tv(id int(100),
                setupbox_no varchar(255),
                home_address varchar(255),
                house_no varchar(255),
                ammount_paid varchar(255),
                paid_on date)''')
                print('''create table water(id int(100),
                city_address varchar(255),
                home_address varchar(255),
                house_no varchar(255),
                ammount_paid varchar(255),
                paid_on date)''')
                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            elif op==2:
                cursor.execute('select sum(balance) from customers')
                sum=cursor.fetchall()
                sum=sum[0]
                for row in sum:
                    print("Total Balance: ",row)
                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            elif op==3:
                cursor.execute('select count(sno) from customers')
                count=cursor.fetchall()
                count=count[0]
                for row in count:
                    print('Total No of Peoples: ',row)
                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            elif op==4:
                cursor.execute("select count(gender) from customers where gender='m'")
                g=cursor.fetchall()
                g=g[0]
                for row in g:
                    print('Total No of Male: ',row)
                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            elif op==5:
                cursor.execute("select count(gender) from customers where gender='f'")
                g=cursor.fetchall()
                g=g[0]
                for row in g:
                    print('Total No of Male: ',row)
                    print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
            elif op==6:
                break
            else:
                print("Please provide valid information")
                print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
    else:
        print('           Wrong Option')
        print(color.RED+ '<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>' +color.END)
        break    
db.close()