from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, 
                 gets_transportation=False):
        
        super().__init__(name, grade, classes)
        self.get_transportation = gets_transportation

    def summary(self):
        first_line = super().summary()
        if self.get_transportation == True:
            second_line = f"{self.name} has {self.get_transportation()}"
            return first_line + second_line
        else:
            return first_line