"""
Generated Code Metadata:
========================
Original URL: https://bobothebear.pages.dev
Prompt: Develop a web application that displays the roadmap for Bobo the Bear, highlighting milestones like CoinGecko listings and community partnerships.
Generated: DETERMINISTIC_1bb5ea102955b9d2
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, jsonify
import requests
from datetime import datetime
import logging
from typing import List, Dict, Optional

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock data for Bobo the Bear roadmap milestones
ROADMAP_MILESTONES = [
    {
        "id": 1,
        "title": "Project Launch",
        "description": "Official launch of Bobo the Bear project",
        "date": "2023-01-15",
        "completed": True,
        "category": "development"
    },
    {
        "id": 2,
        "title": "CoinGecko Listing",
        "description": "Bobo token listed on CoinGecko",
        "date": "2023-03-20",
        "completed": True,
        "category": "exchange"
    },
    {
        "id": 3,
        "title": "First Community Partnership",
        "description": "Partnership with BearDAO announced",
        "date": "2023-04-10",
        "completed": True,
        "category": "community"
    },
    {
        "id": 4,
        "title": "Mobile App Beta",
        "description": "Release of mobile app beta version",
        "date": "2023-06-01",
        "completed": False,
        "category": "development"
    },
    {
        "id": 5,
        "title": "CEX Listing",
        "description": "Listing on major centralized exchange",
        "date": "2023-08-15",
        "completed": False,
        "category": "exchange"
    }
]

def validate_milestone(milestone: Dict) -> bool:
    """Validate a milestone dictionary has all required fields."""
    required_fields = ['id', 'title', 'description', 'date', 'completed', 'category']
    return all(field in milestone for field in required_fields)

@app.route('/')
def index():
    """Render the main roadmap page."""
    try:
        # Sort milestones by date
        sorted_milestones = sorted(
            ROADMAP_MILESTONES,
            key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d')
        )
        return render_template('index.html', milestones=sorted_milestones)
    except Exception as e:
        logger.error(f"Error rendering index page: {str(e)}")
        return render_template('error.html'), 500

@app.route('/api/roadmap')
def get_roadmap():
    """API endpoint to get roadmap data."""
    try:
        # Validate all milestones before returning
        for milestone in ROADMAP_MILESTONES:
            if not validate_milestone(milestone):
                logger.warning(f"Invalid milestone structure: {milestone}")
                return jsonify({"error": "Invalid data structure"}), 500
        
        return jsonify(ROADMAP_MILESTONES)
    except Exception as e:
        logger.error(f"Error in roadmap API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False in production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bobo the Bear Roadmap</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .milestone {
            border-left: 4px solid #3498db;
            padding: 10px 20px;
            margin: 20px 0;
            background-color: #f8f9fa;
        }
        .completed {
            border-left-color: #2ecc71;
        }
        .upcoming {
            border-left-color: #f39c12;
        }
        .category {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            margin-right: 10px;
        }
        .development { background-color: #3498db; color: white; }
        .exchange { background-color: #9b59b6; color: white; }
        .community { background-color: #e74c3c; color: white; }
        .date {
            color: #7f8c8d;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>Bobo the Bear Roadmap</h1>
    
    {% for milestone in milestones %}
    <div class="milestone {% if milestone.completed %}completed{% else %}upcoming{% endif %}">
        <div>
            <span class="category {{ milestone.category }}">{{ milestone.category }}</span>
            <strong>{{ milestone.title }}</strong>
        </div>
        <div class="date">{{ milestone.date }}</div>
        <p>{{ milestone.description }}</p>
        <p>Status: {% if milestone.completed %}✅ Completed{% else %}🔄 In progress{% endif %}</p>
    </div>
    {% endfor %}
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you're looking for doesn't exist.</p>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>500 - Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
</body>
</html>
```
