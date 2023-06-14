from datetime import datetime 
#creating a menu for each input option
def display_menu():
    print("MENU:")
    print("1) Display current time : ")
    print("2) Display current time in Unix format: ")
    print("3) Display the converted string into a dt object: ")
    print("4) Check if the year is a leap year: ")
    print("5) ") 
#defining a function for each task  
def user_choice():
    choice = input ("Enter your choice: ")
    return choice


def current_time():

    current_time = datetime.now()
    formatted_time= current_time.strftime("%H:%M:%S %p")
    print("The time is :" , formatted_time)
    

def unix_format():
    
    current_time = datetime.now()
    given_date = current_time.strftime("%m/%d/%Y, %H:%M:%S")
    formatted_date = datetime.strptime(given_date,"%m/%d/%Y, %H:%M:%S")
    unix_timestamp = datetime.timestamp(formatted_date)
    print("The Unix timestamp for the current date is:", unix_timestamp)
    
#adding a while loop to repeats the block of code
while True:
    display_menu()
    choice = user_choice()
    if choice == "1":
        current_time()
        
    elif choice == "2":
        unix_format()
        
    else :
        print("Finished!")