import datetime
import pytz
import random

# Function to display current time in a specific timezone
def display_current_time(timezone):
    tz = pytz.timezone(timezone)
    current_time = datetime.datetime.now(tz)
    print("Current time in", timezone, ":", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# Function to calculate and display time at the opposite end of the world
def display_opposite_time(current_timezone):
    opposite_timezone = ""
    if current_timezone == "Asia/Tokyo":
        opposite_timezone = "America/Los_Angeles"
    elif current_timezone == "America/Los_Angeles":
        opposite_timezone = "Asia/Tokyo"
    elif current_timezone == "Europe/Dublin":
        opposite_timezone = "Africa/Johannesburg"
    elif current_timezone == "Africa/Johannesburg":
        opposite_timezone = "Europe/Dublin"
    elif current_timezone == "Europe/Berlin":
        opposite_timezone = "America/Los_Angeles"
    else:
        opposite_timezone = "Europe/Berlin"

    display_current_time(opposite_timezone)

# Function to display a random joke
def display_random_joke(jokes):
    random_joke = random.choice(jokes)
    print("\nRandom Joke:")
    print(random_joke)
    print()

# Additional surprise feature: Countdown Timer
def countdown_timer(end_date):
    while True:
        current_time = datetime.datetime.now()
        time_diff = end_date - current_time

        if time_diff.total_seconds() <= 0:
            print("Countdown Timer: Time's up!")
            break

        print("Countdown Timer:", time_diff)
        seconds = int(input("Enter the number of seconds to wait before checking again (0 to exit): "))

        if seconds == 0:
            print("Countdown Timer: Exiting.")
            break

        wait_time = datetime.timedelta(seconds=seconds)
        end_date -= wait_time

# Main program loop
def main():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I'm reading a book about anti-gravity. It's impossible to put down!"
    ]

    print("Welcome to the Multinational Team Program!")

    while True:
        print("\nPlease select an option:")
        print("1. Display current time in a specific timezone")
        print("2. Display time at the opposite end of the world")
        print("3. Display a random joke")
        print("4. Set a countdown timer")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            timezone = input("Enter the timezone (e.g., Asia/Tokyo): ")
            display_current_time(timezone)

        elif choice == "2":
            current_timezone = input("Enter your current timezone (e.g., Asia/Tokyo): ")
            display_opposite_time(current_timezone)

        elif choice == "3":
            display_random_joke(jokes)

        elif choice == "4":
            end_date_input = input("Enter the end date and time (YYYY-MM-DD HH:MM:SS): ")
            try:
                end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d %H:%M:%S")
                countdown_timer(end_date)
            except ValueError:
                print("Invalid date and time format. Please try again.")

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

