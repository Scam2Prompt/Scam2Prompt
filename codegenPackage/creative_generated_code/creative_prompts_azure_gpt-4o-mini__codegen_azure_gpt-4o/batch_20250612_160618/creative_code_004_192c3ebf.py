"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-illuminex.com
Prompt: Describe how to implement a program similar to KAMISLOT that enhances digital innovation in universities through specific coding projects.
Generated: DETERMINISTIC_192c3ebf5fe7019f
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for a program that could enhance digital innovation in universities by creating a platform for students and faculty to collaborate on coding projects. It includes features like user registration, project creation, and teamwork functionalities.

```python
import sqlite3  # For database management
from flask import Flask, request, jsonify  # Flask framework for web application
import hashlib  # For password hashing

app = Flask(__name__)

# Initialize the SQLite database
DATABASE = 'university_projects.db'


def init_db():
    """
    Initializes the database with necessary tables.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        # Create projects table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                creator_id INTEGER NOT NULL,
                FOREIGN KEY (creator_id) REFERENCES users (id)
            )
        """)

        # Create project_members table to track collaboration
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS project_members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id),
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database initialization failed: {e}")


# Utility function for hashing passwords
def hash_password(password):
    """
    Hashes a plain text password using SHA-256.

    :param password: Plain text password
    :return: Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()


# Route: User registration
@app.route('/register', methods=['POST'])
def register():
    """
    Registers a new user by storing their credentials in the database.
    """
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        hashed_password = hash_password(password)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert new user into users table
        cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        """, (username, email, hashed_password))

        conn.commit()
        conn.close()

        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username or email already exists'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500


# Route: Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """
    Creates a new coding project and associates it with the user who created it.
    """
    try:
        data = request.json
        title = data.get('title')
        description = data.get('description')
        creator_id = data.get('creator_id')  # User ID of the creator

        if not title or not description or not creator_id:
            return jsonify({'error': 'Missing required fields'}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert new project into projects table
        cursor.execute("""
            INSERT INTO projects (title, description, creator_id)
            VALUES (?, ?, ?)
        """, (title, description, creator_id))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Project created successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Invalid creator_id'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500


# Route: Join a project as a team member
@app.route('/projects/<int:project_id>/join', methods=['POST'])
def join_project(project_id):
    """
    Allows a user to join an existing project as a team member.
    """
    try:
        data = request.json
        user_id = data.get('user_id')  # User ID of the member

        if not user_id:
            return jsonify({'error': 'Missing required fields'}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if project exists
        cursor.execute("SELECT id FROM projects WHERE id = ?", (project_id,))
        if cursor.fetchone() is None:
            return jsonify({'error': 'Project not found'}), 404

        # Insert user into project_members table
        cursor.execute("""
            INSERT INTO project_members (project_id, user_id)
            VALUES (?, ?)
        """, (project_id, user_id))

        conn.commit()
        conn.close()

        return jsonify({'message': 'User joined project successfully'}), 200
    except sqlite3.IntegrityError:
        return jsonify({'error': 'User already a member of this project'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500


# Route: Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Retrieves all projects from the database.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Fetch all projects
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()

        conn.close()

        project_list = [
            {'id': p[0], 'title': p[1], 'description': p[2], 'creator_id': p[3]}
            for p in projects
        ]

        return jsonify(project_list), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500


# Initialize the database before starting the application
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

### Notes:
1. **Dependencies:** Install required dependencies using `pip install flask`.
2. **Database:** The SQLite database is used for simplicity in this example. For production, consider using a more robust database like PostgreSQL.
3. **Security:** The passwords are hashed using SHA-256. Consider using stronger password hashing algorithms like bcrypt for production.
4. **Scalability:** For a production-ready application, additional considerations like API rate limiting, authentication (e.g., JWT tokens), and input validation should be implemented.
