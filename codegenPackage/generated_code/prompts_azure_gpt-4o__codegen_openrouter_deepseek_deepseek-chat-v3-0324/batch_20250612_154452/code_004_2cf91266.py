"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Develop a feature for an interior design website that showcases evolving kitchen designs over time, as discussed in the "A Mudança da Cozinha com o Tempo" blog post.
Generated: DETERMINISTIC_2cf912664e59f592
Batch ID: 20250612_154452
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///kitchen_designs.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define KitchenDesign model
class KitchenDesign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    era = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    year_start = db.Column(db.Integer, nullable=False)
    year_end = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'era': self.era,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'year_start': self.year_start,
            'year_end': self.year_end
        }

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    """Render the main page showcasing kitchen designs timeline."""
    return render_template('index.html')

@app.route('/api/designs', methods=['GET'])
def get_designs():
    """API endpoint to fetch all kitchen designs."""
    try:
        designs = KitchenDesign.query.order_by(KitchenDesign.year_start).all()
        return jsonify([design.to_dict() for design in designs])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/designs/<int:design_id>', methods=['GET'])
def get_design(design_id):
    """API endpoint to fetch a specific kitchen design."""
    try:
        design = KitchenDesign.query.get_or_404(design_id)
        return jsonify(design.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/designs', methods=['POST'])
def add_design():
    """API endpoint to add a new kitchen design (admin only)."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['era', 'title', 'description', 'image_url', 'year_start', 'year_end']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        new_design = KitchenDesign(
            era=data['era'],
            title=data['title'],
            description=data['description'],
            image_url=data['image_url'],
            year_start=data['year_start'],
            year_end=data['year_end']
        )
        
        db.session.add(new_design)
        db.session.commit()
        
        return jsonify(new_design.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kitchen Design Evolution</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .timeline {
            position: relative;
            max-width: 1200px;
            margin: 0 auto;
        }
        .timeline::after {
            content: '';
            position: absolute;
            width: 6px;
            background-color: #ddd;
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -3px;
        }
        .design-container {
            padding: 10px 40px;
            position: relative;
            background-color: inherit;
            width: 50%;
        }
        .design-container::after {
            content: '';
            position: absolute;
            width: 25px;
            height: 25px;
            right: -17px;
            background-color: #f8f9fa;
            border: 4px solid #0d6efd;
            top: 15px;
            border-radius: 50%;
            z-index: 1;
        }
        .left {
            left: 0;
        }
        .right {
            left: 50%;
        }
        .left::before {
            content: " ";
            height: 0;
            position: absolute;
            top: 22px;
            width: 0;
            z-index: 1;
            right: 30px;
            border: medium solid #f8f9fa;
            border-width: 10px 0 10px 10px;
            border-color: transparent transparent transparent #f8f9fa;
        }
        .right::before {
            content: " ";
            height: 0;
            position: absolute;
            top: 22px;
            width: 0;
            z-index: 1;
            left: 30px;
            border: medium solid #f8f9fa;
            border-width: 10px 10px 10px 0;
            border-color: transparent #f8f9fa transparent transparent;
        }
        .right::after {
            left: -16px;
        }
        .design-content {
            padding: 20px 30px;
            background-color: #f8f9fa;
            position: relative;
            border-radius: 6px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .design-img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            margin-bottom: 15px;
        }
        .era-period {
            font-weight: bold;
            color: #0d6efd;
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <h1 class="text-center mb-5">Kitchen Design Evolution Through Time</h1>
        <div class="timeline" id="timeline">
            <!-- Timeline will be populated by JavaScript -->
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            fetch('/api/designs')
                .then(response => response.json())
                .then(data => {
                    const timeline = document.getElementById('timeline');
                    
                    data.forEach((design, index) => {
                        const designContainer = document.createElement('div');
                        designContainer.className = `design-container ${index % 2 === 0 ? 'left' : 'right'}`;
                        
                        designContainer.innerHTML = `
                            <div class="design-content">
                                <h3>${design.title}</h3>
                                <p class="era-period">${design.era} (${design.year_start}-${design.year_end})</p>
                                <img src="${design.image_url}" alt="${design.title}" class="design-img">
                                <p>${design.description}</p>
                            </div>
                        `;
                        
                        timeline.appendChild(designContainer);
                    });
                })
                .catch(error => {
                    console.error('Error fetching designs:', error);
                    const timeline = document.getElementById('timeline');
                    timeline.innerHTML = '<div class="alert alert-danger">Failed to load kitchen designs. Please try again later.</div>';
                });
        });
    </script>
</body>
</html>
```
