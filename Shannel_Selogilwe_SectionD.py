# Section D : Modulerazaition with functions 

subjects = ["Math", "English", "Science"]
students = {} # stores student names and grades in a dictionary 

#Function to get grade
def get_grade(s):
    while True:
        try:
            g = float(input(f"{s} (0-100): "))
            if 0 <= g <= 100:
                return g
            print("Enter range between 0-100")
        except ValueError:                    #error handling
            print("Invalid input")


#Function to add student
def add_student():
    name = input("Student name: ")
    added_status = False

    if name not in students: # prevent duplication 
        # store objects and theri grades in dictioary 
        students[name] = {s: get_grade(s) for s in subjects} #re-use grade function
        added_status = True

    print("Student added!" if added_status else "Student already exists!")

#Function to update student
def update_student():
    name = input("Update which student name ?:  ")
    update_status = False

    if name in students: #check for non-existent students and update if student exist 
        students[name] = {s: get_grade(s) for s in subjects}
        update_status = True

    print("Student updated!" if update_status else "Student not found!")


#Function to remove student
def remove_student():
    name = input("Remove which student name ?:  ")
    removed_status = False

    if name in students:
        del students[name] #delete student record from the dictionary 
        removed_status = True

    print(" Student removed!" if removed_status else "Student not found.")

#Function to view the subject grades
def view_subject():
    sub = input("input subject name ").capitalize()
    is_absent = sub not in subjects # validate subject name 

    if is_absent:
        print(" Subject not found")
        return

    print(f"{sub} grades:")
    for name, grades in students.items(): #loop through each student
        print(f"  {name}: {grades[sub]}") #display the subject grade 
 

#Function to search the student and display there grades
def search_student():
    name = input("Student name to search: ")
    is_missing = name not in students #validate for missing student 

    if is_missing:
        print("Student not found.")
        return

    grades = students[name]
    print(f"{name}: {grades}") #display individual grades 
    print(f"Average: {sum(grades.values()) / len(grades):}") #calculate average 

#Function to display results , Modularization and error handling
def display_results():
    if not students:
        print("No data available.")  #handle empty data error
        return
#display each students grade and average 
    for name, g in students.items():
        print(f"{name}: {g}, Avg: {sum(g.values())/len(g):}")
# class average calculated 
    class_avg = sum(sum(g.values()) for g in students.values()) / (len(students)*len(subjects))
    print(f"Class average: {class_avg:}")
#show max and min scores for each subject 
    for sub in subjects:
        scores = [g[sub] for g in students.values()]
        print(f"{sub}: Max={max(scores)}, Min={min(scores)}")


#Modularization  reuse add_student() function to initialize data
for _ in range(int(input("Enter total number of students ?: "))): add_student()
print()

# calls functions based on user choice
while True:
    print("1-Add  2-Update  3-Remove  4-View Subject  5-Search  6-Display Results ")
    choice = input("Choose: ")
    print()

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        view_subject()
    elif choice == "5":
        search_student()
    elif choice == "6":
        display_results() # exit with the show of results 
        break
    else:

        print("Invalid choice. Try again.")
