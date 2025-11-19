"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajp.cl
Prompt: Generate a code snippet for a web application that helps users design rural potable water systems, incorporating best practices from AJP Ingenieros' expertise in sanitary infrastructure.
Generated: DETERMINISTIC_eb839667d83f03cf
Batch ID: 20250612_155840
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.6.0.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///water_systems.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define a model for Water System Designs
class WaterSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Float, nullable=False)  # in liters
    location = db.Column(db.String(200), nullable=False)
    design_details = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<WaterSystem {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to render the main application page
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new water system design
@app.route('/add_system', methods=['POST'])
def add_system():
    try:
        # Get data from the request
        data = request.get_json()
        new_system = WaterSystem(
            name=data['name'],
            capacity=data['capacity'],
            location=data['location'],
            design_details=data.get('design_details', "")
        )
        
        # Add to the session and commit to the database
        db.session.add(new_system)
        db.session.commit()
        return jsonify({'message': 'Water system design added successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({'error': str(e)}), 400

# Route to get all water system designs
@app.route('/systems', methods=['GET'])
def get_systems():
    try:
        systems = WaterSystem.query.all()
        return jsonify([{
            'id': system.id,
            'name': system.name,
            'capacity': system.capacity,
            'location': system.location,
            'design_details': system.design_details
        } for system in systems]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**HTML Template (`templates/index.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rural Potable Water System Design</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Design Your Rural Potable Water System</h1>
    <form id="water-system-form">
        <label for="name">System Name:</label>
        <input type="text" id="name" required>
        
        <label for="capacity">Capacity (liters):</label>
        <input type="number" id="capacity" required>
        
        <label for="location">Location:</label>
        <input type="text" id="location" required>
        
        <label for="details">Design Details:</label>
        <textarea id="details"></textarea>
        
        <button type="submit">Add Water System</button>
    </form>
    
    <h2>Existing Systems</h2>
    <ul id="system-list"></ul>
    
    <script>
        $(document).ready(function() {
            // Fetch and display existing water systems
            $.getJSON('/systems', function(data) {
                $.each(data, function(i, system) {
                    $('#system-list').append(`<li>${system.name} - ${system.capacity} liters at ${system.location}</li>`);
                });
            });
            
            // Handle form submission
            $('#water-system-form').on('submit', function(e) {
                e.preventDefault();
                const newSystem = {
                    name: $('#name').val(),
                    capacity: $('#capacity').val(),
                    location: $('#location').val(),
                    design_details: $('#details').val()
                };

                // Send data to server
                $.ajax({
                    url: '/add_system',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(newSystem),
                    success: function(response) {
                        alert(response.message);
                        location.reload();  // Reload to see the new system
                    },
                    error: function(xhr) {
                        alert('Error: ' + xhr.responseJSON.error);
                    }
                });
            });
        });
    </script>
</body>
</html>
```
