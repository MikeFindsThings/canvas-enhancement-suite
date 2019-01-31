#!/usr/bin/env python3
#
# A Python script to:
# - interact directly with Canvis API
# - pass API calls to other modules
#
import requests
import argparse


parser = argparse.ArgumentParser(description="A Python script for interacting with the Canvas LMS API.")
parser.add_argument('-k','--api_key', type=str, required=True,
                  help='Canvas API key. Can be generated in Canvas settings.')
parser.add_argument('-u','--url', type=str,
                  help="Your institution's Canvas base URL (defaults to unt.instructure.com")

args = parser.parse_args()

if not args.url:
    args.url ='unt.instructure.com'

HEADERS = {'Authorization': f'Bearer {args.api_key}'}

API_URL = f'https://{args.url}/api/v1'

COURSES = requests.get(f'{API_URL}/courses', params=None, headers=HEADERS)

class Course:
    """Canvas organizes its data into courses
    
    The following attributes are useful to me now:
    ID
    Name
    Calendar (.ics)
    
    There are more attributes that do not appear useful now but can be added later
    """
    def __init__(self, name, id, calendar):
        self.name = name
        self.id = id
        self.calendar = calendar


def get_course(field):
    field = 'name'
    course_json = COURSES.json()
    if field == 'name':
        for course in course_json:
            print(course["name"])
            return(course['name'])


#get_course('name')
jeff = Courses('intro to bananas', 4, 'thisisacalander')
print (jeff.name)