"""
Generated Code Metadata:
========================
Original URL: https://proposal-ownthedoge.com
Prompt: "Propose a community-driven project funded by The Bark Tank, focusing on Doge's cultural impact and how to preserve its history for future generations."
Generated: DETERMINISTIC_1628f31995191190
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Proposal: Doge Cultural Preservation Platform
This Python script outlines a community-driven project funded by The Bark Tank.
The project focuses on preserving Doge's cultural impact and history for future generations.
The platform will allow users to contribute Doge-related content, vote on submissions, and access curated archives.
"""

import os
import json
from datetime import datetime
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Directory to store Doge-related content
CONTENT_DIR = "doge_content"
os.makedirs(CONTENT_DIR, exist_ok=True)

# Error messages
ERROR_MESSAGES = {
    "missing_fields": "Required fields are missing.",
    "invalid_data": "Invalid data provided.",
    "not_found": "Requested resource not found.",
}

# Helper function to load content from file
def load_content():
    """Load all Doge-related content from the storage directory."""
    content = []
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(CONTENT_DIR, filename), "r") as file:
                content.append(json.load(file))
    return content

# Helper function to save content to file
def save_content(data):
    """Save Doge-related content to a file."""
    try:
        filename = f"{CONTENT_DIR}/{data['id']}.json"
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise RuntimeError(f"Failed to save content: {e}")

# Route: Submit Doge-related content
@app.route("/submit", methods=["POST"])
def submit_content():
    """
    Submit Doge-related content.
    Expected JSON format:
    {
        "title": "Title of the content",
        "description": "Description of the content",
        "author": "Author's name",
        "tags": ["tag1", "tag2"]
    }
    """
    try:
        data = request.json
        # Validate input
        if not all(key in data for key in ["title", "description", "author", "tags"]):
            return jsonify({"error": ERROR_MESSAGES["missing_fields"]}), 400

        # Create content object
        content = {
            "id": str(datetime.now().timestamp()).replace(".", ""),
            "title": data["title"],
            "description": data["description"],
            "author": data["author"],
            "tags": data["tags"],
            "timestamp": datetime.now().isoformat(),
        }

        # Save content
        save_content(content)
        return jsonify({"message": "Content submitted successfully!", "content": content}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: View all Doge-related content
@app.route("/content", methods=["GET"])
def view_content():
    """
    View all Doge-related content.
    Returns a list of all submitted content.
    """
    try:
        content = load_content()
        return jsonify({"content": content}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Search content by tag
@app.route("/search", methods=["GET"])
def search_content():
    """
    Search Doge-related content by tag.
    Query parameter: ?tag=<tag>
    """
    try:
        tag = request.args.get("tag")
        if not tag:
            return jsonify({"error": ERROR_MESSAGES["missing_fields"]}), 400

        content = load_content()
        filtered_content = [item for item in content if tag in item.get("tags", [])]
        return jsonify({"content": filtered_content}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Vote on content
@app.route("/vote/<content_id>", methods=["POST"])
def vote_content(content_id):
    """
    Vote on Doge-related content.
    Expected JSON format:
    {
        "vote": "up" or "down"
    }
    """
    try:
        data = request.json
        if "vote" not in data or data["vote"] not in ["up", "down"]:
            return jsonify({"error": ERROR_MESSAGES["invalid_data"]}), 400

        content = load_content()
        for item in content:
            if item["id"] == content_id:
                item["votes"] = item.get("votes", 0) + (1 if data["vote"] == "up" else -1)
                save_content(item)
                return jsonify({"message": "Vote recorded successfully!", "content": item}), 200

        return jsonify({"error": ERROR_MESSAGES["not_found"]}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
```
