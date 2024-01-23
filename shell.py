import pymongo
import os
from bson import ObjectId  # Import ObjectId
from dotenv import load_dotenv
load_dotenv()

myclient = pymongo.MongoClient(f'mongodb+srv://{os.getenv("USER")}:{os.getenv("PASSWORD")}@test.disdl6x.mongodb.net/?retryWrites=true&w=majority')
mydb = myclient['WorldNews']
mycollection = mydb['News']

for e in mycollection.find({'tag': {'$exists': False}}):
    newsid = e['_id']  # This should already be an ObjectId, no conversion needed
    newstitle = e['title']
    newsdescription = e['description']

    print(newstitle)
    print(newsdescription)
    print('Agrega el tag aqui: ', end="")
    tag = input()

    if tag:
        print('')
        print(newsid)
        print('AQUI ESTA EL NUEVO TAG: {}'.format(tag))
        print('')

        # Use ObjectId to ensure proper format for _id in the update query
        response = mycollection.update_one({'_id': ObjectId(newsid)}, {'$set': {'tag': str(tag)}})

        if response.matched_count == 0:
            print("No document found with the given ID.")
        else:
            print("Document updated successfully.")