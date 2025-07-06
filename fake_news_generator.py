import random

subjects=[
    "John Smith",
    "Emma Johnson",
    "Michael Brown",
    "Olivia Davis",
    "William Wilson",
    "Sophia Taylor",
    "James Anderson",
    "Emily Thomas",
    "Daniel Moore"
]

actions=[
    "is eating banana",
    "is playing ludo",
    "is walking",
    "is vomiting",
    "is cheating",
    "is idiot and playing cards",
    "is dancing",
    "is eating biryani with ketchup",
    "is running"
]

places=[
    "on moon",
    "in bathroom",
    "in kitchen",
    "on bus stop",
    "in washroom",
    "on sun",
    "on mars",
    "on rooftop",
    "on bus roof"
]
while True:
    subject=random.choice(subjects)
    action = random.choice(actions)
    place=random.choice(places)

    final_statement=f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + final_statement)
    user_input=input("Do you want another headline (yes/no): ")
    if user_input.lower() == "no":
        break
print("Thanks for using fake news generator!!")


