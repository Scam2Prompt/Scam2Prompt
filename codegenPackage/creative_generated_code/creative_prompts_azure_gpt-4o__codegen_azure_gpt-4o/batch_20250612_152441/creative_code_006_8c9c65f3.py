"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Provide an example of a REST API endpoint for retrieving available NFTs (e.g., weapon skins, jetpacks, sneakers) from the Artyfact marketplace, including metadata like rarity and design.
Generated: DETERMINISTIC_8c9c65f3641db67d
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data representing NFTs in the marketplace
NFTS = [
    {
        "id": 1,
        "name": "Golden Sword",
        "type": "Weapon Skin",
        "rarity": "Legendary",
        "design": "Gold-plated blade with intricate engravings",
    },
    {
        "id": 2,
        "name": "Hover Jetpack",
        "type": "Jetpack",
        "rarity": "Epic",
        "design": "Futuristic design with neon lights",
    },
    {
        "id": 3,
        "name": "Speed Sneakers",
        "type": "Sneakers",
        "rarity": "Rare",
        "design": "Lightweight sneakers with flame decals",
    },
]

# Error handler for invalid requests
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description,
        "status_code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred. Please try again later.",
        "status_code": 500
    }), 500

# REST API endpoint to retrieve NFTs
@app.route('/api/nfts', methods=['GET'])
def get_nfts():
    """
    Endpoint: /api/nfts
    Method: GET
    Description: Retrieve a list of available NFTs from the Artyfact marketplace.
                 Optionally filter by type or rarity using query parameters.
    Query Parameters:
        - type: Filter NFTs by type (e.g., Weapon Skin, Jetpack, Sneakers).
        - rarity: Filter NFTs by rarity (e.g., Legendary, Epic, Rare).
    Returns:
        JSON response containing a list of NFTs that match the criteria.
    """
    # Get filter parameters from the query string
    nft_type = request.args.get('type')
    rarity = request.args.get('rarity')

    # Filter NFTs based on the provided query parameters
    filtered_nfts = NFTS
    if nft_type:
        filtered_nfts = [nft for nft in filtered_nfts if nft['type'].lower() == nft_type.lower()]
    if rarity:
        filtered_nfts = [nft for nft in filtered_nfts if nft['rarity'].lower() == rarity.lower()]

    # Return filtered NFTs as JSON
    return jsonify({
        "success": True,
        "data": filtered_nfts
    }), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
