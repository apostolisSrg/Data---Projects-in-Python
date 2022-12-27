from teachers import Teachers
from students import Students
from lessons import Lessons


def main():
    students = Students()
    teachers = Teachers()
    lessons = Lessons()
    while True:
        print("+-----Main-Menu-----+")
        print("|1 - Edit Students  |")
        print("|2 - Edit Teachers  |")
        print("|3 - Edit Lessons   |")
        print("|4 - Exit           |")
        print("+-------------------+")
        while True:
            choose = input("Choose from 1 to 4: ")
            if not choose.isdigit():
                print("only numbers..")
                continue
            else:
                number = int(choose)
            if number < 1 or number > 4:
                print("between 1 and 4 please..")
                continue
            else:
                break
        if number == 1:
            print("+----Students-Menu----+")
            print("|1 - Create Students  |")
            print("|2 - Print Students   |")
            print("|3 - Update Students  |")
            print("|4 - Delete Students  |")
            print("+---------------------+")
            while True:
                choose = input("Choose from 1 to 4: ")
                if not choose.isdigit():
                    print("only numbers..")
                    continue
                else:
                    number = int(choose)
                if number < 1 or number > 4:
                    print("between 1 and 4 please..")
                    continue
                else:
                    break
            if number == 1:
                students.create_student()
                print("")
                print(f"Successful Process! New student added with id: {students.student_next_id() - 1}")
                print("")
            elif number == 2:
                if not students.students:
                    print("")
                    print("There are no students in Database! Back to Main Menu")
                    print("")
                else:
                    while True:
                        print("+------------Print-Menu-------------+")
                        print("|1 - Print Student                  |")
                        print("|2 - Print all Students             |")
                        print("|3 - Print Students in special form |")
                        print("+-----------------------------------+")
                        choose = input("Choose from 1 to 3: ")
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
                        students.print_student_by_id()
                    elif number == 2:
                        print(students)
                    else:
                        students.print_students_name()
            elif number == 3:
                if not students.students:
                    print("")
                    print("There are no students in Database! Back to Main Menu")
                    print("")
                else:
                    while True:
                        print("1 - Search by 'id'")
                        print("2 - Search by 'surname'")
                        choose = input("Choose from 1 to 2: ")
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
                        while True:
                            student_id = input("Select the id of a student: ")
                            if student_id.isdigit():
                                int_student_id = int(student_id)
                                break
                            else:
                                print("Only numbers please..")
                        student = students.search_student_by_id(int_student_id)
                        if student is not None:
                            students.student_update(student)
                            print("")
                            print(f"Student with id: {student.student_id} Updated!")
                            print("")
                        else:
                            print("")
                            print("Error!No student with this id.Back to Main-Menu...")
                            print("")
                            continue
                    else:
                        while True:
                            surname = input("Give a surname: ")
                            surname = surname.strip()
                            if surname.isalpha():
                                n_surname = surname.title()
                                break
                            else:
                                print("only characters please!")
                        matching_list = students.search_student_by_surname(n_surname)
                        if not matching_list:
                            print("")
                            print("There are no students with this surname")
                            print("Back to Main-Menu...")
                            print("")
                        elif len(matching_list) == 1:
                            student = matching_list[0]
                        else:
                            print("I noticed that are more than one students with this surname. Here they are: ")
                            for s in matching_list:
                                print("")
                                print(f"student_id = {s.student_id}")
                                print(s)
                            while True:
                                student_id = input("Give the proper 'student_id' from the matching list above: ").strip()
                                if student_id.isdigit():
                                    new_int_id = int(student_id)
                                    break
                                else:
                                    print("Only numbers please..")
                            for s in matching_list:
                                if new_int_id == s.student_id:
                                    student = students.search_student_by_id(new_int_id)
                                    break
                            else:
                                print("")
                                print("Error!You should type the proper id from the ids where given above.Back to"
                                      " Main-Menu...")
                                print("")
                                continue
                        students.student_update(student)
                        print("")
                        print(f"Student with surname: {student.surname} and student_id: {student.student_id} Updated!")
                        print("")
            else:
                if not students.students:
                    print("")
                    print("There are no students in Database! Back to Main Menu")
                    print("")
                else:
                    while True:
                        print("1 - Delete by 'id'")
                        print("2 - Delete by 'surname'")
                        choose = input("Choose from 1 to 2: ")
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
                        while True:
                            student_id = input("Select the id of a student: ")
                            if student_id.isdigit():
                                int_student_id = int(student_id)
                                break
                            else:
                                print("Only numbers please..")
                        student = students.search_student_by_id(int_student_id)
                        if student is not None:
                            lessons_student_was_part_of = students.delete_student_by_id(student.student_id, lessons)
                            print("")
                            student_n_sn = student.first_name + " " + student.surname
                            print(f"Student {student_n_sn} with student_id: {student.student_id} deleted!")
                            if not lessons_student_was_part_of:
                                print(f"{student.first_name} did not attend any lessons..")
                                print("")
                            else:
                                st = ", ".join(lessons_student_was_part_of)
                                print(f"Also {student.first_name} deleted from lessons: {st}.")
                                print("")
                            students.adjust_student_ids(student.student_id)
                        else:
                            print("")
                            print("Error!No student with this id.Back to Main-Menu...")
                            print("")
                            continue
                    else:
                        while True:
                            surname = input("Give a surname: ")
                            surname = surname.strip()
                            if surname.isalpha():
                                n_surname = surname.title()
                                break
                            else:
                                print("only characters please!")
                        matching_list = students.search_student_by_surname(n_surname)
                        if not matching_list:
                            print("")
                            print("There are no students with this surname")
                            print("Back to Main-Menu...")
                            print("")
                            continue
                        elif len(matching_list) == 1:
                            student = matching_list[0]
                        else:
                            print("I noticed that are more than one students with this surname. Here they are: ")
                            for s in matching_list:
                                print("")
                                print(f"student_id = {s.student_id}")
                                print(s)
                            while True:
                                student_id = input("Give the proper 'student_id' from the matching list above: ").strip()
                                if student_id.isdigit():
                                    new_int_id = int(student_id)
                                    break
                                else:
                                    print("Only numbers please..")
                            for s in matching_list:
                                if new_int_id == s.student_id:
                                    student = students.search_student_by_id(new_int_id)
                                    break
                            else:
                                print("")
                                print("Error!You should type the proper id from the ids where given above.Back to "
                                      "Main-Menu...")
                                print("")
                                continue
                        lessons_student_was_part_of = students.delete_student_by_id(student.student_id, lessons)
                        print("")
                        student_n_sn = student.first_name + " " + student.surname
                        print(f"Student {student_n_sn} with student_id: {student.student_id} deleted!")
                        if not lessons_student_was_part_of:
                            print(f"{student.first_name} did not attend any lessons..")
                            print("")
                        else:
                            st = ", ".join(lessons_student_was_part_of)
                            print(f"Also {student.first_name} deleted from lessons: {st}.")
                            print("")
                        students.adjust_student_ids(student.student_id)
        elif number == 2:
            print("+----Teacher-Menu----+")
            print("|1 - Create Teacher  |")
            print("|2 - Print Teacher   |")
            print("|3 - Update Teacher  |")
            print("|4 - Delete Teacher  |")
            print("+--------------------+")
            while True:
                choose = input("Choose from 1 to 4: ")
                if not choose.isdigit():
                    print("only numbers..")
                    continue
                else:
                    number = int(choose)
                if number < 1 or number > 4:
                    print("between 1 and 4 please..")
                    continue
                else:
                    break
            if number == 1:
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
                teachers.create_teacher(n_name, n_surname)
                print("")
                print(f"Successful Process! new teacher added with id:{teachers.next_id() - 1}")
                print("")
            elif number == 2:
                if not teachers.teachers:
                    print("")
                    print("There are not teachers in Database!. Back to Main Menu")
                    print("")
                else:
                    while True:
                        print("+-------Print-Menu--------+")
                        print("|1 - Print Teacher        |")
                        print("|2 - Print all Teachers   |")
                        print("+-------------------------+")
                        choose = input("Choose from 1 to 2: ")
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
                        while True:
                            user_input = input("Give me the id of the teacher: ")
                            if not user_input.isdigit():
                                print("only numbers..")
                                continue
                            else:
                                n_user_input = int(user_input)
                                break
                        teacher = teachers.read_teacher(n_user_input)
                        if teacher is not None:
                            print("")
                            print(teacher)
                            print("")
                        else:
                            print("")
                            print("This id doesn't exist.Back to Main-Menu.")
                            print("")
                    else:
                        print("")
                        print(teachers)
                        print("")
            elif number == 3:
                if not teachers.teachers:
                    print("")
                    print("There are not teachers in Database!. Back to Main Menu")
                    print("")
                else:
                    while True:
                        user_input = input("Give me the id of the teacher: ")
                        if not user_input.isdigit():
                            print("only numbers..")
                            continue
                        else:
                            n_user_input = int(user_input)
                            break
                    teacher = teachers.read_teacher(n_user_input)
                    if teacher is not None:
                        teachers.update_teacher(teacher)
                        print("")
                        print(f"teacher with id: {teacher.teacher_id} Updated!")
                        print("")
                    else:
                        print("")
                        print("This id doesn't exist.Back to Main-Menu...")
                        print("")
            else:
                if not teachers.teachers:
                    print("")
                    print("There are not teachers in Database!. Back to Main Menu")
                    print("")
                else:
                    while True:
                        user_input = input("Give me the id of the teacher: ")
                        if not user_input.isdigit():
                            print("only numbers..")
                            continue
                        else:
                            n_user_input = int(user_input)
                            break
                    teacher = teachers.read_teacher(n_user_input)
                    if teacher is not None:
                        teacher_n_sn = teacher.first_name + " " + teacher.surname
                        lessons_teacher_was_part_of = teachers.delete_teacher(teacher.teacher_id, lessons)
                        print("")
                        print(f"Teacher {teacher_n_sn} deleted!")
                        if not lessons_teacher_was_part_of:
                            print(f"{teacher.first_name} was not teaching any lesson..")
                            print("")
                        else:
                            st = ", ".join(lessons_teacher_was_part_of)
                            print(f"Also {teacher.first_name} deleted from lessons: {st}.")
                            print("")
                        teachers.adjust_teacher_ids(teacher.teacher_id)
                    else:
                        print("")
                        print("This id doesn't exist.Back to Main-Menu.")
                        print("")
        elif number == 3:
            print("+----Lessons-Menu----+")
            print("|1 - Create Lessons  |")
            print("|2 - Print Lessons   |")
            print("|3 - Update Lessons  |")
            print("|4 - Delete Lessons  |")
            print("+--------------------+")
            while True:
                choose = input("Choose from 1 to 4: ")
                if not choose.isdigit():
                    print("only numbers..")
                    continue
                else:
                    number = int(choose)
                if number < 1 or number > 4:
                    print("between 1 and 4 please..")
                    continue
                else:
                    break
            if number == 1:
                while True:
                    lesson = input("Give a name for the new lesson: ").strip()
                    if not lesson.isalpha():
                        print("Type only characters!")
                    else:
                        new_lesson = lesson.title()
                        break
                lessons.create_lesson(new_lesson)
                print("")
                print(f"Lesson {new_lesson} successfully created!")
                print("")
            elif number == 2:
                if not lessons.lessons:
                    print("")
                    print("There are no lessons in Database! Back to Main Menu")
                    print("")
                else:
                    print("+---------Print-Menu-----------+")
                    print("|1 - Print Lesson with details |")
                    print("|2 - Print all Lessons         |")
                    print("+------------------------------+")
                    while True:
                        choose = input("Choose from 1 to 2: ")
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
                        while True:
                            user_input = input("Give the id of the Lesson: ")
                            if not user_input.isdigit():
                                print("only numbers..")
                                continue
                            else:
                                n_user_input = int(user_input)
                                break
                        lesson = lessons.read_lesson(n_user_input)
                        if lesson is not None:
                            print("")
                            lesson.print_lesson_details(teachers, students)
                            print("")
                        else:
                            print("")
                            print("This Lesson id doesn't exist.Back to Main-Menu.")
                            print("")
                    else:
                        print("")
                        lessons.print_lessons()
                        print("")
            elif number == 3:
                if not lessons.lessons:
                    print("")
                    print("There are no lessons in Database! Back to Main Menu")
                    print("")
                else:
                    while True:
                        user_input = input("Give the id of the Lesson: ")
                        print("")
                        if not user_input.isdigit():
                            print("only numbers..")
                            continue
                        else:
                            n_user_input = int(user_input)
                            break
                    lesson = lessons.read_lesson(n_user_input)
                    if lesson is not None:
                        lessons.update_lesson(n_user_input, teachers, students)
                    else:
                        print("")
                        print("This Lesson id doesn't exist.Back to Main-Menu.")
                        print("")
            else:
                if not lessons.lessons:
                    print("")
                    print("There are no lessons in Database! Back to Main Menu")
                    print("")
                else:
                    while True:
                        user_input = input("Give the id of the Lesson: ")
                        if not user_input.isdigit():
                            print("only numbers..")
                            continue
                        else:
                            n_user_input = int(user_input)
                            break
                    lesson = lessons.read_lesson(n_user_input)
                    if lesson is not None:
                        lessons.delete_lesson(n_user_input)
                        print("")
                        print(f"Lesson {lesson} Deleted!")
                        print("")
                        lessons.adjust_lesson_ids()
                    else:
                        print("")
                        print("This Lesson id doesn't exist.Back to Main-Menu.")
                        print("")
        else:
            students.save_students_data()
            teachers.save_teachers_data()
            lessons.save_lessons_data()
            print("")
            print("~Program Terminated from User~")
            return


try:
    main()
except KeyboardInterrupt as f:
    print("\n\n~There was an unexpected termination of the program.No save was made~")
