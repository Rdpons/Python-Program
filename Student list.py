from os import system
filename:str = "students.txt"
def addstudent():
    system("cls")
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    with open(filename, 'a') as f:
        idno = input("Enter IdNo: ")
        lastName = input("Enter Last Name: ")
        firstName = input("Enter First Name: ")
        course = input("Enter Course: ")
        yearLevel = input("Enter Year Level: ")
        entry = f" Id No: {idno}, Last Name: {lastName}, First Name: {firstName}, Course: {course}, Year Level: {yearLevel}\n"
        f.write(entry)
    print("Student added Successfully")
def findstudent():
    system("cls")
    print("-------------------------")
    print("        Find Student     ")
    print("-------------------------")
    studentFind = input("Enter IdNo. to search: ")
    found = False
    with open(filename, 'r') as f:
        for line in f:
            if f" Id No: {studentFind}," in line:
                print("Student Found: ")
                print(line.strip())
                found = True
                break
    if not found:
        print(f"Id No {studentFind} is not found.")
def updatestudent():
    system("cls")
    print("---------------------------")
    print("      Update Student     ")
    print("---------------------------")
    studentUpdate = input("Enter IdNo to update: ")
    students = []
    updated = False
    with open(filename, 'r') as f:
        for line in f:
            if f" Id No: {studentUpdate}," in line:
                newLastName = input("Enter updated Student LastName: ")
                newFirstName = input("Enter updated Student FirstName: ")
                newCourse = input("Enter updated Student Course: ")
                newYearLvl = input("Enter updated Student Year Level: \n")
                updatedLine = f"Id No: {studentUpdate}, Last Name: {newLastName}, First Name: {newFirstName}, Course: {newCourse}, Year Level: {newYearLvl}\n"
                students.append(updatedLine)
                updated = True
            else:
                students.append(line)
    if updated:
        with open(filename, 'w') as f:
            f.writelines(students)
        print(f"Id No {studentUpdate} is updated.")
    else:
        print(f"Id No {studentUpdate} is not found.")
def removestudent():
    system("cls")
    print("-------------------------")
    print("      Remove Student    ")
    print("-------------------------")
    studentDelete = input("Enter IdNo to Delete: ")
    students = []
    deleted = False
    with open(filename, 'r') as f:
        for line in f:
            if f"Id No: {studentDelete}," not in line:
                students.append(line)
                print(line.strip())
            else:
                deleted = True
    if deleted:
        with open(filename, 'w') as f:
            f.writelines(students)
        print(f"Id No {studentDelete} deleted.")
    else:
        print(f"Id No {studentDelete} not found.")
def displayallstudent():
    system("cls")
    with open(filename, 'r') as f:
        print("List of Students:")
        for line in f:
            print(line.strip())
    input("Press Enter to continue...")
def displaymenu():
    print("------- Main Menu -------")
    print("1. Add Student")
    print("2. Find Student")
    print("3. Update Student")
    print("4. Remove Student")
    print("5. Display All Student")
    print("0. Quit/End")
    print("-------------------------")
def main():
    while True:
        displaymenu()
        option = input("Enter Option (0..5): ")
        if option == "0":
            print("----------------")
            print("Goodbye!")
            print("----------------")
            break
        elif option == "1":
            addstudent()
        elif option == "2":
            findstudent()
        elif option == "3":
            updatestudent()
        elif option == "4":
            removestudent()
        elif option == "5":
            displayallstudent()
            f = open(filename)
            index = 1
            for item in f:
                fields:list = item.split(",")
                print(index)
                print(" ",fields[0])
                print(" ",fields[1])
                print(" ",fields[2])
                print(" ",fields[3])
                print(" ",fields[4], )
                index += 1
            f.close()
        else:
            print("Invalid option. Please choose a valid option (0..5).")
if _name_ == "_main_":
    main()
