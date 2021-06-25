""" I will try the default method in calling a function for the project DC"""

# Contract that has Name, age, country A and B

import random
class Country_:

    print("WELCOME TO CONTINENTS:\t Please only type A or B when asked about country!")


    def details(self):
        self.name
        str(self.age)
        self.country
        self.random
       

A = Country_()
A.name = input("Enter Name:")
A.age = input("Enter Age:")
A.country = input("Enter Country:")
while True:
    if A.country == "A" and "B":
        print("Welcome, " + A.name + " from Country " + A.country)
        break
    if A.country == "B" and "A":
        print("Welcome, " + A.name + " from Country " + A.country)
        break
    if A.country != "A":
        print("Enter valid data!")   
        A.country = False
        break     
    if A.country != "A":
        print("Enter valid data!")    
        A.country = False
        break 
A.random = 10101 ** random.random() # Can also use ord() if needed at time.
print("Your key: " + str(A.random))  

print("\t")

B = Country_()
B.name = input("Enter Name:")
B.age = input("Enter Age:")
B.country = input("Enter Country:")
while True:
    if B.country == "A" and "B":
        print("Welcome, " + B.name + " from Country " + B.country)
        break
    if B.country == "B" and "A":
        print("Welcome, " + B.name + " from Country " + B.country)
        break
    if B.country != "A":
        print("Enter valid data!")   
        B.country = False
        break     
    if B.country != "A":
        print("Enter valid data!")    
        B.country = False
        break     
B.random = 10101 ** random.random() # Can also use ord() if needed at time.
print("Your key: " + str(B.random))

A.details()
B.details()

