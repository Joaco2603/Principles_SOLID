
#Single Responsibility Principle - SRP:
#A class should have only one reason to change, meaning that it should have only one responsibility or job within the software system.

class Car:
    def __init__(self,fuel):
        self.__position = 0;
        self.__fuel = fuel;
    
    def move(self,distance):
        if self.__fuel.get_fuel() >= distance/2:
            self.__position += distance;
            self.__fuel.use_fuel(distance/2);
            return "You have successfully moved the car";
        else:
            return "There is not enough fuel";
        
    def get_position(self):
        return self.__position;
            
class Fuel_tank:
    def __init__(self):
        self.fuel = 100;
    
    def get_fuel(self):
        return self.fuel;
    

    def set_fuel(self,amount):
        self.fuel += amount;
    

    def use_fuel(self,amount):
        self.fuel -= amount;
        
        
new_fuel_tank = Fuel_tank();
new_Car = Car(new_fuel_tank);

print(new_Car.get_position());
print(new_Car.move(100));
print(new_Car.get_position());