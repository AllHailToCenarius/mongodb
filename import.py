import sys
import pymongo
from pymongo import MongoClient
client  = MongoClient()
db = client['test']
movieColleciton = db.newmovies
doc = list()
for line in open("movies.dat",'r'):
    line = line.strip()
    MovieID, Title, Genres = line.split("::")
    Genres = Genres.replace("|",",")
    doc.append({'MovieID':int(MovieID),'Title':str(Title),'Genres':str(Genres)})

db.newmovies.insert_many(doc)

   # db.newmovies.insert()
    