class Car:
    def move(self):
        return "The car is moving fast."
class Plane:
    def move (self):
        return "The plane is flying high."
for vehicle in [Car(), Plane()]:
        print(vehicle.move())