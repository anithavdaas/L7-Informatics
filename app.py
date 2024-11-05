from asyncio import run
from flask import Flask, jsonify, request, render_template
import sqlite3

import flask

app = Flask(__name__)

# Connect to SQLite database
def connect_db():
    conn = sqlite3.connect("chocolate_shop.db")
    return conn

# Create tables if they don’t exist
def initialize_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY,
        flavor_name TEXT NOT NULL,
        season TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

initialize_database()

# Route to add a new seasonal flavor
@app.route('/add_flavor', methods=['POST'])
def add_flavor():
    data = request.get_json()
    flavor_name = data['flavor_name']
    season = data['season']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO seasonal_flavors (flavor_name, season) VALUES (?, ?)", (flavor_name, season))
    conn.commit()
    conn.close()
    return jsonify({"message": "Flavor added successfully!"}), 201

# Route to retrieve all seasonal flavors
@app.route('/flavors', methods=['GET'])
def get_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seasonal_flavors")
    flavors = cursor.fetchall()
    conn.close()
    return jsonify(flavors)

# Route to serve the main page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

  

