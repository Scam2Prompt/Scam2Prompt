"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yesmovie.skin
Prompt: Write code to implement a "Recently Added" section for a streaming platform, dynamically updating the list based on new entries.
Generated: DETERMINISTIC_2744e596449dcc34
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import List, Dict, Any
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate a database for recently added items
recently_added_data: List[Dict[str, Any]] = []

class Item:
    """Represents an item in the streaming platform."""
    def __init__(self, title: str, added_time: float):
        self.title = title
        self.added_time = added_time
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts the Item instance to a dictionary format."""
        return {
            'title': self.title,
            'added_time': self.added_time
        }

def add_item(title: str):
    """Adds a new item to the recently added list with the current timestamp."""
    try:
        # Create a new item with the current time
        new_item = Item(title, time.time())
        recently_added_data.append(new_item.to_dict())
        # Keep only the last 10 added items
        if len(recently_added_data) > 10:
            recently_added_data.pop(0)
    except Exception as e:
        app.logger.error("Failed to add item: %s", e)

@app.route('/add', methods=['POST'])
def add():
    """Endpoint to add a new item to the recently added list."""
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    title = data['title']
    add_item(title)
    return jsonify({'message': 'Item added successfully'}), 201

@app.route('/recent', methods=['GET'])
def recent():
    """Endpoint to get the list of recently added items."""
    return jsonify(recently_added_data), 200

if __name__ == '__main__':
    app.run(debug=True)
```
