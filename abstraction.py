from abc import ABC, abstractmethod

class Teacher(ABC):
    @abstractmethod
    def teacher(self):
        print("teacher department")


class Student(Teacher):
    def student(self):
        print("student department..")

    def teacher(self):
        return super().teacher()
    

class Employeee(Teacher):
    def employee(self):
        print("both")

    def teacher(self):
        print("male")

    

obj  = Student()
obj.student()
obj.teacher()

obj = Employeee()
obj.employee()
obj.teacher()