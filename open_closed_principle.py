
#Open/Closed Principle - OCP:
#Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification, allowing new functionality to be added without altering existing code.

from abc import ABC, abstractmethod

#The user could be another class.
#The message could be another class.

class Notifier(ABC):
    def __init__(self,user,message):
        self.user = user;
        self.message = message;
    
    @abstractmethod
    def notify(self):
        pass
    
class Notifier_email(Notifier):
    
    def notify(self):
        print(f"Email notification");
        
class Notifier_SMS(Notifier):
    def notify(self):
        print(f"Email notification");
        
class Notifier_instagram(Notifier):
    
    def notify(self):
        print(f"Email notification");
        
        
new_notifier = Notifier_email("Joaco","jpappa2603@gmail.com");

print(new_notifier.user);
print(new_notifier.message);