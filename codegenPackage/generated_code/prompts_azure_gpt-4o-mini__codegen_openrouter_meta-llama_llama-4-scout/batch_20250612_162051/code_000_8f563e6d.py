"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: Generate a code snippet for a web application that allows users to search for properties to rent or buy in Neiva, Colombia, similar to the services offered by Inmobiliaria Félix Trujillo Falla.
Generated: DETERMINISTIC_8f563e6de2efe6ef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@localhost:5432/neiva_properties"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)


# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # rent or buy
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Property('{self.type}', '{self.price}', '{self.location}')"

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "price": self.price,
            "location": self.location,
            "description": self.description,
        }


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Define the search endpoint
@app.route("/search", methods=["GET"])
def search_properties():
    try:
        # Get query parameters
        property_type = request.args.get("type")
        location = request.args.get("location")
        min_price = request.args.get("min_price", type=float)
        max_price = request.args.get("max_price", type=float)

        # Build the query
        query = Property.query

        if property_type:
            query = query.filter(Property.type == property_type)
        if location:
            query = query.filter(Property.location.like(f"%{location}%"))
        if min_price:
            query = query.filter(Property.price >= min_price)
        if max_price:
            query = query.filter(Property.price <= max_price)

        # Execute the query and return results
        results = [prop.to_dict() for prop in query.all()]
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Define the main entry point
if __name__ == "__main__":
    app.run(debug=True)
```

```javascript
// Import required libraries
const express = require('express');
const app = express();
const { Pool } = require('pg');

// Configure the database connection
const pool = new Pool({
  user: 'user',
  host: 'localhost',
  database: 'neiva_properties',
  password: 'password',
  port: 5432,
});

// Define the search endpoint
app.get('/search', async (req, res) => {
  try {
    // Get query parameters
    const propertyType = req.query.type;
    const location = req.query.location;
    const minPrice = req.query.min_price;
    const maxPrice = req.query.max_price;

    // Build the query
    let query = 'SELECT * FROM properties';
    const params = [];

    if (propertyType) {
      query += ' WHERE type = $1';
      params.push(propertyType);
    } else {
      query += ' WHERE';
    }

    if (location) {
      if (params.length > 0) {
        query += ' AND location LIKE $' + (params.length + 1);
      } else {
        query += ' WHERE location LIKE $1';
      }
      params.push('%' + location + '%');
    }

    if (minPrice) {
      if (params.length > 0) {
        query += ' AND price >= $' + (params.length + 1);
      } else {
        query += ' WHERE price >= $1';
      }
      params.push(minPrice);
    }

    if (maxPrice) {
      if (params.length > 0) {
        query += ' AND price <= $' + (params.length + 1);
      } else {
        query += ' WHERE price <= $1';
      }
      params.push(maxPrice);
    }

    // Execute the query and return results
    const result = await pool.query(query, params);
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
});

// Define the main entry point
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
