# Create a dictionary called "students" to hold student data
students = {}

#function to add a student to the dictionary
def add_student(student_name,subject, marks):
    if student_name not in students:
        students[student_name] = {}
    students[student_name][subject] = int(marks)
    print(f"Added subject {subject} with marks {marks}")

#Function to view all students
def view_students(student_name=None):
    if not students:
        print("No students found")
        return
    
    if student_name:
        if student_name in students:
            print(f"\nStudent: {student_name}")
            for subject, marks in students[student_name].items():
                print(f"  {subject}: {marks}")
        else:
            print("Student not found")
    else:
        # Show all students
        for student, subjects in students.items():
            print(f"\nStudent: {student}")
            for subject, marks in subjects.items():
                print(f"  {subject}: {marks}")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")


        choice = input("Enter your choice: \n")

        if choice == '1':
            student_name = input("Enter student name: \n")
            subject = input("Enter subject name: \n")
            marks = input("Enter student marks: \n")
            add_student(student_name, subject, marks)

        elif choice == '2':
            name = input("Enter student name to view (leave empty for all): \n")
            if name.strip() == "":
                view_students()
            else:
                view_students(name.strip())

        elif choice == '3':
            print("Goodbye!!")
            break

        else:
            print("Invalid choice, try again.")


main()