from Student import Student
class HaniehStudent(Student):

    def __init__(self, name, lastname, major, gpa,age):
        self.age=age
        super().__init__(name, lastname, major, gpa)
    def on_honor_roll(self):
        print("congratulations you get the honor of best student ")