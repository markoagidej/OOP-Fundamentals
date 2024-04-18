
class Bus:
    buses = []
    bus_counter = 0
    fare = 1.50
    city = "New York City"
    def __init__(self, route_num, capacity):
        self.route_num = route_num
        self.capacity = capacity


    # Adding a bus routes creates a new bus and assigns it a route number which incrementally increases
    def add_bus_route(self, capacity):
        self.bus_counter += 1
        self.buses.append(Bus(self.bus_counter, capacity))


    # This will effect a class variable so increasing fare can be done through any bus 
    def hike_fare(self, change):
        self.fare += change
        print(f"Fare is now {self.fare}.")


    # Returns the Route for a specific bus in the list of buses
    def get_bus_route(self, index):
        return self.buses[index].route_num
    

    # Lets you change the Route of a specific bus in the list of buses
    def set_bus_route(self, index, route):
        self.buses[index].route_num = route