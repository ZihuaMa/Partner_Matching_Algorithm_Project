"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

import functions
from functions import read_file
from classes import Person
import pandas as pd

def test_file_reading():

    assert type(read_file("./Partner_Matching_Survey_Data.xlsx")) == pd.core.frame.DataFrame
    

def test_class_Person_Init():
    df = pd.read_excel('./Partner_Matching_Survey_Data.xlsx', header = 0)
    person = Person(df.iloc[0],26)
    assert person.name == "Alexandra"
    assert person.gender == "Female"
    assert person.sameness["10"] == "Personality"
    

def test_class_Person_Reconfig():
    df = pd.read_excel('./Partner_Matching_Survey_Data.xlsx', header = 0)
    person = Person(df.iloc[0],26)
    person.reconfigure()
    assert person.grade == 1
    assert person.comparisons['20'] == 1
    


    

