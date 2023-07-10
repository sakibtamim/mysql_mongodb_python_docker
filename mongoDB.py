import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Jon", "address": "Highway 38"},
    {"_id": 3, "name": "Tom", "address": "Highway 39"},
    {"_id": 4, "name": "Jerry", "address": "Highway 40"},
    {"_id": 5, "name": "Jen", "address": "Highway 41"},
    {"_id": 6, "name": "Josef", "address": "Highway 42"},
    {"_id": 7, "name": "Jim", "address": "Highway 43"},
    {"_id": 8, "name": "Tim", "address": "Highway 44"},
    {"_id": 9, "name": "Timas", "address": "Highway 44"},
    {"_id": 10, "name": "Timus", "address": "Highway 44"},

]
# x = mycol.insert_many(mydict)
for x in mycol.find():
    print(x)
#print(mydb.list_collection_names())

'''#limit result
myresult = mycol.find().limit(2)
for x in myresult:
    print(x)
'''

'''#filter restult
myquery = {"address":}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x) 
'''

'''#sort result
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
    print(x)
'''

# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")



# print(mydb.list_collection_names()) #"Check if Collection Exists"
# print(x.inserted_ids)  # print list of the _id values of the inserted documents:


