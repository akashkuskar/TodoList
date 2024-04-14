

# This function is about Getting user input and validating the input
def starting():
    print("\n Choose one of the Following Option:"
      "\n1: for ADD the Task."
      "\n2: for SHOW the Task."
      "\n3: for DELETE the Task.\n")
    num=input("Enter the choice of Task You want to Perform:\n")
    try:
        num=int(num)
        if(num>0 and num<4):
            print("Task Accepted...!")
        else:
            print("Enter the Correct Choice of Task!")
    except:
        print("You entere Invalid Choice of Task!")
    return num

# switch case statement is not used in python so
# I used 'match' keyword which is used to match the argument of a function.
# Performing the tasks as per user input:
def switch(arg):
    match arg:
        case 1:
            print("\nEnter the task Name and task Description\n")
            name=str(input("\nEnter the task Name Here(Task name are always in String not Number) :"))
            desc=input("\nEnter the Description Here:")
            tasks.update({name:desc})
            print("Task Entered Successfully !\n")

        case 2:
            if (bool(tasks)):
                print("\n#  Tasks   # \nName: \t Description\n")
                for i,j in tasks.items():
                    print(i,":",j,"\n")
            else:
                print("No Tasks in Dictonary!\n")
                return  0

        case 3:
            if (bool(tasks)):
                print("Enter Task name you want to Delete:\n")
                n = str(input(""))
                if n in tasks:
                    tasks.pop(n)
                    print("Deleted Successfully !\n")

                else:
                    print("Invalid Task Name\n")
            else:
                print("Dictonary is Empty\n")
                return 0
        case _:
            return "Enter the valid choice: \n"

def getInput():
    a = input("\nTo Continue Press: c\t"
              "To End press: e\n")
    try:
        a = str(a)
        if(a=='c' or a=='e'):
            return a
        else:
            print("\n Invalid input...!\n")
    except:
        print("\nInvalid...!\n ")


print("\n\t\t\t\t#-->   Welcome to the To-Do-List Project   <--#\n"
      "Here You can ADD , SHOW and DELETE Your Daily Important Tasks as per Your requirement")
# Creating a dictonary for the tasks:
tasks=dict();

# Initializing the num variable
num = 0

a=0 #initializing the user input varibale a
# created a function which takes input and decide continue Running the App or Not
a=getInput()

while(a=='c'):
    num=starting()
    switch(num)
    a=getInput()
print("Thank You,Visit Again...!")
