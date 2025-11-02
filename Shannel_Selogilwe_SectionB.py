# SECTION B

total_students = int(input("Enter total number of students in a class: "))

total_grades = 0

#Multiple subjects
subjects = ["Math", "English", "Science"]  #list for subjects for each student in the class
students = []  #list to store each student in a class as a tuples

#Input each student's grades with validation
for i in range(total_students):
    name = input("Enter the name of student: ")
    grades = []  #list to store multiple grades for each student
    student_total = 0

    for subject in subjects:  #allow each student to have grades for all subjects
        grade = float(input(f"Enter {subject} grade between 0 and 100: "))
        while grade < 0 or grade > 100:
            print("Invalid grade. Please enter between 0 and 100.")
            grade = float(input(f"Enter {subject} grade between 0 and 100: "))

        grades.append(grade)      #grade is stored in a list
        student_total = student_total +grade
        total_grades = total_grades + grade

    students.append((name, grades, student_total))  #store data for students in tuple

#Enhanced output - student grades and average per student
print()
print("Student Grades, Averages, and Summary:")

for student in students:
    (name, grades, student_total) = student
    average = student_total / len(subjects)  #calculate average for each student

     #data display
    print("Name:", name) #display student name
    print("Math:", grades[0], "English:", grades[1], "Science:", grades[2]) #display grades
    print("Average:", average)  # display the average for all subjects
    print()

#Enhanced Output
average = total_grades / (total_students * len(subjects))  #ensures student has multiple grades like for 3 subjects
print("Total of all grades:", total_grades)
print("Class average:", average)
print()

#Determine and print highest and lowest grade for each subject
print("Highest and lowest grades per subject:")
for i in range(len(subjects)):
    subject = subjects[i]
    grades = [s[1][i] for s in students]  #get all grades for this subject

    print(subject, "Highest:", max(grades), "Lowest:", min(grades))  #print the highest and lowest garde
