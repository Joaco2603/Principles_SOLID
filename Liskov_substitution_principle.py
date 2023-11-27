
#Liskov Substitution Principle - LSP:
#Subtypes must be substitutable for their base types without altering the correctness of the program, ensuring that derived classes can be used wherever their base classes are used.

class Bird:
    def bird():
        print("I am a Bird");

class Fly(Bird):
    def fly():
        print("I can fly");
        
        
class NoFly(Bird):
    def no_fly():
        print("I can not fly");