"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then
prints the equivalent weight on that planet.

Note that the user should type in a planet with
the first letter as uppercase, and you do not need
to handle the case where a user types in something
other than one of the planets (that is not Earth).
"""

# MERCURY_GRAVITY = 0.376
# VENUS_GRAVITY = 0.889
# MARS_GRAVITY = 0.378
# JUPITER_GRAVITY = 2.36
# SATURN_GRAVITY = 1.081
# URANUS_GRAVITY = 0.815
# NEPTUNE_GRAVITY = 1.14
# EARTH_GRAVITY = 1.0
#
# while True:
#     user_weight = input("Enter your weight on Earth (in kgs): ")
#     if user_weight.isdigit():
#         user_weight = float(user_weight)
#         break
#     else:
#         print("Enter valid weight!")
#         continue
#
# while True:
#     planet = input("Enter name of planet: ").capitalize()
#
#     if planet == "Mercury":
#         print(f"Your weight on Mercury: {(user_weight * MERCURY_GRAVITY):.2f}")
#         break
#     elif planet == "Venus":
#         print(f"Your weight on Venus: {(user_weight * VENUS_GRAVITY):.2f}")
#         break
#     elif planet == "Earth":
#         print(f"Your weight on Earth: {(user_weight * EARTH_GRAVITY):.2f}")
#         break
#     elif planet == "Mars":
#         print(f"Your weight on Mars: {(user_weight * MARS_GRAVITY):.2f}")
#         break
#     elif planet == "Jupiter":
#         print(f"Your weight on Jupiter: {(user_weight * JUPITER_GRAVITY):.2f}")
#         break
#     elif planet == "Saturn":
#         print(f"Your weight on Saturn: {(user_weight * SATURN_GRAVITY):.2f}")
#         break
#     elif planet == "Uranus":
#         print(f"Your weight on Uranus: {(user_weight * URANUS_GRAVITY):.2f}")
#         break
#     elif planet == "Neptune":
#         print(f"Your weight on Neptune: {(user_weight * NEPTUNE_GRAVITY):.2f}")
#         break
#     else:
#         print("Enter valid planet name!")
#         continue

planets = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
    "Earth": 1.0
}

while True:
    try:
        weight = float(input("Enter weight: "))
        break
    except TypeError as t:
        print("Invalid!", t)

while True:
    choice = input("Choose Planet: ").capitalize()
    if not choice.isalpha() or choice not in planets:
        print("Invalid!")
        continue
    break

for planet, gravity in planets.items():
    if choice == planet:
        modified_weight = weight * planets[planet]
        print(f"Your weight on {planet} is", round(modified_weight, 2))

