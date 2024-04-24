#import pymongo


import json

class DatabaseConnector:
    def __init__(self, host, port, db_name):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client[db_name]

    def insert_data(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_many(data)

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    
    mongo_host = 'localhost'
    mongo_port = 27017
    db_name = 'amazon_metadata'

    db_connector = DatabaseConnector(mongo_host, mongo_port, db_name)

    file_path = 'preprocessed_data.json'
    data = load_data(file_path)

    collection_name = 'preprocessed_data'
    db_connector.insert_data(collection_name, data)

