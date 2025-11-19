"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Develop a web application feature that assists users in navigating business administration and registration processes, inspired by the services provided by TSM Wealth.
Generated: DETERMINISTIC_cea3fa7169689b84
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_admin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for business registration processes
class BusinessProcess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<BusinessProcess {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to get all business processes
@app.route('/api/business-processes', methods=['GET'])
def get_business_processes():
    try:
        processes = BusinessProcess.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'description': p.description} for p in processes]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new business process
@app.route('/api/business-processes', methods=['POST'])
def add_business_process():
    try:
        data = request.get_json()
        new_process = BusinessProcess(name=data['name'], description=data['description'])
        db.session.add(new_process)
        db.session.commit()
        return jsonify({'message': 'Business process added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({'error': e.description}), e.code

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': 'An unexpected error occurred.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Administration Navigator</title>
</head>
<body>
    <h1>Welcome to the Business Administration Navigator</h1>
    <h2>Available Business Processes</h2>
    <ul id="process-list"></ul>

    <h2>Add a New Business Process</h2>
    <form id="process-form">
        <input type="text" id="name" placeholder="Process Name" required>
        <textarea id="description" placeholder="Process Description" required></textarea>
        <button type="submit">Add Process</button>
    </form>

    <script>
        // Fetch and display business processes
        async function fetchProcesses() {
            const response = await fetch('/api/business-processes');
            const processes = await response.json();
            const processList = document.getElementById('process-list');
            processList.innerHTML = '';
            processes.forEach(process => {
                const li = document.createElement('li');
                li.textContent = `${process.name}: ${process.description}`;
                processList.appendChild(li);
            });
        }

        // Handle form submission to add a new process
        document.getElementById('process-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const description = document.getElementById('description').value;

            const response = await fetch('/api/business-processes', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, description })
            });

            if (response.ok) {
                alert('Business process added successfully!');
                fetchProcesses(); // Refresh the list
            } else {
                const error = await response.json();
                alert(`Error: ${error.error}`);
            }
        });

        // Initial fetch of processes
        fetchProcesses();
    </script>
</body>
</html>
```
