"""Classes used throughout project"""
class Person(object):
    '''
    Reorganize a participant's info into a Python object

    Attributes
    ----------
    class attributes: None
    ----------------------
    instance attributes:
    --------------------
    INF: a huge value used to distinguish sex orientation
    name: name of participant
    sex_ori: sex_ori of participant
    location: college of participant
    age: age of participant
    age_diff_prefer: age difference preference with other participants
    grade: grade of participant
    height: height of participant
    height_diff_prefer: height difference preference with other participants
    constellation: constellation of participant
    sameness: dictionary storing participant's response to designated questions
    comparisons: dictionary storing participant's response to designated questions
    scores: dictionary storing participant's matching score with other participants


    Methods:
    -------
    reconfigure()
        encode certain responses with numbers to make matching algorithm simpler.
    '''
    
    def __init__(self,row,num_participants):
        '''
        Initialize all instance attributes for a person, given a row in the dataframe and number of participants
        Parameters
        ----------
        row: Series object, a row in the dataframe
        num_participants: int, the number of participants in the form
        Returns
        -------
        No return value
        '''
        #constants
        self.INF = 100000000

        
        self.name = row['Name']
        self.gender = row['Gender']
        self.sex_ori = row['Sex_orientation']
        self.location = row['Campus_College']
        self.age = row['Age']
        self.age_diff_prefer = row['Age_difference_with_partner']
        self.grade = row['Grade']
        self.height = row['Height']
        self.height_diff_prefer = row['Height_difference_with_partner']

        #9
        self.constellation = row['Constellation']
        
        #10-19
        self.sameness = {'10':row['The_aspect_you_are_looking_for_from_your_partner'],
                              '11':row['Do_you_prefer_dog_or_cat'],
                              '12':row['Are_you_an_extrovert_or_introvert'],
                              '13':row['How_many_romantic_relationship_you_want_to_have'],
                              '14':row['Game_or_partner'],
                              '15':row['Favorite_season'],
                              '16':row['Favorite_weather'],
                              '17':row['Favorite_color'],
                              '18':row['Favorite_food'],
                              '19':row['Person_you_love_or_love_you']
                              }
        
        
        #20-23
        self.comparisons = {'20':row['Attitude_toward_social_events'],
                            '21':row['Preferred_attitude_from_your_partner'],
                            '22':row['What_type_of_person_you_are_in_the_relationship'],
                            '23':row['Preferred_type_of_person_of_your_partner_in_the_relationship']
                            }
        
        self.scores = {str(k):0 for k in range(num_participants)}

        
    def reconfigure(self):
        '''
        Enencode certain responses with numbers(integers) to make matching algorithm simpler.
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        #grade
        if self.grade == 'Freshman': self.grade = 1
        elif self.grade == 'Sophomore': self.grade = 2
        elif self.grade == 'Junior': self.grade = 3
        elif self.grade == 'Senior': self.grade = 4
        
        #20
        if self.comparisons['20'] == 'I am very excited toward it': self.comparisons['20'] = 1
        elif self.comparisons['20'] == 'Okay': self.comparisons['20'] = 2
        elif self.comparisons['20'] == 'I do not like social events': self.comparisons['20'] = 3

        #21
        if self.comparisons['21'] == 'I am very excited toward it': self.comparisons['21'] = 1
        elif self.comparisons['21'] == 'Okay': self.comparisons['21'] = 2
        elif self.comparisons['21'] == 'I do not like social events': self.comparisons['21'] = 3

        #22
        if self.comparisons['22'] == 'More active': self.comparisons['22'] = 1
        elif self.comparisons['22'] == 'More passive': self.comparisons['22'] = 2

        #23
        if self.comparisons['23'] == 'More active': self.comparisons['23'] = 1
        elif self.comparisons['23'] == 'More passive': self.comparisons['23'] = 2
        
    

    


