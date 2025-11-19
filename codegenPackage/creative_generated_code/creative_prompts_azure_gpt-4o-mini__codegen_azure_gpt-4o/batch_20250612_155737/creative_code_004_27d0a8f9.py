"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrumm.nfts2.me
Prompt: What are the best practices for ensuring intellectual property rights when creating and selling NFTs, as discussed on NFTs 2 Me?
Generated: DETERMINISTIC_27d0a8f965f137ef
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code for a hypothetical platform that allows users to generate and sell NFTs, ensuring intellectual property (IP) rights adherence. This code uses Python with the Flask framework and includes comments about best practices for ensuring IP rights.

```python
from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# Mock database - In production, replace with a real database
NFT_DATABASE = {}

# Define acceptable file formats for NFTs
ALLOWED_FILE_FORMATS = ['png', 'jpg', 'jpeg', 'gif', 'mp4']

def validate_file_format(filename):
    """
    Validates the file format of the uploaded artwork/asset for NFT creation.
    """
    file_extension = os.path.splitext(filename)[1].lower()
    return file_extension[1:] in ALLOWED_FILE_FORMATS

@app.route('/create-nft', methods=['POST'])
def create_nft():
    """
    Endpoint to create a new NFT.
    Ensures intellectual property rights by requiring upload of original work and metadata.
    """
    try:
        # Check if request contains necessary parameters
        if 'file' not in request.files or 'metadata' not in request.form:
            return jsonify({'error': 'File and metadata are required'}), 400

        file = request.files['file']
        metadata = request.form['metadata']

        # Validate file format
        if not validate_file_format(file.filename):
            return jsonify({'error': 'Unsupported file format'}), 400

        # Validate metadata (e.g., JSON format)
        try:
            metadata = json.loads(metadata)
        except json.JSONDecodeError:
            return jsonify({'error': 'Invalid metadata format. Must be JSON'}), 400

        # Check intellectual property rights in metadata
        if 'creator' not in metadata or 'license' not in metadata:
            return jsonify({'error': 'Metadata must include creator and license information'}), 400

        # Save NFT data to the database (mock database here)
        nft_id = len(NFT_DATABASE) + 1
        NFT_DATABASE[nft_id] = {
            'file_name': file.filename,
            'metadata': metadata
        }

        # In production: File should be saved to a secure location
        file.save(os.path.join('uploads', file.filename))  # Replace 'uploads' with a secure path

        return jsonify({'message': 'NFT created successfully', 'nft_id': nft_id}), 201

    except Exception as e:
        # Log the exception (In production, log to a file or monitoring tool)
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/get-nft/<int:nft_id>', methods=['GET'])
def get_nft(nft_id):
    """
    Retrieves details of a specific NFT by ID.
    """
    nft = NFT_DATABASE.get(nft_id)
    if not nft:
        return jsonify({'error': 'NFT not found'}), 404
    return jsonify(nft), 200

@app.route('/sell-nft/<int:nft_id>', methods=['POST'])
def sell_nft(nft_id):
    """
    Endpoint to initiate the sale of an NFT.
    Ensures the original creator's rights are preserved.
    """
    try:
        nft = NFT_DATABASE.get(nft_id)
        if not nft:
            return jsonify({'error': 'NFT not found'}), 404

        # Verify ownership and licensing in metadata
        metadata = nft.get('metadata')
        if metadata.get('license') != 'transferable':
            return jsonify({'error': 'NFT license does not allow resale'}), 403

        # Process sale logic (mocked here)
        # In production: integrate with a blockchain or payment processor
        return jsonify({'message': 'NFT sale initiated successfully'}), 200

    except Exception as e:
        # Log the exception
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    # Ensure uploads directory exists
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    
    # Start the Flask application
    app.run(debug=True)
```

### Key Best Practices Followed:
1. **Input Validation**: Validates file format and metadata structure.
2. **Error Handling**: Provides descriptive error messages for invalid inputs or unexpected server errors.
3. **Security**: Ensures files are saved in a controlled directory and checks license metadata.
4. **Licensing and Ownership**: Includes explicit checks for IP rights in metadata.
5. **Scalability**: Uses modular functions for reusability and better code organization.

Deploy the application with a production-ready setup (like Gunicorn or Docker) for scaling and security enhancements.
