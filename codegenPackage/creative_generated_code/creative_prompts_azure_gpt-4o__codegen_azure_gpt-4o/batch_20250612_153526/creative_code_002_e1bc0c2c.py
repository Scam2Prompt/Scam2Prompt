"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disney-pinnacles.web.app
Prompt: Generate a script to integrate Disney Pinnacle NFT minting functionality into a web application, referencing Dapper Labs' blockchain infrastructure.
Generated: DETERMINISTIC_e1bc0c2c69bac1c9
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries and dependencies
from flask import Flask, request, jsonify
from flow_py_sdk import flow_client, signer, tx
import os

# Initialize the web application
app = Flask(__name__)

# Configuration settings (should be stored securely in production)
DAPPER_FLOW_NETWORK = "testnet"  # Use 'mainnet' for production
DISNEY_PINNACLE_CONTRACT_ADDRESS = "0xDisneyNFTContract"  # Replace with actual contract address
SERVICE_ACCOUNT_ADDRESS = "0xYourServiceAccountAddress"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key for signing transactions (use environment variables)
SERVICE_ACCOUNT_KEY_INDEX = 0  # Key index for the service account

# Initialize Flow blockchain client
flow_client.connect_network(DAPPER_FLOW_NETWORK)

# Route to mint Disney Pinnacle NFTs
@app.route('/mint', methods=['POST'])
def mint_nft():
    """
    Endpoint to mint a Disney Pinnacle NFT.
    Expects JSON input with the following fields:
    - recipient: Flow address of the recipient
    - metadata: Metadata for the NFT (e.g., name, image URL, attributes)
    """
    try:
        # Parse request JSON
        data = request.json
        recipient = data.get('recipient')
        metadata = data.get('metadata')

        # Validate input
        if not recipient or not metadata:
            return jsonify({"error": "Recipient and metadata are required."}), 400

        # Prepare the NFT minting transaction
        tx_body = tx.Transaction(
            code=f"""
                import DisneyPinnacleNFT from {DISNEY_PINNACLE_CONTRACT_ADDRESS}

                transaction(recipient: Address, metadata: {type(metadata)}) {{
                    prepare(signer: AuthAccount) {{
                        let collection = signer.borrow<&DisneyPinnacleNFT.Collection>(from: DisneyPinnacleNFT.CollectionStoragePath)
                            ?? signer.create<&DisneyPinnacleNFT.Collection>(DisneyPinnacleNFT.CollectionStoragePath)
                        DisneyPinnacleNFT.mintNFT(recipient: recipient, metadata: metadata)
                    }}
                }}
            """,
            proposer=SERVICE_ACCOUNT_ADDRESS,
            payer=SERVICE_ACCOUNT_ADDRESS,
            authorizer=[SERVICE_ACCOUNT_ADDRESS]
        )

        # Sign and submit the transaction
        tx_body.sign(signer(SERVICE_ACCOUNT_ADDRESS, PRIVATE_KEY, SERVICE_ACCOUNT_KEY_INDEX))
        transaction_id = flow_client.send_transaction(tx_body)

        # Wait for transaction confirmation
        result = flow_client.wait_for_confirmation(transaction_id)

        # Return success response
        return jsonify({
            "message": "NFT minted successfully.",
            "transaction_id": transaction_id,
            "result": result
        }), 200

    except Exception as e:
        # Handle errors and return response
        return jsonify({"error": str(e)}), 500


# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint to check if the service is up and running.
    """
    return jsonify({"status": "ok"}), 200


# Run the application
if __name__ == '__main__':
    # Ensure the private key is loaded
    if not PRIVATE_KEY:
        raise EnvironmentError("PRIVATE_KEY environment variable is not set.")
    
    # Start the web server
    app.run(host='0.0.0.0', port=5000)
```
