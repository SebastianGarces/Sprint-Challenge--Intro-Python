# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class
class Vehicle:
    pass

# child
class FlightVehicle(Vehicle):
    pass

# grand-child
class Starship(FlightVehicle):
    pass

# grand-child
class Airplane(FlightVehicle):
    pass

# child
class GroundVehicle(Vehicle):
    pass

# grand-child
class Car(GroundVehicle):
    pass

# grand-child
class Motorcycle(GroundVehicle):
    pass
