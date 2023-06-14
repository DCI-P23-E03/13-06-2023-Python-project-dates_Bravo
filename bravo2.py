import datetime
import time
import pytz
import random
import calendar

# Task 0: Show a simple menu
def show_menu():
    print("========================Menu:")
    print("1. Display current time")
    print("2. Display current time in UNIX format")
    print("3. Convert string to datetime")
    print("4. Check leap year and time until next leap year")
    print("5. Output timedelta object with options")
    print("6. Print calendar")
    print("7. Display current time in different time zones")
    print("8. Display time at the opposite end of the world")
    print("9. Output random joke")
    print("10. Surprise feature")
    print("0. Exit")

# Task 1: Display current time
def display_current_time():
    current_time = datetime.datetime.now()
    print("Current time:", current_time)

# Task 2: Display current time in UNIX format
def display_current_time_unix():
    current_time_unix = int(time.time())
    print("Current time in UNIX format:", current_time_unix)

# Task 3: Convert string to datetime
def convert_string_to_datetime():
    user_input = input("Enter a date and time (e.g., '2023-06-13 12:30'): ")
    datetime_format = "%Y-%m-%d %H:%M"
    if datetime.datetime.strptime(user_input, datetime_format):
        datetime_obj = datetime.datetime.strptime(user_input, datetime_format)
        print(f"Converted datetime: {datetime_obj}")
    else:
        print("Invalid format. Please try again.")

# Task 4: Check leap year and time until next leap year
def check_leap_year():
    current_year = datetime.datetime.now().year
    if calendar.isleap(current_year):
        print(f"{current_year} is a leap year")
    else:
        print(f"{current_year} is not a leap year")
    
    next_leap_year = current_year
    while not calendar.isleap(next_leap_year):
        next_leap_year += 1
    time_until_next_leap_year = datetime.datetime(next_leap_year, 1, 1) - datetime.datetime.now()
    print("Time until next leap year:", time_until_next_leap_year)

# Task 5: Output timedelta object with options
def output_timedelta():
    time_delta = datetime.timedelta(days=5, hours=3, minutes=15)
    choices = {
        "1": ("Seconds:", time_delta.total_seconds()),
        "2": ("Days:", time_delta.days),
        "3": ("Years:", time_delta.days // 365)
    }
    choice = input("Which unit to display? (1. seconds, 2. days, 3. years): ")
    unit, value = choices.get(choice, ("Invalid choice.", None))
    print(f"{unit} {value}" if value is not None else unit)

# Task 6: Print calendar
def print_calendar():
    print("Current month Calendar will be displayed or enter year and month: ")
    month = input("Month 'mm': ")
    year = input("Year 'yyyy': ")
    if month and year:
        print(calendar.month(int(year), int(month)))
    else:
        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year
        print(calendar.month(current_year, current_month))

# Task 7: Display current time in different time zones
def display_time_in_timezone():
    time_zones = {
        "1": "Europe/Dublin",
        "2": "America/Los_Angeles",
        "3": "Europe/Berlin",
        "4": "Africa/Johannesburg"
    }
    print("Select a timezone:")
    print("\n".join(f"{key}. {value}" for key, value in time_zones.items()))
    selected_timezone = time_zones.get(input("Enter your choice: "))
    if selected_timezone:
        current_time = datetime.datetime.now(pytz.timezone(selected_timezone))
        print(f"Current time in {selected_timezone}: {current_time}")
    else:
        print("Invalid choice.")

# Task 8: Display time at the opposite end of the world
def display_opposite_end_time():
    opposite_end_timezone = pytz.timezone('Pacific/Apia')
    current_time = datetime.datetime.now()
    opposite_end_time = current_time.astimezone(opposite_end_timezone)
    print("Current time:", current_time)
    print("Opposite end of the world time:", opposite_end_time)

# Task 9: Output random joke
def output_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why did the tomato turn red? Because it saw the salad dressing!"
    ]
    random_joke = random.choice(jokes)
    print("Random Joke:", random_joke)

# Task 10: Surprise feature
def surprise(birthday):
    # Check if it's April 1st
    if birthday.month == 4 and birthday.day == 1:
        print("April Fools' Day Surprise: You've been pranked!")
    else:
        print("Sorry, no surprise for you today.")

# Main program loop
while True:
    show_menu()
    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        display_current_time()
    elif user_choice == "2":
        display_current_time_unix()
    elif user_choice == "3":
        convert_string_to_datetime()
    elif user_choice == "4":
        check_leap_year()
    elif user_choice == "5":
        output_timedelta()
    elif user_choice == "6":
        print_calendar()
    elif user_choice == "7":
        display_time_in_timezone()
    elif user_choice == "8":
        display_opposite_end_time()
    elif user_choice == "9":
        output_random_joke()
    elif user_choice == "10":
        # Prompt the user to enter their birthday
        birthday_str = input("Enter your birthday (e.g: YYYY-MM-DD): ")
        if len(birthday_str) != 10:
            print("Invalid birthday format. Please try again.")
            continue
        try:
            birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()
            surprise(birthday)
        except ValueError:
            print("Invalid birthday format. Please try again.")
            continue
    elif user_choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
