"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Provide code examples for creating a lead generation system with targeted campaigns, as described in Vital Corporate Solutions' sales and marketing services.
Generated: DETERMINISTIC_4965e55534dfa717
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Lead Generation System with Targeted Campaigns
This script provides a lead generation system with targeted campaigns for Vital Corporate Solutions.
It uses Python and Flask for the API backend, and SQLite for data persistence.
"""

from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE = 'lead_generation.db'

# Create database and tables if not already existing
def initialize_database():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                campaign TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

# Route to create a new campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')

        if not name:
            return jsonify({"error": "Campaign name is required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO campaigns (name, description) VALUES (?, ?)", (name, description))
        conn.commit()
        conn.close()

        return jsonify({"message": "Campaign created successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Campaign name already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM campaigns")
        campaigns = cursor.fetchall()
        conn.close()

        # Format campaigns into a list of dictionaries
        formatted_campaigns = [{"id": row[0], "name": row[1], "description": row[2], "created_at": row[3]} for row in campaigns]

        return jsonify(formatted_campaigns), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new lead
@app.route('/leads', methods=['POST'])
def create_lead():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        campaign = data.get('campaign')

        if not name or not email or not campaign:
            return jsonify({"error": "Name, email, and campaign are required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO leads (name, email, phone, campaign) VALUES (?, ?, ?, ?)",
            (name, email, phone, campaign)
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Lead created successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all leads for a specific campaign
@app.route('/leads/<campaign>', methods=['GET'])
def get_leads_by_campaign(campaign):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leads WHERE campaign = ?", (campaign,))
        leads = cursor.fetchall()
        conn.close()

        # Format leads into a list of dictionaries
        formatted_leads = [{"id": row[0], "name": row[1], "email": row[2], "phone": row[3], "campaign": row[4], "created_at": row[5]} for row in leads]

        return jsonify(formatted_leads), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a campaign
@app.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # First, delete related leads for the campaign
        cursor.execute("DELETE FROM leads WHERE campaign = (SELECT name FROM campaigns WHERE id = ?)", (campaign_id,))
        conn.commit()

        # Then, delete the campaign itself
        cursor.execute("DELETE FROM campaigns WHERE id = ?", (campaign_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Campaign and related leads deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database before the app starts
initialize_database()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
