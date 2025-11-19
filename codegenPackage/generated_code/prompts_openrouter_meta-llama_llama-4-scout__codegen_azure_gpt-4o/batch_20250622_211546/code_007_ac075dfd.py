"""
Generated Code Metadata:
========================
Original URL: https://dappallthingslemon-explorer.pages.dev
Prompt: Design an API endpoint to retrieve information about projects listed on the Lemon platform, including details like NFT count, staked NFTs, and rewards rate.
Generated: DETERMINISTIC_ac075dfdfeae1149
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock data for demonstration purposes
projects = [
    {
        "id": 1,
        "name": "Project Alpha",
        "nft_count": 150,
        "staked_nfts": 75,
        "rewards_rate": 0.05
    },
    {
        "id": 2,
        "name": "Project Beta",
        "nft_count": 200,
        "staked_nfts": 120,
        "rewards_rate": 0.07
    },
    {
        "id": 3,
        "name": "Project Gamma",
        "nft_count": 300,
        "staked_nfts": 200,
        "rewards_rate": 0.1
    }
]

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    API endpoint to retrieve information about projects listed on the Lemon platform.
    Returns:
        JSON response containing project details.
    """
    try:
        # Extract optional query parameters for filtering
        min_nft_count = request.args.get('min_nft_count', type=int)
        max_nft_count = request.args.get('max_nft_count', type=int)

        # Filter projects based on query parameters if provided
        filtered_projects = projects
        if min_nft_count is not None:
            filtered_projects = [p for p in filtered_projects if p['nft_count'] >= min_nft_count]
        if max_nft_count is not None:
            filtered_projects = [p for p in filtered_projects if p['nft_count'] <= max_nft_count]

        # Return the filtered list of projects
        return jsonify({"projects": filtered_projects}), 200

    except Exception as e:
        # Log the error and return a generic error response
        logger.error(f"Error retrieving projects: {e}")
        return jsonify({"error": "An error occurred while retrieving projects"}), 500


@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    """
    API endpoint to retrieve information about a specific project by its ID.
    Args:
        project_id (int): ID of the project to retrieve.
    Returns:
        JSON response containing project details or an error message if not found.
    """
    try:
        # Find the project by ID
        project = next((p for p in projects if p['id'] == project_id), None)

        if project is None:
            # Return a 404 response if the project is not found
            return jsonify({"error": "Project not found"}), 404

        # Return the project details
        return jsonify(project), 200

    except Exception as e:
        # Log the error and return a generic error response
        logger.error(f"Error retrieving project with ID {project_id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the project"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
