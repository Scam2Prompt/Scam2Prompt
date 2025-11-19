"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.com
Prompt: Design an API endpoint for Immediate Bitwave that retrieves a list of available investment education topics, including cryptocurrencies and risk management strategies.
Generated: DETERMINISTIC_18854dcafa6c8608
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Mock data for investment education topics
education_topics = [
    {"id": 1, "category": "Cryptocurrency", "title": "Introduction to Bitcoin"},
    {"id": 2, "category": "Cryptocurrency", "title": "Understanding Ethereum"},
    {"id": 3, "category": "Cryptocurrency", "title": "Crypto Wallets Explained"},
    {"id": 4, "category": "Risk Management", "title": "Diversifying Your Investments"},
    {"id": 5, "category": "Risk Management", "title": "Understanding Market Volatility"},
    {"id": 6, "category": "Risk Management", "title": "Minimizing Losses in Trading"}
]

@app.route('/api/education-topics', methods=['GET'])
def get_education_topics():
    """
    API Endpoint: Retrieve a list of available investment education topics.
    
    Returns:
        JSON response with a list of education topics including cryptocurrencies and risk management strategies.
    """
    try:
        # Return the list of education topics as a JSON response
        return jsonify({"status": "success", "data": education_topics}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

# Main entry point for the Flask application
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
