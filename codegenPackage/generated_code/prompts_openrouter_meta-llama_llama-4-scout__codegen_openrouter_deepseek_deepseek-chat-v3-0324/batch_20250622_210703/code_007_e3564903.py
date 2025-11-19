"""
Generated Code Metadata:
========================
Original URL: https://futureforai.com
Prompt: Design a conversational search engine like Perplexity, using AI and NLP techniques mentioned in the webpage content.
Generated: DETERMINISTIC_e356490369ba8182
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import logging
from typing import Dict, List, Optional

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Conversation history storage
conversation_history: Dict[str, List[Dict[str, str]]] = {}

def initialize_conversation(session_id: str) -> None:
    """Initialize a new conversation history for a session."""
    conversation_history[session_id] = [
        {"role": "system", "content": "You are a helpful assistant that provides accurate and concise answers to user queries."}
    ]

def get_conversation_history(session_id: str) -> List[Dict[str, str]]:
    """Retrieve conversation history for a session."""
    if session_id not in conversation_history:
        initialize_conversation(session_id)
    return conversation_history[session_id]

def add_to_conversation(session_id: str, role: str, content: str) -> None:
    """Add a message to the conversation history."""
    if session_id not in conversation_history:
        initialize_conversation(session_id)
    conversation_history[session_id].append({"role": role, "content": content})

def generate_response(session_id: str, user_input: str) -> str:
    """
    Generate a response using OpenAI's chat completion API.
    
    Args:
        session_id: Unique identifier for the conversation
        user_input: User's query
    
    Returns:
        Generated response from the AI
    """
    try:
        # Add user message to conversation history
        add_to_conversation(session_id, "user", user_input)
        
        # Get conversation history
        messages = get_conversation_history(session_id)
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        
        # Extract and store the assistant's response
        assistant_response = response.choices[0].message['content']
        add_to_conversation(session_id, "assistant", assistant_response)
        
        return assistant_response
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        return "Sorry, I encountered an error while processing your request."

@app.route('/api/search', methods=['POST'])
def handle_search():
    """
    Handle search requests from the client.
    
    Expects JSON payload with:
    - session_id: Unique identifier for the conversation
    - query: User's search query
    
    Returns JSON response with:
    - response: Generated answer
    - status: Success/error status
    """
    try:
        data = request.get_json()
        if not data or 'query' not in data or 'session_id' not in data:
            return jsonify({"error": "Invalid request format", "status": "error"}), 400
        
        session_id = data['session_id']
        query = data['query']
        
        if not query.strip():
            return jsonify({"error": "Query cannot be empty", "status": "error"}), 400
        
        response = generate_response(session_id, query)
        
        return jsonify({
            "response": response,
            "status": "success"
        })
    except Exception as e:
        logger.error(f"Error handling search request: {str(e)}")
        return jsonify({"error": "Internal server error", "status": "error"}), 500

@app.route('/api/new_session', methods=['POST'])
def new_session():
    """
    Create a new conversation session.
    
    Returns JSON response with:
    - session_id: New session identifier
    - status: Success/error status
    """
    try:
        session_id = os.urandom(16).hex()
        initialize_conversation(session_id)
        
        return jsonify({
            "session_id": session_id,
            "status": "success"
        })
    except Exception as e:
        logger.error(f"Error creating new session: {str(e)}")
        return jsonify({"error": "Internal server error", "status": "error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
