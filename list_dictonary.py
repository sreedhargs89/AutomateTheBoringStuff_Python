# Difference with arrays to list
# 1. Arrays (Lists) are ordered collections of items, while dictionaries are unordered collections of key-value pairs.
# 2. Lists are accessed by their index, whereas dictionaries are accessed by their keys.
# 3. Lists can contain duplicate items, while dictionary keys must be unique.


# List of colors
colors = ["Red", "Green", "Blue"]
print(f"Colors: {colors}")
print(f"Number of colors: {len(colors)}")
for color in colors:
    print(f"Color: {color}")


# Dictionary for a person
person = {
    "Name": "Sree",
    "Age": 30,
    "Is Student": True
}
print(f"Person Dictionary: {person}")

# Array of dictionaries for multiple people
people = [
    {"Name": "Alice", "Age": 30, "Is Student": True},
    {"Name": "Bob", "Age": 25, "Is Student": False},
    {"Name": "Charlie", "Age": 35, "Is Student": True}
]

for person in people:
    print(f"Person Dictionary: {person}")

# Automate the Boring Stuff Ch 3-4 (lists, dictionaries): https://automatetheboringstuff.com/2e/chapter3/

