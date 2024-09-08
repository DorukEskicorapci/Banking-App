import sqlite3
from sqlcommands import dbfunctions


def useraccess(cursor, IDinput, userinput, passwordinput):
    check = dbfunctions.checkinput(cursor, IDinput, userinput, passwordinput)

    if check == True:
        print('User Access Granted' + '\n')
    else:
        print('User Access Denied' + '\n' + 'Redirecting to main menu')
        driver(cursor, sqliteConnection)
            
        
    print('1. View your balance' + '\n' + '2. View your transaction history' + '\n' + '3. Make new transaction' + '\n' + '4. Delete your account')
    nextstep = int(input('What do you want to do: '))
    print()

    if nextstep == 1:
        dbfunctions.balance_return(cursor, IDinput, userinput, passwordinput)
        print('Your balance is:', dbfunctions.balance_return(cursor, IDinput, userinput, passwordinput))
    elif nextstep == 2:
        
        dbfunctions.select_transaction(cursor, 'TransactionHistory', IDinput)

        filecontrol = open("printfile.txt", "a")
        filecontrol.write("\n"+ "Transaction history (UserID, Company Name, Cost):\n")
        cursor.execute('''SELECT UserID, CompanyName, Cost FROM {} WHERE UserID = ?'''.format('TransactionHistory'), (IDinput,))
        for row in cursor:
            filecontrol.write(str(row))

        print()
        print('Transaction history printed to printfile.txt')
            
        
        
        filecontrol.close()

    elif nextstep == 3:
        askcompany = input('Enter the company name: ')
        askcost = int(input('Enter the cost: '))
        print()
        dbfunctions.insertTransaction(cursor, 'TransactionHistory', IDinput, askcompany, askcost)
        balance = dbfunctions.balance_return(cursor, IDinput, userinput, passwordinput) - askcost
            
        print("Your balance after the transaction is:", balance)
            
        #Update the balance
        dbfunctions.updateCustomer(cursor, IDinput, balance)
        print("Transaction successful" + '\n')
        
        filecontrol = open("printfile.txt", "a")
        
        filecontrol.write("Transaction successful" + '\n' + 'Company: ' + askcompany + '\n' + 'Cost: ' + str(askcost) + '\n' + 'Balance: ' + str(balance) + '\n' + '\n')

    elif nextstep == 4:
        dbfunctions.deleteCustomer(cursor, IDinput)
        print('Account deleted successfully!')

def driver(cursor, sqliteConnection):
    try:

        
        print()
        print('1. Log in' + '\n' + '2. Sign up')
        Option1 = input('Type 1 or 2: ')
        print()
        
        if Option1 == '1':
            IDinput = input('Enter your ID: ')
            userinput = input('Enter your name: ')
            passwordinput = input('Enter your password: ')
            useraccess(cursor, IDinput, userinput, passwordinput)
        elif Option1 == '2':
            userinput = input('Enter a name: ')
            passwordinput = input('Enter a password: ')
            balanceinput = input('Enter the balance you want to deposit: ')
            dbfunctions.insertCustomer(cursor, 'Customers', userinput, passwordinput, balanceinput)
            dbfunctions.insertTransaction(cursor, 'TransactionHistory', dbfunctions.idreturn(cursor, userinput, passwordinput), 'null', balanceinput)
            print('Account created successfully!')
            print('Your ID is:', dbfunctions.idreturn(cursor, userinput, passwordinput))


        sqliteConnection.commit()

        
        sqliteConnection.commit()
        # Close the cursor
        
 
    # Handle errors
    except sqlite3.Error as error:
        print('Error occurred;', error )
    

sqliteConnection = sqlite3.connect('database.db')
cursor = sqliteConnection.cursor()
print('Database initialization successful' + '\n')


driver(cursor, sqliteConnection)
ask = input('Do you want to continue? (Y/N): ')
while ask == 'Y' or ask == 'y' or ask == 'yes' or ask == 'Yes' or ask == 'YES':
    driver(cursor, sqliteConnection)
    print()
    ask = input('Do you want to continue? (Y/N): ')

cursor.close()

if sqliteConnection:
    sqliteConnection.close()
    print('Database connection closed')

    

        #filecontrol = open("demofile.txt", "a")
        
        #filecontrol.write(dbfunctions.return_select(cursor))
 
    '''
        dbfunctions.insert(cursor, 'John Doe', 50, 100)
        

        f = open("demofile3.txt", "w")
        f.write("Woops! I have deleted the content!")
        f.close()

        "x" - Create - will create a file, returns an error if the file exist

        "a" - Append - will create a file if the specified file does not exist

        "w" - Write - will create a file if the specified file does not exist

        "a" - Append - will append to the end of the file

        "w" - Write - will overwrite any existing content
        '''
