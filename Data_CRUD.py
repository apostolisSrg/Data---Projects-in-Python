students = [
    {
        "id": 1001,
        "name": "Will",
        "surname": "Buyers",
        "father-name": "Thomas",
        "age": 8,
        "school-class": 4,
        "id_number": "AH12345"
    },
    {
        "id": 1002,
        "name": "John",
        "surname": "Waldo",
        "father-name": "Ken",
        "age": 10,
        "school-class": 6,
        "id_number": "AH12323"
    },
    {
        "id": 1003,
        "name": "Lucas",
        "surname": "Kennedy",
        "father-name": "Harry",
        "age": 9,
        "school-class": 5,
        "id_number": "AH12313"
    }
]


def create_student():
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
        for student in students:
            if n_name == student["name"] and n_surname == student["surname"] and n_father_name == \
                    student["father-name"]:
                print("Im sorry , but i noticed that a student with these characteristics already exists: ")
                print(f"{student} \n")
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

        student = {"id": next_id(), "name": n_name, "surname": n_surname, "father-name": n_father_name,
                   "age": int_age, "school-class": school_class, "id_number": n_id_number}
        students.append(student)
        return student


def next_id():
    ids = []
    for student in students:
        ids.append(student["id"])
    return max(ids) + 1


def print_students_details():
    print("")
    print("        Students:")
    for student in students:
        print_student(student)


def print_students_name():
    print("")
    print("  Students names-fnames-surnames:")
    for student in students:
        print(f"{student['name']} ", end="")
        print(f"{student['father-name'][0] + '.'}", end="")
        print(f"{student['surname']}", end="")
        print("")
    print("")


def print_student_by_id():
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
        for student in students:
            if student["id"] == n_user_input:
                print_student(student)
                print("Successful Print!")
                found = True
                stop = True
        if not found:
            print("This id doesn't exist.Try again.")
            stop = True


def print_student(student):
    print(f"+{24 * '-'}+")
    print(f"| {('id: ' + str(student['id'])).ljust(23)}|")
    print(f"| {('name: ' + student['name']).ljust(23)}|")
    print(f"| {('surname: ' + student['surname']).ljust(23)}|")
    print(f"| {('father-name: ' + student['father-name']).ljust(23)}|")
    print(f"| {('age: ' + str(student['age'])).ljust(23)}|")
    print(f"| {('school-class: ' + str(student['school-class'])).ljust(23)}|")
    print(f"| {('id_number: ' + student['id_number']).ljust(23)}|")
    print(f"+{24 * '-'}+")


def search_student_by_surname(surname):
    surname_list = []
    for student in students:
        if student["surname"] == surname:
            surname_list.append(student)
    return surname_list


def search_student_by_id(id):
    for student in students:
        if student["id"] == id:
            return student
    return None


def student_update(student):
    print_student(student)
    print("Type what you want to change")
    print("+------------------+")
    print("|1 - 'name'        |")
    print("|2 - 'surname'     |")
    print("|3 - 'father-name' |")
    print("|4 - 'age'         |")
    print("|5 - 'school-class'|")
    print("|6 - 'id_number'   |")
    print("+------------------+")
    while True:
        choose = input("Choose from 1 to 6: ")
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
        student["name"] = new_name
    elif update == 2:
        while True:
            new_surname = input("Give a new surname: ")
            new_surname = new_surname.strip()
            if new_surname.isalpha():
                new_surname = new_surname.title()
                break
            else:
                print("only characters please!")
        student["surname"] = new_surname
    elif update == 3:
        while True:
            new_father_name = input("Give a  new father name: ")
            new_father_name = new_father_name.strip()
            if new_father_name.isalpha():
                new_father_name = new_father_name.title()
                break
            else:
                print("only characters please!")
        student["father-name"] = new_father_name
    elif update == 4:
        while True:
            new_age = input("Give a new age: ")
            if new_age.isdigit():
                new_int_age = int(new_age)
                break
            else:
                print("Only numbers please..")
        student["age"] = new_int_age
    elif update == 5:
        while True:
            new_school_class = int(input("Give a new school-class: "))
            while new_school_class < 1 or new_school_class > 6:
                print("between 1 and 6 please: ")
                new_school_class = int(input("Give a new school-class: "))
            break
        student["school-class"] = new_school_class
    else:
        while True:
            new_id_number = input("Give aa new id number: ")
            new_id_number = new_id_number.strip()
            if new_id_number.isalnum():
                new_id_number = new_id_number.upper()
                break
            else:
                print("only characters or numbers please!")
        student["id_number"] = new_id_number


