
# Task 1: Public Transportation Module

import public_transportation as p_t

mock_bus = p_t.Bus(0,0)
mock_bus.add_bus_route(80)
mock_bus.add_bus_route(100)
mock_bus.add_bus_route(40)
mock_bus.add_bus_route(60)
mock_bus.add_bus_route(80)

bus_index = int(input("Input which bus number you would like to see the route of: "))
mock_bus.get_bus_route(bus_index)

new_route = input("Input a new route for this bus: ")
mock_bus.set_bus_route(bus_index, new_route)

print(f"New route is {mock_bus.buses[bus_index].route_num}")

price_hike = float(input("How much do you want ot increase fare by? "))
mock_bus.hike_fare(.5)