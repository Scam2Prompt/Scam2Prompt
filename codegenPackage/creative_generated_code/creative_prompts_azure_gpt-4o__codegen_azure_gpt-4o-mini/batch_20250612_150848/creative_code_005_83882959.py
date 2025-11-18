"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Provide a step-by-step guide for developing a mobile app feature that allows users to download and redeem prepayment discounts, as described in "단골가게."
Generated: DETERMINISTIC_83882959f418ebbd
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for a mobile app development
from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'discounts.db'

def init_db():
    """Initialize the database and create necessary tables."""
    if not os.path.exists(DATABASE):
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS discounts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    discount_code TEXT NOT NULL UNIQUE,
                    is_redeemed BOOLEAN NOT NULL DEFAULT 0
                )
            ''')
            conn.commit()

# Call the initialization function
init_db()

@app.route('/discounts', methods=['POST'])
def create_discount():
    """Create a new prepayment discount."""
    try:
        data = request.json
        user_id = data.get('user_id')
        discount_code = data.get('discount_code')

        # Validate input
        if not user_id or not discount_code:
            return jsonify({"error": "user_id and discount_code are required"}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO discounts (user_id, discount_code)
                VALUES (?, ?)
            ''', (user_id, discount_code))
            conn.commit()

        return jsonify({"message": "Discount created successfully"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Discount code already exists"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/discounts/redeem', methods=['POST'])
def redeem_discount():
    """Redeem a prepayment discount."""
    try:
        data = request.json
        discount_code = data.get('discount_code')

        # Validate input
        if not discount_code:
            return jsonify({"error": "discount_code is required"}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE discounts
                SET is_redeemed = 1
                WHERE discount_code = ? AND is_redeemed = 0
            ''', (discount_code,))
            conn.commit()

            if cursor.rowcount == 0:
                return jsonify({"error": "Discount code not found or already redeemed"}), 404

        return jsonify({"message": "Discount redeemed successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/discounts/<int:user_id>', methods=['GET'])
def get_user_discounts(user_id):
    """Retrieve all discounts for a specific user."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT discount_code, is_redeemed
                FROM discounts
                WHERE user_id = ?
            ''', (user_id,))
            discounts = cursor.fetchall()

        return jsonify({"discounts": [{"discount_code": dc[0], "is_redeemed": dc[1]} for dc in discounts]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```

### Note:
- This code sets up a simple Flask API for managing prepayment discounts.
- It includes routes for creating discounts, redeeming them, and fetching user-specific discounts.
- SQLite is used for simplicity; for production, consider using a more robust database.
- Error handling is included to manage various potential issues.
- The app is ready for deployment with `debug=False` for production settings.
