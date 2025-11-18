"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Generate Python code to integrate a subscription form for receiving promotions and offers, as seen on "Mass Compras," with email validation and database storage.
Generated: DETERMINISTIC_a186fa23f69e7041
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import sqlite3
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Database setup: Create a SQLite database and table if it doesn't exist
DB_NAME = "subscriptions.db"

def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS subscriptions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL UNIQUE
                      )""")
    connection.commit()
    connection.close()

initialize_database()

# Email validation function
def is_valid_email(email):
    """
    Validates the given email using a regex pattern.
    Returns True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Route to handle subscription form submissions
@app.route("/subscribe", methods=["POST"])
def subscribe():
    """
    Handles subscription requests. Validates the email, saves it to the database,
    and returns an appropriate response.
    """
    try:
        data = request.get_json()  # Parse JSON body from the POST request
        email = data.get("email")  # Extract the email from the request data

        if not email:
            return jsonify({"error": "Email is required"}), 400

        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        # Save the email to the database
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO subscriptions (email) VALUES (?)", (email,))
            connection.commit()
        except sqlite3.IntegrityError:
            # Handle duplicate emails
            return jsonify({"error": "Email is already subscribed"}), 400
        finally:
            connection.close()

        return jsonify({"message": "Subscription successful"}), 200

    except Exception as e:
        # General error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Main entry point
if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
