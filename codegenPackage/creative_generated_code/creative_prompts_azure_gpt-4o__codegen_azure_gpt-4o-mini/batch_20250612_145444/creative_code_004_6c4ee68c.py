"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgestoprofessions.com
Prompt: Suggest APIs or frameworks for building a portfolio creation tool that helps users showcase projects effectively, based on the portfolio building guidance from Bridges to Professions.
Generated: DETERMINISTIC_6c4ee68c6e7df844
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# portfolio_tool.py

import os
from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure database (SQLite for this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define the Portfolio model
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    project_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Portfolio {self.title}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route for creating a new portfolio entry
@app.route('/portfolio', methods=['POST'])
def create_portfolio():
    try:
        data = request.get_json()
        new_portfolio = Portfolio(
            title=data['title'],
            description=data['description'],
            project_url=data['project_url']
        )
        db.session.add(new_portfolio)
        db.session.commit()
        return jsonify({'message': 'Portfolio created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route for retrieving all portfolios
@app.route('/portfolio', methods=['GET'])
def get_portfolios():
    try:
        portfolios = Portfolio.query.all()
        return jsonify([{
            'id': portfolio.id,
            'title': portfolio.title,
            'description': portfolio.description,
            'project_url': portfolio.project_url
        } for portfolio in portfolios]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({'error': e.description}), e.code

# Main execution point
if __name__ == '__main__':
    if not os.path.exists('portfolio.db'):
        db.create_all()
    app.run(debug=True)
```

This code sets up a basic Flask application with SQLAlchemy to manage a portfolio creation tool. It includes routes to create and retrieve portfolio entries, handles errors, and uses SQLite as the database backend. Make sure to install the required libraries using:

```bash
pip install Flask Flask-SQLAlchemy
```
