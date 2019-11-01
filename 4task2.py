
class Airplane:
    def __init__(self, make, model, year):
        self.is_flying = False
        self.odometer = 0

    def take_off(self, bool): #взлет
        self.is_flying
        print("Самолет взлетает!")
       

    def fly(self, distance):
        self.odometer = self.odometer + distance
        print(self.odometer)

    def land(self,bool):
        self.is_flying = False
        print("Самолет приземлился!")

airplane1 = Airplane("Su-", "33", "1998")
airplane1.take_off(True)
airplane1.fly(1500)
airplane1.fly(1500)
airplane1.land(False)



