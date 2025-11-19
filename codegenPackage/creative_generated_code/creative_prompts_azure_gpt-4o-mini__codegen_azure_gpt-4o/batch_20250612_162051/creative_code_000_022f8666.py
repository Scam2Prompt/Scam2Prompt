"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Generate a code snippet for a web application that allows users to submit their interior design ideas and receive feedback based on Nyiku Design's innovative design principles.
Generated: DETERMINISTIC_022f8666c113c378
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Mock feedback generation function based on "Nyiku Design's innovative design principles"
def generate_feedback(user_design):
    """
    Generate feedback based on Nyiku Design principles.

    Args:
        user_design (str): User's interior design idea.

    Returns:
        str: Feedback text.
    """
    # Example principles (placeholder for actual Nyiku Design rules)
    principles = [
        "Balance and harmony are key.",
        "Focus on natural lighting wherever possible.",
        "Use sustainable and eco-friendly materials.",
        "Combine functionality with aesthetic appeal.",
    ]
    
    # Basic feedback based on length of submission
    if len(user_design) < 20:
        return "Your idea is too short. Please elaborate more on your design concept."
    elif len(user_design) > 500:
        return "Your idea is quite detailed! Consider breaking it into smaller actionable steps."
    else:
        # Provide one principle as part of feedback randomly
        import random
        principle = random.choice(principles)
        return f"Your design aligns with Nyiku Design principles. Here's a tip: {principle}"

@app.route('/submit_design', methods=['POST'])
def submit_design():
    """
    Endpoint for submitting interior design ideas and receiving feedback.

    Returns:
        JSON response with feedback or error message.
    """
    try:
        # Parse user input
        data = request.json
        if not data or 'design_idea' not in data:
            return jsonify({"error": "Invalid input. Please provide a design idea in the 'design_idea' field."}), 400
        
        user_design = data['design_idea']
        
        # Validate input (example: basic profanity filter)
        if re.search(r'\b(badword1|badword2|badword3)\b', user_design, re.IGNORECASE):
            return jsonify({"error": "Your submission contains inappropriate language."}), 400
        
        # Generate feedback
        feedback = generate_feedback(user_design)
        
        return jsonify({"message": "Design idea submitted successfully.", "feedback": feedback}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """
    Handle 405 errors.
    """
    return jsonify({"error": "Method not allowed for this endpoint."}), 405

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
