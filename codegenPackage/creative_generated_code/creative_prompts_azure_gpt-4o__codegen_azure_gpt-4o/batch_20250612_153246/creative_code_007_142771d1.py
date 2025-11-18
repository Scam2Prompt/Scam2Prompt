"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futureforai.com
Prompt: Develop a chatbot using OpenAI’s ChatGPT Pro Max API and include premium subscription features like those described on Future For AI.
Generated: DETERMINISTIC_142771d1b749c650
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key (make sure to keep this secure)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Fetch API key from environment variables

# Subscription tiers
SUBSCRIPTION_TIERS = {
    "free": {
        "max_messages_per_day": 50,
        "model": "gpt-3.5-turbo",
    },
    "premium": {
        "max_messages_per_day": 500,
        "model": "gpt-4",
    },
    "pro_max": {
        "max_messages_per_day": 1000,
        "model": "gpt-4",
        "priority_support": True,
    }
}

# In-memory storage for user data (replace with proper database in production)
USER_DATA = {
    "user_1": {"tier": "free", "messages_today": 0},
    "user_2": {"tier": "premium", "messages_today": 0},
    # Example user; add more as needed
}

# Helper function to validate subscription limits
def validate_subscription(user_id):
    user_info = USER_DATA.get(user_id)
    if not user_info:
        return False, "User not found."
    
    tier = user_info.get("tier")
    subscription = SUBSCRIPTION_TIERS.get(tier)
    
    if not subscription:
        return False, "Invalid subscription tier."
    
    if user_info["messages_today"] >= subscription["max_messages_per_day"]:
        return False, "Message limit reached for your subscription tier."
    
    return True, "Validation passed."

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint for chatbot interaction.
    Expected request JSON: {"user_id": "user_1", "message": "Hello, bot!"}
    """
    try:
        # Parse incoming request
        data = request.get_json()
        user_id = data.get("user_id")
        user_message = data.get("message")
        
        if not user_id or not user_message:
            return jsonify({"error": "Missing required user_id or message."}), 400
        
        # Validate subscription
        is_valid, validation_message = validate_subscription(user_id)
        if not is_valid:
            return jsonify({"error": validation_message}), 403
        
        # Retrieve user tier and associated model
        user_info = USER_DATA[user_id]
        tier = user_info["tier"]
        model = SUBSCRIPTION_TIERS[tier]["model"]
        
        # Call OpenAI ChatGPT API
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_message}
            ]
        )
        
        # Extract response text
        bot_reply = response.choices[0].message["content"]
        
        # Update message count for the user
        user_info["messages_today"] += 1
        
        # Send back chatbot response
        return jsonify({"reply": bot_reply})
    
    except openai.error.OpenAIError as e:
        # Handle API errors
        return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500
    
    except Exception as e:
        # Handle general errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/reset_messages", methods=["POST"])
def reset_messages():
    """
    Admin endpoint to reset daily message counts for all users.
    (This would typically run as a scheduled job instead of being exposed via API.)
    """
    try:
        for user in USER_DATA.values():
            user["messages_today"] = 0
        
        return jsonify({"status": "Message counts reset successfully."})
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    # Run the Flask app on port 5000
    app.run(host="0.0.0.0", port=5000)
```
