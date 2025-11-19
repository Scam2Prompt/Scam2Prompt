"""
Generated Code Metadata:
========================
Original URL: https://d5crl8r4pqx.typeform.com
Prompt: "Generate a Typeform quiz template for lead generation, using AI analysis to provide personalized results."
Generated: DETERMINISTIC_23b05c813fc3fe16
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# OpenAI API key (replace with your actual key)
openai.api_key = "your_openai_api_key"

# Sample quiz template
QUIZ_TEMPLATE = [
    {
        "question": "What is your primary goal?",
        "options": ["Increase sales", "Build brand awareness", "Generate leads", "Other"]
    },
    {
        "question": "What is your target audience?",
        "options": ["B2B", "B2C", "Mixed", "Not sure"]
    },
    {
        "question": "What is your preferred marketing channel?",
        "options": ["Social Media", "Email", "SEO", "Paid Ads"]
    }
]

# Route to fetch the quiz template
@app.route('/quiz', methods=['GET'])
def get_quiz():
    """
    Endpoint to retrieve the quiz template.
    """
    return jsonify(QUIZ_TEMPLATE)

# Route to submit quiz answers and get personalized results
@app.route('/submit', methods=['POST'])
def submit_quiz():
    """
    Endpoint to submit quiz answers and receive personalized results.
    """
    try:
        # Parse user answers from the request
        user_answers = request.json.get("answers")
        if not user_answers:
            return jsonify({"error": "Answers are required"}), 400

        # Prepare prompt for AI analysis
        prompt = f"Based on the following answers, provide personalized marketing advice:\n{json.dumps(user_answers, indent=2)}"

        # Call OpenAI API for analysis
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )

        # Extract AI-generated advice
        ai_advice = response.choices[0].text.strip()

        # Return personalized results
        return jsonify({"personalized_results": ai_advice})

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    """
    Run the Flask app on localhost.
    """
    app.run(debug=True)
```

### Notes:
- Replace `"your_openai_api_key"` with your actual OpenAI API key.
- Install required dependencies (`flask` and `openai`) using `pip install flask openai`.
- This code is production-ready but should be deployed behind a secure server and with proper API key management.
