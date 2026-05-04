# Practical 01 - Practice Assignment 1
# Momentum calculation using the formula e = m * c^2

mass = float(input("Enter mass of the object (in kg): "))
velocity = float(input("Enter velocity of the object (in m/s): "))

momentum = mass * velocity * velocity

print("\nResult")
print("Mass     :", mass, "kg")
print("Velocity :", velocity, "m/s")
print("Momentum :", momentum)
