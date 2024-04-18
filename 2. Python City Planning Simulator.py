
# Task 1: File Handling for Building Records
# Imports
import os

# Definitions
class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    
    # Each building will be saved as its own file
    def save_building_to_file(self):
        try:
            with open(f"\\{self.name}.txt", "w") as file:
                file.write(f"{self.name}")
                file.write(f"\n{self.floors}")
        except:
            print(f"Could not create file {self.name}.txt!")

    # Building files are named by their Building.name. For purposes of the assignment, the script creates a Town Hall, then opens the Town Hall file
    def load_building_from_file(self, filename):
        try:
            with open(f"\\{filename}.txt", "r") as file:
                info = []
                for line in file:
                    info.append(line.strip())
                self.name = info[0]
                self.floors = info[1]
        except FileNotFoundError:
            print(f"There is no file named \"{filename}.txt\"")
        except:
            print(f"Could not open \"{filename}.txt\"!")

# Script
buildings = [
    Building("Town hall", 3),
    Building("Utilities", 2),
    Building("Police Station", 2),
    Building("Senior Center", 1),
    Building("", 0)
]

for building in buildings:
    print(building.name, building.floors)

buildings[0].save_building_to_file()
buildings[2].save_building_to_file()
buildings[4].load_building_from_file("Town hall")

for building in buildings:
    print(building.name, building.floors)