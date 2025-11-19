"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itmastar.pages.dev
Prompt: Create an API integration example for an IT agency that highlights real success stories.
Generated: DETERMINISTIC_baacdf448f85d975
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data: In a real application, this would come from a database
success_stories = [
    {
        'id': 1,
        'title': 'Project A',
        'description': 'Increased performance by 30% for client X.',
        'client': 'Client X',
        'date': '2023-01-15'
    },
    {
        'id': 2,
        'title': 'Project B',
        'description': 'Successfully migrated infrastructure for client Y.',
        'client': 'Client Y',
        'date': '2023-02-10'
    }
]

@app.route('/api/success_stories', methods=['GET'])
def get_success_stories():
    """
    Retrieve the list of success stories.

    Returns:
        JSON response containing a list of success stories
    """
    return jsonify(success_stories), 200

@app.route('/api/success_stories/<int:story_id>', methods=['GET'])
def get_success_story(story_id):
    """
    Retrieve a single success story by ID.

    Args:
        story_id (int): The ID of the success story to retrieve.

    Returns:
        JSON response containing the success story or an error message
    """
    story = next((s for s in success_stories if s['id'] == story_id), None)
    if story:
        return jsonify(story), 200
    else:
        return jsonify({'error': 'Success story not found'}), 404

@app.route('/api/success_stories', methods=['POST'])
def create_success_story():
    """
    Create a new success story.

    Returns:
        JSON response containing the created success story or an error message
    """
    try:
        data = request.json
        if not all(key in data for key in ('title', 'description', 'client', 'date')):
            return jsonify({'error': 'Missing required fields'}), 400

        new_story = {
            'id': len(success_stories) + 1,
            'title': data['title'],
            'description': data['description'],
            'client': data['client'],
            'date': data['date']
        }
        success_stories.append(new_story)
        return jsonify(new_story), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
