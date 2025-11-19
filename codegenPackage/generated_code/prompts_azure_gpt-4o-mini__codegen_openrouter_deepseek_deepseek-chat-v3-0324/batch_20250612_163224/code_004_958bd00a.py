"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Construct a RESTful API endpoint in Node.js that provides information on tire sales and alignment services, inspired by the offerings of Pneus ML.
Generated: DETERMINISTIC_958bd00af8aca2e6
Batch ID: 20250612_163224
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
const cors = require('cors');

// Initialize Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// In-memory data store (in a production environment, this would be a database)
const tireServices = [
  {
    id: 1,
    name: 'All-Season Tires',
    brand: 'Michelin',
    price: 120.99,
    description: 'High-performance all-season tires for various weather conditions.',
    inStock: true
  },
  {
    id: 2,
    name: 'Winter Tires',
    brand: 'Bridgestone',
    price: 145.50,
    description: 'Specialized tires for winter conditions with excellent traction.',
    inStock: true
  },
  {
    id: 3,
    name: 'Summer Tires',
    brand: 'Goodyear',
    price: 110.75,
    description: 'Optimized for summer driving with superior handling.',
    inStock: false
  }
];

const alignmentServices = [
  {
    id: 1,
    name: 'Standard Wheel Alignment',
    price: 65.00,
    description: 'Basic wheel alignment service for most vehicles.',
    duration: '1 hour'
  },
  {
    id: 2,
    name: 'Premium Wheel Alignment',
    price: 95.00,
    description: 'Comprehensive alignment with detailed inspection.',
    duration: '1.5 hours'
  }
];

// Helper function to find a service by ID
const findServiceById = (collection, id) => {
  return collection.find(service => service.id === parseInt(id));
};

// API Routes

/**
 * @route GET /api/tires
 * @description Get all tire products
 * @returns {Array} List of tire products
 */
app.get('/api/tires', (req, res) => {
  try {
    res.status(200).json(tireServices);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve tire products' });
  }
});

/**
 * @route GET /api/tires/:id
 * @description Get a specific tire product by ID
 * @param {number} id - Tire product ID
 * @returns {Object} Tire product details
 */
app.get('/api/tires/:id', (req, res) => {
  try {
    const tire = findServiceById(tireServices, req.params.id);
    if (!tire) {
      return res.status(404).json({ error: 'Tire product not found' });
    }
    res.status(200).json(tire);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve tire product' });
  }
});

/**
 * @route GET /api/alignments
 * @description Get all alignment services
 * @returns {Array} List of alignment services
 */
app.get('/api/alignments', (req, res) => {
  try {
    res.status(200).json(alignmentServices);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve alignment services' });
  }
});

/**
 * @route GET /api/alignments/:id
 * @description Get a specific alignment service by ID
 * @param {number} id - Alignment service ID
 * @returns {Object} Alignment service details
 */
app.get('/api/alignments/:id', (req, res) => {
  try {
    const alignment = findServiceById(alignmentServices, req.params.id);
    if (!alignment) {
      return res.status(404).json({ error: 'Alignment service not found' });
    }
    res.status(200).json(alignment);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve alignment service' });
  }
});

// 404 handler for undefined routes
app.use((req, res) => {
  res.status(404).json({ error: 'Endpoint not found' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```
