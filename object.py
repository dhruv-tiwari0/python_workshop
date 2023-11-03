#example of self and init
'''class dog:
    def __init__(self,name):
        self.name=name
dog1=dog("buddy")
print(dog1.name)'''

#example of classes
'''class car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
car1=car("toyota","camry")        
car2=car("honda","civic")
print(car1.make,car1.model)
print(car2.make,car2.model)'''

#example of incapsulation
'''class bankaccount:
    def __init__(self,account_number,balance):
        self.accountnumber=account_number
        self.balance=balance
    def getbalance(self):
        return self.balance
account1=bankaccount("12345","1000")        
print(account1.accountnumber)
print(account1.getbalance())'''

#example of inheritance
class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
         pass
class dog(animal):
    def speak(self):
        return "woof!"
class cat(animal):
    def speak(self):
        return "meow!"
dog1=dog("buddy")        
cat1=cat("whisker")
print(dog1.name,dog1.speak())
print(cat1.name,cat1.speak())

