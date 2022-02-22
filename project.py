#! /usr/bin/env python3 


import mysql.connector 
from time import sleep 
from sys import exit
#u = input("Enter username: ")
#p = input("Enter Password: ")
#
#try:
#     mydb = mysql.connector.connect(
#            host = "localhost" , 
#            user = u , 
#            password = p
#       )
#except Exception: 
#    print("Username or password incorrect")
#    


mydb = mysql.connector.connect(
        host = "localhost",
        user = "zeus",
        password = "zeus"
    )

mycursor = mydb.cursor() 
mycursor.execute("create database if not exists Impact_of_covid_on_airlines") 
print("Creating Database .....")


mydb = mysql.connector.connect(
            host = "localhost" , 
            user = "zeus" , 
            password = "zeus",
            database = "Impact_of_covid_on_airlines"
        ) 

mycursor = mydb.cursor()  

def Table():
    mycursor.execute("""create table if not exists Airlines(Airline_company varchar(250) primary key,
    Revenue_in_billion_USD int not null,
    Passanger_carried_in_2020_in_millions int not null,
    Passenger_carried_before_2020_in_Millions_ int not null,
    Comments varchar(50)) """) 
    print("\ntable created")

def printTable():
    mycursor.execute("select * from Airlines")
    mytable = mycursor.fetchall()
    for item in mytable : 
        print(item)

def DescribeTable():
    mycursor.execute("describe Airlines") 
    for x in mycursor.fetchall():
        print(x)

def addTableDefaultValues():
    mycursor.execute("insert ignore into Airlines values('Qatar Airlines',1,32,29,'Better')")
    mycursor.execute("insert ignore into Airlines values('Lufthansa',13,36,50,'Better')")
    mycursor.execute("insert ignore into Airlines values('Emirates',3,1,58,'GREAT LOSS')")
    mycursor.execute("insert ignore into Airlines values('Singapore Airlines',3,7,10,'LOSS')")
    mycursor.execute("insert ignore into Airlines values('British Airways',7,11,4,'GREAT LOSS')")
    mycursor.execute("insert ignore into Airlines values('Qantas',1,4,8,'GREAT LOSS')")
    mycursor.execute("insert ignore into Airlines values('American Airline',8,95,925,'GREAT LOSS')")
    mycursor.execute("insert ignore into Airlines values('Air Canada',4,13,51,'GREAT LOSS')")
    mycursor.execute("insert ignore into Airlines values('Air India',4,7,144,'GREAT LOSS')")
    mycursor.execute("insert ignore into Airlines values('Air France',13,6,104,'GREAT LOSS')")
    mycursor.execute("insert ignore into Airlines values('Japan Airlines',2,1,23,'GREAT LOSS')")
    mycursor.execute("insert ignore into Airlines values('KLM Royal Dutch Airlines',13,11,35,'LOSS')")
    mydb.commit()

"""COMMENTS : European airline economy increased but airline economy of countries like US, India, Canada suffered great losses """


def DeleteRecord() :
    x = int(input("How many entries to delete ? (enter -1 to exit) : "))
    temp  = 0 
    while (x > temp):
        inp = input("Enter Company name(type exit to quit): ")
        mycursor.execute("DELETE FROM Airlines WHERE Airline_company = '{}'".format(inp))
        temp += 1 

def SortTable():
    print("""
1. Sort and print companies alphabatically (ascending)
2. Sort and print companies alphabetically (descending)
3. Sort and print revenue (ascending)
4. Sort and print revenue (descending)
""")
    a = int(input("\nOption: "))

    if (a == 1) : 
        mycursor.execute("select * from Airlines order by Airline_company")
        for i in mycursor: 
            print(i)
    elif (a == 2) : 
        mycursor.execute("select * from Airlines order by Airline_company desc")
        for i in mycursor: 
            print(i)
    elif (a == 3) : 
        mycursor.execute("select * from Airlines order by Revenue_in_billion_USD")
        for i in mycursor: 
            print(i)
    elif (a == 4) : 
        mycursor.execute("select * from Airlines order by Revenue_in_billion_USD desc")
        for i in mycursor: 
            print(i)
    

