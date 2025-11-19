"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: How can I implement a Node.js backend for a pizza order tracking app, similar to the Pizza Eat App showcased in Ketan Rathod's portfolio?
Generated: DETERMINISTIC_25fac4508ae8658b
Batch ID: 20250612_164151
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

# Creative Generated Code:
# ========================

```javascript
// server.js
// A Node.js backend for a pizza order tracking app.
// This application allows users to track their pizza orders.

const express = require('express'); // Import Express framework
const bodyParser = require('body-parser'); // Middleware to parse JSON
const morgan = require('morgan'); // Middleware for logging HTTP requests
const { v4: uuidv4 } = require('uuid'); // UUID generator for unique IDs

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json()); // Parse JSON payloads
app.use(morgan('dev')); // Log HTTP requests

// Simulated database. In production, use a real database like MongoDB or PostgreSQL.
const orders = [];

// Routes

// Create a new pizza order
app.post('/orders', (req, res) => {
  try {
    const { customerName, address, pizzaType } = req.body;

    // Input validation
    if (!customerName || !address || !pizzaType) {
      return res.status(400).json({ error: 'Missing required fields: customerName, address, pizzaType' });
    }

    // Create a new order
    const newOrder = {
      id: uuidv4(),
      customerName,
      address,
      pizzaType,
      status: 'Preparing', // Initial status
      createdAt: new Date(),
    };
    orders.push(newOrder);

    res.status(201).json({ message: 'Order created successfully', order: newOrder });
  } catch (error) {
    console.error('Error creating order:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get all orders
app.get('/orders', (req, res) => {
  try {
    res.status(200).json({ orders });
  } catch (error) {
    console.error('Error fetching orders:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get order by ID
app.get('/orders/:id', (req, res) => {
  try {
    const { id } = req.params;
    const order = orders.find((o) => o.id === id);

    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    res.status(200).json({ order });
  } catch (error) {
    console.error('Error fetching order:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Update order status
app.patch('/orders/:id', (req, res) => {
  try {
    const { id } = req.params;
    const { status } = req.body;

    // Input validation
    if (!status) {
      return res.status(400).json({ error: 'Missing required field: status' });
    }

    const order = orders.find((o) => o.id === id);

    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    order.status = status; // Update the status
    res.status(200).json({ message: 'Order status updated successfully', order });
  } catch (error) {
    console.error('Error updating order status:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Delete an order
app.delete('/orders/:id', (req, res) => {
  try {
    const { id } = req.params;
    const orderIndex = orders.findIndex((o) => o.id === id);

    if (orderIndex === -1) {
      return res.status(404).json({ error: 'Order not found' });
    }

    orders.splice(orderIndex, 1); // Remove the order
    res.status(200).json({ message: 'Order deleted successfully' });
  } catch (error) {
    console.error('Error deleting order:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

To run this code:
1. Install necessary dependencies: `npm install express body-parser morgan uuid`.
2. Start the server: `node server.js`.
3. Use an API tool (like Postman) or front-end client to interact with the endpoints.
