"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testing-ipfs.pages.dev
Prompt: How can I implement a drop game using IPFS for asset verification in a community-driven project?
Generated: DETERMINISTIC_56ede15939308630
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import ipfshttpclient
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize IPFS client
try:
    ipfs = ipfshttpclient.connect()
except Exception as e:
    print(f"Error connecting to IPFS: {e}")
    exit(1)

# Directory to store metadata temporarily
METADATA_DIR = "metadata"
if not os.path.exists(METADATA_DIR):
    os.makedirs(METADATA_DIR)


def upload_to_ipfs(file_path):
    """
    Uploads a file to IPFS and returns the CID (Content Identifier).
    :param file_path: Path to the file to upload.
    :return: The CID of the uploaded file.
    """
    try:
        res = ipfs.add(file_path)
        return res['Hash']
    except Exception as e:
        raise RuntimeError(f"Failed to upload to IPFS: {e}")


def create_metadata(asset_name, description, asset_cid):
    """
    Creates metadata for an asset.
    :param asset_name: Name of the asset.
    :param description: Description of the asset.
    :param asset_cid: CID of the associated asset on IPFS.
    :return: Path to the JSON metadata file.
    """
    metadata = {
        "name": asset_name,
        "description": description,
        "asset_url": f"ipfs://{asset_cid}"
    }
    metadata_file = os.path.join(METADATA_DIR, f"{asset_name}.json")

    try:
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=4)
        return metadata_file
    except Exception as e:
        raise RuntimeError(f"Failed to create metadata file: {e}")


@app.route('/drop', methods=['POST'])
def create_drop():
    """
    Endpoint to create a new "drop" in the game.
    :return: JSON response with asset verification details.
    """
    try:
        # Extract data from request
        data = request.form
        asset_name = data.get('asset_name')
        description = data.get('description')
        asset_file = request.files['asset_file']

        if not asset_name or not description or not asset_file:
            return jsonify({"error": "Missing required fields"}), 400

        # Save the uploaded asset locally
        asset_file_path = os.path.join(METADATA_DIR, asset_file.filename)
        asset_file.save(asset_file_path)

        # Upload asset to IPFS
        asset_cid = upload_to_ipfs(asset_file_path)

        # Create metadata and upload it to IPFS
        metadata_file_path = create_metadata(asset_name, description, asset_cid)
        metadata_cid = upload_to_ipfs(metadata_file_path)

        # Cleanup local files (optional, for security reasons)
        os.remove(asset_file_path)
        os.remove(metadata_file_path)

        # Return response with IPFS CIDs
        return jsonify({
            "success": True,
            "asset_cid": asset_cid,
            "metadata_cid": metadata_cid
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
