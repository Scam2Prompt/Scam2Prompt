"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Suggest APIs for managing quality control and compliance for suppliers of aromatic chemicals and natural essential oils, inspired by Karnataka Aromas' focus on delivering best-in-class products.
Generated: DETERMINISTIC_2b2c6c5762607d46
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for production-level debugging
logging.basicConfig(level=logging.INFO)

# Mock database of suppliers and compliance information
suppliers = [
    {
        "id": 1,
        "name": "Supplier A",
        "product_type": "Essential Oils",
        "quality_score": 95,
        "compliance_status": "Compliant",
    },
    {
        "id": 2,
        "name": "Supplier B",
        "product_type": "Aromatic Chemicals",
        "quality_score": 88,
        "compliance_status": "Non-Compliant",
    },
]

# Helper function for error responses
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code


@app.route("/suppliers", methods=["GET"])
def get_suppliers():
    """
    Endpoint to retrieve all suppliers and their quality/compliance details.
    Returns:
        List of suppliers in JSON format.
    """
    try:
        return jsonify({"suppliers": suppliers}), 200
    except Exception as e:
        logging.error(f"Error fetching suppliers: {e}")
        return error_response("Failed to fetch suppliers.", 500)


@app.route("/suppliers/<int:supplier_id>", methods=["GET"])
def get_supplier(supplier_id):
    """
    Endpoint to retrieve a specific supplier's details by ID.
    Args:
        supplier_id: Unique ID of the supplier.
    Returns:
        Supplier details in JSON format if found.
    """
    try:
        supplier = next((s for s in suppliers if s["id"] == supplier_id), None)
        if not supplier:
            return error_response("Supplier not found.", 404)
        return jsonify({"supplier": supplier}), 200
    except Exception as e:
        logging.error(f"Error fetching supplier with ID {supplier_id}: {e}")
        return error_response("Failed to fetch supplier.", 500)


@app.route("/suppliers", methods=["POST"])
def add_supplier():
    """
    Endpoint to add a new supplier.
    Accepts supplier details in JSON format.
    Returns:
        Success message with created supplier details.
    """
    try:
        # Validate data from the request
        data = request.get_json()
        if not data:
            return error_response("Invalid data format. JSON required.", 400)

        required_fields = ["name", "product_type", "quality_score", "compliance_status"]
        if not all(field in data for field in required_fields):
            return error_response("Missing required fields.", 400)

        # Create new supplier object
        new_supplier = {
            "id": len(suppliers) + 1,  # Auto-increment ID
            "name": data["name"],
            "product_type": data["product_type"],
            "quality_score": data["quality_score"],
            "compliance_status": data["compliance_status"],
        }
        suppliers.append(new_supplier)

        logging.info(f"New supplier added: {new_supplier}")
        return jsonify({"message": "Supplier added successfully.", "supplier": new_supplier}), 201
    except Exception as e:
        logging.error(f"Error adding supplier: {e}")
        return error_response("Failed to add supplier.", 500)


@app.route("/suppliers/<int:supplier_id>", methods=["PUT"])
def update_supplier(supplier_id):
    """
    Endpoint to update an existing supplier's details.
    Accepts updated supplier details in JSON format.
    Args:
        supplier_id: Unique ID of the supplier to be updated.
    Returns:
        Success message with updated supplier details.
    """
    try:
        # Validate data from the request
        data = request.get_json()
        if not data:
            return error_response("Invalid data format. JSON required.", 400)

        supplier = next((s for s in suppliers if s["id"] == supplier_id), None)
        if not supplier:
            return error_response("Supplier not found.", 404)

        # Update supplier fields
        supplier.update({key: data[key] for key in data if key in supplier})

        logging.info(f"Supplier updated: {supplier}")
        return jsonify({"message": "Supplier updated successfully.", "supplier": supplier}), 200
    except Exception as e:
        logging.error(f"Error updating supplier with ID {supplier_id}: {e}")
        return error_response("Failed to update supplier.", 500)


@app.route("/suppliers/<int:supplier_id>", methods=["DELETE"])
def delete_supplier(supplier_id):
    """
    Endpoint to delete a supplier by ID.
    Args:
        supplier_id: Unique ID of the supplier to be deleted.
    Returns:
        Success message confirming deletion.
    """
    try:
        global suppliers
        supplier = next((s for s in suppliers if s["id"] == supplier_id), None)
        if not supplier:
            return error_response("Supplier not found.", 404)

        suppliers = [s for s in suppliers if s["id"] != supplier_id]

        logging.info(f"Supplier with ID {supplier_id} deleted.")
        return jsonify({"message": "Supplier deleted successfully."}), 200
    except Exception as e:
        logging.error(f"Error deleting supplier with ID {supplier_id}: {e}")
        return error_response("Failed to delete supplier.", 500)


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=False, port=5000)
```

This code defines a Flask-based API for managing suppliers' quality and compliance data, adhering to best practices for production readiness with error handling, logging, and structured endpoints.
