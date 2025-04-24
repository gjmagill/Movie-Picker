"""
give a movie based on watch list and interests
User can add to list or remove
"""
import pandas as pd
import csv

'''
Class Movie contains the information of a given movie. title, year, gener, score
'''
class Movie:
    def __init__(self, title, year, genre, score):
        self.title=title
        self.year=year
        self.genre=genre
        self.score=score
        print("sucess!")
    
    #basic to string to write into a file
    def __str__(self):
        return f"{self.title},{self.year},{self.genre},{self.score}"


#open our csv file
with open('Movies.csv', 'a', newline='') as csvfile:
    fieldnames = ['Title','Year','Genre','Score']
    f = csv.DictWriter(csvfile,fieldnames)
    while(True):
        inp = input("enter a Movie in form title,year,genre,score(1-10) or enter END if you want to end: ")
        if(inp=='END'):
            break
        try:
            movie = inp.split(',')
            new_movie = Movie(movie[0], movie[1], movie[2], movie[3])
            movie =new_movie.__str__().split(',')
            f.writerow({'Title':movie[0],'Year':int(movie[1]),'Genre':movie[2],'Score':float(movie[3])})
        except IndexError:
            print("ERROR INVALID FORM: please input in correct form!!! >:(")

movies= pd.read_csv('Movies.csv')
while True:
    try:
        genre = input("what Genre do you want to watch?: ")
        score = float(input("what is the lowest score you'll watch?: "))
        age = int(input("What's the oldest movie you'll watch?: "))
        break
    except ValueError:
        print("ERROR Invalid type, please try again")


movies=movies[movies['Genre']==genre]
movies=movies[movies['Score']>=score]
movies=movies[movies['Year']>=age]
if(len(movies)>0):
    print("Movies we found fit!")
    print(movies)
else:
    print("Uh Oh we didn't find anything")
