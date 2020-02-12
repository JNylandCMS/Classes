
class CarClass:

    def __init__(self, wheels, colour, doors, price, engine_size, leatherSeats =  False):
        self.wheels = wheels
        self.colour = colour
        self.doors = doors
        self.price = price
        self.engine_size = engine_size
        self.leatherSeats = leatherSeats



    def ChangeColour(self, no):
        self.windows = no
        

    def ChangeDoorsNumber(self, no):
        self.doors = no 



toyota = CarClass(4,"red", 4, 25000, 2 )

toyota.ChangeDoorsNumber(2)
print(toyota.colour)
print(toyota.price)
print(toyota.engine_size)

'''Ford = CarClass(4,1,2, leatherSeats=True )'''

'''if Ford.leatherSeats == True:
    print("this car has leather seats")
else:
    print("this car doesnt have leather seats")'''
    