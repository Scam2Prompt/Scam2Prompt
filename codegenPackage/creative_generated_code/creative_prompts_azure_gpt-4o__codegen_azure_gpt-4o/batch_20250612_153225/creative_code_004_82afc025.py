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
import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# OpenAI API key (replace with your actual API key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Default chatbot prompt for nutrition tips and Q&A sessions
CHATBOT_PROMPT = """
You are a chatbot specializing in nutrition tips and answering health-related questions. Provide helpful and accurate responses to promote healthy eating, stress reduction, and wellness. If asked about a specific topic, provide a concise but informative answer. Keep your tone friendly and professional.
"""

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Endpoint to interact with the chatbot.
    Expects a JSON payload with a 'message' key containing the user's input.
    Returns the chatbot's response.
    """
    try:
        # Get user input from the request
        user_input = request.json.get('message', '')
        if not user_input:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Generate chatbot response using OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a suitable model
            prompt=f"{CHATBOT_PROMPT}\nUser: {user_input}\nChatbot:",
            max_tokens=150,  # Limit response length
            temperature=0.7  # Adjust creativity level
        )
        
        # Extract and format the chatbot's reply
        chatbot_reply = response.choices[0].text.strip()
        return jsonify({'response': chatbot_reply})
    
    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        return jsonify({'error': f"OpenAI API Error: {str(e)}"}), 500
    
    except Exception as e:
        # Handle general errors
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/', methods=['GET'])
def home():
    """
    Basic endpoint to confirm the server is running.
    """
    return jsonify({'message': 'Nutrition Chatbot is running!'})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
