"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teameleven-x1.xyz
Prompt: Generate Python code to track user orders and display live chat support functionality, as described in the Ayuwin APK system.
Generated: DETERMINISTIC_15882336044e3d69
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to emulate order tracking
orders = {
    1: {"user_id": 1001, "status": "Processing", "date": datetime.datetime.now()},
    2: {"user_id": 1002, "status": "Shipped", "date": datetime.datetime.now()},
}

# Sample data for chat support
live_chat_messages = []


@app.route('/track_order/<int:order_id>', methods=['GET'])
def track_order(order_id):
    """
    Endpoint to track a user's order by order ID.
    """
    try:
        if order_id in orders:
            return jsonify({"success": True, "order_details": orders[order_id]}), 200
        else:
            return jsonify({"success": False, "message": "Order not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"}), 500


@app.route('/live_chat', methods=['POST'])
def live_chat():
    """
    Endpoint for live chat functionality. 
    Accepts user messages and stores them in a list.
    """
    try:
        user_message = request.json.get('message')
        user_id = request.json.get('user_id')

        if not user_message or not user_id:
            return jsonify({"success": False, "message": "Invalid input"}), 400

        # Append message to chat history
        chat_entry = {
            "user_id": user_id,
            "message": user_message,
            "timestamp": datetime.datetime.now()
        }
        live_chat_messages.append(chat_entry)

        # Simulate a response from support agent
        support_response = {
            "user_id": "support",
            "message": "Thank you for reaching out. How can I assist you?",
            "timestamp": datetime.datetime.now()
        }
        live_chat_messages.append(support_response)

        return jsonify({"success": True, "chat": live_chat_messages[-2:]}), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"}), 500


@app.route('/get_chat_history', methods=['GET'])
def get_chat_history():
    """
    Endpoint to get the full chat history.
    """
    try:
        return jsonify({"success": True, "chat_history": live_chat_messages}), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
