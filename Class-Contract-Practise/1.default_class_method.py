""" I will try the default method in calling a function for the project DC"""

# Contract that has Name, age, country A and B

import random
class Country_:

    print("CONTINENTS:")
    print("\n")


    def details(self):
        print("You name is " + self.name)
        print("You age is " + str(self.age))
        print("You belong to Country " + self.country)
        random_number_generator = 10101 ** random.random() # Can also use ord() if needed at time.
        print(random_number_generator)
        print("\n")

A = Country_()
A.name = input("Enter Name:")
A.age = input("Enter Age:")
A.country = input("Enter Country:")

B = Country_()
B.name = input("Enter Name:")
B.age = input("Enter Age:")
B.country = "B"

A.details()
B.details()

