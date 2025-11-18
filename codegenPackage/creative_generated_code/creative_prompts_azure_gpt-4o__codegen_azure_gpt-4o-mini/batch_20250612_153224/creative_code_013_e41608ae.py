"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Develop a chatbot using Python that can answer questions about Ecoplast product categories, installation guides, and dealer registration based on the website's content.
Generated: DETERMINISTIC_e41608ae7a5b915c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data simulating product categories, installation guides, and dealer registration info.
ecoplast_data = {
    "product_categories": [
        "Eco-friendly Paints",
        "Biodegradable Containers",
        "Sustainable Building Materials",
        "Recycled Plastic Products"
    ],
    "installation_guides": {
        "Eco-friendly Paints": "1. Prepare the surface. 2. Apply primer. 3. Use a quality brush or roller. 4. Allow to dry before applying a second coat.",
        "Biodegradable Containers": "1. Ensure the surface is clean. 2. Fill with the desired material. 3. Store in a cool, dry place.",
        "Sustainable Building Materials": "Refer to the installation manual provided with the product.",
        "Recycled Plastic Products": "1. Check compatibility with the intended use. 2. Follow standard installation practices."
    },
    "dealer_registration": "To become a dealer, please visit our registration page at www.ecoplast.com/dealers."
}

def find_response(user_input):
    """
    Find the appropriate response based on user input.

    Args:
        user_input (str): The input question from the user.

    Returns:
        str: The response related to product categories, installation guides, or dealer registration.
    """
    # Normalize input for easier matching
    user_input = user_input.lower()

    # Search for keywords in the user input
    if re.search(r'product categories?', user_input):
        return random.choice(ecoplast_data["product_categories"])
    elif re.search(r'installation guide|how to install', user_input):
        category = re.search(r'eco-friendly paints|biodegradable containers|sustainable building materials|recycled plastic products', user_input)
        if category:
            return ecoplast_data["installation_guides"].get(category.group(0).title(), "Installation guide not found.")
        else:
            return "Please specify the product category for the installation guide."
    elif re.search(r'dealer registration|become a dealer', user_input):
        return ecoplast_data["dealer_registration"]
    else:
        return "I'm sorry, I don't have information on that topic."

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle incoming chat messages.

    Returns:
        JSON response containing the chatbot's reply.
    """
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({"error": "No message provided."}), 400
        
        response = find_response(user_input)
        return jsonify({"response": response}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
