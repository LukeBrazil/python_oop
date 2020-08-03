# class Human:
#     species: "homo erectus"
#     arms: 2
#     legs: 2

#     def __init__(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location
    
#     def __str__(self):
#         return "This human is named %s, %d years old, and lives in %s." % (self.name, self.age, self.location)

# Bob = Human("Bob", 42, "Miami")

# print(Bob)
        

class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))
    


sonny = Person("Sonny", "sonny@hoymail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print("Sonny's contact info: " + sonny.email, sonny.phone)
print("Jordan's contact info: " + jordan.email, jordan.phone)