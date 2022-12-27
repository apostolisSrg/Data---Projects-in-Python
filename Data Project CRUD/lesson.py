from students import Students
from teachers import Teachers


class Lesson:
    def __init__(self, lesson_name="", lesson_id=-1):
        self.lesson_name = lesson_name
        self.lesson_id = lesson_id
        self.student_ids = []
        self.teacher_ids = []

    def __str__(self):
        st = ""
        st += f"{('lesson_name: ' + self.lesson_name.upper())}" + "\n"
        st += f"{('lesson_id: ' + str(self.lesson_id))}" + "\n"
        st += f"{('student_ids: ' + str(self.student_ids))}" + "\n"
        st += f"{('teacher_ids: ' + str(self.teacher_ids))}" + "\n"
        return st

    def from_dict(self, lesson_dict):
        self.lesson_name = lesson_dict["lesson_name"]
        self.lesson_id = lesson_dict["lesson_id"]
        self.student_ids = lesson_dict["student_ids"]
        self.teacher_ids = lesson_dict["teacher_ids"]

    def to_dict(self):
        lesson_dict = {"lesson_name": self.lesson_name,
                       "lesson_id": self.lesson_id,
                       "student_ids": self.student_ids,
                       "teacher_ids": self.teacher_ids

                       }
        return lesson_dict

    def print_lesson_details(self, teachers, students):
        print(f"LESSON: {self.lesson_name.upper()} (id = {self.lesson_id})")
        print("TEACHERS: ", end="")
        teachers_list = []
        for teacher_id in self.teacher_ids:
            teacher = teachers.read_teacher(teacher_id)
            teachers_list.append(teacher.first_name + " " + teacher.surname)
        print(", ".join(teachers_list))
        print("STUDENTS: ", end="")
        students_list = []
        for student_id in self.student_ids:
            student = students.search_student_by_id(student_id)
            students_list.append(student.first_name + " " + student.surname)
        print(", ".join(students_list))
