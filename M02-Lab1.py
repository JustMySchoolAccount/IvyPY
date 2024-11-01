"""
Name: Ross Gandy
File Name: GPA.py
Desc: takes in user input to determine if a student's GPA gets them on the dean's list
"""
import string
#variable declaration
user_input = ""
gpa = 0.0
#main while loop, handles accepting user input, logic for Dean's list eligibility, and output.

while(True):
    user_input = input("What is the first and last name of the student?(Type ZZZ to close)\n")
    
    if(user_input == "ZZZ"):
        break
    
    gpa = float(input("What is the student's GPA? (From 0.0-4.0)\n"))
    gpa = round(gpa, 2)
    
    if(gpa >= 3.5 and gpa <= 4.0):
        print("Student " +user_input + " has a GPA of: " + str(gpa) + ", Which qualifies them for the Dean's list!\n")
    
    elif(gpa <3.5 and gpa >=0.0):
        print("Student " + user_input + " Has a GPA of: " + str(gpa) + ", Which does not qualify them for the Dean's list.\n")
    else:
        print("Please only input a GPA between 0.0 and 4.0.\n")
