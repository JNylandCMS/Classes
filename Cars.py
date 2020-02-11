
class CarClass:

    def __init__(self, wheels, windows, doors, leatherSeats =  False):
        self.wheels = wheels
        self.windows = windows
        self.doors = doors
        self.leatherSeats = leatherSeats



    def ChangeWindowsNumbers(seklf, no):
        self.windows = no
        

    def ChangeDoorsNumber(self, no):
        self.doors = no 



toyota = CarClass(4,2,4)

toyota.ChangeDoorsNumber(2)
print("here")

Ford = CarClass(4,1,2, leatherSeats=True )

if Ford.leatherSeats == True:
    print("this car has leather seats")
else:
    print("this car doesent have leather seats")
    