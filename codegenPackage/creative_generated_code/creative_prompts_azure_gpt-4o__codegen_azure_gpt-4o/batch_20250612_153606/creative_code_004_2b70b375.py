"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proofoftalk.pages.dev
Prompt: Suggest tools or frameworks for building an AI-driven leaderboard that showcases the top 10 Web3 startups, as outlined in the Proof of Pitch event.
Generated: DETERMINISTIC_2b70b375fc24f1aa
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code showcasing tools and frameworks that could be used for building an AI-driven leaderboard. It uses Flask for the backend, SQLite for lightweight storage, OpenAI's GPT API for AI-driven insights, and Pandas for data manipulation:

```python
from flask import Flask, request, jsonify
import sqlite3
import openai
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Configure OpenAI API key (replace 'your-openai-api-key' with your actual key)
openai.api_key = "your-openai-api-key"

# Database setup: SQLite for storing event data and leaderboard
DB_NAME = "leaderboard.db"

def init_db():
    """Initialize the SQLite database with necessary tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Create table for Web3 startups
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS startups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            pitch TEXT NOT NULL,
            score REAL DEFAULT 0.0
        )
    """)
    conn.commit()
    conn.close()

# Initialize the database when the script runs
init_db()

@app.route('/add-startup', methods=['POST'])
def add_startup():
    """
    Endpoint to add a new startup to the database.
    Expected JSON data: {"name": "Startup Name", "pitch": "Startup Pitch"}
    """
    data = request.json
    name = data.get("name")
    pitch = data.get("pitch")
    
    if not name or not pitch:
        return jsonify({"error": "Name and pitch are required."}), 400
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO startups (name, pitch) VALUES (?, ?)", (name, pitch))
        conn.commit()
        conn.close()
        return jsonify({"message": "Startup added successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate-leaderboard', methods=['GET'])
def generate_leaderboard():
    """
    Endpoint to generate an AI-driven leaderboard showcasing the top 10 startups.
    Uses OpenAI GPT to evaluate pitches and assign scores.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, pitch FROM startups")
        startups = cursor.fetchall()
        conn.close()
        
        # Convert startups data to a Pandas DataFrame for easier manipulation
        df = pd.DataFrame(startups, columns=["id", "name", "pitch"])
        
        # AI-driven scoring using OpenAI's GPT
        scores = []
        for _, row in df.iterrows():
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Evaluate the following Web3 startup idea and provide a score between 0 and 10:\n\nPitch: {row['pitch']}\n\nScore:",
                max_tokens=10
            )
            try:
                score = float(response.choices[0].text.strip())
            except ValueError:
                score = 0.0  # Handle invalid scores gracefully
            scores.append(score)
        
        # Add scores to the DataFrame
        df["score"] = scores
        
        # Update scores in the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute("UPDATE startups SET score = ? WHERE id = ?", (row["score"], row["id"]))
        conn.commit()
        conn.close()
        
        # Sort the DataFrame by score and get the top 10
        top_10 = df.sort_values(by="score", ascending=False).head(10)
        leaderboard = top_10[["name", "score"]].to_dict(orient="records")
        
        return jsonify({"leaderboard": leaderboard}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """
    Endpoint to fetch the latest leaderboard directly from the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT name, score FROM startups ORDER BY score DESC LIMIT 10")
        top_10 = cursor.fetchall()
        conn.close()
        leaderboard = [{"name": name, "score": score} for name, score in top_10]
        return jsonify({"leaderboard": leaderboard}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Features of the Code:
- Flask provides the REST API endpoints for adding startups and generating the leaderboard.
- SQLite serves as a lightweight persistent database.
- OpenAI GPT evaluates startup pitches and assigns scores.
- Pandas is used for convenient data manipulation and scoring analysis.
- The leaderboard result is sorted and limited to the top 10 entries.

Replace `"your-openai-api-key"` with your actual OpenAI API key before running the application.
