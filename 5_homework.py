class Animal:
    def __init__(self, name, age, chip_num=0, vaccine=None):
        self.name = name
        self.age = age
        self.__chip_num = chip_num
        self._vaccine = vaccine


class Cat(Animal):
    def info(self):
        print(f'I am a cat. My name is {self.name}. I am {self.age} years old.')

    @staticmethod
    def make_sound():
        print('Meow')


class Dog(Animal):
    def info(self):
        print(f'I am a dog. My name is {self.name}. I am {self.age} years old.')

    @staticmethod
    def make_sound():
        print('Bow')


cat1 = Cat('Tabby', 2.5, 624763, 'Feline-123')
dog1 = Dog('Fluffy', 1, 139896)

for animal in (cat1, dog1):
    animal.info()
    animal.make_sound()


# print(cat1.__dict__)
# print(dog1.__dict__)
# print(cat1._vaccine)
