"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Develop a script to organize and display school achievements, such as sports medals and academic awards, similar to the "News & Events" section on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_8cb37810a3223bc2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to organize and display school achievements such as sports medals and academic awards.
This application uses Python's Flask framework to serve achievements dynamically on a webpage.
"""

from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# Path to achievements data (can be a database in production)
ACHIEVEMENTS_FILE = 'achievements.json'


def load_achievements():
    """
    Load achievements from a JSON file. The file contains a list of achievements.
    """
    if not os.path.exists(ACHIEVEMENTS_FILE):
        # Create an empty file if it does not exist
        with open(ACHIEVEMENTS_FILE, 'w') as f:
            json.dump([], f)

    try:
        with open(ACHIEVEMENTS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Handle corrupt JSON file
        return []


def save_achievements(achievements):
    """
    Save achievements to a JSON file.
    """
    with open(ACHIEVEMENTS_FILE, 'w') as f:
        json.dump(achievements, f, indent=4)


@app.route('/')
def home():
    """
    Home page to display achievements.
    """
    achievements = load_achievements()
    return render_template('index.html', achievements=achievements)


@app.route('/add-achievement', methods=['POST'])
def add_achievement():
    """
    API endpoint to add a new achievement.
    """
    achievements = load_achievements()
    try:
        data = request.get_json()

        # Validate input data
        title = data.get('title')
        description = data.get('description')
        category = data.get('category')
        date = data.get('date')

        if not title or not description or not category or not date:
            return jsonify({'error': 'All fields are required (title, description, category, date).'}), 400

        # Add new achievement
        achievements.append({
            'title': title,
            'description': description,
            'category': category,
            'date': date
        })

        save_achievements(achievements)
        return jsonify({'message': 'Achievement added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/achievements', methods=['GET'])
def get_achievements():
    """
    API endpoint to fetch all achievements.
    """
    achievements = load_achievements()
    return jsonify(achievements), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)

"""
Templates Folder: Create a folder named 'templates' in the same directory.
Inside it, create an 'index.html' file with the following content:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>School Achievements</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .achievement-container { margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
        h1 { text-align: center; color: #333; }
    </style>
</head>
<body>
    <h1>School Achievements</h1>
    {% if achievements %}
        {% for achievement in achievements %}
            <div class="achievement-container">
                <h2>{{ achievement['title'] }}</h2>
                <p><strong>Category:</strong> {{ achievement['category'] }}</p>
                <p><strong>Date:</strong> {{ achievement['date'] }}</p>
                <p>{{ achievement['description'] }}</p>
            </div>
        {% endfor %}
    {% else %}
        <p>No achievements to display.</p>
    {% endif %}
</body>
</html>
"""

```
