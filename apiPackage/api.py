#api.py
 
# Name: Jake Elmore
# email: Elmorejc@mail.uc.edu
# Assignment Number: Assignment 9
# Due Date: April 04 2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Pulls an api
# Brief Description of what this module does. Creates a class with an api
# Citations: In class
# Anything else that's relevant:
 
import requests
import json
 
class myAPI:
    def __init__(self):
        #added self so that we could get the count_photos function tied to the myAPI object
        self.response = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=SaiSUTX86CuRN2lqBeZHs5k12rGx5TyhxfnaMku5')
        self.json_string = self.response.content
        self.parsed_json = json.loads(self.json_string)
       
    def count_photos(self):
        '''
        Count the number of photos in parsed_json.
        '''
        photos = self.parsed_json.get('photos', [])
        return len(photos)
