"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurs.io
Prompt: Write code for an AI agent that can handle user queries and dynamically update website content, as described on Blurs.io.
Generated: DETERMINISTIC_7353bf11ef9bcae0
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for the app

# Mock database to store website content
DATABASE = {
    "content": {
        "title": "Welcome to Blurs.io",
        "description": "Your go-to platform for dynamic content."
    }
}

def update_content(new_content):
    """Update the website content in the mock database."""
    try:
        # Validate new content structure
        if not isinstance(new_content, dict):
            raise ValueError("New content must be a dictionary.")
        
        # Update content in the database
        DATABASE['content'].update(new_content)
        return True
    except Exception as e:
        print(f"Error updating content: {e}")
        return False

@app.route('/api/content', methods=['GET'])
def get_content():
    """Retrieve the current website content."""
    return jsonify(DATABASE['content']), 200

@app.route('/api/content', methods=['POST'])
def post_content():
    """Update the website content with the provided JSON data."""
    try:
        new_content = request.json
        if not new_content:
            return jsonify({"error": "No content provided."}), 400
        
        # Attempt to update content
        if update_content(new_content):
            return jsonify({"message": "Content updated successfully."}), 200
        else:
            return jsonify({"error": "Failed to update content."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app
```
