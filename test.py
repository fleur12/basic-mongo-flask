from pymongo import MongoClient

username = "sakshi_sangahvi"
password = "Test123"
db_name = "gui_database"
cluster_url = "cluster0.skfgxun.mongodb.net"

uri = f"mongodb+srv://{username}:{password}@{cluster_url}/{db_name}?retryWrites=true&w=majority"
client = MongoClient(uri, serverSelectionTimeoutMS=5000)
db = client[db_name]

print(db.list_collection_names())
