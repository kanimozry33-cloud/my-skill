def weather_skill():
    name = input("What is your name? ")
    mood = input("How are you feeling today? ")

    if mood.lower() == "happy":
        print(f"Hey {name}! The sun is shining in your code today! ☀️")
    elif mood.lower() == "tired":
        print(f"Hang in there {name}. High chance of coffee incoming! ☕")
    else:
        print(f"Hello {name}! Today's forecast: 100% chance of productivity.")

if __name__ == "__main__":
    weather_skill()

