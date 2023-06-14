import datetime
import random
import calendar
import pytz

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_current_time()
        elif choice == "2":
            display_unix_time()
        elif choice == "3":
            convert_string_to_datetime()
        elif choice == "4":
            check_leap_year()
        elif choice == "5":
            extract_units_from_timedelta()
        elif choice == "6":
            print_calendar()
        elif choice == "7":
            display_time_in_different_timezones()
        elif choice == "8":
            display_opposite_end_of_the_world()
        elif choice == "9":
            display_random_joke()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    menu = [
        "================Menu:===============",
        "1. Display current time",
        "2. Display current time in UNIX format",
        "3. Convert string to datetime",
        "4. Check leap year and time until next leap year",
        "5. Extract units from timedelta",
        "6. Print calendar",
        "7. Display current time in different time zones",
        "8. Display time at the opposite end of the world",
        "9. Random joke",
        "0. Exit"
    ]
    print("\n".join(menu))

def display_current_time():
    current_time = datetime.datetime.now()
    print(f"Current time: {current_time}")

def display_unix_time():
    current_time = datetime.datetime.now()
    unix_time = int(current_time.timestamp())
    print(f"Current time (UNIX format): {unix_time}")

def convert_string_to_datetime():
    user_input = input("Enter a date and time (e.g., '2023-06-13 12:30'): ")
    try:
        datetime_obj = datetime.datetime.strptime(user_input, "%Y-%m-%d %H:%M")
        print(f"Converted datetime: {datetime_obj}")
    except ValueError:
        print("Invalid format. Please try again.")

def check_leap_year():
    current_year = datetime.datetime.now().year
    is_leap_year = calendar.isleap(current_year)

    if is_leap_year:
        print(f"{current_year} is a leap year.")
    else:
        next_leap_year = next(year for year in range(current_year+1, current_year+5) if calendar.isleap(year))
        time_until_next_leap_year = datetime.datetime(next_leap_year, 1, 1) - datetime.datetime.now()
        print(f"{current_year} is not a leap year.")
        print(f"Time until next leap year: {time_until_next_leap_year}")

def extract_units_from_timedelta():
    time_delta = datetime.timedelta(days=5, hours=3, minutes=15)
    choices = {
        "1": ("Seconds:", time_delta.total_seconds()),
        "2": ("Days:", time_delta.days),
        "3": ("Years:", time_delta.days // 365)
    }
    choice = input("Which unit to display? (1. seconds, 2. days, 3. years): ")

    unit, value = choices.get(choice, ("Invalid choice.", None))
    print(f"{unit} {value}" if value is not None else unit)

#-------------------------Sergii
def print_calendar():
    year, month = map(int, input("Enter the year and month (e.g., '2023 6'): ").split())
    calendar_obj = calendar.monthcalendar(year, month)
    
    # Print month and year
    print(calendar.month_name[month], year)
    
    # Print weekday names
    print("Mon Tue Wed Thu Fri Sat Sun")
    
    # Print calendar days
    for week in calendar_obj:
        for day in week:
            if day != 0:
                print(str(day).rjust(3), end=" ")
            else:
                print("   ", end=" ")
        print()
#----------------------------------

def display_time_in_different_timezones():
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

def display_opposite_end_of_the_world():
    current_time = datetime.datetime.now()
    opposite_time = current_time + datetime.timedelta(hours=12)
    print(f"Current time: {current_time}")
    print(f"Opposite end of the world time: {opposite_time}")

def display_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I got a job at a bakery because I kneaded dough.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I used to be a baker, but I couldn't make enough dough.",
        "What did the grape say when it got stepped on? Nothing, it just let out a little wine."
    ]

    print(f"Random Joke:\n{random.choice(jokes)}")

if __name__ == "__main__":
    main()
