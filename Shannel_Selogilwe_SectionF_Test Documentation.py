# TESTING DOCUMENTATION

# Test 1: Normal Case
# Input:
#   Number of students: 2
#   Student 1
#   Student 2
# Expected output:
#   - Students added successfully
#   - Correct averages each student
#   - Class average
# Result: Continue

# Test 2: Invalid Grade Input
# Input:  Grade between 0 and 100 = -10
# Input:  Grade between 0 and 100 = 150
# Expected:raises ValueError = Prompts "Enter a grade between 0 and 100" until valid input.
# Result: Continue

#  TEST 3: Duplicate Student
# Input: Add "Shannel" twice
# Expected: raises DuplicateStudentError = “Student 'Shannel' already exists!”
# Result:  Continue

# TEST 4: Remove Non-existent Student
# Input: Remove "Selogilwe" when not in class
# Expected: raises StudentNotFoundError = “Student not found!”
# Result:  Continue

# TEST 5: Sort by Name
# Input: Students [Zain,Anitah, Mailo]
# Input: Grades for all 3 subjects
# Expected Order: Anitah, Mailo, Zain. Alphabetical order with grades and average
# Result:  Continue

#  TEST 6: Sort by Subject
# Input: "Enter subject name"
# Initial Input of subject grades: [89,70,30]
# Input ordered to : grades [30, 70, 89]
# Expected: Sorted descending order by Math scores.
# Result:  Continue

# TEST 7: Search Non-Existent Subject
# Input: Subject = "History"
# Expected: raises SubjectNotFound = “Subject not found!”
# Result:  Continue

#  TEST 8: Empty Gradebook
# Input: Display results with no students
# Expected: raise EmptyGradeBookError = "No student data."
# Result: Continue

#  TEST 9: Update Student Grades
# Input: Update "Shannel’s" grades from 88,60,72 → 90,76,70
# Expected: Updated successfully, new average 78.67
# Result:  Continue

# TEST 10: Handle Non-numeric Input
# Input: Grade = "abc"
# Expected: “Invalid input, enter a number”
# Result: Continue

# TEST 11: Search Non-existent Student
# Input: Search student “Debbie”
# Expected: raises StudentNotFoundError = “Student not found!”
# Result:  Continue

#  TEST 12: Add Student with Empty Name
# Input: Name = " "
# Expected:raises InvalidGradeError = “name is empty.”
# Result: Continue

#  TEST 13: Remove Student with Empty Name
# Input: Name = " "
# Expected: raises InvalidGradeError = “Name cannot be empty!”
# Result:  Continue

#  TEST 14: Sort by Average with Empty Gradebook
# Input: " "
# Expected:raises EmptyGradebookError → “No students found!”
# Result: Continue

#  TEST 15: Display Results with Students
# Input: Students input with grades
# Expected:
#   - Displays each student with grades and average
#   - Displays class average
#   - Displays max and min per subject
# Result: Continue

# TEST 16: Sort by Subject with No Grades
# Input: Subject = "Math" but no students yet
# Expected: raises EmptyGradebookError → “No students found!”
# Result:  Continue

#  TEST 17: Update Non-existent Student
# Input: Update student “Alex”
# Expected: StudentNotFoundError → “Student not found!”
# Result:    Continue

# TEST 18: Search Existing Student
# Input: Search student “John”
# Expected: Displays John’s grades and average
# Result:    Continue

#  TEST 19: Exit Program
# Input: Choice outside menu = anything from number outside 1 and 8 to words or letters
# Expected: Prints “Invalid choice, please try again.”
# Result:  Continue


# Section F

# Custom Exceptions
class StudentNotFoundError(Exception): pass
class InvalidGradeError(Exception): pass
class EmptyGradebookError(Exception): pass
class DuplicateStudentError(Exception): pass
class SubjectNotFound(Exception): pass


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


# Class Gradebook
class Gradebook:
    def __init__(self, subjects):
        self.subjects = subjects
        self.students = {}

    @staticmethod
    def input_grade():
        while True:
            try:
                g = float(input("Enter grade between 0 and 100: "))
                if 0 <= g <= 100:
                    return g
                print("Enter a grade between 0 and 100")
            except ValueError:
                print("Invalid input, enter a number")
#add more students to class
    def add_student(self):
        try:
            name = input("Input student name: ").strip()
            if not name:
                raise InvalidGradeError(" name is empty.")
            if name in self.students:
                raise DuplicateStudentError(f"Student '{name}' already exists!")

            s = Student(name)
            for subject in self.subjects:
                s.add_grade(subject, self.input_grade())

            self.students[name] = s
            print("Student added!")
            return True

        except (InvalidGradeError, DuplicateStudentError) as e:
            print(e)
            return False
