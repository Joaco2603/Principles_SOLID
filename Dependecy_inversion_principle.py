
#Dependency Inversion Principle - DIP:
#High-level modules should not depend on low-level modules; both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions. This principle encourages the use of interfaces or abstract classes to decouple high-level and low-level modules.

from abc import ABC,abstractmethod

class Verify(ABC):
    def verify_word(self,word):
        #Logic that verify words
        pass
    
class Dictionary(Verify):
    def verify_word(self, word):
        #Logic that verify words
        pass
    
class Dictionary_online(Verify):
   def verify_word(self, word):
        #Logic that verify words
        pass  
    
class Concealer:
    def __init__(self,verify):
        pass
    
    
    def concealer_text(self,text):
        #Use the verify for concealer text
        #Dictionary or Dictionary_online 
        pass
    
    
# concealer = Concealer(Dictionary_online())
concealer = Concealer(Dictionary());