import json
from student import Student


class Students:
    def __init__(self):
        try:
            with open("students.json") as f:
                students_list = json.load(f)

                self.students = []
            for student_dict in students_list:
                s = Student()
                s.from_dict(student_dict)
                self.students += [s]
        except FileNotFoundError:
            self.students = []

    def save_students_data(self):
        list_to_write = []
        for student in self.students:
            list_to_write += [student.to_dict()]

        with open("students.json", "w") as f:
            json.dump(list_to_write, f)

    def student_next_id(self):
        if not self.students:
            return 1
        else:
            ids = []
            for student in self.students:
                ids.append(student.student_id)
            return max(ids) + 1

    # 1 - Create Mode

    def create_student(self):
        while True:
            while True:
                name = input("Give a name: ")
                name = name.strip()
                if name.isalpha():
                    n_name = name.title()
                    break
                else:
                    print("only characters please!")
            while True:
                surname = input("Give a surname: ")
                surname = surname.strip()
                if surname.isalpha():
                    n_surname = surname.title()
                    break
                else:
                    print("only characters please!")
            while True:
                father_name = input("Give a father name: ")
                father_name = father_name.strip()
                if father_name.isalpha():
                    n_father_name = father_name.title()
                    break
                else:
                    print("only characters please!")
            stop = False
            stop1 = False
            for student in self.students:
                if n_name == student.first_name and n_surname == student.surname and n_father_name == \
                        student.father_name:
                    print("Im sorry , but i noticed that a student with these characteristics already exists: ")
                    print(f"{student} \n")  # it will print in default mode 2
                    while True:
                        choice = input("Do you wish to continue? Type 'yes' or 'no: ")
                        if choice.isalpha():
                            choice = choice.lower().strip()
                            if choice == "yes":
                                break
                            elif choice == "no":
                                stop = True
                                break
                            else:
                                print("Type 'yes or 'no' please..")
                        else:
                            print("Only characters please..")
                    if stop:
                        stop1 = True
                        break
            if stop1:
                continue
            while True:
                age = input("Give age: ")
                if age.isdigit():
                    int_age = int(age)
                    break
                else:
                    print("Only numbers please..")
            while True:
                school_class = input("Give school-class: ")
                if school_class.isdigit():
                    int_school_class = int(school_class)
                    if int_school_class < 1 or int_school_class > 6:
                        print("between 1 and 6 please: ")
                        continue
                    else:
                        break
                else:
                    print("Only numbers please..")
            while True:
                id_number = input("Give an id number: ")
                id_number = id_number.strip()
                if id_number.isalnum():
                    n_id_number = id_number.upper()
                    break
                else:
                    print("only characters or numbers please!")

            s = Student(self.student_next_id(), n_name, n_surname, n_father_name, int_age, int_school_class,
                        n_id_number)
            self.students.append(s)
            return s

    # 2 - Print Modes

    # Print Mode 1
    def print_student_by_id(self):
        found = False
        stop = False
        while True:
            if stop:
                break
            user_input = input("Give me the id of the student: ")
            if not user_input.isdigit():
                print("only numbers..")
                continue
            else:
                n_user_input = int(user_input)
            for student in self.students:
                if student.student_id == n_user_input:
                    print("")
                    print(" Students -- Print Mode 1")
                    print(student)
                    print("Successful Print!")
                    print("")
                    found = True
                    stop = True
            if not found:
                print("This id doesn't exist.Try again.")
                stop = True

    # Print Mode 2
    def __str__(self):
        st = "" + "\n"
        st += " Students -- Print Mode 2" + "\n"
        for student in self.students:
            st += str(student) + "\n"
        return st

    # Print Mode 3
    def print_students_name(self):
        print("")
        print("Students -- Print Mode 3")
        print("+------------------------+")
        for student in self.students:
            print("-", end="")
            print(f"{student.first_name} ", end="")
            print(f"{student.father_name[0] + '.'}", end="")
            print(f"{student.surname}", end="")
            print("")
        print("+------------------------+")
        print("")


    # Search Methods

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student_by_surname(self, surname):
        surname_list = []
        for student in self.students:
            if student.surname == surname:
                surname_list.append(student)
        return surname_list

    # 3 - Update Mode

    def student_update(self, student):
        print(student)
        print("1 - 'first_name'")
        print("2 - 'surname'")
        print("3 - 'father-name'")
        print("4 - 'age'")
        print("5 - 'school-class'")
        print("6 - 'id_number'")
        print("")
        while True:
            choose = input("Type what you want to change from the student above.\nChoose from 1 to 6: ")
            if not choose.isdigit():
                print("only numbers..")
                continue
            else:
                update = int(choose)
            if update < 1 or update > 6:
                print("between 1 and 6 please..")
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
            student.first_name = new_name
        elif update == 2:
            while True:
                new_surname = input("Give a new surname: ")
                new_surname = new_surname.strip()
                if new_surname.isalpha():
                    new_surname = new_surname.title()
                    break
                else:
                    print("only characters please!")
            student.surname = new_surname
        elif update == 3:
            while True:
                new_father_name = input("Give a  new father name: ")
                new_father_name = new_father_name.strip()
                if new_father_name.isalpha():
                    new_father_name = new_father_name.title()
                    break
                else:
                    print("only characters please!")
            student.father_name = new_father_name
        elif update == 4:
            while True:
                new_age = input("Give a new age: ")
                if new_age.isdigit():
                    new_int_age = int(new_age)
                    break
                else:
                    print("Only numbers please..")
            student.age = new_int_age
        elif update == 5:
            while True:
                new_school_class = int(input("Give a new school-class: "))
                while new_school_class < 1 or new_school_class > 6:
                    print("between 1 and 6 please: ")
                    new_school_class = int(input("Give a new school-class: "))
                break
            student.school_class = new_school_class
        else:
            while True:
                new_id_number = input("Give aa new id number: ")
                new_id_number = new_id_number.strip()
                if new_id_number.isalnum():
                    new_id_number = new_id_number.upper()
                    break
                else:
                    print("only characters or numbers please!")
            student.id_number = new_id_number

    # 4 - Delete Mode
    def delete_student_by_id(self, student_id, lessons):
        for i in range(len(self.students)):
            if self.students[i].student_id == student_id:
                self.students.pop(i)
                # Delete the lessons in which Student maybe was part of
                lessons_student_was_part_of = []
                for lesson in lessons.lessons:
                    if student_id in lesson.student_ids:
                        lesson.student_ids.remove(student_id)
                        lessons_student_was_part_of.append(lesson.lesson_name)
                return lessons_student_was_part_of

    # adjust ids after delete
    def adjust_student_ids(self, deleted_student_id):
        ids = []
        for student in self.students:
            ids.append(student.student_id)
        min_id = min(ids)
        if deleted_student_id < min_id:
            self.students[0].student_id = deleted_student_id
            for i in range(1, len(self.students)):
                self.students[i].student_id = deleted_student_id + i
            return self
        else:
            self.students[0].student_id = min_id
            for i in range(1, len(self.students)):
                self.students[i].student_id = min_id + i
            return self