#update existing student
    def update_student(self):
        try:
            name = input("Update which student name?: ").strip()
            if name not in self.students:
                raise StudentNotFoundError("Student not found!")

            s = self.students[name]
            s.grades = {}
            for subject in self.subjects:
                s.add_grade(subject, self.input_grade())

            print("Student updated!")
            return True

        except StudentNotFoundError as e:
            print(e)
            return False
#remove student from gradebook
    def remove_student(self):
        try:
            name = input("Remove which student name: ").strip()

            if not name:
                raise InvalidGradeError("Name cannot be empty!")
            if name not in self.students:
                raise StudentNotFoundError("Student not found!")

            del self.students[name]
            print("Student removed!")
            return True

        except (InvalidGradeError, StudentNotFoundError) as e:
            print(e)
            return False
#search student
    def search_student(self):
        try:
            name = input("Student name to search: ").strip()
            if not name:
                raise InvalidGradeError("Name cannot be empty!")
            if name not in self.students:
                raise StudentNotFoundError("Student not found!")

            self.students[name].details()
            return True

        except (InvalidGradeError, StudentNotFoundError) as e:
            print(e)
            return False
#view by subject
    def view_by_subject(self):
        try:
            subject = input("Input subject name: ").strip().capitalize()
            if not subject:
                raise InvalidGradeError("Subject cannot be empty!")
            if subject not in self.subjects:
                raise SubjectNotFound("Subject  not found!")

            print(f"{subject} grades:")
            for s in self.students.values():
                print(f"  {s.name}: {s.grades.get(subject, 'No grade awarded')}")

            return True

        except (InvalidGradeError, SubjectNotFound) as e:
            print(e)
            return False
#sort by average
    def sort_by_average(self):
        try:
            if not self.students:
                raise EmptyGradebookError("No students found!")
            ranked = sorted(self.students.values(), key=lambda x: x.average(), reverse=True)
            print("Students sorted by average:")
            for s in ranked:
                print(f"{s.name}: {s.average():}")

            return True

        except EmptyGradebookError as e:
            print(e)
            return False
#sort by subject
    def sort_by_subject(self, subject):
        try:
            subject = subject.strip().capitalize()
            if not self.students:
                raise EmptyGradebookError("No students found!")
            if subject not in self.subjects:
                raise SubjectNotFound(f"Subject '{subject}' not found!")

            ranked = sorted(self.students.values(), key=lambda x: x.grades.get(subject, 0), reverse=True)
            print(f"Students sorted by {subject}:")

            for s in ranked:
                print(f"{s.name}: {s.grades.get(subject, 'No grade awarded')}")

            return True

        except (EmptyGradebookError, SubjectNotFound) as e:
            print(e)
            return False
#sort by name and use bubble sort
    def sort_by_name(self):
        try:
            if not self.students:
                raise EmptyGradebookError("No students to sort!")

            students_list = list(self.students.values())
            n = len(students_list)

            for i in range(n):
                for j in range(0, n - i - 1):
                    if students_list[j].name > students_list[j + 1].name:
                        students_list[j], students_list[j + 1] = students_list[j + 1], students_list[j]

            print("Students sorted by name:")

            for s in students_list:
                print(f"{s.name}: {s.grades}, Avg: {s.average():}")

            return True

        except EmptyGradebookError as e:
            print(e)
            return False

    # Display all results
    def display_results(self):
        if not self.students:
            print("No student data.")
            return False

        for s in self.students.values():
            s.details()

        class_avg = sum(s.average() for s in self.students.values()) / len(self.students)
        print(f"Class avg: {class_avg:}")

        for subj in self.subjects:
            scores = [s.grades[subj] for s in self.students.values() if subj in s.grades]
            if scores:
                print(f"{subj}: Max={max(scores)}, Min={min(scores)}")
        return True

# Main Program
def main():
    subjects = ["Math", "English", "Science"]
    book = Gradebook(subjects)

    try:
        for _ in range(int(input("Enter number of students in a class: "))):
            book.add_student()
    except ValueError:
        print("Invalid number.")

    while True:
        print("\n1= Add Student "
              "\n2= Update Student "
              "\n3= Remove Student"
              "\n4= Search Subject "
              "\n5= Search Student "
              "\n6= AvgSort "
              "\n7= SubjSort "
              "\n8= SortByName"
              "\n9= Display results")

        print()
        c = input("Enter choice 1-8: ")

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
            book.sort_by_subject(input("Subject: "))
        elif c == "8":
            book.sort_by_name()
        elif c == "9":
            book.display_results()
            break
        else:
            print("Invalid choice, please try again.")

main()


