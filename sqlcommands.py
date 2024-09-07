import sqlite3

class dbfunctions:
    def insertCustomer(cursor, table, name, password, balance):
            
        cursor.execute('''INSERT INTO {} (Name, Password, Balance) VALUES(?, ?, ?)'''.format(table), (name, password, balance))
    
    def insertTransaction(cursor, table, UserID, CompanyName, Cost):
            
        cursor.execute('''INSERT INTO {} (UserID, CompanyName, Cost) VALUES(?, ?, ?)'''.format(table), (UserID, CompanyName, Cost))
        
    def updateCustomer(cursor, CustomerID, balance):   
        cursor.execute('''UPDATE Customers SET Balance = ? WHERE CustomerID = ?''', (balance, CustomerID)) 

    def select(cursor, table):

        cursor.execute('''SELECT * FROM {}'''.format(table))
        for row in cursor:
            print(row)

    def return_select(cursor):
        printc = ''
        cursor.execute('''SELECT * FROM Customers''')
        for row in cursor:
            printc += str(row)
        return printc
    
    def checkinput(cursor, IDinput, userinput, passwordinput):
        checkname = False
        checkpassword = False
        checkid = False
        check = False
        cursor.execute('''SELECT * FROM Customers WHERE CustomerID = ? AND Name = ? AND Password = ?''', (IDinput, userinput, passwordinput))
        
        for row in cursor:
            if row[0] == IDinput and row[1] == userinput and row[2] == passwordinput:
                check = True
        return check

    def balance_return(cursor, IDinput, userinput, passwordinput):
        cursor.execute('''SELECT Balance FROM Customers WHERE CustomerID = ? AND Name = ? AND Password = ?''', (IDinput, userinput, passwordinput))
        result = cursor.fetchone()
        if result:
            #print('Dear', userinput, 'your balance after the transaction is:', result[0])
            return result[0]
            #print('Dear', userinput, 'your balance is:', result[0])

        else:
            print('No matching record found')