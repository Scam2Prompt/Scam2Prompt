"""
Generated Code Metadata:
========================
Original URL: https://wenwendrop.com
Prompt: "Generate a simple e-commerce delivery system API using Node.js, including endpoints for listing available fruits, delivery areas, and calculating shipping costs based on the provided zip codes."
Generated: DETERMINISTIC_523468154852457d
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Sample data
const fruits = [
    { id: 1, name: 'Apple', price: 1.50 },
    { id: 2, name: 'Banana', price: 0.75 },
    { id: 3, name: 'Orange', price: 1.25 },
    { id: 4, name: 'Mango', price: 2.50 },
    { id: 5, name: 'Pineapple', price: 3.00 }
];

const deliveryAreas = {
    '10001': { name: 'Manhattan', shippingCost: 5.00 },
    '90001': { name: 'Los Angeles', shippingCost: 7.50 },
    '60601': { name: 'Chicago', shippingCost: 6.00 },
    '77001': { name: 'Houston', shippingCost: 8.00 },
    '85001': { name: 'Phoenix', shippingCost: 7.00 }
};

// Helper function to validate zip code
const isValidZipCode = (zipCode) => {
    return deliveryAreas.hasOwnProperty(zipCode);
};

// Routes
/**
 * @api {get} /fruits List all available fruits
 * @apiName GetFruits
 * @apiGroup Fruits
 */
app.get('/fruits', (req, res) => {
    try {
        res.status(200).json(fruits);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * @api {get} /delivery-areas List all delivery areas
 * @apiName GetDeliveryAreas
 * @apiGroup Delivery
 */
app.get('/delivery-areas', (req, res) => {
    try {
        res.status(200).json(deliveryAreas);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * @api {post} /calculate-shipping Calculate shipping cost
 * @apiName CalculateShipping
 * @apiGroup Delivery
 * @apiParam {String} zipCode Customer's zip code
 */
app.post('/calculate-shipping', (req, res) => {
    try {
        const { zipCode } = req.body;

        if (!zipCode) {
            return res.status(400).json({ error: 'Zip code is required' });
        }

        if (!isValidZipCode(zipCode)) {
            return res.status(400).json({ error: 'Delivery not available for this zip code' });
        }

        const shippingCost = deliveryAreas[zipCode].shippingCost;
        res.status(200).json({ shippingCost });
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'OK' });
});

// 404 handler
app.use((req, res) => {
    res.status(404).json({ error: 'Endpoint not found' });
});

// Error handler
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
