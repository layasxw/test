class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def sound(self):
        return "Sound"
    

class Dog(Animal):
    def __init__(self, name, type, color, age):
        #вызов родительского класса через super()
        super().__init__(name, type, color)
        self.age = age
    
    def sound(self):
        #использовать супер() для вызова метода sound() из класса энимал
        parent_sound = super().sound()
        return parent_sound + 'Гав!'
    
dog = Dog("Bobik", "2 years", "Labrador", "yellow")
print(dog.name)  
print(dog.type)
print(dog.age)  
print(dog.color)