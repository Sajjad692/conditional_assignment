# Check Age 

age=15 # you can change the age for different results
if age>=18:
    print("You are an adult.")

# Age Check with Else
else:
    print("You are not an adult.")

# Grading System

while True:
    student_name=input("Studen Name:  ")
    marks=int(input("Enter Marks:   "))
    if marks>=90:
        print(f"Dear {student_name} you got the Grade: A+")
    elif marks>=85:
        print(f"Dear {student_name} you got the Grade: A")
    elif marks>=80:
        print(f"Dear {student_name} you got the Grade: B+")
    elif marks>=75:
        print(f"Dear {student_name} you got the Grade: B")
    elif marks>=70:
        print(f"Dear {student_name} you got the Grade: C+")
    elif marks>=65:
        print(f"Dear {student_name} you got the Grade: C")
    elif marks>=60:
        print(f"Dear {student_name} you got the Grade: D")
    elif marks>=50:
        print(f"Dear {student_name} you got the Grade: E")
    else:
        print(f"Dear {student_name} Your Progress same as Rafale")
    restart=input("Do you want to enter another result? (yes/no): ")
    if restart.lower() != 'yes':
        break

#  Weather Advice 
while True:
    weather=input("Enter the Weather:    ").lower()
    if weather =="rainy":
        print("Take an umbrella")
    elif weather =="sunny":
        print("Wear sunglasses")
    elif weather == "cloudy":
        print("It might rain later")
    elif weather == "foggy":
        print("Drive carefully, visibility is low!")
    elif weather == "snowy":
        print("Wear warm clothes")
    elif weather == "stormy":
        print("Stay indoors if possible")
    else:
        print("Sorry, I don't recognize that weather condition.")
    restart=input("Do you want to know about another weather safety? (yes/no): ")
    if restart.lower() !="yes":
        break

# Feeling Hungry?

hungry = True  # or False
if hungry:
    print("Go eat something!")
else:
    print("Maybe have a snack later.")

# Bonus Fun Task: Mini Chatbot

mood = input("How are you feeling today? ").lower()
if mood == "happy":
    print("That's great to hear!")
elif mood == "sad":
    print("I hope your day gets better.")
elif mood == "bored":
    print("Try reading a book or going for a walk.")
else:
    print("Thanks for sharing your mood!")

