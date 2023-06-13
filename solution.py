
from datetime import datetime
import calendar
import pytz
import random

print("Hello, you are Welcome to the coolest Python-project, input 'Start' if you are ready to start: ")
if input().lower() == 'start':
    print("""Chose your option: 
          1. Display the current time
          2. Display the current time in UNIX format
          3. Check if this year is a leap year
          4. Calendar
          5. Check local time in opposite side of the world
          6. Joke time
          7. Interesting facts""")
    num = input()
    if num == '1':
        now_time = datetime.now()
        print(now_time.strftime("%X"))
    elif num == '2':
        now_time = datetime.now()
        unix = now_time.time()
        print(unix)

    elif num == '3':
        year = datetime.now().year
        if calendar.isleap(year):
            print("This year is a leap year")
        else:
            print("This year is not a leap year. Want to know when is next leap year? Input Yes or No ")
            user_in = input()
            if user_in.lower() == 'yes':
                leap = year
                while not calendar.isleap(leap):
                    leap += 1
                print(f"""Next leap year is:{leap}
                      If you would like to know how much if left in seconds input 's', in days- input 'd', in years- input 'y': """)
                user_in_delta = input()
                # delta count
                today = datetime.now().date()
                delta = datetime(leap, 1, 1).date() - today
                # output of delta in days years (days*hours*min*sec) and sec
                if user_in_delta.lower() == 'y':
                    years = delta.total_seconds() / (365 * 24 * 60 * 60)
                    print(f"{years} years are left till leap year")
                if user_in_delta.lower() == 'd':
                    days = delta.days
                    print(f"{days} days are left till leap year")
                if user_in_delta.lower() == 's':
                    sec = delta.total_seconds()
                    print(f"{sec} seconds are left till leap year")
    
    elif num == '4':
        print("Current month Calandar will be displayed or enter year and month: ")
        month =  input("Month 'mm' ")
        year = input("Year 'yyyy' ")
        if month and year:
            print(calendar.month(int(year), int(month)))
        else:
            current_month = datetime.now().month
            current_year = datetime.now().year
            print(calendar.month(current_year, current_month))
            
    elif num == '5':
        print("""Our partners are located in different timezones, choose location to see time at their office and compare to your local time: 
        1.Tokyo/Japan
        2.Dublin/Ireland
        3.San Francisco/USA
        4.Berlin/Germany
        5.Johannesburg/South Africa
        Enter number 1 to 5""")
        location = input("")
        if location == "1":
            timezone = pytz.timezone('Asia/Tokyo')
        elif location == "2":
            timezone = pytz.timezone('Europe/Dublin')
        elif location == "3":
            timezone = pytz.timezone('America/Los_Angeles')
        elif location == "4":
            timezone = pytz.timezone('Europe/Berlin')
        elif location == "5":
            timezone = pytz.timezone('Africa/Johannesburg')
        else:
            print("Incorrect input. Please enter a number from 1 to 5")
            
        local = datetime.now(pytz.utc)
        local1 = local.strftime("%H:%M:%S")
        city = datetime.now(timezone)
        city1 = city.strftime("%H:%M:%S")
        delta = local - city

        print("Time in selected city: ", city1)
        print("Local time: ", local1)
        print("Time difference: ", delta)

    elif num == '6':
        jokes = [
                "You and I will be friends forever because at this point, you know too much",
                "I told my doctor that I broke my arm in two places – he told me to stop going to those places",
                "When I was a kid, my dad got fired from his job as a road worker for theft. I refused to believe he could do such a thing, but when I got home, the signs were all there",
                "Happy birthday. At least you’re not as old as you will be next year",
                "Nothing is really lost... Unless even Mom can’t find it",
            ]
        joke = random.choice(jokes)
        print(joke)

    elif num == '7':
        facts = [
                "Fact: Sudan has more pyramids than any country in the world",
                "Fact: The circulatory system is more than 60,000 miles long",
                "Fact: The average person spends about six months of their lifetime waiting for red traffic lights to turn green",
                "Fact: The shortest war in history lasted only 38 to 45 minutes. It was between Britain and Zanzibar in 1896",
                "Fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible",
                "Fact: The first recorded instance of someone using LOL (meaning laugh out loud) was in 1989",
            ]
        fact = random.choice(facts)
        print(fact)
     





    


 

    





