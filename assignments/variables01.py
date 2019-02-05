import math

first_name = input("What is your name?")
diameter = input("What's the diameter of the circle that you wish to calculate the area for?")
current_year = input("Tell me, what year is it?")
year_of_birth = input("And finally, what year were you born?")

age = int(current_year) - int(year_of_birth)

print("Hello {0}, I see that you are {1} Years old".format(first_name, age))
print("The circumference of a circle with the diameter {0}  is {1}".format(diameter, float(diameter) * math.pi))˜˜