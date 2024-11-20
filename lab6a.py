#!/usr/bin/env python3
# Author ID: rrakshit

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure student number is stored as a string
        self.courses = {}

    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if len(self.courses) == 0:
            return f'GPA of student {self.name} is 0.0'
        gpa = sum(self.courses.values()) / len(self.courses)
        return f'GPA of student {self.name} is {gpa:.1f}'

    def displayCourses(self):
        return [course for course, grade in self.courses.items() if grade > 0.0]

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)  # Test with integer student number
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
