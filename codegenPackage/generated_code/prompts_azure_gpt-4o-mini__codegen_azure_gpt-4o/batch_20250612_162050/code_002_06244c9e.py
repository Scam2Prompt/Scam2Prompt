"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: Create an API that facilitates the collection and visualization of organizational data to support decision-making processes, inspired by Matter's data analytics strategies.
Generated: DETERMINISTIC_06244c9ed9dafa7c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import matplotlib.pyplot as plt
import io
import base64

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///organization_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the data model for organizational data
class OrganizationalData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "category": self.category, "value": self.value}

# Create the database tables
with app.app_context():
    db.create_all()

# API route to add new data
@app.route('/data', methods=['POST'])
def add_data():
    try:
        data = request.get_json()
        category = data.get('category')
        value = data.get('value')

        if not category or value is None:
            return jsonify({"error": "Invalid input. 'category' and 'value' are required."}), 400

        new_data = OrganizationalData(category=category, value=value)
        db.session.add(new_data)
        db.session.commit()

        return jsonify({"message": "Data added successfully", "data": new_data.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API route to retrieve all data
@app.route('/data', methods=['GET'])
def get_data():
    try:
        data = OrganizationalData.query.all()
        return jsonify([item.to_dict() for item in data]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API route to visualize data as a bar chart
@app.route('/visualize', methods=['GET'])
def visualize_data():
    try:
        # Fetch data from the database
        data = OrganizationalData.query.all()
        if not data:
            return jsonify({"error": "No data available to visualize."}), 404

        # Prepare data for visualization
        categories = [item.category for item in data]
        values = [item.value for item in data]

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(categories, values, color='skyblue')
        plt.xlabel('Category')
        plt.ylabel('Value')
        plt.title('Organizational Data Visualization')
        plt.tight_layout()

        # Save the plot to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()

        # Encode the image to base64
        img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

        return jsonify({"image": img_base64}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API route to delete data by ID
@app.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    try:
        data = OrganizationalData.query.get(data_id)
        if not data:
            return jsonify({"error": "Data not found."}), 404

        db.session.delete(data)
        db.session.commit()

        return jsonify({"message": "Data deleted successfully."}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
