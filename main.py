import sqlite3
from sqlcommands import dbfunctions



def driver():
    try:

        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print('Database initialization successful')
        
        dbfunctions.insert(cursor, 'Doruk', 'sifre', 50, 100)

        filecontrol = open("demofile.txt", "a")
        
        filecontrol.write(dbfunctions.return_select(cursor))
        dbfunctions.select(cursor)

        IDinput = int(input('Enter a ID: '))
        userinput = input('Enter a name: ')
        passwordinput = input('Enter a password: ')

        check = dbfunctions.checkinput(cursor, IDinput, userinput, passwordinput)

        if check == True:
            print('User Access Granted')
            dbfunctions.balance_return(cursor, IDinput, userinput, passwordinput)
                  

        
        



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

        sqliteConnection.commit()
        # Close the cursor
        cursor.close()

        if sqliteConnection:
            sqliteConnection.close()
            print('Database connection closed')
 
    # Handle errors
    except sqlite3.Error as error:
        print('Error occurred;', error )
    

driver()