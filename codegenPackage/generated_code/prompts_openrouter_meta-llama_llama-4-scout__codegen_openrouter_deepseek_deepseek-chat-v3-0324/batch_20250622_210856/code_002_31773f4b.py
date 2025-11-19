"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Generate a RESTful API endpoint using Node.js and Express to manage property listings, including creating, reading, updating, and deleting (CRUD) operations, inspired by Presval's property management services.
Generated: DETERMINISTIC_31773f4b1caf4c6b
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demonstration
let properties = [];

/**
 * Property model:
 * {
 *   id: string,
 *   title: string,
 *   description: string,
 *   location: string,
 *   price: number,
 *   bedrooms: number,
 *   bathrooms: number,
 *   area: number,
 *   amenities: string[],
 *   createdAt: string,
 *   updatedAt: string
 * }
 */

// Helper function to validate property data
const validateProperty = (property) => {
  if (!property.title || typeof property.title !== 'string') {
    return { valid: false, message: 'Title is required and must be a string' };
  }
  if (!property.location || typeof property.location !== 'string') {
    return { valid: false, message: 'Location is required and must be a string' };
  }
  if (!property.price || typeof property.price !== 'number' || property.price <= 0) {
    return { valid: false, message: 'Price is required and must be a positive number' };
  }
  return { valid: true };
};

// Create a new property
app.post('/api/properties', (req, res) => {
  const validation = validateProperty(req.body);
  if (!validation.valid) {
    return res.status(400).json({ error: validation.message });
  }

  const newProperty = {
    id: uuidv4(),
    ...req.body,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString()
  };

  properties.push(newProperty);
  res.status(201).json(newProperty);
});

// Get all properties
app.get('/api/properties', (req, res) => {
  res.json(properties);
});

// Get a single property by ID
app.get('/api/properties/:id', (req, res) => {
  const property = properties.find(p => p.id === req.params.id);
  if (!property) {
    return res.status(404).json({ error: 'Property not found' });
  }
  res.json(property);
});

// Update a property
app.put('/api/properties/:id', (req, res) => {
  const propertyIndex = properties.findIndex(p => p.id === req.params.id);
  if (propertyIndex === -1) {
    return res.status(404).json({ error: 'Property not found' });
  }

  const validation = validateProperty(req.body);
  if (!validation.valid) {
    return res.status(400).json({ error: validation.message });
  }

  const updatedProperty = {
    ...properties[propertyIndex],
    ...req.body,
    updatedAt: new Date().toISOString()
  };

  properties[propertyIndex] = updatedProperty;
  res.json(updatedProperty);
});

// Delete a property
app.delete('/api/properties/:id', (req, res) => {
  const propertyIndex = properties.findIndex(p => p.id === req.params.id);
  if (propertyIndex === -1) {
    return res.status(404).json({ error: 'Property not found' });
  }

  properties.splice(propertyIndex, 1);
  res.status(204).end();
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```
