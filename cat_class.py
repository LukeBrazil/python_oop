class Cat:
    species = "mammal"
    legs = 4
    fur = "long hair"

    #initialize class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #string method for class
    def __str__(self):
        return "%s is %d years old." % (self.name, self.age)

    # Instance method
    def eat(self, cans_of_food):
        self.cans_of_food = cans_of_food
        return "%s ate %d cans of food." % (self.name, self.cans_of_food)
        
frank = Cat("Frank", 10)
beans = Cat("Beans", 11)

print(frank.eat(1))
print(beans.eat(2))