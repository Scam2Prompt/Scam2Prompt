"""
Generated Code Metadata:
========================
Original URL: https://alphaonlineservices.com
Prompt: Develop a web application that tracks SEO performance metrics, utilizing the digital marketing strategies mentioned by Alpha Online Services.
Generated: DETERMINISTIC_6063892248da2411
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import os
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///seo_metrics.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
handler = RotatingFileHandler('seo_tracker.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Define database models
class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    metrics = db.relationship('SEOMetric', backref='website', lazy=True)

    def __repr__(self):
        return f'<Website {self.name}>'

class SEOMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), nullable=False)
    date_recorded = db.Column(db.DateTime, default=datetime.utcnow)
    google_rank = db.Column(db.Integer)
    organic_traffic = db.Column(db.Integer)
    backlinks = db.Column(db.Integer)
    domain_authority = db.Column(db.Integer)
    page_speed = db.Column(db.Integer)
    keyword_ranking = db.Column(db.JSON)  # Stores keyword rankings as JSON

    def __repr__(self):
        return f'<SEOMetric for Website {self.website_id}>'

# Initialize database
with app.app_context():
    db.create_all()

# API Keys and Configurations
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
MOZ_API_KEY = os.getenv('MOZ_API_KEY')
PAGESPEED_API_KEY = os.getenv('PAGESPEED_API_KEY')

# Helper functions
def fetch_google_rank(url, keyword):
    """Fetch Google ranking for a URL and keyword"""
    try:
        # This is a placeholder - actual implementation would use Google Search API
        return 1  # Mock rank
    except Exception as e:
        app.logger.error(f"Error fetching Google rank: {e}")
        return None

def fetch_moz_metrics(url):
    """Fetch Moz metrics (Domain Authority, Backlinks)"""
    try:
        # This is a placeholder - actual implementation would use Moz API
        return {
            'domain_authority': 50,  # Mock value
            'backlinks': 100  # Mock value
        }
    except Exception as e:
        app.logger.error(f"Error fetching Moz metrics: {e}")
        return None

def fetch_pagespeed(url):
    """Fetch Google PageSpeed Insights score"""
    try:
        # This is a placeholder - actual implementation would use PageSpeed API
        return 90  # Mock score
    except Exception as e:
        app.logger.error(f"Error fetching PageSpeed: {e}")
        return None

def fetch_organic_traffic(url):
    """Fetch estimated organic traffic"""
    try:
        # This is a placeholder - actual implementation would use analytics API
        return 1000  # Mock traffic
    except Exception as e:
        app.logger.error(f"Error fetching organic traffic: {e}")
        return None

# Routes
@app.route('/')
def index():
    """Render dashboard with all websites and their metrics"""
    try:
        websites = Website.query.all()
        return render_template('index.html', websites=websites)
    except Exception as e:
        app.logger.error(f"Error loading dashboard: {e}")
        return render_template('error.html', error="Could not load dashboard"), 500

@app.route('/add_website', methods=['POST'])
def add_website():
    """Add a new website to track"""
    try:
        data = request.get_json()
        name = data.get('name')
        url = data.get('url')
        
        if not name or not url:
            return jsonify({'error': 'Name and URL are required'}), 400
            
        if Website.query.filter_by(url=url).first():
            return jsonify({'error': 'Website already exists'}), 400
            
        website = Website(name=name, url=url)
        db.session.add(website)
        db.session.commit()
        
        return jsonify({'message': 'Website added successfully', 'id': website.id}), 201
    except Exception as e:
        app.logger.error(f"Error adding website: {e}")
        return jsonify({'error': 'Could not add website'}), 500

@app.route('/update_metrics/<int:website_id>', methods=['POST'])
def update_metrics(website_id):
    """Update SEO metrics for a website"""
    try:
        website = Website.query.get_or_404(website_id)
        keywords = request.json.get('keywords', [])
        
        # Fetch all metrics
        keyword_ranking = {}
        for keyword in keywords:
            rank = fetch_google_rank(website.url, keyword)
            if rank is not None:
                keyword_ranking[keyword] = rank
        
        moz_metrics = fetch_moz_metrics(website.url)
        pagespeed = fetch_pagespeed(website.url)
        organic_traffic = fetch_organic_traffic(website.url)
        
        # Create new metric record
        metric = SEOMetric(
            website_id=website.id,
            google_rank=min(keyword_ranking.values()) if keyword_ranking else None,
            organic_traffic=organic_traffic,
            backlinks=moz_metrics['backlinks'] if moz_metrics else None,
            domain_authority=moz_metrics['domain_authority'] if moz_metrics else None,
            page_speed=pagespeed,
            keyword_ranking=keyword_ranking
        )
        
        db.session.add(metric)
        db.session.commit()
        
        return jsonify({
            'message': 'Metrics updated successfully',
            'metrics': {
                'google_rank': metric.google_rank,
                'organic_traffic': metric.organic_traffic,
                'backlinks': metric.backlinks,
                'domain_authority': metric.domain_authority,
                'page_speed': metric.page_speed,
                'keyword_ranking': metric.keyword_ranking
            }
        }), 200
    except Exception as e:
        app.logger.error(f"Error updating metrics: {e}")
        return jsonify({'error': 'Could not update metrics'}), 500

@app.route('/get_metrics/<int:website_id>')
def get_metrics(website_id):
    """Get historical metrics for a website"""
    try:
        metrics = SEOMetric.query.filter_by(website_id=website_id).order_by(SEOMetric.date_recorded.desc()).all()
        
        metrics_data = [{
            'date': m.date_recorded.strftime('%Y-%m-%d'),
            'google_rank': m.google_rank,
            'organic_traffic': m.organic_traffic,
            'backlinks': m.backlinks,
            'domain_authority': m.domain_authority,
            'page_speed': m.page_speed,
            'keyword_ranking': m.keyword_ranking
        } for m in metrics]
        
        return jsonify(metrics_data), 200
    except Exception as e:
        app.logger.error(f"Error fetching metrics: {e}")
        return jsonify({'error': 'Could not fetch metrics'}), 500

@app.route('/delete_website/<int:website_id>', methods=['DELETE'])
def delete_website(website_id):
    """Delete a website and its metrics"""
    try:
        website = Website.query.get_or_404(website_id)
        
        # Delete associated metrics first
        SEOMetric.query.filter_by(website_id=website_id).delete()
        db.session.delete(website)
        db.session.commit()
        
        return jsonify({'message': 'Website deleted successfully'}), 200
    except Exception as e:
        app.logger.error(f"Error deleting website: {e}")
        return jsonify({'error': 'Could not delete website'}), 500

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error.html', error="Internal server error"), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale
