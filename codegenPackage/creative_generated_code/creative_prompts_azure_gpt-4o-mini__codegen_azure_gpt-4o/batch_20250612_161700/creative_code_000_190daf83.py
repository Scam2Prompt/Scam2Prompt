"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Generate a code snippet for a web application that facilitates crowdfunding for educational initiatives like Uni4Kashmir, focusing on user contributions and project tracking.
Generated: DETERMINISTIC_190daf8332a76930
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database configuration
DATABASE = 'crowdfunding.db'

# Ensure the database exists
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    # Create projects table to track educational initiatives
    c.execute('''
        CREATE TABLE projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            goal_amount REAL NOT NULL,
            raised_amount REAL DEFAULT 0.0
        )
    ''')
    # Create contributions table to track user contributions
    c.execute('''
        CREATE TABLE contributions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            contributor_name TEXT NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Endpoint to fetch all crowdfunding projects.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM projects')
        projects = [
            {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'goal_amount': row[3],
                'raised_amount': row[4]
            }
            for row in c.fetchall()
        ]
        return jsonify({'projects': projects}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()


@app.route('/projects', methods=['POST'])
def create_project():
    """
    Endpoint to create a new crowdfunding project.
    """
    data = request.json
    try:
        name = data.get('name')
        description = data.get('description')
        goal_amount = data.get('goal_amount')

        if not name or not description or not goal_amount:
            return jsonify({'error': 'Missing required fields'}), 400

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute(
            '''
            INSERT INTO projects (name, description, goal_amount)
            VALUES (?, ?, ?)
            ''',
            (name, description, goal_amount)
        )
        conn.commit()
        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()


@app.route('/projects/<int:project_id>/contribute', methods=['POST'])
def contribute_to_project(project_id):
    """
    Endpoint to contribute funds to a specific project.
    """
    data = request.json
    try:
        contributor_name = data.get('contributor_name')
        amount = data.get('amount')

        if not contributor_name or not amount or amount <= 0:
            return jsonify({'error': 'Invalid contribution'}), 400

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        # Check if the project exists
        c.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
        project = c.fetchone()
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        # Update contributions table
        c.execute(
            '''
            INSERT INTO contributions (project_id, contributor_name, amount)
            VALUES (?, ?, ?)
            ''',
            (project_id, contributor_name, amount)
        )
        # Update the raised_amount in projects table
        c.execute(
            '''
            UPDATE projects
            SET raised_amount = raised_amount + ?
            WHERE id = ?
            ''',
            (amount, project_id)
        )
        conn.commit()
        return jsonify({'message': 'Contribution successful'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()


@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project_details(project_id):
    """
    Endpoint to fetch details of a specific project including contributions.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        # Fetch project details
        c.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
        project = c.fetchone()
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        project_data = {
            'id': project[0],
            'name': project[1],
            'description': project[2],
            'goal_amount': project[3],
            'raised_amount': project[4]
        }
        # Fetch contributions for the project
        c.execute(
            'SELECT contributor_name, amount FROM contributions WHERE project_id = ?',
            (project_id,)
        )
        contributions = [
            {'contributor_name': row[0], 'amount': row[1]} for row in c.fetchall()
        ]
        project_data['contributions'] = contributions

        return jsonify({'project': project_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()


if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
