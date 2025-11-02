# SECTION A

#Student Data Entry - ask for number of students in class
num_students = int(input("Enter total number of students in a class: "))
total_grade = 0  #to calculate total for grade calculation ( used later)

for i in range(num_students):  #loop to process input for multiple students being entered
    name = input("Enter the name of student: ")  #ask for student name

    #Basic Validation
    grade = float(input("Enter Math grade between 0 and 100: "))  #ask to input  single grade
    while grade < 0 or grade > 100:  #validate grade to only input values within range 0-100
        print("Invalid grade. Please enter a number between 0 and 100.")
        grade = float(input("Enter Math grade between 0 and 100: "))

    #Display each student’s name along with their grade
    print()
    print("Name:", name, "Grade:", grade)
    print()

    total_grade = total_grade + grade #add grade to total for class average

#Grade Calculation, display overall class average
average = total_grade / num_students
print("Total of all grades:", total_grade)
print("Class average:", average)
print()




