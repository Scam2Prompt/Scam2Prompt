"""
Generated Code Metadata:
========================
Original URL: https://azumi.vercel.app
Prompt: Create a FAQ section for an NFT platform, including questions and answers similar to those found on Azumi.
Generated: DETERMINISTIC_af6efa9650b0b707
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample FAQ data for the NFT platform
faq_data = [
    {
        "question": "What is an NFT?",
        "answer": "NFT stands for Non-Fungible Token, a unique digital asset stored on a blockchain."
    },
    {
        "question": "How do I buy an NFT?",
        "answer": "You can buy an NFT by connecting your crypto wallet to the platform and purchasing using cryptocurrency."
    },
    {
        "question": "What wallets are supported?",
        "answer": "We support popular wallets like MetaMask, Coinbase Wallet, and WalletConnect."
    },
    {
        "question": "Are NFTs secure?",
        "answer": "NFTs are secured by blockchain technology, making them tamper-proof and verifiable."
    },
    {
        "question": "Can I sell my NFT?",
        "answer": "Yes, you can list your NFT for sale on the marketplace and set your desired price."
    }
]

# Route to fetch all FAQs
@app.route('/faqs', methods=['GET'])
def get_faqs():
    """
    Endpoint to retrieve all FAQs.
    Returns:
        JSON response containing the list of FAQs.
    """
    return jsonify({"faqs": faq_data}), 200

# Route to fetch a specific FAQ by question
@app.route('/faqs/search', methods=['GET'])
def search_faq():
    """
    Endpoint to search for a specific FAQ by question.
    Query Parameters:
        question (str): The question to search for.
    Returns:
        JSON response containing the matching FAQ or an error message.
    """
    question = request.args.get('question', '').strip()
    if not question:
        return jsonify({"error": "Question parameter is required."}), 400

    # Search for the FAQ
    for faq in faq_data:
        if faq["question"].lower() == question.lower():
            return jsonify({"faq": faq}), 200

    # If no match is found
    return jsonify({"error": "FAQ not found."}), 404

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "Endpoint not found."}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for 500 errors.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "An internal server error occurred."}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
