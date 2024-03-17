class Animal:
    def __init__(self, name, age, chip_num=0, vaccine=None):
        self.name = name
        self.age = age  # public attr
        self._vaccine = vaccine  # protected attr
        self.__chip_num = chip_num  # private attr

    @property
    def vaccine(self):  # protected method
        return self._vaccine

    @vaccine.setter
    def vaccine(self, new_vaccine):
        if self.vaccine is not None:
            self._vaccine = new_vaccine
        else:
            print('Pet is not vaccinated')

    @property
    def chip_num(self):  # private method
        return self.__chip_num

    @chip_num.setter
    def chip_num(self, new_chip_num):
        if self.chip_num is not None:
            self.__chip_num = new_chip_num
        else:
            print('Pet has no chip')


class Cat(Animal):
    def info(self):
        print(f'Hello! My name is {self.name}. I am {self.age} years old.')

    @staticmethod
    def make_sound():
        print('Meow')


class Dog(Animal):
    def info(self):
        print(f'Hi! My name is {self.name}. I am {self.age} years old.')

    @staticmethod
    def make_sound():
        print('Bow')


cat1 = Cat('Tabby', 2.5, 624763, 'Feline-123')
dog1 = Dog('Fluffy', 1, 139896)

for animal in (cat1, dog1):
    animal.info()
    animal.make_sound()

print(cat1.__dict__)
print(dog1.__dict__)

# print(cat1._vaccine)  # protected atribute
print(cat1.vaccine)  # protected method

# print(Cat.chip_num)  # <property object... (private method)
# print(dog1.__chip_num)  # AttributeError (private atribute)
print(dog1.chip_num)  # AttributeError (private method)

# print(f'Access to private atribute: {cat1._Animal__chip_num}')  # not recomended
# print(f'Access to private method: {dog1._Animal__chip_num}')  # not recomended
