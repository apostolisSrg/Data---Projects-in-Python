import json
from teacher import Teacher


class Teachers:
    def __init__(self):
        try:
            with open("teachers.json") as f:
                teachers_list = json.load(f)

            self.teachers = []
            for teacher_dict in teachers_list:
                t = Teacher()
                t.from_dict(teacher_dict)
                self.teachers += [t]
        except FileNotFoundError:
            self.teachers = []


    def save_teachers_data(self):
        list_to_write = []
        for teacher in self.teachers:
            list_to_write += [teacher.to_dict()]

        with open("teachers.json", "w") as f:
            json.dump(list_to_write, f)

    def next_id(self):
        if not self.teachers:
            return 1
        else:
            ids = []
            for t in self.teachers:
                ids.append(t.teacher_id)
            return max(ids) + 1

    # 1 - Create Mode
    def create_teacher(self,first_name, surname):
        for teacher in self.teachers:
            if first_name == teacher.first_name and surname == teacher.surname:
                print("Im sorry , but i noticed that a teacher with these characteristics already exists: ")
                teacher.print_teacher()
                while True:
                    choice = input("Do you wish to continue? Type 'yes' or 'no: ")
                    if choice.isalpha():
                        choice = choice.lower().strip()
                        if choice == "yes":
                            t = Teacher(self.next_id(), first_name, surname,)
                            self.teachers.append(t)
                            return t
                        elif choice == "no":
                            return "Back to Main menu"
                        else:
                            print("Type 'yes or 'no' please..")
                    else:
                        print("Only characters please..")
        else:
            t = Teacher(self.next_id(), first_name, surname)
            self.teachers.append(t)
            return t

    # 2 - Print Modes
    def __str__(self):
        st = "" + "\n"
        st += " Teachers -- Print Mode 2" + "\n"
        for teacher in self.teachers:
            st += str(teacher) + "\n"
        return st

    # Search Method
    def read_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                return teacher
        else:
            return None

    # 3 - Update Mode
    def update_teacher(self, teacher):
        print(teacher)
        print("")
        print("1 - 'first_name'")
        print("2 - 'last_name'")
        while True:
            choose = input("Type what you want to change from the teacher above.\nChoose from 1 to 2: ")
            if not choose.isdigit():
                print("only numbers..")
                continue
            else:
                update = int(choose)
            if update < 1 or update > 2:
                print("between 1 and 2 please..")
                continue
            else:
                break
        if update == 1:
            while True:
                new_name = input("Give a new name: ")
                new_name = new_name.strip()
                if new_name.isalpha():
                    new_name = new_name.title()
                    break
                else:
                    print("only characters please!")
            teacher.first_name = new_name
        else:
            while True:
                new_surname = input("Give a new surname: ")
                new_surname = new_surname.strip()
                if new_surname.isalpha():
                    new_surname = new_surname.title()
                    break
                else:
                    print("only characters please!")
            teacher.surname = new_surname

    # 4 - Delete Mode
    def delete_teacher(self, teacher_id, lessons):
        for i in range(len(self.teachers)):
            if teacher_id == self.teachers[i].teacher_id:
                self.teachers.pop(i)
                # Delete the lessons in which Teacher maybe was part of
                lessons_teacher_was_part_of = []
                for lesson in lessons.lessons:
                    if teacher_id in lesson.teacher_ids:
                        lesson.teacher_ids.remove(teacher_id)
                        lessons_teacher_was_part_of.append(lesson.lesson_name)
                return lessons_teacher_was_part_of
        else:
            print("No teacher with this id!")

    # adjust ids after delete
    def adjust_teacher_ids(self, deleted_teacher_id):
        ids = []
        for teacher in self.teachers:
            ids.append(teacher.teacher_id)
        min_id = min(ids)
        if deleted_teacher_id < min_id:
            self.teachers[0].teacher_id = deleted_teacher_id
            for i in range(1, len(self.teachers)):
                self.teachers[i].teacher_id = deleted_teacher_id + i
            return self
        else:
            self.teachers[0].teacher_id = min_id
            for i in range(1, len(self.teachers)):
                self.teachers[i].teacher_id = min_id + i
            return self
