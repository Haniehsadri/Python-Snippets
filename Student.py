class Student:
    def __init__(self,name,lastname,major,gpa):
        self.name=name
        self.lastname=lastname
        self.major=major
        self.gpa=gpa

    def on_honor_roll(self):
        if self.gpa>=3.5:
            return True
        else:
            return False


