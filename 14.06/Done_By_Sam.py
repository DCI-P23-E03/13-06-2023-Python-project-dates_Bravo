import random
import datetime

# Collection of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What's the best time to go to the dentist? Tooth-hurty!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "How do you organize a space party? You planet!"
]

# Function to output a random joke
def tell_joke():
    random_joke = random.choice(jokes)
    print(random_joke)

# Additional surprise feature
def surprise(birthday):
    # Check if it's April 1st
    if birthday.month == 4 and birthday.day == 1:
        print("April Fools' Day Surprise: You've been pranked!")
    else:
        print("Sorry, no surprise for you today.")

# Prompt the user to enter their birthday
birthday_str = input("Enter your birthday (e.g:YYYY-04-01): ")
year, month, day = map(int, birthday_str.split("-"))
birthday = datetime.date(year, month, day)

# Call the functions
tell_joke()
surprise(birthday)
