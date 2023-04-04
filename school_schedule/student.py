class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade.lower()
        self.classes = classes
    
    def add_class(self, class_name):
        self.classes.append(class_name)
        return self
    
    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        return(f"{self.name} is a {self.grade}. {self.name} " 
              f"takes {self.get_num_classes()} classes: " 
              f"{', '.join(self.classes)}")