def groupBy():
    print("""
1.  Average tourists in 2020 
2.  Average tourists before 2020
3.  Minimim tourist for 2020
4.  Maximum tourist for 2020 
5.  Minimum tourist before 2020
6.  Maximum tourist before 2020
7.  Average revenue in billions 
8.  print countries which have more than 'x' revenue 
9.  print countries which have less than 'x' revenue 
10. Go back
""")

    a = int(input("\nOption: "))

    # average 
    if (a==1): 
        command = "select AVG(Passanger_carried_in_2020_in_millions) AS average from Airlines"
        mycursor.execute(command) 
        rows = mycursor.fetchall()
        for i in rows: 
            print("\nAverage tourists in 2020 (in million): "+str(i[0]))
    elif (a==2): 
        command = "select AVG(Passenger_carried_before_2020_in_Millions_) AS average from Airlines"
        mycursor.execute(command) 
        rows = mycursor.fetchall()
        for i in rows: 
            print("\nAverage tourists before 2020 (in million): "+str(i[0]))

    # min max for 2020

    elif (a==3):
        command = "select MIN(Passanger_carried_in_2020_in_millions) from Airlines"
        mycursor.execute(command)
        rows = mycursor.fetchall()
        for i in rows:
            print("\nMinimum tourists for 2020 (in million): "+str(i[0]))

    elif (a==4):
        command = "select MAX(Passanger_carried_in_2020_in_millions) from Airlines"
        mycursor.execute(command)
        rows = mycursor.fetchall()
        for i in rows:
            print("\nMaximum tourists for 2020 (in million): "+str(i[0]))
    

    # min max before 2020

    elif (a==5):
        command = "select MIN(Passenger_carried_before_2020_in_Millions_) from Airlines"
        mycursor.execute(command)
        rows = mycursor.fetchall()
        for i in rows:
            print("\nMinimum tourists before 2020 (in million): "+str(i[0]))
    elif (a==6):
        command = "select MAX(Passanger_carried_in_2020_in_millions) from Airlines"
        mycursor.execute(command)
        rows = mycursor.fetchall()
        for i in rows:
            print("\nMaximum tourists before 2020 (in million): "+str(i[0]))

    # average revenue
    elif (a==7): 
        command = "select AVG(Revenue_in_billion_USD) from Airlines"
        mycursor.execute(command) 
        rows = mycursor.fetchall()
        for i in rows: 
            print("\nAverage revenue (in billion): "+str(i[0]))

    elif (a==8):
        x = input("Revenue : ")
        command = "select * from Airlines where Revenue_in_billion_USD > {}".format(x)
        mycursor.execute(command) 
        rows = mycursor.fetchall()
        for i in rows: 
            print("\nCountries are: "+str(i[0]))
    elif (a==9):
        x = input("Revenue : ")
        command = "select * from Airlines where Revenue_in_billion_USD < {}".format(x)
        mycursor.execute(command) 
        rows = mycursor.fetchall()
        for i in rows: 
            print("\nCountries are: "+str(i[0]))



def TableMenu():
    while True : 
        Table()
        addTableDefaultValues()
        print("\t----Table Menu----\n")
        print("""
1. Describe table 
2. print table 
3. add custom values to table
4. Delete a company record 
5. Sort table 
6. aggregate functions and group by (and misc.)
7. go back
    """)
        a = int(input("\n")) 
        if (a == 1): DescribeTable()
        elif (a == 2) : printTable() 
        elif (a == 3) : insertRecord()
        elif (a == 4) : DeleteRecord() 
        elif (a == 5) : SortTable()
        elif (a == 6) : groupBy()
        elif (a == 7) : DatabaseMenu()    

def insertRecord():
    x = 0  
    n = int(input("Number of items to add: "))
    while (x<n):
        company = input("Airline company: ")
        revenue = int(input("Revenue: "))
        passengerCarried = int(input("Passenger in 2020: "))
        passengerBefore = int(input("Passanger before: "))
        comment = input("Comments(if any): ")
        mycursor.execute("insert ignore into Airlines values('"+company+"','"+str(revenue)+"','"+str(passengerCarried)+"','"+str(passengerBefore)+"','"+comment+"')")
        mydb.commit()   
        x+=1 ; 

def searchInTable_name(a:str):
    nm=input("enter name: ")
    mycursor.execute("select * from student where name='"+nm+"'")
    for x in mycursor:
        print(x)

def showDatabases():
    print("\n")
    mycursor.execute("show databases")
    for database in mycursor:
        print(database) 


def DatabaseMenu():
    while True : 
        print("\t-----Database Menu-----")
        print("""
1. Show Databases 
2. Table menu 
3. exit 
""")
        a = int(input("\nOption: \n\n" ))
        if (a == 1): showDatabases()
        elif (a == 2) : TableMenu() 
        elif (a==3) : 
            print("Bye!") 
            exit(0)
            break 

def main():
    DatabaseMenu() 


if __name__=='__main__':
    main()
        
