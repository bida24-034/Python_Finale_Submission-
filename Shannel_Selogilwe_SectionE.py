# Section E

# Class Student
class Student:
    def __init__(self, name):
        self.name, self.grades = name, {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0

    def details(self):
        print(f"{self.name}: {self.grades}, Avg: {self.average():}")

# class Gradebook
class Gradebook:
    def __init__(self, subjects):
        self.subjects = subjects
        self.students = {}

    @staticmethod
    def input_grade(s):
        while True:
            try:
                g = float(input("Enter garde between 0 and 100 "))
                if 0 <= g <= 100:
                    return g
                print("Enter grades between 0 and 100")
            except ValueError:
                print("Invalid input")

    # Add student
    def add_student(self):
        name = input("Input student name: ").strip()
        added_status = False

        if not name:
            print("Cannot add student")
            return False

        if name not in self.students:
            s = Student(name)
            for subject in self.subjects:
                s.add_grade(subject, self.input_grade(subject))
            self.students[name] = s
            added_status = True

        print("Student added!" if added_status else "student already exists!")
        return added_status

    # Update student
    def update_student(self):
        name = input("Update which student name?: ").strip()
        update_status = False

        if name in self.students:
            s = self.students[name]
            s.grades = {}
            for subject in self.subjects:
                s.add_grade(subject, self.input_grade(subject))
            update_status = True

        print("Student updated!" if update_status else "student not found!")
        return update_status

    # Remove student
    def remove_student(self):
        name = input("Remove which student name: ")
        removed_status = False

        if not name:
            print(" name cannot be empty!")
            return False

        if name in self.students:
            del self.students[name]
            removed_status = True

        print("Student removed!" if removed_status else " student not found!")
        return removed_status

    # Search for student
    def search_student(self):
        name = input("Student name to search: ").strip()
        found_status = False

        if not name:
            print(" name cannot be empty!")
            return False

        if name in self.students:
            self.students[name].details()
            found_status = True

        print("Student found!" if found_status else " student not found!")
        return found_status

    # View grades by subject
    def view_by_subject(self):
        subject = input("Input subject name: ").capitalize()
        found_status = False

        if not subject:
            print("Cannot view: subject cannot be empty!")
            return False

        if subject in self.subjects:
            print(f"{subject} grades:")
            for s in self.students.values():
                print(f"  {s.name}: {s.grades.get(subject, 'No grade awarded')}")
            found_status = True

        print("Subject found!" if found_status else "Cannot view: subject not found!")
        return found_status

    # Sort students by average
    def sort_by_average(self):
        if not self.students:
            print("Student not found")
            return False

        ranked = sorted(self.students.values(), key=lambda x: x.average(), reverse=True)
        for s in ranked:
            print(f"{s.name}: {s.average():.2f}")
        return True

    # Sort by specific subject
    def sort_by_subject(self, subject):
        if not self.students:
            print("No subject data.")
            return False

        if subject not in self.subjects:
            print("Subject not found")
            return False

        ranked = sorted(self.students.values(), key=lambda x: x.grades.get(subject, 0), reverse=True)
        for s in ranked:
            print(f"{s.name}: {s.grades.get(subject, 'No grade awarded')}")
        return True

    # Display all results
    def display_results(self):
        if not self.students:
            print("No student data.")
            return

        for s in self.students.values():
            s.details()

        class_avg = sum(s.average() for s in self.students.values()) / len(self.students)
        print(f"Class avg: {class_avg:}")

        for subj in self.subjects:
            scores = [s.grades[subj] for s in self.students.values() if subj in s.grades]
            if scores:
                print(f"{subj}: Max={max(scores)}, Min={min(scores)}")

def main():
    subjects = ["Math", "English", "Science"]
    book = Gradebook(subjects)

    try:
        for _ in range(int(input("Enter number of students in a class: "))):
            book.add_student()
    except ValueError:
        print("Invalid number.")

    while True:
        print ("\n1= Add Student "           
               "\n2= Update Student  "  
               "\n3= Remove Student"
               "\n4= Search Subject "
               "\n5= Search Student "
               "\n6= AvgSort "
               "\n7= SubjSort "              
               "\n8= Display results")
        print()
        c = input("Enter choice 1-8:")

        if c == "1":
            book.add_student()
        elif c == "2":
            book.update_student()
        elif c == "3":
            book.remove_student()
        elif c == "4":
            book.view_by_subject()
        elif c == "5":
            book.search_student()
        elif c == "6":
            book.sort_by_average()
        elif c == "7":
            book.sort_by_subject(input("Subject: ").capitalize())
        elif c == "8":
            book.display_results()
            break
        else:
            print("Invalid choice , please try again.")

main()