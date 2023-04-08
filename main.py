class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("walking")

class Student(Person):
    mark = 1
    def __init__(self,name):
        super().__init__(name, 15)

class Teacher(Person):

    def __init__(self, name):
        super().__init__(name, 25)

    def give_mark(self, student):
        print('Teacher gave grade to', student.name)
        student.mark = 12


good_student1 = Student("Sasha")
good_student2 = Student("Slavik")

print(good_student1.age)