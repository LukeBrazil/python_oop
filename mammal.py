class Mammal:
    def __init__(self, type_of_mammal, breed, legs):
        self.type_of_mammal = type_of_mammal
        self.breed = breed
        self.legs = legs

    def eat(self):
        return "The %s is eating" % (self.type_of_mammal)    

        
class Cat(Mammal):
    def __init__(self, name, type_of_mammal, breed, legs, fur):
        super().__init__(type_of_mammal, breed, legs)
        self.fur = fur
        self.name = name

    def __str__(self):
        return '%s is a %s %s with %d legs and %s fur' % (self.name, self.type_of_mammal, self.breed, self.legs, self.fur)

    def pur(self):
        return "%s is purring" % (self.name)
        
    def eat(self):
        return "The cats eat poop"
        
frank = Cat('frank', 'cat', 'mixed', 4, 'hairy')
bob = Mammal('cat', 'ugly', 4)

print(frank)
print(frank.pur())
print(frank.eat())
print(bob.eat())
# frank = Mammal("cat", "lion", 4)