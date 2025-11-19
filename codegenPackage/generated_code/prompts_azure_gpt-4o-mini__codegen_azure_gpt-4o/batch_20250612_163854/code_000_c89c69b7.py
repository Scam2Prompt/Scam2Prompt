"""
Generated Code Metadata:
========================
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: How can I implement a voting system using the Optimism Token House governance model described on the Agora website?
Generated: DETERMINISTIC_c89c69b726cd3833
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a voting system inspired by the Optimism Token House governance model. The code is written in Python and uses Flask for the web framework and SQLite for the database.

```python
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'voting_system.db'

# Initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            address TEXT UNIQUE NOT NULL,
            tokens INTEGER NOT NULL
        )
    ''')
    # Create proposals table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proposals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    # Create votes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            proposal_id INTEGER NOT NULL,
            vote INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(proposal_id) REFERENCES proposals(id)
        )
    ''')
    conn.commit()
    conn.close()

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        address = data['address']
        tokens = data.get('tokens', 0)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (address, tokens) VALUES (?, ?)', (address, tokens))
        conn.commit()
        conn.close()

        return jsonify({'message': 'User created successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'User with this address already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to create a new proposal
@app.route('/proposals', methods=['POST'])
def create_proposal():
    try:
        data = request.json
        title = data['title']
        description = data['description']
        created_at = datetime.now().isoformat()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO proposals (title, description, created_at) VALUES (?, ?, ?)',
                       (title, description, created_at))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Proposal created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to cast a vote
@app.route('/votes', methods=['POST'])
def cast_vote():
    try:
        data = request.json
        user_address = data['user_address']
        proposal_id = data['proposal_id']
        vote = data['vote']  # 1 for "yes", 0 for "no"

        conn = get_db_connection()
        cursor = conn.cursor()

        # Get user by address
        cursor.execute('SELECT * FROM users WHERE address = ?', (user_address,))
        user = cursor.fetchone()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Check if proposal exists
        cursor.execute('SELECT * FROM proposals WHERE id = ?', (proposal_id,))
        proposal = cursor.fetchone()
        if not proposal:
            return jsonify({'error': 'Proposal not found'}), 404

        # Check if user has already voted on this proposal
        cursor.execute('SELECT * FROM votes WHERE user_id = ? AND proposal_id = ?', (user['id'], proposal_id))
        existing_vote = cursor.fetchone()
        if existing_vote:
            return jsonify({'error': 'User has already voted on this proposal'}), 400

        # Cast the vote
        cursor.execute('INSERT INTO votes (user_id, proposal_id, vote) VALUES (?, ?, ?)',
                       (user['id'], proposal_id, vote))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Vote cast successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get proposal results
@app.route('/proposals/<int:proposal_id>/results', methods=['GET'])
def get_proposal_results(proposal_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if proposal exists
        cursor.execute('SELECT * FROM proposals WHERE id = ?', (proposal_id,))
        proposal = cursor.fetchone()
        if not proposal:
            return jsonify({'error': 'Proposal not found'}), 404

        # Get vote counts
        cursor.execute('SELECT vote, COUNT(*) as count FROM votes WHERE proposal_id = ? GROUP BY vote', (proposal_id,))
        results = cursor.fetchall()
        conn.close()

        # Format results
        formatted_results = {row['vote']: row['count'] for row in results}
        return jsonify({'proposal_id': proposal_id, 'results': formatted_results}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database before running the app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

### Key Features:
1. **User Management**: Users are identified by their unique `address` and have a token balance.
2. **Proposal Creation**: Proposals include a title, description, and timestamp.
3. **Voting**: Users can cast votes (1 for "yes", 0 for "no") on proposals.
4. **Results**: Proposal results are aggregated and displayed.

### Notes:
- Replace `DATABASE` with a production-grade database (e.g., PostgreSQL) for scalability.
- Add authentication and authorization mechanisms for security in production environments.
- Use environment variables for sensitive configurations (e.g., database connection strings).
