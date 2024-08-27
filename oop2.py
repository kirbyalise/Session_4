class Dog():
    # class attributes
    kind = 'canine'
    breed = 'pug'
    age = 5
    colour = 'black'
    
    # def __init__(self, name):
    #     
        


    # instance attribute
    def __init__(self, name, breed, age, colour):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age 
        self.weight = weight
        
    def eat(self):
    
dog = Dog('Jett', 'pug', 5, 'black', 12)
print(dog.name, dog.breed, dog.age, dog.colour, dog.weight)
dog2 = Dog('Bub', 'poodle', 3, 'white' 10)
print(dog2.name, dog2.breed, dog2.age, dog2.colour, dog.weight)

# dog = Dog(a,b,c)
# print(dog.age, dog.breed, dog.colour)
# dog2 = Dog()
# print(dog2.age,dog2.breed,dog2.colour)