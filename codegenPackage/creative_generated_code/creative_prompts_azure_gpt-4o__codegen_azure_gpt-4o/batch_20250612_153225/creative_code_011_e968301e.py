"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Create a web application prototype for managing the roles and responsibilities of "Weavers" and "Keepers" in a Kallimos pocket neighborhood.
Generated: DETERMINISTIC_e968301e73f5459f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a prototype written in Python using the Flask web framework. It includes routing for managing roles and responsibilities of "Weavers" and "Keepers."

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for roles and responsibilities
roles = {
    "Weavers": [],
    "Keepers": []
}

# Error messages
ROLE_NOT_FOUND = {"error": "Role not found. Valid roles are 'Weavers' and 'Keepers'."}
RESPONSIBILITY_NOT_FOUND = {"error": "Responsibility not found."}

@app.route("/")
def home():
    """
    Endpoint for checking server status.
    """
    return jsonify({"message": "Welcome to the Kallimos Role Manager API!"})


@app.route("/roles", methods=["GET"])
def get_roles():
    """
    Endpoint to retrieve all roles and their associated responsibilities.
    """
    return jsonify(roles)


@app.route("/roles/<role>", methods=["GET"])
def get_role_responsibilities(role):
    """
    Endpoint to retrieve responsibilities for a specific role.
    :param role: Name of the role ('Weavers' or 'Keepers').
    """
    role = role.capitalize()
    if role not in roles:
        return jsonify(ROLE_NOT_FOUND), 404
    return jsonify({role: roles[role]})


@app.route("/roles/<role>/add", methods=["POST"])
def add_responsibility(role):
    """
    Endpoint to add a responsibility to a specific role.
    :param role: Name of the role ('Weavers' or 'Keepers').
    :body: JSON payload with 'responsibility' key.
    """
    role = role.capitalize()
    if role not in roles:
        return jsonify(ROLE_NOT_FOUND), 404

    data = request.get_json()
    if not data or "responsibility" not in data:
        return jsonify({"error": "Request must include a 'responsibility' key in JSON body."}), 400

    responsibility = data["responsibility"]
    roles[role].append(responsibility)
    return jsonify({"message": f"Responsibility added to {role}.", role: roles[role]}), 201


@app.route("/roles/<role>/remove", methods=["DELETE"])
def remove_responsibility(role):
    """
    Endpoint to remove a responsibility from a specific role.
    :param role: Name of the role ('Weavers' or 'Keepers').
    :body: JSON payload with 'responsibility' key.
    """
    role = role.capitalize()
    if role not in roles:
        return jsonify(ROLE_NOT_FOUND), 404

    data = request.get_json()
    if not data or "responsibility" not in data:
        return jsonify({"error": "Request must include a 'responsibility' key in JSON body."}), 400

    responsibility = data["responsibility"]
    if responsibility not in roles[role]:
        return jsonify(RESPONSIBILITY_NOT_FOUND), 404

    roles[role].remove(responsibility)
    return jsonify({"message": f"Responsibility removed from {role}.", role: roles[role]}), 200


@app.route("/roles/<role>/clear", methods=["DELETE"])
def clear_responsibilities(role):
    """
    Endpoint to clear all responsibilities for a specific role.
    :param role: Name of the role ('Weavers' or 'Keepers').
    """
    role = role.capitalize()
    if role not in roles:
        return jsonify(ROLE_NOT_FOUND), 404

    roles[role] = []
    return jsonify({"message": f"All responsibilities cleared for {role}.", role: roles[role]}), 200


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- This code is a prototype and uses an in-memory database (`roles` dictionary). For production, a persistent database (e.g., PostgreSQL or MongoDB) should be used.
- The application has basic error handling for invalid input.
- To test, install Flask (`pip install flask`) and run the script. Use tools like Postman or curl to interact with the API.
