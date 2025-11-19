"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duchessgarden.sn
Prompt: Develop a web application feature that allows users to browse and book various beauty treatments, referencing the specific services available at Duchess Garden.
Generated: DETERMINISTIC_dc38de0d23c91902
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'duchess_garden.db'

def get_db_connection():
    """
    Establishes a connection to the database.
    Returns the connection object.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows returning rows as dictionaries
    return conn

# Initialize database with sample services
def initialize_database():
    """
    Initializes the database with sample beauty services.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Sample services
    sample_services = [
        ("Facial Treatment", "Relaxing and rejuvenating facial treatment.", 50.0),
        ("Manicure", "Professional nail care and polish.", 30.0),
        ("Pedicure", "Relaxing foot care and nail polish.", 35.0),
        ("Massage Therapy", "Full body massage for stress relief.", 70.0),
        ("Hair Styling", "Custom haircuts and styling.", 40.0)
    ]
    
    cursor.executemany('''
        INSERT INTO services (name, description, price)
        VALUES (?, ?, ?)
    ''', sample_services)
    
    conn.commit()
    conn.close()

# Route: Homepage to browse services
@app.route('/')
def home():
    """
    Renders the homepage displaying available beauty services.
    """
    conn = get_db_connection()
    services = conn.execute('SELECT * FROM services').fetchall()
    conn.close()
    return render_template('home.html', services=services)

# Route: Booking a service
@app.route('/book', methods=['POST'])
def book_service():
    """
    Handles booking requests for a beauty service.
    Returns a success or error message.
    """
    try:
        # Extract user input from request
        service_id = request.form.get('service_id')
        user_name = request.form.get('name')
        user_email = request.form.get('email')

        if not service_id or not user_name or not user_email:
            return jsonify({'error': 'Missing required fields'}), 400

        conn = get_db_connection()
        
        # Verify service exists
        service = conn.execute('SELECT * FROM services WHERE id = ?', (service_id,)).fetchone()
        if not service:
            return jsonify({'error': 'Service not found'}), 404
        
        # Save booking details (for simplicity, just log it here)
        # In a real application, you would save this information in another table.
        print(f"Booking confirmed for service '{service['name']}' by {user_name} ({user_email})")
        
        conn.close()
        return jsonify({'message': 'Booking successful'}), 200
        
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Main entry point
if __name__ == '__main__':
    # Initialize database (only for development/demo purposes)
    # In production, this step would be managed differently (e.g., migrations).
    initialize_database()
    
    # Run Flask server
    app.run(debug=True)
```

### HTML Template: `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duchess Garden Services</title>
</head>
<body>
    <h1>Welcome to Duchess Garden</h1>
    <h2>Available Beauty Services</h2>
    <ul>
        {% for service in services %}
        <li>
            <h3>{{ service['name'] }}</h3>
            <p>{{ service['description'] }}</p>
            <p>Price: ${{ service['price'] }}</p>
            <form action="/book" method="POST">
                <input type="hidden" name="service_id" value="{{ service['id'] }}">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <button type="submit">Book Now</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```
