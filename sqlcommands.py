import sqlite3

class dbfunctions:
    def insert(cursor, name, password, cost, afterbalance):
        
        cursor.execute('''INSERT INTO BillingHistory (Name, Password, Cost, AfterBalance) VALUES(?, ?, ?,?)''', (name, password, cost, afterbalance))
        
    
    def select(cursor):

        cursor.execute('''SELECT * FROM BillingHistory''')
        for row in cursor:
            print(row)

    def return_select(cursor):
        printc = ''
        cursor.execute('''SELECT * FROM BillingHistory''')
        for row in cursor:
            printc += str(row)
        return printc
    
    def checkinput(cursor, IDinput, userinput, passwordinput):
        checkname = False
        checkpassword = False
        checkid = False
        check = False
        cursor.execute('''SELECT * FROM BillingHistory WHERE TransactionID = ? AND Name = ? AND Password = ?''', (IDinput, userinput, passwordinput))
        
        for row in cursor:
            if row[0] == IDinput and row[1] == userinput and row[2] == passwordinput:
                check = True
        return check

    def balance_return(cursor, IDinput, userinput, passwordinput):
        cursor.execute('''SELECT AfterBalance FROM BillingHistory WHERE TransactionID = ? AND Name = ? AND Password = ?''', (IDinput, userinput, passwordinput))
        result = cursor.fetchone()
        if result:
            print('Dear', userinput, 'your balance after the transaction is:', result[0])

        else:
            print('No matching record found')