import csv
FILE_NAME = "students.csv"
def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    maths = int(input("Maths Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))
    with open(FILE_NAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, maths, science, english])
    print(" Student added successfully!")
def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
def generate_report():
    roll = input("Enter Roll No: ")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] == roll:
                marks = list(map(int, row[2:]))
                total = sum(marks)
                avg = total / len(marks)
                if avg >= 90:
                    grade = 'A'
                elif avg >= 75:
                    grade = 'B'
                elif avg >= 50:
                    grade = 'C'
                else:
                    grade = 'Fail'
                print("Report Card")
                print("Name:", row[0])
                print("Total:", total)
                print("Average:", avg)
                print("Grade:", grade)
                return
    print(" Student not found")
while True:
    print("--- Student Report Generator ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Generate Report")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        generate_report()
    elif choice == '4':
        print(" Exiting...")
        break
    else:
        print("Invalid choice")
