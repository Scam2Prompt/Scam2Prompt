"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: "Create a RESTful API in Node.js to manage orders of refractory products, including endpoints for creating, reading, updating, and deleting orders, and provide a sample API request."
Generated: DETERMINISTIC_265ce04edc90857d
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// In-memory database for demonstration
let orders = {};

/**
 * Order Model
 * @typedef {Object} Order
 * @property {string} id - Unique identifier
 * @property {string} customerName - Name of the customer
 * @property {Array<Object>} products - List of products
 * @property {string} status - Order status
 * @property {string} createdAt - Creation timestamp
 * @property {string} updatedAt - Last update timestamp
 */

// Helper function to validate order data
const validateOrderData = (orderData) => {
    if (!orderData.customerName || typeof orderData.customerName !== 'string') {
        throw new Error('Invalid customer name');
    }
    if (!orderData.products || !Array.isArray(orderData.products) || orderData.products.length === 0) {
        throw new Error('Invalid products list');
    }
    return true;
};

// Create a new order
app.post('/api/orders', (req, res) => {
    try {
        const orderData = req.body;
        validateOrderData(orderData);

        const orderId = uuidv4();
        const timestamp = new Date().toISOString();

        const newOrder = {
            id: orderId,
            customerName: orderData.customerName,
            products: orderData.products,
            status: 'pending',
            createdAt: timestamp,
            updatedAt: timestamp
        };

        orders[orderId] = newOrder;
        res.status(201).json(newOrder);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Get all orders
app.get('/api/orders', (req, res) => {
    res.status(200).json(Object.values(orders));
});

// Get a specific order
app.get('/api/orders/:id', (req, res) => {
    const orderId = req.params.id;
    const order = orders[orderId];

    if (!order) {
        return res.status(404).json({ error: 'Order not found' });
    }

    res.status(200).json(order);
});

// Update an order
app.put('/api/orders/:id', (req, res) => {
    try {
        const orderId = req.params.id;
        const order = orders[orderId];

        if (!order) {
            return res.status(404).json({ error: 'Order not found' });
        }

        const orderData = req.body;
        validateOrderData(orderData);

        const updatedOrder = {
            ...order,
            customerName: orderData.customerName,
            products: orderData.products,
            status: orderData.status || order.status,
            updatedAt: new Date().toISOString()
        };

        orders[orderId] = updatedOrder;
        res.status(200).json(updatedOrder);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Delete an order
app.delete('/api/orders/:id', (req, res) => {
    const orderId = req.params.id;
    const order = orders[orderId];

    if (!order) {
        return res.status(404).json({ error: 'Order not found' });
    }

    delete orders[orderId];
    res.status(204).send();
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

// Sample API request:
/*
POST /api/orders
Content-Type: application/json

{
    "customerName": "John Doe",
    "products": [
        {
            "productId": "ref-001",
            "name": "High Alumina Brick",
            "quantity": 100,
            "unitPrice": 5.50
        },
        {
            "productId": "ref-002",
            "name": "Fire Clay Brick",
            "quantity": 200,
            "unitPrice": 3.20
        }
    ]
}
*/
```
