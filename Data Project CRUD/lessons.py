import json
from lesson import Lesson


class Lessons:
    def __init__(self):
        try:
            with open("lessons.json") as f:
                lessons_list = json.load(f)

                self.lessons = []
            for lesson_dict in lessons_list:
                l = Lesson()
                l.from_dict(lesson_dict)
                self.lessons += [l]
        except FileNotFoundError:
            self.lessons = []

    def save_lessons_data(self):
        list_to_write = []
        for lesson in self.lessons:
            list_to_write += [lesson.to_dict()]

        with open("lessons.json", "w") as f:
            json.dump(list_to_write, f)

    def next_id(self):
        if not self.lessons:
            return 1
        else:
            ids = []
            for l in self.lessons:
                ids.append(l.lesson_id)
            return max(ids) + 1

    # 1 - Create Mode
    def create_lesson(self, lesson_name):
        for lesson in self.lessons:
            if lesson.lesson_name == lesson_name:
                print("Error. Lesson already exists! ")
                return None

        l = Lesson(lesson_name, self.next_id())
        self.lessons.append(l)
        return l

    def read_lesson(self, lesson_id):
        for lesson in self.lessons:
            if lesson_id == lesson.lesson_id:
                return lesson
        else:
            return None

    # 2 - Print Mode
    def print_lessons(self):
        cnt = 1
        for lesson in self.lessons:
            print(f"{cnt}) {lesson.lesson_name} (id = {lesson.lesson_id})")
            cnt += 1

    # 3 - Update Mode
    def update_lesson(self, lesson_id, teachers, students):
        for lesson in self.lessons:
            if lesson_id == lesson.lesson_id:
                lesson.print_lesson_details(teachers, students)
                print("")
                choose = input("Update 1-Name, 2-Teachers, 3-Students: ")
                while True:
                    if not choose.isdigit():
                        print("only numbers..")
                        continue
                    else:
                        number = int(choose)
                    if number < 1 or number > 3:
                        print("between 1 and 3 please..")
                        continue
                    else:
                        break
                if number == 1:
                    while True:
                        name = input("Give a  new name: ")
                        name = name.strip()
                        if name.isalpha():
                            n_name = name.title()
                            break
                        else:
                            print("only characters please!")
                    lesson.lesson_name = n_name
                elif number == 2:
                    while True:
                        choose = input("Updating lesson teachers: 1-add, 2-remove: ")
                        if not choose.isdigit():
                            print("only numbers..")
                            continue
                        else:
                            number = int(choose)
                        if number < 1 or number > 2:
                            print("between 1 and 2 please..")
                            continue
                        else:
                            break
                    if number == 1:
                        not_applied_teachers = []
                        print("")
                        print("Teachers (not in lesson): ")
                        for teacher in teachers.teachers:
                            if teacher.teacher_id not in lesson.teacher_ids:
                                not_applied_teachers.append(teacher.teacher_id)
                                print(f"(id = {teacher.teacher_id}) -> {teacher.first_name} {teacher.surname}")
                        print("")
                        while True:
                            upd_teacher_id = input("Pick the (id) to add: ").strip()
                            if not upd_teacher_id.isdigit():
                                print("only numbers..")
                                continue
                            else:
                                upd_teacher_id = int(upd_teacher_id)
                                break
                        if upd_teacher_id in not_applied_teachers:
                            lesson.teacher_ids.append(upd_teacher_id)
                            teacher = teachers.read_teacher(upd_teacher_id)
                            print("")
                            print(f"Teacher {teacher.first_name} {teacher.surname} will also teach {lesson.lesson_name}")
                            print("")
                        else:
                            print("")
                            print("Error! You should pick from (ids) where given above")
                            print("")
                    elif number == 2:
                        del_lesson_teachers = []
                        print("")
                        print("Lesson Teachers: ")
                        for teacher_id in lesson.teacher_ids:
                            del_lesson_teachers.append(teacher_id)
                            teacher = teachers.read_teacher(teacher_id)
                            print(f"(id = {teacher.teacher_id}) -> {teacher.first_name} {teacher.surname}")
                        print("")
                        if del_lesson_teachers:
                            while True:
                                upd_teacher_id = input("Pick the (id) to delete: ").strip()
                                if not upd_teacher_id.isdigit():
                                    print("only numbers..")
                                    continue
                                else:
                                    upd_teacher_id = int(upd_teacher_id)
                                    break
                            if upd_teacher_id in del_lesson_teachers:
                                lesson.teacher_ids.remove(upd_teacher_id)
                                teacher = teachers.read_teacher(upd_teacher_id)
                                print("")
                                print(f"Teacher {teacher.first_name} {teacher.surname} deleted from lesson"
                                      f" {lesson.lesson_name}")
                                print("")
                            else:
                                print("")
                                print("Error! You should pick from (ids) where given above")
                                print("")
                else:
                    while True:
                        choose = input("Updating lesson students: 1-add, 2-remove: ")
                        if not choose.isdigit():
                            print("only numbers..")
                            continue
                        else:
                            number = int(choose)
                        if number < 1 or number > 2:
                            print("between 1 and 2 please..")
                            continue
                        else:
                            break
                    if number == 1:
                        not_applied_students = []
                        print("")
                        print("Students(not in lesson): ")
                        for student in students.students:
                            if student.student_id not in lesson.student_ids:
                                not_applied_students.append(student.student_id)
                                print(f"(id = {student.student_id}) -> {student.first_name} {student.surname}")
                        print("")
                        while True:
                            upd_student_id = input("Pick the (id) to add: ").strip()
                            if not upd_student_id.isdigit():
                                print("only numbers..")
                                continue
                            else:
                                upd_student_id = int(upd_student_id)
                                break
                        if upd_student_id in not_applied_students:
                            lesson.student_ids.append(upd_student_id)
                            student = students.search_student_by_id(upd_student_id)
                            print("")
                            print(f"Student {student.first_name} {student.surname} applied to lesson {lesson.lesson_name}")
                            print("")
                        else:
                            print("")
                            print("Error! You should pick from (ids) where given above")
                            print("")
                    elif number == 2:
                        del_lesson_students = []
                        print("Lesson Students: ")
                        for student_id in lesson.student_ids:
                            del_lesson_students.append(student_id)
                            student = students.search_student_by_id(student_id)
                            print(f"(id = {student.student_id}) -> {student.first_name} {student.surname}")
                        if del_lesson_students:
                            while True:
                                upd_student_id = input("Pick the (id) to delete: ").strip()
                                if not upd_student_id.isdigit():
                                    print("only numbers..")
                                    continue
                                else:
                                    upd_student_id = int(upd_student_id)
                                    break
                            if upd_student_id in del_lesson_students:
                                lesson.student_ids.remove(upd_student_id)
                                student = students.search_student_by_id(upd_student_id)
                                print("")
                                print(f"Student {student.first_name} {student.surname} deleted from lesson {lesson}")
                                print("")
                            else:
                                print("")
                                print("Error! You should pick from (ids) where given above")
                                print("")
                    break

    # 4 - Delete Mode
    def delete_lesson(self, lesson_id):
        for i in range(len(self.lessons)):
            if lesson_id == self.lessons[i].lesson_id:
                self.lessons.pop(i)
                return
        else:
            print("No lesson with this id!")

    # adjust ids after delete
    def adjust_lesson_ids(self):
        ids = []
        for lesson in self.lessons:
            ids.append(lesson.lesson_id)
        min_id = min(ids)
        self.lessons[0].lesson_id = min_id
        for i in range(1, len(self.lessons)):
            self.lessons[i].lesson_id = min_id + i
        return self
