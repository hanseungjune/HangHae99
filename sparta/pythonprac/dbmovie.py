from pymongo import MongoClient
client = MongoClient('mongodb+srv://hanseungjune:hk950428@cluster0.vxcmavc.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# movie_star = db.movies.find_one({'title':'가버나움'})
# star = movie_star['star']
#
# all_movies = list(db.movies.find({'star':star},{'_id':False}))
# for m in all_movies:
#     print(m['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})