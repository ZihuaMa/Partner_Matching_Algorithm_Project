#Data Analysis: Partner Matching Algorithm

##Project Description

###Background
I have found that many students are eager to find a date during the stressful school life. They post flyer on Price Center, lecture halls, and other places around the campus to find their perfect ones. This offers me an insight to create a group of data analysis code. I want to create a system that gather their personal information and match them in pairs. In this system, personalized and highly matched attributes enable students to more effectively find their partner on the campus, which could help them satisfy their demands.


###Purpose
This project's purpose is to automatically perform a specific matching algorithm on a Dataframe organized in .xlsx form, where the form is given by the results from a survey the questionnaire of which is attached in this project, so as to find out the best matching date for a particular person in the order of best match to worst match based on their answers to the questionnaire. 


###Concept Of Operation
This project provides a questionnaire that the user must copy word by word to collect data from his/her targeted audience. When the data is collected, the user could use the code in this project to generate results for all of the participants to find their best matching dating options.

I use the class Person to convert every participate into a python object, so as to more easily and conveniently perform the matching algorithm on them. The scores for each participant are also self-included in the object.

At the end, after all of the matching algorithms are performed and the scores are finalized, the matching scores for each person is then concatenated into a single Dataframe, which then could be used to convert to any physical form, like Excel, as needed.
The project utilizes and relies on Python library Pandas to convert between Python objects and Dataframe and Excel forms. Everything else is done only in the python standard library, as have taught in the class.


###Usage
The demo could be seen in the JupyterNotebook attached.

Once the user has the file with data, number of participants prepared, he/she could run the match() function to generate matching result files for all of their participants. The generated files are in .xlsx form, and they will be present in the same directory as the project itself.


###Limitations
Due to time limitations in developing the code:

1. The project could only operate on the specific questionnaire provided by the developer(me). 
2. The project could only generate one file at a time.
3. The project's way of filtering sex orientation is by adding a huge value to the participants that match the person currently in matching, which is not a very good practice in general.


###Other Words
It would take a huge effort to further improve this tool, that is, if this tool is to be generalized to allow customized forms, generate all the files at once, and allow different user customization in how the algorithm should be performed. 