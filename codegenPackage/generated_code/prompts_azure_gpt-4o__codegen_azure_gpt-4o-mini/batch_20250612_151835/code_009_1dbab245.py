"""
Generated Code Metadata:
========================
Original URL: https://anshsofttech.com
Prompt: Generate a Python script for automating the creation of a knowledge base system for website support, as highlighted in Ansh Soft Tech's quick support features.
Generated: DETERMINISTIC_1dbab245012dda51
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Flask application
app = Flask(__name__)

# Path to the knowledge base file
KB_FILE = 'knowledge_base.json'

# Load the knowledge base from a JSON file
def load_knowledge_base():
    """Load the knowledge base from a JSON file."""
    if os.path.exists(KB_FILE):
        with open(KB_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save the knowledge base to a JSON file
def save_knowledge_base(kb):
    """Save the knowledge base to a JSON file."""
    with open(KB_FILE, 'w') as file:
        json.dump(kb, file, indent=4)

# Initialize the knowledge base
knowledge_base = load_knowledge_base()

@app.route('/add_article', methods=['POST'])
def add_article():
    """Add a new article to the knowledge base."""
    try:
        data = request.json
        title = data.get('title')
        content = data.get('content')

        if not title or not content:
            return jsonify({'error': 'Title and content are required.'}), 400

        # Add the new article to the knowledge base
        knowledge_base[title] = content
        save_knowledge_base(knowledge_base)

        return jsonify({'message': 'Article added successfully.'}), 201
    except Exception as e:
        logging.error(f"Error adding article: {e}")
        return jsonify({'error': 'An error occurred while adding the article.'}), 500

@app.route('/get_article/<title>', methods=['GET'])
def get_article(title):
    """Retrieve an article from the knowledge base by title."""
    try:
        article = knowledge_base.get(title)
        if article:
            return jsonify({'title': title, 'content': article}), 200
        else:
            return jsonify({'error': 'Article not found.'}), 404
    except Exception as e:
        logging.error(f"Error retrieving article: {e}")
        return jsonify({'error': 'An error occurred while retrieving the article.'}), 500

@app.route('/list_articles', methods=['GET'])
def list_articles():
    """List all articles in the knowledge base."""
    try:
        articles = list(knowledge_base.keys())
        return jsonify({'articles': articles}), 200
    except Exception as e:
        logging.error(f"Error listing articles: {e}")
        return jsonify({'error': 'An error occurred while listing articles.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
