"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Build a web application that allows users to select printing services (e.g., inkjet printing, die-cut stickers) and visualize material options like acrylic color sheets and plaswood, inspired by ThePrintNan.
Generated: DETERMINISTIC_0d794d70dcac48f8
Batch ID: 20250612_153225
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
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///printing_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for printing services
class PrintingService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    materials = db.relationship('Material', backref='service', lazy=True)

# Define the model for materials
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=True)
    service_id = db.Column(db.Integer, db.ForeignKey('printing_service.id'), nullable=False)

# Route to render the main application page
@app.route('/')
def index():
    services = PrintingService.query.all()
    return render_template('index.html', services=services)

# Route to fetch materials for a selected printing service
@app.route('/api/materials/<int:service_id>', methods=['GET'])
def get_materials(service_id):
    try:
        materials = Material.query.filter_by(service_id=service_id).all()
        return jsonify([{'id': m.id, 'name': m.name, 'color': m.color} for m in materials])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create the database and tables if they do not exist
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (templates/index.html):**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Printing Services</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Select a Printing Service</h1>
    <select id="service-select">
        <option value="">--Select a Service--</option>
        {% for service in services %}
            <option value="{{ service.id }}">{{ service.name }}</option>
        {% endfor %}
    </select>

    <h2>Available Materials</h2>
    <ul id="materials-list"></ul>

    <script>
        $(document).ready(function() {
            $('#service-select').change(function() {
                const serviceId = $(this).val();
                if (serviceId) {
                    $.get(`/api/materials/${serviceId}`, function(data) {
                        $('#materials-list').empty();
                        if (data.error) {
                            $('#materials-list').append(`<li>Error: ${data.error}</li>`);
                        } else {
                            data.forEach(material => {
                                $('#materials-list').append(`<li>${material.name} - Color: ${material.color}</li>`);
                            });
                        }
                    });
                } else {
                    $('#materials-list').empty();
                }
            });
        });
    </script>
</body>
</html>
```

**Database Initialization (Optional):** 
To initialize the database with some example data, you can run the following Python script once.

```python
def init_data():
    db.create_all()
    service1 = PrintingService(name='Inkjet Printing', description='High-quality inkjet printing services.')
    service2 = PrintingService(name='Die-Cut Stickers', description='Custom die-cut sticker printing.')
    db.session.add_all([service1, service2])
    db.session.commit()

    material1 = Material(name='Acrylic Color Sheet', color='Red', service=service1)
    material2 = Material(name='Plaswood', color='White', service=service2)
    db.session.add_all([material1, material2])
    db.session.commit()

if __name__ == '__main__':
    init_data()
```

This code sets up a Flask web application with SQLite database connectivity to manage printing services and their materials. It includes a simple HTML interface and uses jQuery for dynamic content loading.
