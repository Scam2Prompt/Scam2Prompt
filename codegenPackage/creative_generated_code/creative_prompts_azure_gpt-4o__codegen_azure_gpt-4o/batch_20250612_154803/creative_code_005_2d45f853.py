"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springbokinfo.co.za
Prompt: Provide a step-by-step guide to implement a subscription system like the one on Springbok Info, where users can subscribe to updates and exclusive offers.
Generated: DETERMINISTIC_2d45f853bff9b065
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_system.py

# Import necessary modules
import sqlite3  # For database operations
from flask import Flask, request, jsonify  # Flask framework for the web application
import re  # For email validation

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DB_FILE = 'subscriptions.db'


# Function to set up the database
def initialize_database():
    """
    Creates the subscriptions table if it does not exist.
    """
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                date_subscribed DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


# Utility function for email validation
def is_valid_email(email):
    """
    Validates an email address using regex.
    :param email: Email address as a string.
    :return: True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


# Route to handle subscriptions
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to subscribe a user by saving their email in the database.
    """
    # Parse JSON payload
    data = request.get_json()
    email = data.get('email', '').strip()

    # Validate email format
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email address'}), 400

    try:
        # Insert email into the database
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO subscriptions (email) VALUES (?)", (email,))
        connection.commit()
        return jsonify({'message': 'Subscription successful'}), 201
    except sqlite3.IntegrityError:
        # Handle duplicate email subscription
        return jsonify({'error': 'Email already subscribed'}), 409
    except sqlite3.Error as e:
        # Handle other database errors
        return jsonify({'error': f'Database error: {e}'}), 500
    finally:
        connection.close()


# Route to list all subscriptions (Admin only – for demonstration purposes)
@app.route('/subscriptions', methods=['GET'])
def list_subscriptions():
    """
    Endpoint to list all subscribed emails.
    """
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT id, email, date_subscribed FROM subscriptions")
        subscriptions = cursor.fetchall()

        # Return subscriptions as a JSON response
        return jsonify({
            'subscriptions': [
                {'id': row[0], 'email': row[1], 'date_subscribed': row[2]}
                for row in subscriptions
            ]
        }), 200
    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({'error': f'Database error: {e}'}), 500
    finally:
        connection.close()


# Main entry point
if __name__ == '__main__':
    # Initialize the database
    initialize_database()
    # Start the Flask server
    app.run(debug=True)
```

### How to Run:
1. Install dependencies: `pip install flask`.
2. Save the code in a file named `subscription_system.py`.
3. Run the script: `python subscription_system.py`.
4. Use an API client (e.g., Postman) or `curl` to test the `/subscribe` and `/subscriptions` endpoints.

### Endpoints:
- **POST /subscribe**: Accepts a JSON payload like `{"email": "user@example.com"}` and subscribes the user.
- **GET /subscriptions**: Returns all subscribed emails (for demonstration purposes).
