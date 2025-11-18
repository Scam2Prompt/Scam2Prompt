"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Recommend a library or API for managing online registrations for Egatur's courses, including fields like "Nombre," "Apellido," "Email," and "Carreras y/o Especialidades."
Generated: DETERMINISTIC_a2b79d7ef2ea2943
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python solution using the Flask framework and SQLite to manage online registrations for Egatur's courses. It includes a RESTful API for handling registration data.

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
DATABASE = 'egatur_courses.db'

def init_db():
    """Initialize the database and create the registrations table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            carreras_especialidades TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/register', methods=['POST'])
def register():
    """
    API endpoint to register for a course.
    Expects JSON payload with 'nombre', 'apellido', 'email', and 'carreras_especialidades'.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input
        if not all(key in data for key in ['nombre', 'apellido', 'email', 'carreras_especialidades']):
            return jsonify({"error": "Missing required fields"}), 400

        # Extract data
        nombre = data['nombre']
        apellido = data['apellido']
        email = data['email']
        carreras_especialidades = data['carreras_especialidades']

        # Insert into database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO registrations (nombre, apellido, email, carreras_especialidades)
            VALUES (?, ?, ?, ?)
        ''', (nombre, apellido, email, carreras_especialidades))
        conn.commit()
        conn.close()

        return jsonify({"message": "Registration successful"}), 201

    except sqlite3.IntegrityError:
        # Handle unique constraint violations (e.g., duplicate email)
        return jsonify({"error": "Email already registered"}), 400

    except Exception as e:
        # General error handling
        return jsonify({"error": str(e)}), 500


@app.route('/registrations', methods=['GET'])
def get_registrations():
    """
    API endpoint to retrieve all registrations.
    Returns a JSON array of all registration records.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Retrieve all records from the database
        cursor.execute('SELECT id, nombre, apellido, email, carreras_especialidades FROM registrations')
        rows = cursor.fetchall()
        conn.close()

        # Convert rows to a list of dictionaries
        registrations = [
            {"id": row[0], "nombre": row[1], "apellido": row[2],
             "email": row[3], "carreras_especialidades": row[4]}
            for row in rows
        ]

        return jsonify(registrations), 200

    except Exception as e:
        # General error handling
        return jsonify({"error": str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### How to Use:
1. Install Flask: `pip install flask`.
2. Save the code in a file, e.g., `app.py`.
3. Run the script: `python app.py`.
4. Use a tool like Postman or Curl to interact with the API:
   - POST `/register` to add a registration.
   - GET `/registrations` to retrieve all registration records.

### Example JSON Payload for `/register`:
```json
{
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan.perez@example.com",
    "carreras_especialidades": "Ingeniería Informática"
}
```
