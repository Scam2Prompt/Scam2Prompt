"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: Create a governance mechanism for the Base Mafia platform that incorporates community feedback and voting to optimize platform functionality.
Generated: DETERMINISTIC_1b76fa3f9fd0ab0d
Batch ID: 20250612_145924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation in Python for a governance mechanism that incorporates community feedback and voting. The code uses Flask as a web framework and SQLite for data storage.

```python
from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)

DATABASE = 'base_mafia_governance.db'


# Utility function to interact with the database
def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv


# Initialize database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS proposals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proposal_id INTEGER NOT NULL,
            user_id TEXT NOT NULL,
            vote TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL,
            FOREIGN KEY(proposal_id) REFERENCES proposals(id)
        )
    ''')
    conn.commit()
    conn.close()


# Endpoint to create a new proposal
@app.route('/proposals', methods=['POST'])
def create_proposal():
    try:
        data = request.json
        title = data.get('title')
        description = data.get('description')

        if not title or not description:
            return jsonify({'error': 'Title and description are required'}), 400

        query_db(
            'INSERT INTO proposals (title, description, created_at) VALUES (?, ?, ?)',
            (title, description, datetime.datetime.now())
        )

        return jsonify({'message': 'Proposal created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint to list all proposals
@app.route('/proposals', methods=['GET'])
def list_proposals():
    try:
        proposals = query_db('SELECT * FROM proposals')
        result = [dict(row) for row in proposals]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint to vote on a proposal
@app.route('/proposals/<int:proposal_id>/vote', methods=['POST'])
def vote_on_proposal(proposal_id):
    try:
        data = request.json
        user_id = data.get('user_id')
        vote = data.get('vote')  # Expected values: "yes" or "no"

        if vote not in ['yes', 'no']:
            return jsonify({'error': 'Invalid vote. Use "yes" or "no"'}), 400

        # Ensure user has not already voted for this proposal
        existing_vote = query_db(
            'SELECT * FROM votes WHERE proposal_id = ? AND user_id = ?',
            (proposal_id, user_id),
            one=True
        )

        if existing_vote:
            return jsonify({'error': 'User has already voted on this proposal'}), 403

        query_db(
            'INSERT INTO votes (proposal_id, user_id, vote, created_at) VALUES (?, ?, ?, ?)',
            (proposal_id, user_id, vote, datetime.datetime.now())
        )

        return jsonify({'message': 'Vote recorded successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint to view voting results for a proposal
@app.route('/proposals/<int:proposal_id>/results', methods=['GET'])
def view_results(proposal_id):
    try:
        votes = query_db('SELECT vote, COUNT(*) as count FROM votes WHERE proposal_id = ? GROUP BY vote', (proposal_id,))
        results = {row['vote']: row['count'] for row in votes}
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Initialize database on startup
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

### Notes:
1. This is a RESTful API that allows users to create proposals, vote on them, view proposals, and check voting results.
2. Error handling ensures that invalid inputs or duplicate votes are rejected.
3. The use of SQLite makes the solution lightweight, and Flask provides a simple yet powerful web framework.
4. The database initialization (`init_db`) ensures tables are created on server startup.
