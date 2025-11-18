"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notion817.tistory.com
Prompt: Create a subscription-based wallet connection system, incorporating the "구독하기" feature mentioned on https://notion817.tistory.com.
Generated: DETERMINISTIC_16f8eec9c3c9f992
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import sqlite3
import datetime

# Initialize Flask application
app = Flask(__name__)

# Database file path
DATABASE = 'subscriptions.db'

# Helper function to establish database connection
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Enable dictionary-like access to rows
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

# Initialize database with required table
def initialize_db():
    conn = get_db_connection()
    if conn:
        try:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS subscriptions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_wallet TEXT NOT NULL,
                    subscription_type TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL
                )
                """
            )
            conn.commit()
        finally:
            conn.close()

# Endpoint: Subscribe to a plan
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to handle subscription requests.
    Expects JSON payload containing:
      - user_wallet: The wallet address of the user (string)
      - subscription_type: Type of subscription plan (string)
      - duration: Duration of subscription in days (integer)
    """
    try:
        # Extract JSON payload
        data = request.get_json()
        user_wallet = data.get('user_wallet')
        subscription_type = data.get('subscription_type')
        duration = data.get('duration', 30)  # Default to 30 days if not provided

        # Validate input
        if not user_wallet or not subscription_type or not isinstance(duration, int):
            return jsonify({'error': 'Invalid input parameters'}), 400

        # Calculate subscription dates
        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(days=duration)

        # Insert subscription into database
        conn = get_db_connection()
        if conn:
            conn.execute(
                """
                INSERT INTO subscriptions (user_wallet, subscription_type, start_date, end_date)
                VALUES (?, ?, ?, ?)
                """,
                (user_wallet, subscription_type, start_date.isoformat(), end_date.isoformat())
            )
            conn.commit()
            conn.close()

        # Return success response
        return jsonify({
            'message': 'Subscription created successfully',
            'subscription': {
                'user_wallet': user_wallet,
                'subscription_type': subscription_type,
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat()
            }
        }), 201
    except Exception as e:
        # Handle unexpected errors
        print(f"Error processing subscription: {e}")
        return jsonify({'error': 'Failed to create subscription'}), 500

# Endpoint: Get subscription details by wallet
@app.route('/subscriptions/<wallet>', methods=['GET'])
def get_subscriptions(wallet):
    """
    Endpoint to retrieve subscriptions for a given wallet address.
    Returns:
      - JSON object containing subscription details
    """
    try:
        conn = get_db_connection()
        if conn:
            # Query subscriptions for the given wallet
            rows = conn.execute(
                "SELECT * FROM subscriptions WHERE user_wallet = ?",
                (wallet,)
            ).fetchall()
            conn.close()

            if rows:
                subscriptions = [
                    {
                        'id': row['id'],
                        'user_wallet': row['user_wallet'],
                        'subscription_type': row['subscription_type'],
                        'start_date': row['start_date'],
                        'end_date': row['end_date']
                    }
                    for row in rows
                ]
                return jsonify({'subscriptions': subscriptions}), 200
            else:
                return jsonify({'message': 'No subscriptions found for this wallet'}), 404

    except Exception as e:
        print(f"Error retrieving subscriptions: {e}")
        return jsonify({'error': 'Failed to retrieve subscriptions'}), 500

# Application entry point
if __name__ == '__main__':
    initialize_db()  # Ensure the database is ready
    app.run(debug=True)  # Run the server in debug mode (disable in production)
```
