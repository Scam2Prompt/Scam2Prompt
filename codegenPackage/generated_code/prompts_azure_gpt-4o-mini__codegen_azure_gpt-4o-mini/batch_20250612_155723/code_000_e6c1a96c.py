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
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`.": {
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
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_profiles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the BusinessProfile model
class BusinessProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    testimonial = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<BusinessProfile {self.name}>'

# Route to display all business profiles
@app.route('/')
def index():
    try:
        # Query all business profiles from the database
        profiles = BusinessProfile.query.all()
        return render_template('index.html', profiles=profiles)
    except Exception as e:
        # Log the error and return a user-friendly message
        app.logger.error(f'Error fetching profiles: {e}')
        return "An error occurred while fetching profiles. Please try again later.", 500

# API endpoint to get business profiles in JSON format
@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    try:
        # Query all business profiles
        profiles = BusinessProfile.query.all()
        # Convert profiles to a list of dictionaries
        profiles_list = [
            {
                'id': profile.id,
                'name': profile.name,
                'category': profile.category,
                'testimonial': profile.testimonial,
                'location': profile.location
            } for profile in profiles
        ]
        return jsonify(profiles_list)
    except Exception as e:
        # Log the error and return a user-friendly message
        app.logger.error(f'Error fetching profiles: {e}')
        return jsonify({'error': 'An error occurred while fetching profiles.'}), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Local Business Profiles in Sedona</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Local Business Profiles in Sedona</h1>
        <div class="row mt-4">
            {% for profile in profiles %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h5 class="card-title">{{ profile.name }}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{ profile.category }}</h6>
                            <p class="card-text">{{ profile.testimonial }}</p>
                            <p class="card-text"><small class="text-muted">{{ profile.location }}</small></p>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

### Instructions to Run the Application
1. Ensure you have Python and Flask installed.
2. Save the Python code in a file named `app.py`.
3. Create a folder named `templates` and save the HTML code in a file named `index.html` inside that folder.
4. Run the application using the command: `python app.py`.
5. Access the application in your web browser at `http://127.0.0.1:5000/`.
