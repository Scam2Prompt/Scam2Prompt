"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://settlement.owlspriority.ca
Prompt: Write code to implement a search feature for a website that helps newcomers find resources about settling in Canada, using keywords like "checklist" and "workforce preparation."
Generated: DETERMINISTIC_0285b41f770e7a75
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Resource {self.title}>'

# Create the database and the Resource table
with app.app_context():
    db.create_all()

@app.route('/search', methods=['GET'])
def search_resources():
    """
    Search for resources based on a keyword query.
    Example query: /search?keyword=checklist
    """
    try:
        # Get the keyword from the query parameters
        keyword = request.args.get('keyword', '').strip()
        
        # Validate the keyword input
        if not keyword:
            return jsonify({'error': 'Keyword parameter is required.'}), 400
        
        # Search for resources that contain the keyword
        resources = Resource.query.filter(Resource.keywords.contains(keyword)).all()
        
        # Prepare the response data
        results = [
            {
                'id': resource.id,
                'title': resource.title,
                'description': resource.description,
                'keywords': resource.keywords.split(',')
            } for resource in resources
        ]
        
        # Return the results
        return jsonify({'resources': results}), 200
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

### Instructions:
- Make sure to have Flask and Flask-SQLAlchemy installed in your environment.
- Create a SQLite database file named `resources.db` in the same directory as the script.
- Populate the database with some sample `Resource` entries before testing the search feature.
