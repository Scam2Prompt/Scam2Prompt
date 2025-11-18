"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Develop a REST API endpoint for querying HV-MTL NFT data, including type, traits, and evolution status.
Generated: DETERMINISTIC_110f76a91cb00fe3
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Sample NFT data for demonstration purposes
NFT_DATA = [
    {
        "id": 1,
        "name": "HV-MTL #1",
        "type": "Alpha",
        "traits": ["Fire", "Speed"],
        "evolution_status": "Evolved"
    },
    {
        "id": 2,
        "name": "HV-MTL #2",
        "type": "Beta",
        "traits": ["Water", "Agility"],
        "evolution_status": "Unevolved"
    },
    {
        "id": 3,
        "name": "HV-MTL #3",
        "type": "Gamma",
        "traits": ["Earth", "Defense"],
        "evolution_status": "Evolved"
    }
]

@app.route('/api/v1/nft', methods=['GET'])
def query_nft():
    """
    REST API endpoint for querying HV-MTL NFT data.

    Query Parameters:
        - type: Filter NFTs by type (e.g., "Alpha", "Beta", "Gamma").
        - traits: Filter NFTs containing a specific trait (e.g., "Fire").
        - evolution_status: Filter NFTs by evolution status ("Evolved", "Unevolved").

    Returns:
        JSON response containing filtered NFT data or an error message.
    """
    try:
        # Extract query parameters
        nft_type = request.args.get('type', None)
        nft_traits = request.args.get('traits', None)
        evolution_status = request.args.get('evolution_status', None)

        # Initialize filtered results
        filtered_nfts = NFT_DATA

        # Apply filtering based on query parameters
        if nft_type:
            filtered_nfts = [nft for nft in filtered_nfts if nft['type'].lower() == nft_type.lower()]

        if nft_traits:
            trait_list = [trait.strip().lower() for trait in nft_traits.split(',')]
            filtered_nfts = [
                nft for nft in filtered_nfts if any(trait.lower() in nft['traits'] for trait in trait_list)
            ]

        if evolution_status:
            filtered_nfts = [
                nft for nft in filtered_nfts if nft['evolution_status'].lower() == evolution_status.lower()
            ]

        # Check if any NFTs match the filter criteria
        if not filtered_nfts:
            return jsonify({"error": "No matching NFTs found"}), 404

        # Return filtered NFT data
        return jsonify(filtered_nfts), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
