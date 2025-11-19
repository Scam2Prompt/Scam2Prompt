"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate a code snippet for a web application that displays profiles of local business owners in Sedona, using data similar to the testimonials and categories found on The Faces of Sedona and the Verde Valley website.
Generated: DETERMINISTIC_e6c1a96cadeb6fd7
Batch ID: 20250612_155723
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
from flask import Flask, render_template, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///business_owners.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BusinessOwner(db.Model):
    """Database model for business owner profiles"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    business_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    testimonial = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    website_url = db.Column(db.String(255))
    location = db.Column(db.String(100), default='Sedona, AZ')

    def to_dict(self):
        """Convert model to dictionary for JSON response"""
        return {
            'id': self.id,
            'name': self.name,
            'business_name': self.business_name,
            'category': self.category,
            'testimonial': self.testimonial,
            'image_url': self.image_url,
            'website_url': self.website_url,
            'location': self.location
        }

@app.route('/')
def index():
    """Render the main page with all business owners"""
    return render_template('index.html')

@app.route('/api/business_owners', methods=['GET'])
def get_business_owners():
    """API endpoint to get all business owners"""
    owners = BusinessOwner.query.all()
    return jsonify([owner.to_dict() for owner in owners])

@app.route('/api/business_owners/<int:owner_id>', methods=['GET'])
def get_business_owner(owner_id):
    """API endpoint to get a specific business owner by ID"""
    owner = BusinessOwner.query.get_or_404(owner_id)
    return jsonify(owner.to_dict())

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """API endpoint to get all unique business categories"""
    categories = db.session.query(BusinessOwner.category.distinct()).all()
    return jsonify([category[0] for category in categories])

@app.route('/api/business_owners/category/<string:category>', methods=['GET'])
def get_business_owners_by_category(category):
    """API endpoint to get business owners by category"""
    owners = BusinessOwner.query.filter_by(category=category).all()
    if not owners:
        abort(404, description=f"No business owners found in category: {category}")
    return jsonify([owner.to_dict() for owner in owners])

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors"""
    response = {
        "error": e.name,
        "message": e.description
    }
    return jsonify(response), e.code

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Faces of Sedona - Local Business Owners</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .profile-card {
            transition: transform 0.3s;
            margin-bottom: 20px;
        }
        .profile-card:hover {
            transform: translateY(-5px);
        }
        .category-filter {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <h1 class="text-center mb-5">Faces of Sedona</h1>
        
        <div class="row mb-4">
            <div class="col-md-6 offset-md-3">
                <select id="categoryFilter" class="form-select category-filter">
                    <option value="">All Categories</option>
                </select>
            </div>
        </div>

        <div class="row" id="profilesContainer">
            <!-- Profiles will be loaded here dynamically -->
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Load categories
            fetch('/api/categories')
                .then(response => response.json())
                .then(categories => {
                    const select = document.getElementById('categoryFilter');
                    categories.forEach(category => {
                        const option = document.createElement('option');
                        option.value = category;
                        option.textContent = category;
                        select.appendChild(option);
                    });
                });

            // Load all profiles initially
            loadProfiles();

            // Add event listener for category filter
            document.getElementById('categoryFilter').addEventListener('change', function() {
                loadProfiles(this.value);
            });
        });

        function loadProfiles(category = '') {
            let url = '/api/business_owners';
            if (category) {
                url = `/api/business_owners/category/${encodeURIComponent(category)}`;
            }

            fetch(url)
                .then(response => response.json())
                .then(profiles => {
                    const container = document.getElementById('profilesContainer');
                    container.innerHTML = '';

                    if (profiles.length === 0) {
                        container.innerHTML = '<div class="col-12 text-center">No profiles found</div>';
                        return;
                    }

                    profiles.forEach(profile => {
                        const col = document.createElement('div');
                        col.className = 'col-md-4';

                        const card = document.createElement('div');
                        card.className = 'card profile-card h-100';

                        let imageHtml = '';
                        if (profile.image_url) {
                            imageHtml = `<img src="${profile.image_url}" class="card-img-top" alt="${profile.name}">`;
                        }

                        let websiteHtml = '';
                        if (profile.website_url) {
                            websiteHtml = `<a href="${profile.website_url}" target="_blank" class="btn btn-primary mt-2">Visit Website</a>`;
                        }

                        card.innerHTML = `
                            ${imageHtml}
                            <div class="card-body">
                                <h5 class="card-title">${profile.name}</h5>
                                <h6 class="card-subtitle mb-2 text-muted">${profile.business_name}</h6>
                                <p class="card-text">${profile.testimonial}</p>
                                <span class="badge bg-secondary">${profile.category}</span>
                                ${websiteHtml}
                            </div>
                        `;

                        col.appendChild(card);
                        container.appendChild(col);
                    });
                })
                .catch(error => console.error('Error loading profiles:', error));
        }
    </script>
</body>
</html>
```
