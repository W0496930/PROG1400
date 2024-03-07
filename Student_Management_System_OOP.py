#Author: William Taylor
#Student ID: W0496930
#Course: PROG1400
#Date: 2024-03-07
#Project: Student_Management_System
#Repository: https://github.com/W0496930/PROG1400
#Programming language: Python 3

#Task 1: Define the Student class with required attributes and methods
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    #Task 2: Method to display student information
    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

    #Added a method to update the student's grade
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"Grade updated for student {self.student_id} to: {new_grade}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    #Task 5: Method to add a new student
    def add_student(self, student):
        self.students.append(student)

    #I added a method to display information of all students
    def display_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                student.display_info()

    # Task 5: Method to search for a student by ID and display their information
    def search_student_by_id(self, student_id):
        found = False
        for student in self.students:
            if student.student_id == student_id:
                student.display_info()
                found = True
                break
        if not found:
            print("Student not found.")

    #Added a method to update the grade of a student by their ID
    def update_grade_by_id(self, student_id, new_grade):
        found = False
        for student in self.students:
            if student.student_id == student_id:
                student.update_grade(new_grade)
                found = True
                break
        if not found:
            print("Student not found.")
    #Implemented the method to run the student management system program
    def run(self):
        while True:
            #Menu options
            print("1. Add new student")
            print("2. Display information of all students")
            print("3. Search for a student by ID")
            print("4. Update the grade of a student by ID")
            print("5. Exit")
            choice = input("Enter your choice: ")

            #Prompt the user with the options within the program
            if choice == '1':
                student_id = int(input("Enter student ID: "))
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                grade = float(input("Enter student grade: "))
                student = Student(student_id, name, age, grade)
                self.add_student(student)

            elif choice == '2':
                print("\nInformation of all students:")
                self.display_all_students()

            elif choice == '3':
                student_id = int(input("Enter student ID to search: "))
                print("Student information:")
                self.search_student_by_id(student_id)

            elif choice == '4':
                student_id = int(input("Enter student ID to update grade: "))
                new_grade = float(input("Enter new grade: "))
                self.update_grade_by_id(student_id, new_grade)

            elif choice == '5':
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

#Running the program
def main():
    student_management_system = StudentManagementSystem()
    student_management_system.run()

if __name__ == "__main__":
    main()
