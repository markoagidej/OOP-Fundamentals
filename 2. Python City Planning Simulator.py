
# Task 1: File Handling for Building Records

import os

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    
    def save_building_to_file(self):
        with open(f"\\{self.name}.txt", "w") as file:
            file.write(f"{self.name}")
            file.write(f"\n{self.floors}")

    def load_building_from_file(self, filename):
        with open(f"\\{filename}.txt", "r") as file:
            info = []
            for line in file:
                info.append(line.strip())
            self.name = info[0]
            self.floors = info[1]


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