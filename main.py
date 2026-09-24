students = []

def add():
    r = int(input("Enter roll no: "))
    n = input("Enter name: ")
    rm = input("Enter room no: ")
    f = float(input("Enter fees: "))

    data = {
        "roll": r,
        "name": n,
        "room": rm,
        "fees": f
    }

    students.append(data)
    print("Student added.")


def show():
    if len(students) == 0:
        print("No student records.")
    else:
        print("\nStudent Details")
        for x in students:
            print("Roll No:", x["roll"])
            print("Name:", x["name"])
            print("Room No:", x["room"])
            print("Fees:", x["fees"])
            print("-------------------")


def search():
    r = int(input("Enter roll no to search: "))

    for x in students:
        if x["roll"] == r:
            print("Roll No:", x["roll"])
            print("Name:", x["name"])
            print("Room No:", x["room"])
            print("Fees:", x["fees"])
            return

    print("Student not found.")


def update():
    r = int(input("Enter roll no to update: "))

    for x in students:
        if x["roll"] == r:
            x["name"] = input("Enter new name: ")
            x["room"] = input("Enter new room no: ")
            x["fees"] = float(input("Enter new fees: "))
            print("Details updated.")
            return

    print("Student not found.")


def delete():
    r = int(input("Enter roll no to delete: "))

    for x in students:
        if x["roll"] == r:
            students.remove(x)
            print("Student deleted.")
            return

    print("Student not found.")


while True:
    print("\nHOSTEL MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add()
    elif ch == "2":
        show()
    elif ch == "3":
        search()
    elif ch == "4":
        update()
    elif ch == "5":
        delete()
    elif ch == "6":
        print("Program ended.")
        break
    else:
        print("Wrong choice.")
