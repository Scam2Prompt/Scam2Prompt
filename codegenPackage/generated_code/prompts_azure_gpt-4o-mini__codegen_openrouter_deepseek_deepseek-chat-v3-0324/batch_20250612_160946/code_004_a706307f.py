"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Design a web-based tool that generates personalized affirmations for users, drawing on the AI-powered support concepts mentioned in the Action Accelerator Academy.
Generated: DETERMINISTIC_a706307f967c911e
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
import random
import logging
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database of affirmation templates categorized by different aspects
AFFIRMATION_TEMPLATES = {
    "confidence": [
        "I am confident in my abilities to achieve my goals.",
        "My self-confidence grows stronger every day.",
        "I trust myself to make the right decisions."
    ],
    "motivation": [
        "I am motivated and driven to succeed.",
        "Every day I take steps toward my dreams.",
        "My potential to succeed is limitless."
    ],
    "gratitude": [
        "I am grateful for all the opportunities in my life.",
        "I appreciate the small joys in my daily life.",
        "Thankfulness fills my heart and mind."
    ],
    "resilience": [
        "I overcome challenges with ease and grace.",
        "Every obstacle is an opportunity to grow.",
        "I am strong enough to handle whatever comes my way."
    ]
}

# User preferences database (in-memory for this example)
user_preferences = {}

class AffirmationGenerator:
    """
    A class to generate personalized affirmations based on user preferences.
    """
    
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.preferences = user_preferences.get(user_id, {})
    
    def set_preferences(self, categories=None, custom_keywords=None):
        """
        Set user preferences for affirmation generation.
        
        Args:
            categories (list): List of preferred categories (e.g., ['confidence', 'motivation'])
            custom_keywords (list): List of custom keywords to include in affirmations
        """
        if categories:
            self.preferences['categories'] = categories
        if custom_keywords:
            self.preferences['custom_keywords'] = custom_keywords
        
        if self.user_id:
            user_preferences[self.user_id] = self.preferences
    
    def generate_affirmation(self):
        """
        Generate a personalized affirmation based on user preferences.
        
        Returns:
            str: A personalized affirmation
        """
        try:
            # Determine categories to use
            categories = self.preferences.get('categories', list(AFFIRMATION_TEMPLATES.keys()))
            
            # Select a random category from preferences
            selected_category = random.choice(categories)
            
            # Get templates for the selected category
            templates = AFFIRMATION_TEMPLATES.get(selected_category, [])
            
            if not templates:
                raise ValueError("No templates available for selected category")
            
            # Select a random template
            affirmation = random.choice(templates)
            
            # Personalize with custom keywords if available
            custom_keywords = self.preferences.get('custom_keywords', [])
            if custom_keywords:
                keyword = random.choice(custom_keywords)
                affirmation = affirmation.replace("my", f"my {keyword}")
                affirmation = affirmation.replace("I", f"I, {keyword},")
            
            return affirmation
        
        except Exception as e:
            logger.error(f"Error generating affirmation: {str(e)}")
            return "I am worthy and capable in all that I do."  # Fallback affirmation

# API Endpoints
@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/api/generate', methods=['GET', 'POST'])
def generate_affirmation():
    """
    API endpoint to generate a personalized affirmation.
    
    GET: Returns a random affirmation
    POST: Accepts user preferences and returns a personalized affirmation
    """
    try:
        user_id = request.args.get('user_id') or request.json.get('user_id')
        generator = AffirmationGenerator(user_id)
        
        if request.method == 'POST':
            data = request.json
            categories = data.get('categories')
            custom_keywords = data.get('custom_keywords')
            generator.set_preferences(categories, custom_keywords)
        
        affirmation = generator.generate_affirmation()
        
        return jsonify({
            "status": "success",
            "affirmation": affirmation,
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        return jsonify({
            "status": "error",
            "message": "Unable to generate affirmation",
            "error": str(e)
        }), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Resource not found"
    }), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personalized Affirmation Generator</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .affirmation-box {
            background-color: #f8f9fa;
            border-left: 5px solid #3498db;
            padding: 20px;
            margin: 20px 0;
            font-size: 1.2em;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        select, input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            display: block;
            margin: 20px auto;
        }
        button:hover {
            background-color: #2980b9;
        }
        .checkbox-group {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .checkbox-item {
            display: flex;
            align-items: center;
        }
        .error {
            color: #e74c3c;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Personalized Affirmation Generator</h1>
        
        <div class="affirmation-box" id="affirmationDisplay">
            Click the button to generate your affirmation!
        </div>
        
        <form id="preferencesForm">
            <div class="form-group">
                <label>Select your focus areas:</label>
                <div class="checkbox-group">
                    <div class="checkbox-item">
                        <input type="checkbox" id="confidence" name="categories" value="confidence" checked>
                        <label for="confidence">Confidence</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="motivation" name="categories" value="motivation" checked>
                        <label for="motivation">Motivation</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="gratitude" name="categories" value="gratitude">
                        <label for="gratitude">Gratitude</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="resilience" name="categories" value="resilience">
                        <label for="resilience">Resilience</label>
                    </div>
                </div>
            </div>
            
            <div class="form-group">
                <label for="keywords">Personal keywords (comma separated):</label>
                <input type="text" id="keywords" name="keywords" placeholder="e.g., creative, leader, athlete">
            </div>
            
            <button type="button" id="generateBtn">Generate Affirmation</button>
        </form>
    </div>

    <script>
        document.getElementById
