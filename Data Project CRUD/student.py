class Student:
    def __init__(self, student_id=-1, first_name="", surname="", father_name="", age=-1, school_class=-1, id_number=""):
        self.student_id = student_id
        self.first_name = first_name
        self.surname = surname
        self.father_name = father_name
        self.age = age
        self.school_class = school_class
        self.id_number = id_number

    def __str__(self):
        st = f"+{25 * '-'}+" + "\n"
        st += f"| {('student_id: ' + str(self.student_id)).ljust(24)}|" + "\n"
        st += f"| {('first_name: ' + self.first_name).ljust(24)}|" + "\n"
        st += f"| {('surname: ' + self.surname).ljust(24)}|" + "\n"
        st += f"| {('father-name: ' + self.father_name).ljust(24)}|" + "\n"
        st += f"| {('age: ' + str(self.age)).ljust(24)}|" + "\n"
        st += f"| {('school-class: ' + str(self.school_class)).ljust(24)}|" + "\n"
        st += f"| {('id_number: ' + self.id_number).ljust(24)}|" + "\n"
        st += f"+{25 * '-'}+"
        return st

    def from_dict(self, student_dict):
        self.student_id = student_dict["student_id"]
        self.first_name = student_dict["first_name"]
        self.surname = student_dict["surname"]
        self.father_name = student_dict["father-name"]
        self.age = student_dict["age"]
        self.school_class = student_dict["school-class"]
        self.id_number = student_dict["id_number"]

    def to_dict(self):
        student_dict = {"student_id": self.student_id,
                        "first_name": self.first_name,
                        "surname": self.surname,
                        "father-name": self.father_name,
                        "age": self.age,
                        "school-class": self.school_class,
                        "id_number": self.id_number
                        }
        return student_dict
