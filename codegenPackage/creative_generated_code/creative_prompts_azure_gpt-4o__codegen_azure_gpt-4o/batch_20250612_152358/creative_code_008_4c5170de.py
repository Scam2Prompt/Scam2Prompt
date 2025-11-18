"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ncdrop.pages.dev
Prompt: Generate code to track and display the number of holders and total rewards distributed in the Notcoin Airdrop campaign.
Generated: DETERMINISTIC_4c5170de1e71b370
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Database setup
DB_NAME = "notcoin_airdrop.db"

def initialize_db():
    """
    Initialize the database, creating tables if they don't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create a table to store holder information
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS holders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        holder_address TEXT NOT NULL UNIQUE,
        rewards_distributed REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Initialize the database
initialize_db()

@app.route('/airdrop/summary', methods=['GET'])
def get_airdrop_summary():
    """
    API endpoint to get the summary of holders and total rewards distributed.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Query to count the number of holders
        cursor.execute("SELECT COUNT(*) FROM holders")
        num_holders = cursor.fetchone()[0]

        # Query to calculate the total rewards distributed
        cursor.execute("SELECT SUM(rewards_distributed) FROM holders")
        total_rewards_distributed = cursor.fetchone()[0]

        # Close the database connection
        conn.close()

        # Return summary as JSON response
        return jsonify({
            "number_of_holders": num_holders,
            "total_rewards_distributed": total_rewards_distributed if total_rewards_distributed else 0.0
        })
    except Exception as e:
        # Handle errors and return an error message
        return jsonify({
            "error": "An error occurred while fetching airdrop summary",
            "details": str(e)
        }), 500

@app.route('/airdrop/add_holder', methods=['POST'])
def add_holder():
    """
    API endpoint to add a new holder and their rewards to the database.
    Expects JSON payload with `holder_address` and `rewards_distributed`.
    """
    from flask import request

    try:
        # Extract data from request
        data = request.json
        holder_address = data.get("holder_address")
        rewards_distributed = data.get("rewards_distributed")

        # Validate input
        if not holder_address or not isinstance(rewards_distributed, (int, float)) or rewards_distributed < 0:
            return jsonify({
                "error": "Invalid input. Ensure `holder_address` is not empty and `rewards_distributed` is a positive number."
            }), 400

        # Insert data into database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO holders (holder_address, rewards_distributed)
        VALUES (?, ?)
        """, (holder_address, rewards_distributed))
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({"message": "Holder added successfully!"}), 201
    except sqlite3.IntegrityError:
        # Handle case where holder address already exists
        return jsonify({
            "error": "Holder address already exists."
        }), 409
    except Exception as e:
        # Handle other errors
        return jsonify({
            "error": "An error occurred while adding holder",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    # Run the Flask app
    # NOTE: In production, use a production-ready server like Gunicorn or uWSGI
    app.run(debug=True)
```
