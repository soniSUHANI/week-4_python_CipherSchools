#raise errrors example 1
# NotimplementedError
# abstract method

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have to define this method in subclassesn ')

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.bread = breed

    def sound(self):
        return 'bhow bhow'

class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'maoo maoo'

doggy = Dog('boony', 'pug')
print(doggy.sound())
caty = Cat('mao', 'mao')
print(caty.sound())