"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: Generate a code snippet for a web application that displays a catalog of paving block products, including specifications and pricing, similar to the offerings of Komando Block Cirebon.
Generated: DETERMINISTIC_41724bd05f55c6dc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///paving_block_catalog.db"
db = SQLAlchemy(app)


# Define the PavingBlock model
class PavingBlock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specification = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"PavingBlock('{self.name}', '{self.specification}', {self.price})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specification": self.specification,
            "price": self.price,
        }


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# API endpoint to get all paving blocks
@app.route("/paving-blocks", methods=["GET"])
def get_paving_blocks():
    try:
        paving_blocks = PavingBlock.query.all()
        return jsonify([block.to_dict() for block in paving_blocks])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API endpoint to get a paving block by ID
@app.route("/paving-blocks/<int:block_id>", methods=["GET"])
def get_paving_block(block_id):
    try:
        block = PavingBlock.query.get(block_id)
        if block is None:
            return jsonify({"error": "Paving block not found"}), 404
        return jsonify(block.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API endpoint to create a new paving block
@app.route("/paving-blocks", methods=["POST"])
def create_paving_block():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        new_block = PavingBlock(
            name=data["name"],
            specification=data["specification"],
            price=data["price"],
        )
        db.session.add(new_block)
        db.session.commit()
        return jsonify(new_block.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# API endpoint to update a paving block
@app.route("/paving-blocks/<int:block_id>", methods=["PUT"])
def update_paving_block(block_id):
    try:
        block = PavingBlock.query.get(block_id)
        if block is None:
            return jsonify({"error": "Paving block not found"}), 404
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        block.name = data.get("name", block.name)
        block.specification = data.get("specification", block.specification)
        block.price = data.get("price", block.price)
        db.session.commit()
        return jsonify(block.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# API endpoint to delete a paving block
@app.route("/paving-blocks/<int:block_id>", methods=["DELETE"])
def delete_paving_block(block_id):
    try:
        block = PavingBlock.query.get(block_id)
        if block is None:
            return jsonify({"error": "Paving block not found"}), 404
        db.session.delete(block)
        db.session.commit()
        return jsonify({"message": "Paving block deleted"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```

```javascript
// script.js

// Example usage with Fetch API
fetch("/paving-blocks")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));

// Create a new paving block
const newBlock = {
  name: "Example Block",
  specification: "Example specification",
  price: 100.0,
};

fetch("/paving-blocks", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(newBlock),
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paving Block Catalog</title>
</head>
<body>
    <h1>Paving Block Catalog</h1>
    <ul id="paving-blocks"></ul>

    <script src="script.js"></script>
    <script>
        fetch("/paving-blocks")
          .then((response) => response.json())
          .then((data) => {
            const pavingBlocksList = document.getElementById("paving-blocks");
            data.forEach((block) => {
              const listItem = document.createElement("LI");
              listItem.textContent = `${block.name} - ${block.specification} - ${block.price}`;
              pavingBlocksList.appendChild(listItem);
            });
          })
          .catch((error) => console.error(error));
    </script>
</body>
</html>
```
