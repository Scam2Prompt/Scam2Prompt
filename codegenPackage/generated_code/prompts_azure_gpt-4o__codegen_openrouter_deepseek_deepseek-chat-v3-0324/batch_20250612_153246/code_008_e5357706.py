"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Develop a chatbot using Python and Flask that can answer customer queries about Apple products and services, referencing the chat functionality highlighted on the Apple Market Bali webpage.
Generated: DETERMINISTIC_e535770664e58c15
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Sample product knowledge base (would typically be a database in production)
PRODUCT_KNOWLEDGE = {
    "iphone": {
        "description": "iPhone is Apple's flagship smartphone with cutting-edge technology.",
        "models": ["iPhone 15", "iPhone 15 Pro", "iPhone 14", "iPhone SE"],
        "services": ["AppleCare+", "Trade-in", "iOS updates"]
    },
    "mac": {
        "description": "Mac computers offer powerful performance with macOS.",
        "models": ["MacBook Air", "MacBook Pro", "iMac", "Mac mini", "Mac Studio"],
        "services": ["AppleCare+", "Trade-in", "macOS updates"]
    },
    "ipad": {
        "description": "iPad is Apple's versatile tablet with powerful apps.",
        "models": ["iPad Pro", "iPad Air", "iPad", "iPad mini"],
        "services": ["AppleCare+", "Trade-in", "iPadOS updates"]
    },
    "watch": {
        "description": "Apple Watch is the ultimate device for a healthy life.",
        "models": ["Apple Watch Series 9", "Apple Watch Ultra 2", "Apple Watch SE"],
        "services": ["AppleCare+", "Trade-in", "watchOS updates"]
    },
    "services": {
        "applecare": "AppleCare+ extends your coverage and includes accidental damage protection.",
        "tradein": "Trade in your eligible device for credit toward your next purchase.",
        "support": "Get 24/7 priority access to Apple experts by chat or phone."
    }
}

# Error messages
ERROR_RESPONSES = {
    "no_query": "Please provide a query about Apple products or services.",
    "no_match": "I couldn't find information about that. Could you try rephrasing or ask about a specific Apple product or service?"
}

def process_query(query):
    """
    Process the user query and return an appropriate response.
    """
    if not query:
        return ERROR_RESPONSES["no_query"]
    
    query = query.lower().strip()
    
    # Check for product categories
    for product in ["iphone", "mac", "ipad", "watch"]:
        if product in query:
            return {
                "response": PRODUCT_KNOWLEDGE[product]["description"],
                "models": PRODUCT_KNOWLEDGE[product]["models"],
                "services": PRODUCT_KNOWLEDGE[product]["services"]
            }
    
    # Check for specific services
    if "applecare" in query:
        return {"response": PRODUCT_KNOWLEDGE["services"]["applecare"]}
    if "trade" in query or "trade-in" in query:
        return {"response": PRODUCT_KNOWLEDGE["services"]["tradein"]}
    if "support" in query or "help" in query:
        return {"response": PRODUCT_KNOWLEDGE["services"]["support"]}
    
    return {"response": ERROR_RESPONSES["no_match"]}

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat requests from the client.
    """
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"error": "Invalid request format"}), 400
        
        query = data['query']
        response = process_query(query)
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['GET'])
def get_products():
    """
    Return a list of all product categories.
    """
    try:
        products = list(PRODUCT_KNOWLEDGE.keys())
        products.remove("services")  # Remove services from product list
        return jsonify({"products": products})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Load configuration from environment variables
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # Start the Flask application
    app.run(host='0.0.0.0', port=port, debug=debug)
```
