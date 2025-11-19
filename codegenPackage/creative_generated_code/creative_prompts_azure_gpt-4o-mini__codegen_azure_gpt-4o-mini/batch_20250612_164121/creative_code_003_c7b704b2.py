"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1o2.ir
Prompt: Develop an API endpoint that returns random questions categorized by topics such as weird/funny and personality, similar to the features on dex.chat.
Generated: DETERMINISTIC_c7b704b22efdbfb4
Batch ID: 20250612_164121
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

# Sample data for questions categorized by topics
questions = {
    'weird_funny': [
        "If animals could talk, which species would be the rudest?",
        "What would be the absolute worst name you could give your child?",
        "If you were a fruit, what fruit would you be and why?",
    ],
    'personality': [
        "If you could only have one superpower, what would it be?",
        "What’s your biggest fear and why?",
        "Which historical figure would you want to have dinner with?",
    ],
}

@app.route('/api/questions', methods=['GET'])
def get_random_question():
    """
    API endpoint to get a random question based on the specified category.
    Query parameters:
        - category: The category of questions to retrieve (weird_funny, personality)
    Returns:
        A JSON response containing a random question from the specified category.
    """
    category = request.args.get('category')
    
    # Validate the category
    if category not in questions:
        return jsonify({'error': 'Invalid category. Available categories: weird_funny, personality.'}), 400

    try:
        # Select a random question from the specified category
        question = random.choice(questions[category])
        return jsonify({'question': question}), 200
    
    except Exception as e:
        # Log the exception (in a real application, use logging library)
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Running the app in debug mode for development (set to False in production)
    app.run(debug=True)
```
