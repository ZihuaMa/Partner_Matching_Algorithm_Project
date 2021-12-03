"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
import pandas as pd
sys.path.append('../')

# Imports
from my_module.functions import sex_ori, location, diff_prefer, sameness, constellations, comparisons, create_match, read_file
from my_module.classes import Person
###
###

#function that would match a person to all of the rest of the participants
#RUN THIS
def match():
    file_name = input("Enter the .xlsx file to be processed")   
    num_parti = input("Enter the number of entries in the file")
    index = input("Enter the index of the person you want to render a match file")
    df = read_file(file_name)
    target = dict()
    for i in range(int(num_parti)):
        target[str(i)] = Person(df.iloc[i],int(num_parti))
        target[str(i)].reconfigure()
    person = target[index]
    temp = target.pop(index)
    sex_ori(person,target)
    location(person,target)
    constellations(person,target)
    diff_prefer(person,target)
    sameness(person,target)
    comparisons(person,target)
    match_file = create_match(person,df)
    print("Matching results for: ",person.name)
    print(match_file)


