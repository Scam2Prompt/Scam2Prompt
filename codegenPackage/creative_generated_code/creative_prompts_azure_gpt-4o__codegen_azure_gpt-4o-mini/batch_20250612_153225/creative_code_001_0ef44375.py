"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Recommend an API or library to design custom uniform patterns for schools and workplaces, similar to the services offered by Real Garment Konveksi Seragam.
Generated: DETERMINISTIC_0ef44375a719521b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import uuid

# Initialize Flask application
app = Flask(__name__)

# In-memory storage for patterns
patterns = {}


@app.route('/api/patterns', methods=['POST'])
def create_pattern():
    """
    Create a new uniform pattern.
    
    Request body should contain:
    - name: str
    - description: str
    - design: dict (custom design specifications)
    
    Returns:
    - JSON response with the created pattern's ID and details.
    """
    try:
        data = request.json
        
        # Validate input data
        if not isinstance(data, dict):
            raise BadRequest("Invalid input format. Expecting JSON object.")
        
        name = data.get('name')
        description = data.get('description')
        design = data.get('design')

        if not name or not description or not design:
            raise BadRequest("Missing required fields: name, description, design")
        
        # Generate a unique ID for the pattern
        pattern_id = str(uuid.uuid4())
        
        # Create the pattern object
        pattern = {
            'id': pattern_id,
            'name': name,
            'description': description,
            'design': design
        }
        
        # Store the pattern in memory
        patterns[pattern_id] = pattern
        
        return jsonify(pattern), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route('/api/patterns/<pattern_id>', methods=['GET'])
def get_pattern(pattern_id):
    """
    Retrieve a specific uniform pattern by its ID.
    
    Parameters:
    - pattern_id: str (the unique ID of the pattern)
    
    Returns:
    - JSON response with the pattern details or a 404 error if not found.
    """
    pattern = patterns.get(pattern_id)
    if not pattern:
        return jsonify({"error": "Pattern not found."}), 404
    return jsonify(pattern), 200


@app.route('/api/patterns', methods=['GET'])
def list_patterns():
    """
    List all available uniform patterns.
    
    Returns:
    - JSON response with a list of all patterns.
    """
    return jsonify(list(patterns.values())), 200


if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
