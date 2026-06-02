import csv
import os

FILE_NAME = "students.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Department", "Age", "Marks"])


def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, dept, age, marks])

    print("Student Added Successfully!")


def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_student():
    sid = input("Enter Student ID to Search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        found = False
        for row in reader:
            if row[0] == sid:
                print("Student Found:", row)
                found = True

        if not found:
            print("Student Not Found")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")