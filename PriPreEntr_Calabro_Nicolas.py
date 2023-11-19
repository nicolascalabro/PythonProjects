import json

option = ""

def register():
    username = input("Enter your username: ")
    if username in database:
        print("Username not available")
    else:
        password = input("Username available. Please set your password: ")
        database.update({username: password})
        print("Username has been created successfully")
        
        database_json = json.dumps(database)

        fd = open("dataBase.txt", "w")
        fd.write(database_json)
        fd.close()
    return

def login():
    username = input("Enter your username: ")
    value = database.get(username,0)    #0 = key doesn't exist
    if value == 0:
        print("Username doesn't exist")  
    else:
        password = input("Valid username. Please enter your password: ")
        if password == value:
            print("Login successfully")
        else:
            print("Incorrect password")      
    return        

def seeDataBase(flag):
    try:
        fd = open("dataBase.txt", "r")
    except FileNotFoundError:        
        fd = open("dataBase.txt", "w")
        print("Database has been created")
        emptyDatabase = {}
        emptyDatabase_json = json.dumps(emptyDatabase)
        fd.write(emptyDatabase_json)
        fd.close()
        return emptyDatabase 
    database_json = fd.read()
    fd.close()
    database = json.loads(database_json)
    if flag != 0:
        print(database)
    return database

database = seeDataBase(flag=0) #read file for the first time: update the dictionary with previous information or create an empty database

#---------------------------------Main---------------------------------
while option != "4":
    option = input("Menu: 1-Register  2-Log In  3-See Database  4-Exit ")
    if option == "1":
        register()
    elif option == "2":
        login()
    elif option == "3":
        database = seeDataBase(flag=1)    
print("End")   