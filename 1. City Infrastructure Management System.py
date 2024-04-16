
# Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

list_of_vehicles = [
    Vehicle(1, "sedan", "Bob"),
    Vehicle(2, "coupe", "Billy"),
    Vehicle(3, "suv", "Susan"),
    Vehicle(4, "exotic", "Stacy")
]

for vehicle in list_of_vehicles:
    print(f"Registration number {vehicle.registration_number} is a {vehicle.type} owned by {vehicle.owner}")

print("Bob bought Stacy's car!")

list_of_vehicles[3].update_owner("Bob")

for vehicle in list_of_vehicles:
    print(f"Registration number {vehicle.registration_number} is a {vehicle.type} owned by {vehicle.owner}")

# Task 2: Event Management System Enhancement

input("Enter to continue to Task 2")

class Event:
    def __init__(self, name, date, participant_number):
        self.name = name
        self.date = date        
        self.participant_number = participant_number

    
    def add_participant(self, change):
        self.participant_number += change


    def get_participant_count(self):
        return self.participant_number
    

event1 = Event("test1", "today", 0)
event2 = Event("test2", "today", 0)

event1.add_participant(10)
event1.add_participant(-5)

event2.add_participant(20)

print(f"Event 1 number is {event1.get_participant_count()}")
print(f"Event 2 number is {event2.get_participant_count()}")