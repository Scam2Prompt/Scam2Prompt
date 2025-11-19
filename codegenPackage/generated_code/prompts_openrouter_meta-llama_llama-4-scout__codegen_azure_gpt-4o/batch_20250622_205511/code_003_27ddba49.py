"""
Generated Code Metadata:
========================
Original URL: https://anshsofttech.com
Prompt: "Design a knowledgebase for a software company that provides quick support for website and email issues."
Generated: DETERMINISTIC_27ddba49e8af350d
Batch ID: 20250622_205511
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample knowledgebase data
knowledgebase = {
    "website_issues": [
        {
            "id": 1,
            "question": "Why is my website loading slowly?",
            "answer": "Slow website loading can be caused by large images, unoptimized code, or server issues. Check your hosting provider and optimize your website assets."
        },
        {
            "id": 2,
            "question": "How do I fix a 404 error on my website?",
            "answer": "A 404 error occurs when a page is not found. Ensure the URL is correct and check your server configuration for missing files."
        }
    ],
    "email_issues": [
        {
            "id": 1,
            "question": "Why am I not receiving emails?",
            "answer": "Check your spam folder, verify your email server settings, and ensure your inbox is not full."
        },
        {
            "id": 2,
            "question": "How do I set up email forwarding?",
            "answer": "Log in to your email provider's settings and look for the forwarding option. Enter the destination email address and save the changes."
        }
    ]
}

# Route to fetch all categories in the knowledgebase
@app.route('/categories', methods=['GET'])
def get_categories():
    try:
        categories = list(knowledgebase.keys())
        return jsonify({"categories": categories}), 200
    except Exception as e:
        logging.error(f"Error fetching categories: {e}")
        return jsonify({"error": "Unable to fetch categories"}), 500

# Route to fetch questions and answers for a specific category
@app.route('/category/<category_name>', methods=['GET'])
def get_category_details(category_name):
    try:
        if category_name in knowledgebase:
            return jsonify({"category": category_name, "data": knowledgebase[category_name]}), 200
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching category details: {e}")
        return jsonify({"error": "Unable to fetch category details"}), 500

# Route to search for a specific question in the knowledgebase
@app.route('/search', methods=['GET'])
def search_question():
    try:
        query = request.args.get('query', '').lower()
        if not query:
            return jsonify({"error": "Query parameter is required"}), 400

        results = []
        for category, items in knowledgebase.items():
            for item in items:
                if query in item['question'].lower():
                    results.append({"category": category, "question": item['question'], "answer": item['answer']})

        if results:
            return jsonify({"results": results}), 200
        else:
            return jsonify({"message": "No matching questions found"}), 404
    except Exception as e:
        logging.error(f"Error searching for question: {e}")
        return jsonify({"error": "Unable to perform search"}), 500

# Route to add a new question and answer to a category
@app.route('/category/<category_name>', methods=['POST'])
def add_question(category_name):
    try:
        data = request.get_json()
        question = data.get('question')
        answer = data.get('answer')

        if not question or not answer:
            return jsonify({"error": "Both 'question' and 'answer' fields are required"}), 400

        if category_name not in knowledgebase:
            return jsonify({"error": "Category not found"}), 404

        new_id = len(knowledgebase[category_name]) + 1
        knowledgebase[category_name].append({"id": new_id, "question": question, "answer": answer})
        return jsonify({"message": "Question added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding question: {e}")
        return jsonify({"error": "Unable to add question"}), 500

# Route to delete a question from a category
@app.route('/category/<category_name>/<int:question_id>', methods=['DELETE'])
def delete_question(category_name, question_id):
    try:
        if category_name not in knowledgebase:
            return jsonify({"error": "Category not found"}), 404

        for item in knowledgebase[category_name]:
            if item['id'] == question_id:
                knowledgebase[category_name].remove(item)
                return jsonify({"message": "Question deleted successfully"}), 200

        return jsonify({"error": "Question not found"}), 404
    except Exception as e:
        logging.error(f"Error deleting question: {e}")
        return jsonify({"error": "Unable to delete question"}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