def delete_student_by_id(id):
    for i in range(len(students)):
        if students[i]["id"] == id:
            students.pop(i)
            return


def main():
    global int_student_id
    while True:
        print("+----Menu----+")
        print("|1 - Create  |")
        print("|2 - Print   |")
        print("|3 - Update  |")
        print("|4 - Delete  |")
        print("|5 - Exit    |")
        print("+------------+")
        while True:
            choose = input("Choose from 1 to 5: ")
            if not choose.isdigit():
                print("only numbers..")
                continue
            else:
                number = int(choose)
            if number < 1 or number > 5:
                print("between 1 and 5 please..")
                continue
            else:
                break
        if number == 1:
            create_student()
            print(f"Successful Process! n student added with id: {next_id() - 1}")
        elif number == 2:
            while True:
                print("1 - Print student")
                print("2 - Print all students")
                print("3 - Print the names of the students only")
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
                print_student_by_id()
            elif number == 2:
                print_students_details()
            else:
                print_students_name()
        elif number == 3:
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
                student = search_student_by_id(int_student_id)
                if student is None:
                    print("Error!No student with this id.Back to main Menu")
                    continue
            elif number == 2:
                while True:
                    surname = input("Give a surname: ")
                    surname = surname.strip()
                    if surname.isalpha():
                        n_surname = surname.title()
                        break
                    else:
                        print("only characters please!")
                matching_list = search_student_by_surname(n_surname)
                if not matching_list:
                    print("There are no students with this surname")
                elif len(matching_list) == 1:
                    student = matching_list[0]
                else:
                    print("I noticed that are more than 1 students with this surname. Here they are: ")
                    for s in matching_list:
                        print_student(s)
                        print(f"id = {s['id']}")
                        print("-" * 15)
                    while True:
                        student_id = input("Give student id: ")
                        if student_id.isdigit():
                            int_student_id = int(student_id)
                            break
                        else:
                            print("Only numbers please..")
                    student = search_student_by_id(int_student_id)
            student_update(student)
            print_student(student)
            print("student Updated!")
        elif number == 4:
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
                student = search_student_by_id(int_student_id)
                if student is None:
                    print("Error!No student with this id.Back to main Menu")
                    continue
            elif number == 2:
                while True:
                    surname = input("Give a surname: ")
                    surname = surname.strip()
                    if surname.isalpha():
                        n_surname = surname.title()
                        break
                    else:
                        print("only characters please!")
                matching_list = search_student_by_surname(n_surname)
                if not matching_list:
                    print("There are no students with this surname")
                elif len(matching_list) == 1:
                    student = matching_list[0]
                else:
                    print("I noticed that are more than 1 students with this surname. Here they are: ")
                    for s in matching_list:
                        print_student(s)
                        print(f"id = {s['id']}")
                        print("-" * 15)
                    while True:
                        student_id = input("Give student id: ")
                        if student_id.isdigit():
                            int_student_id = int(student_id)
                            break
                        else:
                            print("Only numbers please..")
                for s in matching_list:
                    if int_student_id == s["id"]:
                        student = search_student_by_id(int_student_id)
                        break
                else:
                    print("Error!You should type the proper id from the ids where given above.Back to main Menu.")
                    continue
            print_student(student)
            delete_student_by_id(int_student_id)
            print("      Student Deleted!")
        else:
            print("")
            return print("--Program Terminated from User--")


main()
