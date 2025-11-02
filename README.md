# Python Student Grade Management System 

# Project Overview

The Student Grade Management System is a Python  application designed for managing student grades . It allows users to insert, edit, delete, and search for students; provide grade tracking across multiple subjects, calculate averages, and list students based on name, subject, and overall performance.

This system developed continuosly, starting with basic input processing and loops at section A and B, moved on to lists at section C, at section D dictionaries, and functions at section E, and finally object-oriented programming and exception handling in Section F. The resulting program is robust, user-friendly, and extensively tested with respect to invalid inputs, duplicate entries, and empty data sets.

# Objectives

-**Digital Grade Management: Provide a system to store and manage student grades .

-**Create , delete, update and read  Operations: Enable users to Create, Read, Update, and Delete student records.

-**Data Validation: Ensure input is valid and within expected ranges.

-**Error Handling: Handle errors such as duplicate students, missing subjects, or invalid inputs with the use of custom exceptions.

-**Analysis & Sorting: Calculate averages, class statistics, and allow sorting by name, subject, or overall average.

-**Modular & Maintainable Code: Use functions, classes, and clear code structure for easy readability and maintenance.

-**Testing: Verify that all functionalities work correctly through multiple test cases for normal and edge cases.

# Section Descriptions and Integration

**Section A – Scalar Input & Loops
Introduced simple input handling, validation, and loops to collect class size, student names and grade for one subject to give  total of grades nd class average.This sets the foundation for managing data.

**Section B – Lists & Tuples
Expanded to store multiple subjects and grades per student using lists and tuples, enabling multi-subject management not just one. Builds on Section A by handling more complex data structures.

**Section C – Dictionaries
Introduced dictionaries to map students to their grades per subject, making data storage structured and searchable. This allows for more efficient retrieval and updates.Builds on section B. 

**Section D – Functions
Modularized code by creating reusable functions for adding, updating, and displaying grades. Functions make the program organized and easier to maintain.Build on section C. 

**Section E – Classes & OOP
Converted previous procedural code into object-oriented programming with Student and Gradebook classes. This encapsulates data and behavior, making the system more scalable.Builds on section E.

**Section F – Exceptions & Algorithms
Added robust error handling with custom exceptions, plus sorting and searching algorithms. This ensures reliability and handles edge cases. Section F integrates all prior sections into a complete, functional grade management system.Builds on section E and is the final intergrated code and well developed .

# How to Run the Program (PyCharm IDE)

-**Make sure a Python IDE environment is installed on your computer.

-**Recommended: Latest version of PyCharm .

-**Open the folder containing the program.

-**It should open directly in PyCharm.

 ## Run the program by either:

- **Selecting Run → ‘Shannel_Selogilwe_SectionF.py’ Or pressing Shift + F10.
  
-**Follow the Prompts

-**Enter the number of students.

-**Add grades for each student when prompted.

-**Use the menu options to:

1.Add a student

2.Update student grades

3.Remove a student

4.View grades by subject

5.Search for a student

6.Sort by average

7.Sort by subject

8.Sort by name

9.Display results

-**Exit the Program

Choose option 9 to display all results and automatically end the program.


## Expected output and input 

Enter number of students in a class: 2

Input student name: Shannel

Enter Math grade between 0 and 100: 80

Enter English grade between 0 and 100: 90

Enter Science grade between 0 and 100: 70

Student added!

Input student name: Arifa
Enter Math grade between 0 and 100: 50
Enter English grade between 0 and 100: 60
Enter Science grade between 0 and 100: 40
Student added!

1= Add Student 
2= Update Student 
3= Remove Student
4= Search Subject 
5= Search Student 
6= AvgSort 
7= SubjSort 
8= SortByName
9= Display results

Enter choice 1-8: 1
Enter name of student: Charlie 
Enter Math grade between 0 and 100: 27
Enter English grade between 0 and 100: 99
Enter Science grade between 0 and 100: 60
Student added !

Enter choice 1-8: 1
Enter name of student: lemy 
Enter Math grade between 0 and 100: 30
Enter English grade between 0 and 100: 20
Enter Science grade between 0 and 100: 10
Student added !

Enter choice 1-8: 2
Enter name of student: Charlie 
Enter Math grade between 0 and 100: 45
Enter English grade between 0 and 100: 67
Enter Science grade between 0 and 100: 89
Student updated !

Enter choice 1-8: 3
Enter name of student: Charlie  
Student Removed!

Enter choice 1-8: 4
Enter name of subject:English 
Shannel: English 90
Arifa: English 60

Enter choice 1-8: 5
Enter name of student:Shannel
Shannel: {'Math': 80, 'English': 90, 'Science': 70}, Avg: 80.0

Enter choice 1-8: 6
Students sorted by average:
Shannel: 80.0
Arifa: 50.0
Lemy: 20.0

Enter choice 1-8: 7
Subject: Math
Students sorted by Math:
Shannel: 80.0
Arifa: 50.0
Lemy: 30.0

Enter choice 1-8: 8
Students sorted by Name:
Arifa:{'Math': 50, 'English': 60, 'Science': 40}, Avg: 50.0 
Lemy: {'Math': 30, 'English': 20, 'Science': 10}, Avg: 20.0
Shannel: {'Math': 80, 'English': 90, 'Science': 70}, Avg: 80.0

Enter choice 1-8: 9
Shannel: {'Math': 80, 'English': 90, 'Science': 70}, Avg: 80.0
Arifa: {'Math': 50, 'English': 60, 'Science': 40}, Avg: 50.0
Lemy: {'Math': 30, 'English': 20, 'Science': 10}, Avg: 20.0

Class avg: 50.0
Math: Max=80, Min=30
English: Max=90, Min=20
Science: Max=70, Min=10


# Assumptions ( assumed the following are true):

-**Unique Student Names: Each student must have a unique name which mean duplicate names are not allowed.

-**Grade Range: Grades are assumed to be numeric values between 0 and 100 anything other than that is not accepted .

-**Subjects are fixed: The subjects are predefined as Math, English, and Science which mean we cannot add subjects of our own.

-**Class Size: The user inputs the number of students at the start this must be a positive integer.

-**The menu only has 9 options : only choose between 1 and 9 if not then user is told to try again. 

# Limitations ( my program cannot ) :

-**No Persistence: Student data is stored in memory only. Exiting the program will lose all entered data.
-**Case Sensitivity: Student names are case-sensitive when searching or updating (John ≠ john).

# Testing Summary:

## The system was tested under multiple scenarios including:

-**Normal input

-**Invalid grades

-**Duplicate students

-**Non-existent students

-**Empty gradebook

-**Updating grades

-**Sorting by average, subject, and name

 All tests continued successfully, confirming correct behavior for all functionalities.

## Special Instructions:

-**Run Environment: Requires  PyCharm and must be the latest version.

-**Menu Navigation: Use numeric options (1–9) to navigate the menu.

-**Ending the Program: Option 9 displays all results and exits automatically.

-**Correct Input Types: Always enter numeric grades and valid menu options. Invalid types will trigger error messages.
