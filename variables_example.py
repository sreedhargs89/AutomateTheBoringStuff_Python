# Variables
name = "Alice"
age = 30
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is Student: {is_student}")

# Changing variable values
name = "Bob"
age = 25
is_student = False

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is Student: {is_student}")

# Input method
name = input("Enter your name: ")
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid integer for age.")
is_student_input = input("Are you a student? (True/False): ").strip().lower()
is_student = is_student_input == "true"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is Student: {is_student}")

# Array of colors
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
