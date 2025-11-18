"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piclink.me
Prompt: Develop a feature for a bio link page that allows users to preview their PicLink-style link collection before publishing.
Generated: DETERMINISTIC_771d131575e2a7af
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Mock database for storing user bio link data
mock_database = {
    "users": {}
}

@app.route('/preview', methods=['POST'])
def preview_bio_links():
    """
    Endpoint to preview PicLink-style bio links before publishing.
    Users submit their links and a preview response is returned.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        if not data or 'user_id' not in data or 'links' not in data:
            return jsonify({"error": "Invalid input. Must include 'user_id' and 'links' fields."}), 400

        user_id = data['user_id']
        links = data['links']

        # Validate links format
        if not isinstance(links, list) or not all(isinstance(link, dict) for link in links):
            return jsonify({"error": "Invalid links format. Must be a list of dictionaries."}), 400

        # Store the preview in the mock database
        mock_database['users'][user_id] = links

        # Return preview response
        return jsonify({
            "message": "Preview generated successfully.",
            "preview": links
        }), 200

    except Exception as e:
        # Catch unexpected errors and provide a meaningful response
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/publish', methods=['POST'])
def publish_bio_links():
    """
    Endpoint to publish PicLink-style bio links after previewing.
    Users submit their user_id to confirm publishing.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        if not data or 'user_id' not in data:
            return jsonify({"error": "Invalid input. Must include 'user_id' field."}), 400

        user_id = data['user_id']

        # Check if the user has a preview available
        if user_id not in mock_database['users']:
            return jsonify({"error": "No preview found for this user. Generate a preview first."}), 404

        # Publish the links (mock publishing process)
        published_links = mock_database['users'][user_id]
        # Clear the preview from the mock database (to simulate publishing process)
        del mock_database['users'][user_id]

        # Return success response
        return jsonify({
            "message": "Links published successfully.",
            "published_links": published_links
        }), 200

    except Exception as e:
        # Catch unexpected errors and provide a meaningful response
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/preview-ui', methods=['GET'])
def preview_ui():
    """
    Endpoint to render a preview UI for users to visually confirm their links.
    """
    try:
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({"error": "Missing 'user_id' parameter."}), 400

        # Check if the user has a preview available
        if user_id not in mock_database['users']:
            return jsonify({"error": "No preview available for this user."}), 404

        # Retrieve the preview links
        links = mock_database['users'][user_id]
        
        # Render the preview page using a simple template
        return render_template('preview.html', user_id=user_id, links=links)

    except Exception as e:
        # Catch unexpected errors and provide a meaningful response
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Sample HTML template for the preview UI (to be stored in a 'templates' folder)
# File: templates/preview.html
# ------------------------------------
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Preview Bio Links</title>
# </head>
# <body>
#     <h1>Preview Bio Links for User: {{ user_id }}</h1>
#     <ul>
#         {% for link in links %}
#             <li>
#                 <a href="{{ link['url'] }}" target="_blank">{{ link['title'] }}</a>
#             </li>
#         {% endfor %}
#     </ul>
# </body>
# </html>
# ------------------------------------

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```
