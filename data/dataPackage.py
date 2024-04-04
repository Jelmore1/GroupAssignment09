# Name: Jared Turner
# email: turne2jw@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:04/04/2024
# Course/Section: IS4010-001
# Semester/Year: spring 2024
# Brief Description of the assignment:THis assignment uses an API to analyse data 
# Brief Description of what this module does. This module counts photos
# Citations: 
#https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
# Anything else that's relevant:

from apiPackage.api import *
def printInfo():
    myDict =myAPI
    photo_Count = myDict.count_photos()
    print("This is the total number of photos taken by the rover Curiosity, in Sol 1000, on Mars", photo_Count)

