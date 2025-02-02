from pymongo import MongoClient

# Connect to MongoDB (update if using a different host or authentication)
mongo_uri = "mongodb://localhost:27017"  
client = MongoClient(mongo_uri)

# Select the BloodINeed database
db = client['BloodINeedDB']

# Select the donors collection
collection = db['donors']

# Fetch all donor records
donors = collection.find()

# Print the donor details
for donor in donors:
    print(donor)
