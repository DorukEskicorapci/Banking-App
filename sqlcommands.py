import sqlite3

class dbfunctions:
    def insert(cursor, name, cost, afterbalance):
        
        cursor.execute('''INSERT INTO BillingHistory (Name, Cost, AfterBalance) VALUES(?, ?, ?)''', (name, cost, afterbalance))
        
    
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