# Function to calculate grade based on average
def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 75:
        return 'A'
    elif avg >= 60:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'Fail'

# Step 1: Ask how many students
n = int(input("Enter number of students: "))

# Step 2: Create empty list to store student records
students = []

# Step 3: Loop through each student
for i in range(n):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter name: ")
    maths = int(input("Enter Maths marks: "))
    physics = int(input("Enter Physics marks: "))
    chemistry = int(input("Enter Chemistry marks: "))

    total = maths + physics + chemistry
    avg = total / 3
    grade = calculate_grade(avg)

    student = {
        "Name": name,
        "Maths": maths,
        "Physics": physics,
        "Chemistry": chemistry,
        "Total": total,
        "Average": avg,
        "Grade": grade
    }

    students.append(student)

# Step 4: Final Report Card
print("\n📋 Student Report Card:\n")
for s in students:
    print(f"Name: {s['Name']}")
    print(f"Maths: {s['Maths']}, Physics: {s['Physics']}, Chemistry: {s['Chemistry']}")
    print(f"Total: {s['Total']}, Average: {s['Average']:.2f}, Grade: {s['Grade']}")
    print("-" * 30)
