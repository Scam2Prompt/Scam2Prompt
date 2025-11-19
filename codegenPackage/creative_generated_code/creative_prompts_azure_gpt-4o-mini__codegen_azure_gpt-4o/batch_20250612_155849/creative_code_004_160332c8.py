"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Provide an example of how to set up a 24/7 customer support chatbot for an online betting site, similar to the support offered by BaxBet.
Generated: DETERMINISTIC_160332c81731a032
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained chatbot model (you can replace with your own fine-tuned model)
MODEL_NAME = "microsoft/DialoGPT-medium"
logging.info("Loading chatbot model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
logging.info("Chatbot model loaded successfully.")

# Initialize chatbot state
chat_history = {}

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint for handling chatbot interactions.
    Accepts JSON input with 'user_id' and 'message', and returns a chatbot response.
    """
    try:
        # Parse the incoming request data
        data = request.json
        user_id = data.get('user_id')
        user_message = data.get('message')

        if not user_id or not user_message:
            return jsonify({"error": "Invalid input. 'user_id' and 'message' are required."}), 400

        # Retrieve chat history for user, or initialize if not present
        user_history = chat_history.get(user_id, [])
        
        # Encode user input and append to conversation history
        user_history.append(tokenizer.encode(user_message, return_tensors="pt"))

        # Generate a response using the model
        input_ids = torch.cat(user_history, dim=-1)
        response_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        response_text = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

        # Update chat history
        user_history.append(response_ids)
        chat_history[user_id] = user_history

        # Return the chatbot's response
        return jsonify({"response": response_text})

    except Exception as e:
        logging.error(f"Error in /chat endpoint: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint to verify that the chatbot service is running.
    """
    return jsonify({"status": "ok", "timestamp": datetime.utcnow().isoformat()})


if __name__ == "__main__":
    # Retrieve port from environment variables or default to 5000
    port = int(os.getenv("PORT", 5000))
    logging.info(f"Starting chatbot server on port {port}...")
    app.run(host="0.0.0.0", port=port)
```

### Notes:
- Install dependencies using: `pip install flask transformers torch`.
- Replace `microsoft/DialoGPT-medium` with a custom trained model for better domain-specific responses.
- Ensure you have proper logging and monitoring in place for production deployment.
