# special magic method/ dunder methods
#operator overloading
# polymorphism - method overwriting

class phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"

    # str, repr
    def __str__(self):
        return f'{self.brand} {self.model}'

    def __repr__(self):
        return f'phone(\'{self.brand}\',\' {self.model}\',\' {self.price})' 

    def __len__(self):
        return self.price

    def __mul__(self, other):
        return self.price* other.price

class SmartPhone(phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera
    
    def phone_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"




my_phone = phone('nokia' , '1100',1000)
my_phone2 = phone('nokia', '1600',1200 )

my_smartphone = SmartPhone('oneplus','5t',33000,'16 MP')
print(my_smartphone.phone_name())
print(my_phone.phone_name())
print(len(my_smartphone))
print(len(my_phone))