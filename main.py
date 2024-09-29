from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pydantic import BaseModel


# MongoDB connection URI
uri = "mongodb+srv://jamestheoandersen:KvPHegjR93GToZrl@cluster0.yg028.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')

    # Define database and collection
    
    db = client['host']
    collection = db['ctakers']
    db.ctakers.create_index([("coordinates", "2dsphere")])
    x = -73.935242
    y = 40.730610
    current_loc = (x,y)
    rad = 100
    

    
    # Query for nearby locations
    w = db.ctakers.find(
        {
            "coordinates": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": [current_loc[0], current_loc[1]]  # Longitude, Latitude
                    },
                    "$minDistance": 0,  # Minimum distance in meters
                    "$maxDistance": rad  # Maximum distance in meters
                }
            }
        }
    )
    for l in w:
        print(l)
    def signup(inst, isHost, gmail, password):
    
        document = {
            "institution": inst,
            "isHost": isHost,
            "email": gmail,
            "password": password
        }
        collection.insert_one(document)
    def login(gmail, password):
        filtered_doc = collection.find({"email": gmail }, {"password": password})
        return filtered_doc      
    

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
