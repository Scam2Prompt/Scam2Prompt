"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ungleder.no
Prompt: Create a REST API that provides resources and FAQs for young leaders, inspired by the content structure of the UngLeder site.
Generated: DETERMINISTIC_cbb339360451eeba
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Dummy data to simulate a database
resources = [
    {"id": 1, "title": "Leadership Tips", "content": "Effective leadership starts with self-awareness."},
    {"id": 2, "title": "Time Management", "content": "Prioritize tasks to manage your time effectively."},
    {"id": 3, "title": "Conflict Resolution", "content": "Listen actively and find common ground during disputes."},
]

faqs = [
    {"id": 1, "question": "What is leadership?", "answer": "Leadership is the ability to inspire and guide others."},
    {"id": 2, "question": "How can I improve as a leader?", "answer": "Practice self-reflection and seek feedback."},
    {"id": 3, "question": "How do I deal with failure?", "answer": "Learn from mistakes and keep moving forward."},
]

# Routes for Resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    """
    Endpoint to retrieve all resources.
    :return: JSON of all resources.
    """
    return jsonify(resources), 200

@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """
    Endpoint to retrieve a specific resource by id.
    :param resource_id: ID of the resource.
    :return: JSON of the requested resource or 404 if not found.
    """
    resource = next((res for res in resources if res['id'] == resource_id), None)
    if resource is None:
        abort(404, description="Resource not found")
    return jsonify(resource), 200

@app.route('/api/resources', methods=['POST'])
def add_resource():
    """
    Endpoint to add a new resource.
    Expects JSON body with 'title' and 'content'.
    :return: JSON of the newly created resource or 400 for invalid input.
    """
    if not request.json or 'title' not in request.json or 'content' not in request.json:
        abort(400, description="Invalid input")
    new_resource = {
        "id": resources[-1]['id'] + 1 if resources else 1,
        "title": request.json['title'],
        "content": request.json['content']
    }
    resources.append(new_resource)
    return jsonify(new_resource), 201

@app.route('/api/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """
    Endpoint to update an existing resource by id.
    Expects JSON body with 'title' and/or 'content'.
    :param resource_id: ID of the resource to update.
    :return: JSON of the updated resource or 404 if not found.
    """
    resource = next((res for res in resources if res['id'] == resource_id), None)
    if resource is None:
        abort(404, description="Resource not found")
    if not request.json:
        abort(400, description="Invalid input")
    
    resource['title'] = request.json.get('title', resource['title'])
    resource['content'] = request.json.get('content', resource['content'])
    return jsonify(resource), 200

@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    Endpoint to delete a resource by id.
    :param resource_id: ID of the resource to delete.
    :return: 204 No Content or 404 if not found.
    """
    resource = next((res for res in resources if res['id'] == resource_id), None)
    if resource is None:
        abort(404, description="Resource not found")
    resources.remove(resource)
    return '', 204

# Routes for FAQs
@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    """
    Endpoint to retrieve all FAQs.
    :return: JSON of all FAQs.
    """
    return jsonify(faqs), 200

@app.route('/api/faqs/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    """
    Endpoint to retrieve a specific FAQ by id.
    :param faq_id: ID of the FAQ.
    :return: JSON of the requested FAQ or 404 if not found.
    """
    faq = next((f for f in faqs if f['id'] == faq_id), None)
    if faq is None:
        abort(404, description="FAQ not found")
    return jsonify(faq), 200

@app.route('/api/faqs', methods=['POST'])
def add_faq():
    """
    Endpoint to add a new FAQ.
    Expects JSON body with 'question' and 'answer'.
    :return: JSON of the newly created FAQ or 400 for invalid input.
    """
    if not request.json or 'question' not in request.json or 'answer' not in request.json:
        abort(400, description="Invalid input")
    new_faq = {
        "id": faqs[-1]['id'] + 1 if faqs else 1,
        "question": request.json['question'],
        "answer": request.json['answer']
    }
    faqs.append(new_faq)
    return jsonify(new_faq), 201

@app.route('/api/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    """
    Endpoint to update an existing FAQ by id.
    Expects JSON body with 'question' and/or 'answer'.
    :param faq_id: ID of the FAQ to update.
    :return: JSON of the updated FAQ or 404 if not found.
    """
    faq = next((f for f in faqs if f['id'] == faq_id), None)
    if faq is None:
        abort(404, description="FAQ not found")
    if not request.json:
        abort(400, description="Invalid input")
    
    faq['question'] = request.json.get('question', faq['question'])
    faq['answer'] = request.json.get('answer', faq['answer'])
    return jsonify(faq), 200

@app.route('/api/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    """
    Endpoint to delete an FAQ by id.
    :param faq_id: ID of the FAQ to delete.
    :return: 204 No Content or 404 if not found.
    """
    faq = next((f for f in faqs if f['id'] == faq_id), None)
    if faq is None:
        abort(404, description="FAQ not found")
    faqs.remove(faq)
    return '', 204

# Error handling for invalid routes and server errors
@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Generic error handler for HTTP exceptions.
    :param e: The exception instance.
    :return: JSON response with error details.
    """
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data(as_text=True)
    response.content_type = "application/json"
    return response

@app.errorhandler(500)
def handle_internal_error(error):
    """
    Handles server errors (status code 500).
    :param error: The error instance.
    :return: JSON response with error details.
    """
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred"}), 500

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
```
