""" I will try the default method in calling a function for the project DC"""

# Contract that has Name, age, country A and B

class Country_:

    print("CONTINENTS:")
    print("\n")


    def details(self):
        print("You name is " + self.name)
        print("You age is " + str(self.age))
        print("You belong to Country " + self.country)
        print("\n")

A = Country_()
A.name = "Henry Richards"
A.age = 30
A.country = "A"

B = Country_()
B.name = "Dinesh"
B.age = 29
B.country = "B"

A.details()
B.details()

