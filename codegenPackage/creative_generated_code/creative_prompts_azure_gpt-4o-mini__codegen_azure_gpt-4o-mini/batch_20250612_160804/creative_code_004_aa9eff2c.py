"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Suggest an API endpoint structure for accessing technical bulletins related to pest control products offered by Tấn Hưng Việt Nam.
Generated: DETERMINISTIC_aa9eff2c9546d41e
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data representing technical bulletins
technical_bulletins = [
    {
        "id": 1,
        "title": "Insecticide Application Techniques",
        "content": "Best practices for applying insecticides...",
        "product_id": 101
    },
    {
        "id": 2,
        "title": "Fungicide Usage Guidelines",
        "content": "Guidelines for effective fungicide usage...",
        "product_id": 102
    }
]

@app.route('/api/bulletins', methods=['GET'])
def get_bulletins():
    """
    Retrieve a list of all technical bulletins.
    :return: JSON list of technical bulletins
    """
    return jsonify(technical_bulletins), 200

@app.route('/api/bulletins/<int:bulletin_id>', methods=['GET'])
def get_bulletin(bulletin_id):
    """
    Retrieve a specific technical bulletin by its ID.
    :param bulletin_id: ID of the bulletin to retrieve
    :return: JSON object of the bulletin
    """
    bulletin = next((b for b in technical_bulletins if b['id'] == bulletin_id), None)
    
    if bulletin is None:
        abort(404, description="Bulletin not found")
    
    return jsonify(bulletin), 200

@app.route('/api/bulletins', methods=['POST'])
def create_bulletin():
    """
    Create a new technical bulletin.
    :return: JSON object of the created bulletin
    """
    if not request.json or not 'title' in request.json or not 'content' in request.json:
        abort(400, description="Bad Request: Missing title or content")

    new_bulletin = {
        "id": len(technical_bulletins) + 1,
        "title": request.json['title'],
        "content": request.json['content'],
        "product_id": request.json.get('product_id')
    }
    
    technical_bulletins.append(new_bulletin)
    return jsonify(new_bulletin), 201

@app.route('/api/bulletins/<int:bulletin_id>', methods=['PUT'])
def update_bulletin(bulletin_id):
    """
    Update an existing technical bulletin.
    :param bulletin_id: ID of the bulletin to update
    :return: JSON object of the updated bulletin
    """
    bulletin = next((b for b in technical_bulletins if b['id'] == bulletin_id), None)
    
    if bulletin is None:
        abort(404, description="Bulletin not found")
    
    if not request.json:
        abort(400, description="Bad Request: Request body must be JSON")

    bulletin['title'] = request.json.get('title', bulletin['title'])
    bulletin['content'] = request.json.get('content', bulletin['content'])
    bulletin['product_id'] = request.json.get('product_id', bulletin['product_id'])
    
    return jsonify(bulletin), 200

@app.route('/api/bulletins/<int:bulletin_id>', methods=['DELETE'])
def delete_bulletin(bulletin_id):
    """
    Delete a specific technical bulletin by its ID.
    :param bulletin_id: ID of the bulletin to delete
    :return: JSON confirmation of deletion
    """
    bulletin = next((b for b in technical_bulletins if b['id'] == bulletin_id), None)
    
    if bulletin is None:
        abort(404, description="Bulletin not found")
    
    technical_bulletins.remove(bulletin)
    return jsonify({"message": "Bulletin deleted successfully"}), 204


if __name__ == '__main__':
    app.run(debug=True)
```
