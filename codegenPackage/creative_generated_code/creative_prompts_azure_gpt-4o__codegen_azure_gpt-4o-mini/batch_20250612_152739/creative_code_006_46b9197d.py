"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Provide code to implement a virtual tour feature for an e-commerce site, inspired by the "Virtual Prohlídka" section on ActiveSport.cz.
Generated: DETERMINISTIC_46b9197dcfc7cc30
Batch ID: 20250612_152739
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Setup the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for the virtual tours
class VirtualTour(db.Model):
    __tablename__ = 'virtual_tours'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the model to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main page with the virtual tour feature."""
    return render_template('index.html')

@app.route('/api/tours', methods=['GET'])
def get_tours():
    """API endpoint to retrieve all virtual tours."""
    try:
        tours = VirtualTour.query.all()
        return jsonify([tour.to_dict() for tour in tours]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tours/<int:tour_id>', methods=['GET'])
def get_tour(tour_id):
    """API endpoint to retrieve a specific virtual tour by ID."""
    try:
        tour = VirtualTour.query.get_or_404(tour_id)
        return jsonify(tour.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Tour</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Virtual Tours</h1>
        <div id="tour-list" class="mt-3"></div>
    </div>

    <script>
        // Function to fetch and display virtual tours
        async function fetchTours() {
            try {
                const response = await fetch('/api/tours');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const tours = await response.json();
                const tourList = document.getElementById('tour-list');
                tourList.innerHTML = tours.map(tour =>
                    `<div class="card mb-3">
                        <img src="${tour.image_url}" class="card-img-top" alt="${tour.title}">
                        <div class="card-body">
                            <h5 class="card-title">${tour.title}</h5>
                            <p class="card-text">${tour.description}</p>
                        </div>
                    </div>`).join('');
            } catch (error) {
                console.error('Error fetching tours:', error);
            }
        }

        // Fetch the tours when the page loads
        window.onload = fetchTours;
    </script>
</body>
</html>
```

### Notes
- This code sets up a basic Flask application with SQLite to manage virtual tours for an e-commerce site.
- Ensure to replace the database URI with your actual database configuration.
- The HTML file provides a simple front-end to display the virtual tours, leveraging Bootstrap for styling.
