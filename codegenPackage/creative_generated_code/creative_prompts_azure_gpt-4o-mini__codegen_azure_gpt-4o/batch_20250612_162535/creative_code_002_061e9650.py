"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selffeeling.com
Prompt: Create a REST API endpoint that provides guided meditation prompts for self-awareness, based on the Self-Feeling Program's activities.
Generated: DETERMINISTIC_061e96504f7bc2f4
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Sample guided meditation prompts based on the Self-Feeling Program's activities
MEDITATION_PROMPTS = [
    {"id": 1, "prompt": "Close your eyes and take three deep breaths. Reflect on one positive thing that happened today."},
    {"id": 2, "prompt": "Focus on the sensation of your breath. What emotions arise as you stay present in this moment?"},
    {"id": 3, "prompt": "Visualize yourself in a peaceful place. What does this place reveal about your inner desires?"},
    {"id": 4, "prompt": "Observe your thoughts without judgment. What patterns do you notice about your self-talk?"},
    {"id": 5, "prompt": "Think of a recent challenge you faced. How did you grow from that experience?"},
]

@app.route('/api/meditation_prompt', methods=['GET'])
def get_meditation_prompt():
    """
    REST API endpoint to provide a random guided meditation prompt.
    
    Returns:
        JSON: A randomly selected guided meditation prompt.
    """
    try:
        # Randomly select a meditation prompt from the list
        selected_prompt = random.choice(MEDITATION_PROMPTS)
        return jsonify({
            "success": True,
            "data": selected_prompt
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "success": False,
            "error": "An error occurred while retrieving the meditation prompt.",
            "details": str(e)
        }), 500

@app.route('/api/meditation_prompt/<int:prompt_id>', methods=['GET'])
def get_specific_meditation_prompt(prompt_id):
    """
    REST API endpoint to retrieve a specific guided meditation prompt by its ID.
    
    Args:
        prompt_id (int): The ID of the meditation prompt to retrieve.
    
    Returns:
        JSON: The meditation prompt associated with the given ID, or an error message if not found.
    """
    try:
        # Filter the prompts to find the one matching the given ID
        prompt = next((p for p in MEDITATION_PROMPTS if p["id"] == prompt_id), None)
        
        if prompt:
            return jsonify({
                "success": True,
                "data": prompt
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Meditation prompt not found."
            }), 404
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "success": False,
            "error": "An error occurred while retrieving the meditation prompt.",
            "details": str(e)
        }), 500

@app.errorhandler(404)
def handle_404_error(e):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({
        "success": False,
        "error": "The requested resource was not found."
    }), 404

@app.errorhandler(500)
def handle_500_error(e):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({
        "success": False,
        "error": "An internal server error occurred."
    }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
