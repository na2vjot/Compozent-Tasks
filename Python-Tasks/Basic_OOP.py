# E- Basic OOP (Object Oriented Programming)

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        """Display student details."""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average(self):
        """Calculate and return the average grade."""
        if not self.grades:  # To handle the case where there are no grades
            return 0
        return sum(self.grades) / len(self.grades)


# Get user input for student details
name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
grades_input = input("Enter the student's grades separated by commas (e.g., 85, 90, 78): ")

# Convert the grades input to a list of integers
grades = [int(grade) for grade in grades_input.split(",")]

# Create a Student object
student = Student(name=name, age=age, grades=grades)

# Display details and average grade
student.display_details()
average = student.calculate_average()
print(f"Average Grade: {average:.2f}")
