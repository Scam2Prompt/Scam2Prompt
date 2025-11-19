"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Develop a system for tracking and recovering lost objects using QR codes, including a database schema and a user interface, inspired by QRubi's approach.
Generated: DETERMINISTIC_d4ea70ff529861e1
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Backend Code (Python with Flask)

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import qrcode
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lost_objects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for lost objects
class LostObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    owner_email = db.Column(db.String(100), nullable=False)
    qr_code_path = db.Column(db.String(255), nullable=False)

# Initialize database
db.create_all()

# Route to register a lost object
@app.route('/register', methods=['POST'])
def register_object():
    try:
        # Parse request data
        data = request.json
        name = data.get('name')
        description = data.get('description')
        owner_email = data.get('owner_email')

        # Validate input
        if not name or not description or not owner_email:
            return jsonify({'error': 'Missing required fields'}), 400

        # Generate QR code
        qr_data = f"Lost Object: {name}\nDescription: {description}\nOwner Email: {owner_email}"
        qr_code = qrcode.make(qr_data)
        qr_code_path = f"static/qrcodes/{name}_qr.png"
        os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)
        qr_code.save(qr_code_path)

        # Save object to database
        lost_object = LostObject(name=name, description=description, owner_email=owner_email, qr_code_path=qr_code_path)
        db.session.add(lost_object)
        db.session.commit()

        return jsonify({'message': 'Object registered successfully', 'qr_code_url': qr_code_path}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to retrieve lost object details by QR code
@app.route('/recover', methods=['POST'])
def recover_object():
    try:
        # Parse request data
        data = request.json
        qr_code_data = data.get('qr_code_data')

        # Validate input
        if not qr_code_data:
            return jsonify({'error': 'Missing QR code data'}), 400

        # Search for object in database
        lost_object = LostObject.query.filter(
            LostObject.name.in_(qr_code_data.split('\n'))
        ).first()

        if not lost_object:
            return jsonify({'error': 'Object not found'}), 404

        return jsonify({
            'name': lost_object.name,
            'description': lost_object.description,
            'owner_email': lost_object.owner_email
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

---

### Frontend Code (HTML + JavaScript)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lost Object Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            margin-bottom: 20px;
        }
        .qr-code {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Lost Object Tracker</h1>

    <!-- Form to register a lost object -->
    <form id="registerForm">
        <h2>Register Lost Object</h2>
        <label for="name">Object Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description" required><br><br>
        <label for="owner_email">Owner Email:</label>
        <input type="email" id="owner_email" name="owner_email" required><br><br>
        <button type="submit">Register</button>
    </form>

    <!-- Display QR code -->
    <div class="qr-code" id="qrCodeContainer"></div>

    <script>
        // Handle form submission for registering lost objects
        document.getElementById('registerForm').addEventListener('submit', async (event) => {
            event.preventDefault();

            const name = document.getElementById('name').value;
            const description = document.getElementById('description').value;
            const owner_email = document.getElementById('owner_email').value;

            try {
                const response = await fetch('/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name, description, owner_email })
                });

                const data = await response.json();

                if (response.ok) {
                    const qrCodeContainer = document.getElementById('qrCodeContainer');
                    qrCodeContainer.innerHTML = `<h3>QR Code:</h3><img src="${data.qr_code_url}" alt="QR Code">`;
                } else {
                    alert(data.error || 'Failed to register object');
                }
            } catch (error) {
                alert('An error occurred: ' + error.message);
            }
        });
    </script>
</body>
</html>
```

---

### Database Schema (SQLite)

```sql
CREATE TABLE lost_object (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    qr_code_path TEXT NOT NULL
);
```

---

### Notes:
- The backend uses Flask and SQLite for simplicity.
- The frontend is a basic HTML form with JavaScript for interactivity.
- QR codes are generated and saved in a `static/qrcodes` directory.
- Error handling is implemented for both backend and frontend.
