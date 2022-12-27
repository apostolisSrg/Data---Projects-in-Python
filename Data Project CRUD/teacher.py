class Teacher:
    def __init__(self, teacher_id=-1, first_name="", surname=""):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.surname = surname

    def from_dict(self, teacher_dict):
        self.teacher_id = teacher_dict["teacher_id"]
        self.first_name = teacher_dict["first_name"]
        self.surname = teacher_dict["surname"]

    def to_dict(self):
        teacher_dict = {"teacher_id": self.teacher_id,
                        "first_name": self.first_name,
                        "surname": self.surname,
                        }
        return teacher_dict

    # Print Mode 1
    def __str__(self):
        st = f"+{24 * '-'}+" + "\n"
        st += f"| {('teacher_id: ' + str(self.teacher_id)).ljust(23)}|" + "\n"
        st += f"| {('first_name: ' + self.first_name).ljust(23)}|" + "\n"
        st += f"| {('last_name: ' + self.surname).ljust(23)}|" + "\n"
        st += f"+{24 * '-'}+"
        return st
