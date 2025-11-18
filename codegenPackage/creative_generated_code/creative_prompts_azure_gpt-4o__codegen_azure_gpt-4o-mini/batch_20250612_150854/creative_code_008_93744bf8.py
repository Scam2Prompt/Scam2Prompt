"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.se
Prompt: Write code for a chatbot that answers FAQs about investment education and connects users to mentors, inspired by Trade GPT's features.
Generated: DETERMINISTIC_93744bf8ccbf2c0f
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample FAQs and responses
FAQs = {
    "What is an investment?": "An investment is an asset or item acquired with the goal of generating income or appreciation.",
    "What is diversification?": "Diversification is the practice of spreading investments across various financial instruments to reduce risk.",
    "What are stocks?": "Stocks are securities that represent a claim on a company's assets and earnings.",
    "What is a mutual fund?": "A mutual fund is an investment vehicle made up of a pool of money collected from many investors to purchase securities."
}

# Sample list of mentors
mentors = [
    {"name": "Alice Johnson", "expertise": "Stocks", "contact": "alice@example.com"},
    {"name": "Bob Smith", "expertise": "Bonds", "contact": "bob@example.com"},
    {"name": "Charlie Brown", "expertise": "Real Estate", "contact": "charlie@example.com"}
]

@app.route('/ask', methods=['POST'])
def ask_faq():
    """
    Endpoint to handle FAQ queries from users.
    Expects JSON payload with a 'question' field.
    """
    try:
        data = request.get_json()
        question = data.get('question', '').strip()

        if not question:
            return jsonify({"error": "No question provided."}), 400
        
        # Find a response or return a fallback message
        response = FAQs.get(question, "I'm sorry, I don't have the answer to that question. Please contact a mentor for more help.")
        return jsonify({"question": question, "response": response}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/connect', methods=['GET'])
def connect_mentor():
    """
    Endpoint to connect users with a mentor.
    Returns a random mentor from the list.
    """
    try:
        mentor = random.choice(mentors)
        return jsonify({"mentor": mentor}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Failed to start the server: {e}")
```

### Setup Instructions
- Ensure you have Flask installed: `pip install Flask`
- Save the code in a file named `chatbot.py`.
- Run the application with `python chatbot.py`.
- Use tools like Postman or Curl to test the endpoints:
  - `POST /ask` with JSON body `{"question": "What is an investment?"}`
  - `GET /connect` to retrieve a mentor.
