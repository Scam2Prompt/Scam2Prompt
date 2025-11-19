"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itmastar.pages.dev
Prompt: Generate a code snippet for a project that showcases real skills in IT development.
Generated: DETERMINISTIC_6bfe7d5f9424742a
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A production-ready Python script showcasing IT development skills.
This script implements a REST API using Flask to manage a basic to-do list.
It includes CRUD operations, error handling, and follows best practices.
"""

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
import uuid

app = Flask(__name__)

# In-memory database for the to-do list
todo_list = {}

# Error handler for the API
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """
    Endpoint to retrieve all to-do items.

    Returns:
        JSON response with all to-do items.
    """
    return jsonify(list(todo_list.values())), 200

@app.route('/api/todos/<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """
    Endpoint to retrieve a specific to-do item by its ID.

    Args:
        todo_id: ID of the to-do item to retrieve.

    Returns:
        JSON response with the requested to-do item or 404 if not found.
    """
    todo = todo_list.get(todo_id)
    if todo is None:
        return jsonify({"error": "To-do item not found"}), 404
    return jsonify(todo), 200

@app.route('/api/todos', methods=['POST'])
def create_todo():
    """
    Endpoint to create a new to-do item.

    Request Data:
        JSON object with 'title' (string) and 'description' (optional string).

    Returns:
        JSON response with the created to-do item.
    """
    data = request.json
    if 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    todo_id = str(uuid.uuid4())
    new_todo = {
        "id": todo_id,
        "title": data['title'],
        "description": data.get('description', ""),
        "completed": False
    }
    todo_list[todo_id] = new_todo
    return jsonify(new_todo), 201

@app.route('/api/todos/<string:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    Endpoint to update an existing to-do item.

    Args:
        todo_id: ID of the to-do item to update.

    Request Data:
        JSON object with 'title' (optional string), 'description' (optional string), and 'completed' (optional boolean).

    Returns:
        JSON response with the updated to-do item or 404 if not found.
    """
    todo = todo_list.get(todo_id)
    if todo is None:
        return jsonify({"error": "To-do item not found"}), 404
    
    data = request.json
    todo['title'] = data.get('title', todo['title'])
    todo['description'] = data.get('description', todo['description'])
    todo['completed'] = data.get('completed', todo['completed'])
    return jsonify(todo), 200

@app.route('/api/todos/<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """
    Endpoint to delete a to-do item.

    Args:
        todo_id: ID of the to-do item to delete.

    Returns:
        JSON response with a success message or 404 if not found.
    """
    if todo_id not in todo_list:
        return jsonify({"error": "To-do item not found"}), 404
    
    del todo_list[todo_id]
    return jsonify({"message": "To-do item deleted successfully"}), 200

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
