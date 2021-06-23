""" I will try the __init__method in calling a function for the project DC"""

# Contract that has Name, age, country A and B
# With help of __init__ method we can call the function and then use them by simply chaning the string and int
# __init__ method has much more flexibility when working with classes than the other methods.

class Country_:

    print("CONTINENT CONTRACT FORM:")
    

    def __init__(self, name, age, country):
        self.name = name
        self.age = str(age)   # Either we can change the int to str here!
        self.country = country


    def details(self):
        print("You name is " + self.name)
        print("You age is " + self.age) # Or we can change the int to str here!
        print("You belong to Country " + self.country)
        print("\n")

A = Country_("Richard Hendricks", 29, "A")
B = Country_("Dinesh", 30, "B")

A.details()
B.details()

