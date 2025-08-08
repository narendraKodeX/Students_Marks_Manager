# Create a dictionary called "students" to hold student data
students = {}

#function to add a student to the dictionary
def add_student(name, marks):
    pass

#Function to view all students
def view_students():
    pass

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        #choice the user
        choice = input("Enter your choice: \n")

        if choice == '1':
            name = input("Enter student name: \n")
            marks = input("Enter student marks: \n")
            add_student(name,marks)

        elif choice =='2':
            view_students()

        elif choice =='3':
            print("Goodbye!!")
            break

            


