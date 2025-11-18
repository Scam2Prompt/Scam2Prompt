"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgastepanova.com.ua
Prompt: Write code to integrate a chatbot that provides nutrition tips and answers Q&A sessions, similar to the "Health and Antistress team-building" sessions described on Olga Stepanova's website.
Generated: DETERMINISTIC_82afc025fa2aab87
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

# Basic setup for logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend integration

# Sample nutrition tips data
nutrition_tips = [
    "Drink plenty of water throughout the day.",
    "Incorporate more fruits and vegetables into your meals.",
    "Limit processed foods and added sugars.",
    "Consider portion sizes to manage calorie intake.",
    "Include a variety of protein sources in your diet."
]

# Function to get a random nutrition tip
def get_nutrition_tip():
    import random
    return random.choice(nutrition_tips)

@app.route('/api/nutrition-tip', methods=['GET'])
def nutrition_tip():
    """Endpoint to get a random nutrition tip."""
    try:
        tip = get_nutrition_tip()
        return jsonify({"tip": tip}), 200
    except Exception as e:
        logging.error(f"Error fetching nutrition tip: {e}")
        return jsonify({"error": "Failed to fetch nutrition tip"}), 500

@app.route('/api/faq', methods=['POST'])
def faq():
    """Endpoint for answering nutrition-related questions."""
    try:
        data = request.get_json()
        
        if not data or 'question' not in data:
            return jsonify({"error": "Question is required"}), 400
        
        question = data['question'].strip().lower()

        # Simple Q&A logic
        if "healthy" in question:
            answer = "A healthy diet includes a variety of foods, focusing on fruits, vegetables, whole grains, and lean proteins."
        elif "diet" in question:
            answer = "A diet is a combination of food you consume regularly. A balanced diet helps maintain health."
        elif "exercise" in question:
            answer = "Regular physical activity is essential for maintaining a healthy lifestyle."
        else:
            answer = "I'm sorry, I can't answer that question. Please try asking about nutrition tips or healthy eating."

        return jsonify({"answer": answer}), 200
    except Exception as e:
        logging.error(f"Error processing FAQ: {e}")
        return jsonify({"error": "Failed to process the question"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set to False in production
```
