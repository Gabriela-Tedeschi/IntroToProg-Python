# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created/started script
# GTedeschi, 8/07/21, Added code for steps 1-4
# GTedeschi, 8/08/21, Finished adding code for assignment 05
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstRow = []  # A row of data - used as bridge for data between file and dicRow
lstTable = []  # A list that acts as a 'table' of rows
# strMenu = ""  # A menu of user options - don't think this is used
strChoice = ""  # A Capture the user option selection
addtask = ""  # Captures new task user inputs
addpriority = ""  # Captures priority of new task user inputs


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for item in lstTable:
            print(item["Task"] + ", " + item["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        addtask = input("Enter a task: ")
        addpriority = input("Enter its priority (low, medium, high): ")
        dicRow = {"Task": addtask, "Priority": addpriority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        lstTable.remove({"Task": addtask, "Priority": addpriority})
        print("Last task added was removed.")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for item in lstTable:
            objFile.write(item["Task"] + ", " + item["Priority"] + "\n")
        objFile.close()
        print("Data saved to file.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Press any key to exit the program. ")
        break  # and Exit the program
