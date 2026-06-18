import json

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "marks": self.marks
        }


class StudentManagementSystem:
    FILE_NAME = "students.json"

    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)

                for student in data:
                    self.students.append(
                        Student(
                            student["roll_no"],
                            student["name"],
                            student["marks"]
                        )
                    )

        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump(
                [student.to_dict() for student in self.students],
                file,
                indent=4
            )

    def add_student(self):
        try:
            roll_no = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))

            student = Student(roll_no, name, marks)
            self.students.append(student)

            self.save_data()

            print("Student Added Successfully!")

        except ValueError:
            print("Invalid Input!")

    def view_students(self):
        if not self.students:
            print("No Students Found!")
            return

        for student in self.students:
            print("-" * 40)
            print("Roll No:", student.roll_no)
            print("Name:", student.name)
            print("Marks:", student.marks)

    def search_student(self):
        try:
            roll_no = int(input("Enter Roll No to Search: "))

            for student in self.students:
                if student.roll_no == roll_no:
                    print("Student Found")
                    print(student.roll_no)
                    print(student.name)
                    print(student.marks)
                    return

            print("Student Not Found!")

        except ValueError:
            print("Invalid Roll Number!")

    def delete_student(self):
        try:
            roll_no = int(input("Enter Roll No to Delete: "))

            for student in self.students:
                if student.roll_no == roll_no:
                    self.students.remove(student)
                    self.save_data()
                    print("Student Deleted!")
                    return

            print("Student Not Found!")

        except ValueError:
            print("Invalid Roll Number!")


sms = StudentManagementSystem()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.view_students()

    elif choice == "3":
        sms.search_student()

    elif choice == "4":
        sms.delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")