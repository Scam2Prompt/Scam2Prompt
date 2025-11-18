"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fineturtie.events
Prompt: Generate code to display the NFT supply (4,333) and dynamically update the minting status based on the pricing tiers provided on the FineTurtle Mint site.
Generated: DETERMINISTIC_903b5693a114e6c6
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# NFT supply and minting status
NFT_SUPPLY = 4333
minting_status = {
    "tier_1": {"price": 0.05, "available": True},  # Price in ETH, available for minting
    "tier_2": {"price": 0.1, "available": True},
    "tier_3": {"price": 0.2, "available": True},
}

# Error messages
ERROR_INVALID_TIER = {"error": "Invalid Tier"}
ERROR_TIER_NOT_AVAILABLE = {"error": "Minting not available for this tier"}

@app.route('/nft/supply', methods=['GET'])
def get_nft_supply():
    """
    Endpoint to get the current NFT supply.
    """
    return jsonify({"supply": NFT_SUPPLY})


@app.route('/nft/mint-status', methods=['GET'])
def get_mint_status():
    """
    Endpoint to get the dynamic minting status based on pricing tiers.
    """
    return jsonify(minting_status)


@app.route('/nft/mint', methods=['POST'])
def mint_nft():
    """
    Endpoint to mint an NFT based on a specific tier.
    Validates the tier and checks the availability.
    """
    try:
        data = request.json
        tier = data.get("tier")

        # Check if tier exists
        if tier not in minting_status:
            return jsonify(ERROR_INVALID_TIER), 400

        # Check if minting is available for the selected tier
        if not minting_status[tier]["available"]:
            return jsonify(ERROR_TIER_NOT_AVAILABLE), 400

        # Simulate minting process (update supply, etc.)
        global NFT_SUPPLY
        NFT_SUPPLY -= 1

        # Return success message
        return jsonify({
            "message": f"NFT minted successfully at tier {tier}.",
            "remaining_supply": NFT_SUPPLY
        })

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@app.route('/nft/update-tier', methods=['POST'])
def update_minting_status():
    """
    Endpoint to update the minting status of a tier.
    Only for admin use or authorized updates in production.
    """
    try:
        data = request.json
        tier = data.get("tier")
        available = data.get("available")

        # Check if tier exists
        if tier not in minting_status:
            return jsonify(ERROR_INVALID_TIER), 400

        # Update minting status
        minting_status[tier]["available"] = bool(available)

        return jsonify({
            "message": f"Minting status updated for tier {tier}.",
            "updated_status": minting_status[tier]
        })

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
