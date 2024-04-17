
class Bus:
    buses = []
    bus_counter = 0
    fare = 1.50
    city = "New York City"
    def __init__(self, route_num, capacity):
        self.route_num = route_num
        self.capacity = capacity


    def add_bus_route(self, capacity):
        self.bus_counter += 1
        self.buses.append(Bus(self.bus_counter, capacity))


    def hike_fare(self, change):
        self.fare += change
        print(f"Fare is now {self.fare}.")


    def get_bus_route(self, index):
        return self.buses[index].route_num


    def set_bus_route(self, index, route):
        self.buses[index].route_num = route