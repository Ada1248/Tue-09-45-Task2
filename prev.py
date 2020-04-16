class School:
    def __init__(self, classes):
        self.classes = classes

class Class:
    def __init__(self, number, letter, students):
        self.students = students
        self.number = number
        self.letter = letter


    def __str__(self):
        return 'Class: {}{}'.format(self.number, self.letter)



class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.attendance = []
        self.grade = []


    def check_attendance(is_present: bool, student):
        presence = 1 if is_present else 0

    def __str__(self):
        return 'Student: {} {}'.format(self.name, self.surname)

    def count_attendance(self):
        return sum(self.attendance)

    def count_grades_mean():
        return sum(self.grade)/len(self.grade) 


if __name__ == "__main__":

    first_student = Student(name="Jan", surname="Kowalski")
    second_student = Student(name="Kasia", surname="Nowak")
    print(first_student)
    print(second_student)

    first_A_class = Class(1, "A", [first_student, second_student])
    print(first_A_class)

    first_student.check_attendance(True)
    second_student.check_attendance(True)
    first_student.check_attendance(False)
    second_student.check_attendance(True)
    first_student.check_attendance(True)
    second_student.check_attendance(True)

    print(first_student.count_attendance())
    print(second_student.count_attendance())