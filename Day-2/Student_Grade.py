
# Student Grade Tracker
students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]
Student_grade= create_student_grade(students)

def create_student_grade(students):
    student_grade= {}
    for name, grades in students:
        student_grade[name]=grades
    return student_grade
print("Dictionary of student grades:",student_grade)

def Calculating_Average(grades):
    return sum(grades)/len(grades) if grades else 0.0

def Highest_grade()

    


