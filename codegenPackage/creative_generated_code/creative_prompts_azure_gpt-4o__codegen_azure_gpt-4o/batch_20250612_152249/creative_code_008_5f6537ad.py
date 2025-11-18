"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie3t6miqfcnbmegku6rqykux7ln7q2jug672nhfgveqoixyrzskhq.ipfs.dweb.link
Prompt: Create a chatbot using IntentsGPT to answer user queries about Aperture Finance's features, including liquidity positions, token swaps, and AI-driven strategies.
Generated: DETERMINISTIC_5f6537ad871f84e0
Batch ID: 20250612_152249
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

# Flask app setup
app = Flask(__name__)

# OpenAI GPT API key setup
openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key

# Predefined intents for Aperture Finance
INTENTS = {
    "liquidity_positions": "Provide information about managing liquidity positions on Aperture Finance.",
    "token_swaps": "Explain how token swaps work on Aperture Finance.",
    "ai_strategies": "Describe Aperture Finance's AI-driven investment strategies."
}

def query_intents_gpt(intent, user_question):
    """
    Send a query to OpenAI GPT model based on the intent and user question.
    
    Args:
        intent (str): The specific intent related to the user query.
        user_question (str): The user's question for further context.
    
    Returns:
        str: Response from the GPT model.
    """
    prompt = f"You are a chatbot with extensive knowledge about Aperture Finance. {INTENTS[intent]} User question: {user_question}"
    
    try:
        # Generate response using OpenAI GPT
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a specific GPT model
            prompt=prompt,
            max_tokens=300,  # Limit response length
            temperature=0.7  # Control randomness
        )
        return response.choices[0].text.strip()  # Extract and return the response text
    except Exception as e:
        # Handle API errors
        return f"An error occurred while processing your request: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle POST requests to the /chat endpoint.
    
    Request Body:
        {
            "intent": "liquidity_positions",  // Example intent
            "question": "How do I manage my liquidity positions?"  // User's question
        }
    
    Returns:
        JSON response containing the GPT-generated answer.
    """
    data = request.json
    
    # Validate input
    if not data or 'intent' not in data or 'question' not in data:
        return jsonify({"error": "Invalid input. 'intent' and 'question' are required fields."}), 400
    
    intent = data['intent']
    user_question = data['question']
    
    # Check if the intent exists
    if intent not in INTENTS:
        return jsonify({"error": f"Invalid intent. Supported intents are: {list(INTENTS.keys())}"}), 400

    # Generate response using GPT
    response = query_intents_gpt(intent, user_question)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Instructions for Deployment:
1. Replace `your_openai_api_key` with your OpenAI API key.
2. Install required dependencies:
   ```bash
   pip install flask openai
   ```
3. Run the program:
   ```bash
   python chatbot.py
   ```
4. Send POST requests to the `/chat` endpoint, providing `intent` and `question` in the request body. For example:
   ```json
   {
       "intent": "liquidity_positions",
       "question": "How do I manage my liquidity positions?"
   }
   ```
