import pandas as pd


"""A collection of function for doing my project."""


def sex_ori(person,target):
    
    '''
    This function considers the sex orientation of the two sides of the matches, if matched, a huge value will be added.
    Both sides of the matches will be taken into account for the particular person's match(meaning, if the target also matches
    the person's, another INF value will be added to their matching score.)

    Parameters
    ----------
    person: the Person object to be matched
    target: dictionary that contains the rest of the participants to be matched

    Returns
    -------
    returns True, indicating the function has run
    '''

    #iterate through all of the rest of the participants
    for index in list(target.keys()):

        #if A matches B
        if person.sex_ori == "Heterosexual" and target[index].gender != person.gender:
            person.scores[index] += person.INF
        elif person.sex_ori == "Bi-sexual":
            person.scores[index] += person.INF

        #if B matches A
        if target[index].sex_ori == "Heterosexual" and target[index].gender != person.gender:
            person.scores[index] += person.INF
        elif target[index].sex_ori == "Bi-sexual":
            person.scores[index] += person.INF
            
    return True



def location(person,target):

    '''
    This function considers the location of the two sides of the matches, if they are the same, 10 points will be added.
    Both sides of the matches will be taken into account for the particular person's match(meaning, if the target also matches
    the person's, another 10 will be added to their matching score.)

    Parameters
    ----------
    person: the Person object to be matched
    target: dictionary that contains the rest of the participants to be matched

    Returns
    -------
    returns True, indicating the function has run
    '''
    #iterate through all of the rest of the participants
    for index in list(target.keys()):
        #if A matches B
        if person.location == target[index].location:
                person.scores[index] += 10
    return True




#4-8
def diff_prefer(person,target):

    '''
    This function considers the diff_prefer of the two sides of the matches, if they are the same, 4 points will be added 
    for each question.
    Both sides of the matches will be taken into account for the particular person's match(meaning, if the target also matches
    the person's, another 4 will be added to their matching score.)

    Parameters
    ----------
    person: the Person object to be matched
    target: dictionary that contains the rest of the participants to be matched

    Returns
    -------
    returns True, indicating the function has run
    '''
    
    #iterate through all of the rest of the participants
    for index in list(target.keys()):
        #if A matches B
        if (person.age_diff_prefer == "Older_than_me" and target[index].age > person.age)\
            or (person.age_diff_prefer == "Similar_age" and target[index].age == person.age)\
            or (person.age_diff_prefer == "Younger_than_me" and target[index].age < person.age)\
            or (person.age_diff_prefer == "Do_not_care"):
                person.scores[index] += 4

        if (person.age_diff_prefer == "Higher_than_me" and target[index].height > person.height)\
            or (person.age_diff_prefer == "Shorter_than_me" and target[index].height == person.height)\
            or (person.age_diff_prefer == "Do_not_care" and target[index].height < person.height):
                person.scores[index] += 4
        
        #B matches A
        if (target[index].age_diff_prefer == "Older_than_me" and target[index].age < person.age)\
            or (target[index].age_diff_prefer == "Similar_age" and target[index].age == person.age)\
            or (target[index].age_diff_prefer == "Younger_than_me" and target[index].age > person.age)\
            or (person.age_diff_prefer == "Do_not_care"):
                person.scores[index] += 4

        if (target[index].age_diff_prefer == "Higher_than_me" and target[index].height < person.height)\
            or (target[index].age_diff_prefer == "Shorter_than_me" and target[index].height == person.height)\
            or (target[index].age_diff_prefer == "Do_not_care" and target[index].height > person.height):
                person.scores[index] += 4

    return True



#10-19
def sameness(person,target):

    '''
    This function considers the sameness of the two sides of the matches, if they are the same, 2 points will be added to each.
    Both sides of the matches will be taken into account for the particular person's match(meaning, if the target also matches
    the person's, another 2 will be added to their matching score.)

    Parameters
    ----------
    person: the Person object to be matched
    target: dictionary that contains the rest of the participants to be matched

    Returns
    -------
    returns True, indicating the function has run
    '''
    
    #organize all the questions into a dictionary
    questions = list(map(lambda x:str(x),list(range(10,20))))
    
    #iterate through all of the rest of the participants
    for index in list(target.keys()):
        for question in questions:
            #if A matches B
            if person.sameness[question] == target[index].sameness[question]:
                    person.scores[index] += 2

    return True




