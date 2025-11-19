"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Generate a RESTful API endpoint using Node.js and Express to manage property listings, including creating, reading, updating, and deleting (CRUD) operations, inspired by Presval's property management services.
Generated: DETERMINISTIC_31773f4b1caf4c6b
Batch ID: 20250622_210856
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express app
const app = express();
const PORT = 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// In-memory database for property listings (for demonstration purposes)
let properties = [];

// Utility function to generate unique IDs for properties
const generateId = () => Math.random().toString(36).substr(2, 9);

/**
 * GET /properties
 * Retrieve all property listings.
 */
app.get('/properties', (req, res) => {
  res.status(200).json({
    success: true,
    data: properties,
  });
});

/**
 * POST /properties
 * Create a new property listing.
 */
app.post('/properties', (req, res) => {
  try {
    const { name, location, price } = req.body;

    // Validate request body
    if (!name || !location || !price) {
      return res.status(400).json({
        success: false,
        message: 'Missing required fields: name, location, price',
      });
    }

    const newProperty = {
      id: generateId(),
      name,
      location,
      price,
    };

    properties.push(newProperty);

    res.status(201).json({
      success: true,
      data: newProperty,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while creating the property',
    });
  }
});

/**
 * GET /properties/:id
 * Retrieve a single property listing by ID.
 */
app.get('/properties/:id', (req, res) => {
  const { id } = req.params;
  const property = properties.find((prop) => prop.id === id);

  if (!property) {
    return res.status(404).json({
      success: false,
      message: 'Property not found',
    });
  }

  res.status(200).json({
    success: true,
    data: property,
  });
});

/**
 * PUT /properties/:id
 * Update an existing property listing by ID.
 */
app.put('/properties/:id', (req, res) => {
  const { id } = req.params;
  const { name, location, price } = req.body;

  const propertyIndex = properties.findIndex((prop) => prop.id === id);

  if (propertyIndex === -1) {
    return res.status(404).json({
      success: false,
      message: 'Property not found',
    });
  }

  // Update property details
  properties[propertyIndex] = {
    ...properties[propertyIndex],
    name: name || properties[propertyIndex].name,
    location: location || properties[propertyIndex].location,
    price: price || properties[propertyIndex].price,
  };

  res.status(200).json({
    success: true,
    data: properties[propertyIndex],
  });
});

/**
 * DELETE /properties/:id
 * Delete a property listing by ID.
 */
app.delete('/properties/:id', (req, res) => {
  const { id } = req.params;
  const propertyIndex = properties.findIndex((prop) => prop.id === id);

  if (propertyIndex === -1) {
    return res.status(404).json({
      success: false,
      message: 'Property not found',
    });
  }

  const deletedProperty = properties.splice(propertyIndex, 1);

  res.status(200).json({
    success: true,
    data: deletedProperty[0],
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
