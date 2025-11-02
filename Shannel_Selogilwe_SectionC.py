# SECTION C

# prompt for number of students 
total_students = int(input("Enter total number of students in a class: "))
total_grades = 0


# Predifined subjects 
subjects = ["Math", "English", "Science"]
#dictionary for all students 
students = {}  

#collect student details and grades 
for i in range(total_students):
    name = input("Enter the name of student: ")
    grades = {}
    student_total = 0

    #input validation 
    for subject in subjects:
        grade = float(input(f"Enter {subject} grade between 0 and 100: "))
        while grade < 0 or grade > 100:
            print("Invalid grade. Please enter value between 0 and 100.")
            grade = float(input(f"Enter {subject} grade between 0 and 100: "))

        grades[subject] = grade
        student_total = student_total +grade
        total_grades = total_grades + student_total

        students[name] = {"grades": grades, "total": student_total}
print()

# add new student
add_more = input("Add a new student? (yes/no): ").lower()
while add_more == "yes":
    name = input("Enter the name of student: ")
    grades = {}
    student_total = 0

    for subject in subjects:
        grade = float(input(f"Enter {subject} grade between 0 and 100: "))
        while not (0 <= grade <= 100):
            print(f"Invalid grade. Please enter value between 0 and 100 for {subject}.")
            grade = float(input(f"Enter {subject} grade between 0 and 100: "))

        grades[subject] = grade
        student_total = student_total + grade

    total_grades = total_grades + student_total
    students[name] = {"grades": grades, "total": student_total}

    print("student added successfully")
    add_more = input("Add another student? (yes/no): ")

print()

#display all student grades and averages 
print("Student Grades, Averages, and Summary:")

for student, records in students.items():
    grade = records["grades"]
    average= records["total"] / len(subjects)

    print(f"Name: {student}")
    print(f"Math: {grade['Math']}, English: {grade['English']}, Science: {grade['Science']}")
    print(f"Average: {average:}")
    print()

#class average 
average = total_grades / (len(students) * len(subjects))
print("Total of all grades:", total_grades)
print("Class average:", average)
print()

# extend the dictionary to handle multiple subjects and allow viewing of grades per subject 
print("Highest and lowest grades per subject:")
for subject in subjects:
    scores = [s["grades"][subject] for s in students.values()]
    print(f"{subject}: Highest {max(scores)}, Lowest {min(scores)}")
print()

#Update student grades
update = input("Would you like to update a student's grades? (yes/no): ")
if update == "yes":
    while True:
        name = input("Enter the student's name to update: ")

        if name in students:
            new_grades = {}
            student_total = 0
            for subject in subjects:
                grade = float(input(f"Enter {subject} grade between 0 and 100: "))
                while grade < 0 or grade > 100:
                    print("Invalid grade. Please enter value between 0 and 100.")
                    grade = float(input(f"Enter {subject} grade between 0 and 100: "))
                new_grades[subject] = grade
                student_total = student_total +grade

            total_grades = total_grades - students[name]["total"] + student_total
            students[name] = {"grades": new_grades, "total": student_total}
            print(name + "'s grades updated!")
        else:
            print("Student not found. Try again.")

        update = input("Update another student? (yes/no): ")
        if update != "yes":
            break
print()

# Remove student
remove = input("Would you like to remove a student? (yes/no): ")
if remove == "yes":
    while True:
        remove = input("Enter the student's name to remove: ") .strip()

        if remove in students:
            total_grades = total_grades - students[remove]["total"]
            del students[remove]
            print("Student has been removed.")
        else:
            print("Student not found. Try again.")

        another = input("Remove another student? (yes/no): ") .strip()
        if another != "yes":
            break

print()
# View subject-specific grades for all students 
view = input("Would you like to view grades for a subject? (yes/no): ")
if view == "yes":
    while True:
        subject = input("Enter subject name: ") .strip() .capitalize()
        if subject in subjects:
            print("Grades for " + subject + ":")
            for student, record in students.items():
                print(student + ": " + str(record["grades"][subject]))
        else:
            print("Invalid subject. Try again.")

        another = input("View another subject? (yes/no): ").strip().lower()
        if another != "yes":
            break

print()
# Search student for data accessing to retrive specific student grades and averages 
if input("Would you like to search for a student? (yes/no): ") == "yes":
    while True:
        search_name = input("Enter student's name: ").strip()
        if search_name in students:
            grades = students[search_name]["grades"]
            average = sum(grades.values()) / len(subjects)
            print(" " + search_name + "'s Grades and Average:")
            for subject, grade in grades.items():
                print(subject + " " + str(grade))
            print("Average: " + str(average))
        else:
            print("Student not found. Try again.")

        another = input("Search another student? (yes/no): ").strip()
        if another != "yes":
            break