#9
def constellations(person,target):

    '''
    This function considers the constellations of the two sides of the matches, if they match, 8 points will be added.
    Both sides of the matches will be taken into account for the particular person's match(meaning, if the target also matches
    the person's, another 8 will be added to their matching score.)

    Parameters
    ----------
    person: the Person object to be matched
    target: dictionary that contains the rest of the participants to be matched

    Returns
    -------
    returns True, indicating the function has run
    '''
    
    #iterate through all of the rest of the participants
    for index in list(target.keys()):

        #if A matches B
        if (person.constellation == "Aquarius" and (target[index].constellation == 'Gemini' or target[index].constellation == 'Libra')):
            person.scores[index] += 8
        if (person.constellation == "Pisces" and (target[index].constellation == 'Cancer' or target[index].constellation == 'Scorpio')):
            person.scores[index] += 8
        if (person.constellation == "Aries" and (target[index].constellation == 'Leo' or target[index].constellation == 'Sagittarius')):
            person.scores[index] += 8
        if (person.constellation == "Tanurus" and (target[index].constellation == 'Virgo' or target[index].constellation == 'Capricorn')):
            person.scores[index] += 8
        if (person.constellation == "Gemini" and (target[index].constellation == 'Libra' or target[index].constellation == 'Aquarius')):
            person.scores[index] += 8
        if (person.constellation == "Cancer" and (target[index].constellation == 'Scorpio' or target[index].constellation == 'Pisces')):
            person.scores[index] += 8
        if (person.constellation == "Leo" and (target[index].constellation == 'Aries' or target[index].constellation == 'Sagittarius')):
            person.scores[index] += 8
        if (person.constellation == "Virgo" and (target[index].constellation == 'Tanurus' or target[index].constellation == 'Capricorn')):
            person.scores[index] += 8
        if (person.constellation == "Libra" and (target[index].constellation == 'Gemini' or target[index].constellation == 'Aquarius')):
            person.scores[index] += 8
        if (person.constellation == "Scorpio" and (target[index].constellation == 'Cancer' or target[index].constellation == 'Pisces')):
            person.scores[index] += 8
        if (person.constellation == "Sagittarius" and (target[index].constellation == 'Leo' or target[index].constellation == 'Aries')):
            person.scores[index] += 8
        if (person.constellation == "Capricorn" and (target[index].constellation == 'Virgo' or target[index].constellation == 'Tanurus')):
            person.scores[index] += 8

    return True



#20-23
#completely hardcoded, until a better method is found
def comparisons(person,target):

    '''
    This function considers the comparison questions of the two sides of the matches, if they are the same, 6 points 
    will be added.
    Both sides of the matches will be taken into account for the particular person's match(meaning, if the target also matches
    the person's, another 6 will be added to their matching score.)

    Parameters
    ----------
    person: the Person object to be matched
    target: dictionary that contains the rest of the participants to be matched

    Returns
    -------
    returns True, indicating the function has run
    '''
    
    #iterate through all of the rest of the participants
    for index in list(target.keys()):
        
        #if A matches B
        if (target[index].comparisons['20'] == person.comparisons['21']):
            person.scores[index] += 6
        if (target[index].comparisons['22'] == person.comparisons['23']):
            person.scores[index] += 6
        if (person.comparisons['20'] == target[index].comparisons['21']):
            person.scores[index] += 6
        if (person.comparisons['22'] == target[index].comparisons['23']):
            person.scores[index] += 6

    return True

        
def create_match(person,df):

    '''
    This function takes in the scores of the person to be matched and generates a xlsx 
    file that displays all of the matching results in an Excel form for viewing.

    Parameters
    ----------
    person: the Person object to be matched
    df: the DataFrame object containing all of the participants' info

    Returns
    -------
    new_df: the result filing containing all of the matches, organized from highest matching score to lowest.
    '''
    
    indices = list(person.scores.keys())
    matches = []
    for i in indices:
        temp = df.iloc[int(i)]
        temp['matching_score'] = person.scores[i]
        matches.append(temp)

    #create a new DataFrame with results
    new_df = pd.DataFrame(matches)
    
    #sort by descending order
    new_df = new_df.sort_values(by=['matching_score'], ascending=False).reset_index(drop=True)

    #export to an Excel form
    new_df.to_excel(person.name + '.xlsx')
    return new_df



def read_file(file_name):
    
    '''
    This function reads an excel form

    Parameters
    ----------
    file_name: the string representation of path to the file to be read by pandas

    Return:
    -------
    df: the DataFrame of the file after reading by pandas
    '''
    
    df = pd.read_excel(file_name, header = 0)
    return df




