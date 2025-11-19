"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Develop a RESTful API endpoint in Node.js for managing orders, similar to the order management system mentioned on ebrasilbrazz.
Generated: DETERMINISTIC_00a1f4c6b57fcd1f
Batch ID: 20250612_161745
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

// Middleware
app.use(bodyParser.json());

// In-memory database for demonstration
let orders = {};

// Helper function to validate order data
const validateOrderData = (orderData) => {
    if (!orderData || 
        !orderData.customerId || 
        !orderData.items || 
        !Array.isArray(orderData.items) || 
        orderData.items.length === 0) {
        return false;
    }
    return true;
};

// Create a new order
app.post('/api/orders', (req, res) => {
    try {
        const orderData = req.body;
        
        if (!validateOrderData(orderData)) {
            return res.status(400).json({ error: 'Invalid order data' });
        }

        const orderId = uuidv4();
        const newOrder = {
            id: orderId,
            ...orderData,
            status: 'pending',
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };

        orders[orderId] = newOrder;
        res.status(201).json(newOrder);
    } catch (error) {
        console.error('Error creating order:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Get all orders
app.get('/api/orders', (req, res) => {
    try {
        res.status(200).json(Object.values(orders));
    } catch (error) {
        console.error('Error fetching orders:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Get a specific order by ID
app.get('/api/orders/:id', (req, res) => {
    try {
        const orderId = req.params.id;
        const order = orders[orderId];

        if (!order) {
            return res.status(404).json({ error: 'Order not found' });
        }

        res.status(200).json(order);
    } catch (error) {
        console.error('Error fetching order:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Update an order
app.put('/api/orders/:id', (req, res) => {
    try {
        const orderId = req.params.id;
        const orderData = req.body;
        
        if (!orders[orderId]) {
            return res.status(404).json({ error: 'Order not found' });
        }

        if (!validateOrderData(orderData)) {
            return res.status(400).json({ error: 'Invalid order data' });
        }

        const updatedOrder = {
            ...orders[orderId],
            ...orderData,
            updatedAt: new Date().toISOString()
        };

        orders[orderId] = updatedOrder;
        res.status(200).json(updatedOrder);
    } catch (error) {
        console.error('Error updating order:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Delete an order
app.delete('/api/orders/:id', (req, res) => {
    try {
        const orderId = req.params.id;
        
        if (!orders[orderId]) {
            return res.status(404).json({ error: 'Order not found' });
        }

        delete orders[orderId];
        res.status(204).send();
    } catch (error) {
        console.error('Error deleting order:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Update order status
app.patch('/api/orders/:id/status', (req, res) => {
    try {
        const orderId = req.params.id;
        const { status } = req.body;
        
        if (!orders[orderId]) {
            return res.status(404).json({ error: 'Order not found' });
        }

        if (!status || !['pending', 'processing', 'shipped', 'delivered', 'cancelled'].includes(status)) {
            return res.status(400).json({ error: 'Invalid status value' });
        }

        orders[orderId].status = status;
        orders[orderId].updatedAt = new Date().toISOString();
        
        res.status(200).json(orders[orderId]);
    } catch (error) {
        console.error('Error updating order status:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Order management API running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
