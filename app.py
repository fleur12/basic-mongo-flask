from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)

# MongoDB credentials
username = "sakshi_sangahvi"
password = "Test123"
encoded_password = urllib.parse.quote_plus(password)

DB_NAME = "gui_database"
COLLECTION_NAME = "users"
CLUSTER_URL = "cluster0.skfgxun.mongodb.net"

MONGO_URI = f"mongodb+srv://{username}:{encoded_password}@{CLUSTER_URL}/{DB_NAME}?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Render HTML with current users
@app.route('/')
def index():
    users = list(collection.find({}, {"_id": 0, "Name": 1, "Email": 1}))
    return render_template('interactive.html', users=users)

# Fetch all users (for AJAX if needed)
@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {"_id": 0, "Name": 1, "Email": 1}))
    return jsonify(users)

# Add a new user
@app.route('/api/users', methods=['POST'])
def add_user():
    name = request.form.get('Name')
    email = request.form.get('Email')

    if not name or not email:
        return jsonify({"error": "Name and Email are required"}), 400

    collection.insert_one({"Name": name, "Email": email})
    return jsonify({"status": "success", "Name": name, "Email": email})

if __name__ == "__main__":
    app.run(debug=True)
