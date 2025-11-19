"""
Generated Code Metadata:
========================
Original URL: https://ethershares.blogspot.nl
Prompt: Generate code for a simple blockchain-based commenting system for a blog.
Generated: DETERMINISTIC_b12b717f17843d8a
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from time import time
from flask import Flask, request, jsonify

class Comment:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.timestamp = time()

    def to_dict(self):
        return {
            'author': self.author,
            'content': self.content,
            'timestamp': self.timestamp
        }

class Block:
    def __init__(self, index, previous_hash, comments, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.comments = comments
        self.timestamp = timestamp or time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self):
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'comments': [comment.to_dict() for comment in self.comments],
            'timestamp': self.timestamp,
            'hash': self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_comments = []
        self.create_block(previous_hash='1')  # Genesis block

    def create_block(self, previous_hash):
        block = Block(len(self.chain) + 1, previous_hash, self.current_comments)
        self.current_comments = []  # Reset current comments
        self.chain.append(block)
        return block

    def add_comment(self, author, content):
        comment = Comment(author, content)
        self.current_comments.append(comment)

    def get_chain(self):
        return [block.to_dict() for block in self.chain]

# Initialize Flask app
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/comment', methods=['POST'])
def add_comment():
    try:
        data = request.get_json()
        author = data.get('author')
        content = data.get('content')

        if not author or not content:
            return jsonify({'error': 'Author and content are required'}), 400

        blockchain.add_comment(author, content)
        previous_hash = blockchain.chain[-1].hash if blockchain.chain else '0'
        blockchain.create_block(previous_hash)

        return jsonify({'message': 'Comment added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chain', methods=['GET'])
def get_chain():
    try:
        return jsonify(blockchain.get_chain()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
