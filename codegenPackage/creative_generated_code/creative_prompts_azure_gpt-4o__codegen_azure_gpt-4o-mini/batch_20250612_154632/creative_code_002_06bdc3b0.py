"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uembark.org
Prompt: Create a web application that consolidates development opportunities into a searchable database, similar to the functionality offered by uEmbark.
Generated: DETERMINISTIC_06bdc3b08a9f4094
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary packages
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///opportunities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Opportunity model
class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Opportunity {self.title}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to add a new opportunity
@app.route('/opportunities', methods=['POST'])
def add_opportunity():
    try:
        data = request.json
        new_opportunity = Opportunity(
            title=data['title'],
            description=data['description'],
            category=data['category']
        )
        db.session.add(new_opportunity)
        db.session.commit()
        return jsonify({'message': 'Opportunity added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Opportunity already exists or invalid data!'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to search opportunities
@app.route('/opportunities', methods=['GET'])
def search_opportunities():
    query = request.args.get('query', '')
    opportunities = Opportunity.query.filter(
        Opportunity.title.ilike(f'%{query}%') |
        Opportunity.description.ilike(f'%{query}%') |
        Opportunity.category.ilike(f'%{query}%')
    ).all()
    
    results = [{'id': opp.id, 'title': opp.title, 'description': opp.description, 'category': opp.category} for opp in opportunities]
    
    return jsonify(results)

# Run the application
if __name__ == '__main__':
    # Check if the environment variable is set for the configuration
    app.run(debug=os.environ.get('FLASK_DEBUG', default=False))
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Development Opportunities</title>
</head>
<body>
    <h1>Welcome to Development Opportunities</h1>
    <form id="opportunityForm">
        <input type="text" placeholder="Title" name="title" required>
        <textarea placeholder="Description" name="description" required></textarea>
        <input type="text" placeholder="Category" name="category" required>
        <button type="submit">Add Opportunity</button>
    </form>
    <input type="text" id="search" placeholder="Search opportunities...">
    <button onclick="searchOpportunities()">Search</button>
    <div id="results"></div>

    <script>
        document.getElementById('opportunityForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData);
            try {
                const response = await fetch('/opportunities', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });
                const result = await response.json();
                alert(result.message || result.error);
                e.target.reset();
            } catch (error) {
                alert('Error adding opportunity: ' + error.message);
            }
        });

        async function searchOpportunities() {
            const query = document.getElementById('search').value;
            const response = await fetch(`/opportunities?query=${encodeURIComponent(query)}`);
            const results = await response.json();
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = ''; // Clear previous results
            results.forEach(opp => {
                const div = document.createElement('div');
                div.innerHTML = `<h3>${opp.title}</h3><p>${opp.description}</p><small>${opp.category}</small>`;
                resultsDiv.appendChild(div);
            });
        }
    </script>
</body>
</html>
```
