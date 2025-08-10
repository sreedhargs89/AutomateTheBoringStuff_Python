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

