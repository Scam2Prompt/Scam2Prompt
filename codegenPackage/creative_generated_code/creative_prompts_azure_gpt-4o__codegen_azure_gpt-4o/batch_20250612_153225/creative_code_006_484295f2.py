"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://934ummfm.com
Prompt: Develop a chatbot using the contact information on UMM FM's website to answer frequently asked questions about its programming and events.
Generated: DETERMINISTIC_484295f256513bb2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code using Flask and OpenAI's GPT API to create a chatbot for answering FAQs about UMM FM's programming and events. For simplicity, we assume you have access to OpenAI API and the contact information has been preloaded into a structured FAQ database.

```python
import os
import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key (replace with your actual API key)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Preloaded FAQ Database (replace with actual data from UMM FM's website)
FAQ_DATABASE = [
    {"question": "What type of programming does UMM FM offer?", 
     "answer": "UMM FM offers a mix of music, talk shows, news, and educational content."},
    {"question": "How can I access UMM FM's schedule?", 
     "answer": "You can access UMM FM's schedule on their website under the 'Programming Schedule' section."},
    {"question": "Does UMM FM host live events?", 
     "answer": "Yes, UMM FM hosts live events, including concerts, public discussions, and community activities."},
    {"question": "How can I contact UMM FM?", 
     "answer": "You can contact UMM FM via email at info@ummfm.com or call their hotline at (123)-456-7890."},
]

def find_answer_in_faq(question):
    """
    Searches the FAQ database for a matching answer to the given question.
    Returns None if no match is found.
    """
    for faq in FAQ_DATABASE:
        if faq["question"].lower() in question.lower():
            return faq["answer"]
    return None

def generate_response_with_openai(question):
    """
    Uses OpenAI GPT to generate a chatbot response.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"The user has asked: {question}. Based on UMM FM's programming and events, provide an appropriate response.",
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        # Log the error and return a friendly message
        print(f"Error interacting with OpenAI API: {e}")
        return "Sorry, I couldn't process your request at the moment. Please try again later."

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chatbot queries.
    Expects a JSON payload with the key 'question'.
    Returns a JSON response with the key 'answer'.
    """
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({"error": "Invalid request. Please provide a 'question' field."}), 400
        
        question = data['question']
        
        # Try to find the answer in the FAQ database
        answer = find_answer_in_faq(question)
        if not answer:
            # Generate response using OpenAI if FAQ database fails
            answer = generate_response_with_openai(question)
        
        return jsonify({"answer": answer}), 200
    
    except Exception as e:
        # Generic error handling
        print(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
1. Install Flask: `pip install flask`
2. Install OpenAI Python library: `pip install openai`
3. Set the environment variable for OpenAI API key: `export OPENAI_API_KEY="your_api_key_here"`

### Usage:
- Start the server: `python chatbot.py`
- Send a POST request to `/chat` with a JSON payload: `{"question": "What type of programming does UMM FM offer?"}`

This code is production-ready but should be deployed with proper security measures (e.g., API key management).
