"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushiswap.andy.cx
Prompt: Create an API that retrieves and displays childhood memories based on user input, reflecting the personal storytelling style seen on Andy.cx.
Generated: DETERMINISTIC_098082a9197938df
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Sample in-memory database of childhood memories for demonstration
memory_db = [
    {
        "id": 1,
        "title": "Summer Days by the Lake",
        "story": "I remember the warm summer days spent fishing by the lake with grandpa...",
        "tags": ["summer", "lake", "family"],
        "submitted_at": datetime(2023, 1, 15).isoformat()
    },
    {
        "id": 2,
        "title": "First Bicycle Ride",
        "story": "The day I finally learned how to ride my bike was unforgettable...",
        "tags": ["bicycle", "achievement"],
        "submitted_at": datetime(2023, 2, 10).isoformat()
    }
]

# Error messages
ERROR_INVALID_ID = "Invalid memory ID."
ERROR_EMPTY_QUERY = "Query parameter cannot be empty."

@app.route('/api/memories', methods=['GET'])
def get_memories():
    """
    Retrieve childhood memories based on query parameters.

    Query Parameters:
        - id: Retrieve a specific memory by ID.
        - tag: Filter memories by a specific tag.

    Returns:
        JSON response containing the filtered memories or error messages.
    """
    try:
        # Extract query parameters
        memory_id = request.args.get('id')
        tag_filter = request.args.get('tag')

        # Retrieve specific memory by ID
        if memory_id:
            if not memory_id.isdigit():
                return jsonify({"error": ERROR_INVALID_ID}), 400
            memory_id = int(memory_id)
            memory = next((m for m in memory_db if m["id"] == memory_id), None)
            if memory:
                return jsonify(memory), 200
            return jsonify({"error": ERROR_INVALID_ID}), 404

        # Filter memories by tag
        if tag_filter:
            if not tag_filter.strip():
                return jsonify({"error": ERROR_EMPTY_QUERY}), 400
            filtered_memories = [m for m in memory_db if tag_filter.lower() in map(str.lower, m["tags"])]
            return jsonify(filtered_memories), 200

        # Return all memories if no filters are provided
        return jsonify(memory_db), 200

    except Exception as e:
        # Catch unexpected server errors
        return jsonify({"error": str(e)}), 500


# Run the app
if __name__ == '__main__':
    # Use debug mode for development; disable in production
    app.run(debug=True)
```
