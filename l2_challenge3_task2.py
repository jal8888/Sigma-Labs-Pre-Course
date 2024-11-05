people = [{"First name": "Jane", "Last name": "Doe","Age": 42, "Employed": "Yes"},
{"First name": "Tom", "Last name": "Smith","Age": 18, "Employed": "Yes"},
{"First name": "Mariam", "Last name": "Coutler","Age": 66, "Employed": "No"},
{"First name": "Gregory", "Last name":"Tims","Age": 8, "Employed": "No"}]
x=1

def loop_func(people):
    for person in people:
        print(f"Name: {person.get("First name")} {person.get("Last name")}\nAge: {person.get("Age")}\nEmployed: {person.get("Employed")}")

def add_func(people):
    user_first_name= input("What is your First Name?: ").title()
    user_last_name= input("What is your Last Name?: ").title()
    user_age= int(input("What is your age?: "))
    user_employed= input("Are you employed?: ").title()
    people.append({"First name": user_first_name,"Last name": user_last_name,"Age": user_age, "Employed": user_employed})
    return people

def remove_func(people):
    name_removal= input("Please state the first name of the person you would like to remove: ").title()
    new_people_list =[]
    for person1 in people:
        if name_removal == person1.get("First name"):
            continue
        else:
            new_people_list.append(person1)
    return new_people_list

while x == 1:
    user_input= input("Would you like to add or remove a person?: ")
    if user_input.lower() == "add":
        people=add_func(people)
        loop_func(people)
    elif user_input.lower() == "remove":
        people = remove_func(people)
        loop_func(people)
    else:
        print("Incorrect input please select choose add or remove")

    
