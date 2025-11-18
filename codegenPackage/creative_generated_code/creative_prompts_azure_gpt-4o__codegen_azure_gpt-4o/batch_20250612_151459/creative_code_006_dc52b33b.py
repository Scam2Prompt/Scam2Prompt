"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: Write a Node.js application for managing a pizza order system, incorporating real-time tracking and Express.js, as highlighted in Ketankumar Rathod's Pizza Eat App.
Generated: DETERMINISTIC_dc52b33b1c7ddc20
Batch ID: 20250612_151459
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
// Import required modules
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

// Initialize Express app and Socket.io
const app = express();
const server = http.createServer(app);
const io = new Server(server);

// Middleware for JSON parsing
app.use(express.json());

// In-memory store for pizza orders (production systems should use a database)
const orders = {};

// Routes for handling pizza orders

/**
 * Place a new order
 * Request Body: { customerName, pizzaType, address }
 */
app.post('/order', (req, res) => {
  try {
    const { customerName, pizzaType, address } = req.body;

    // Validate input
    if (!customerName || !pizzaType || !address) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Generate unique order ID
    const orderId = `order_${Date.now()}`;

    // Create order object
    const order = {
      orderId,
      customerName,
      pizzaType,
      address,
      status: 'Order placed', // Initial status
    };

    // Save order to in-memory store
    orders[orderId] = order;

    // Emit real-time event to notify order placement
    io.emit('orderPlaced', order);

    // Respond to the client
    res.status(201).json({ message: 'Order placed successfully', order });
  } catch (error) {
    console.error('Error placing order:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * Update the status of an order
 * Request Body: { orderId, status }
 */
app.put('/order/status', (req, res) => {
  try {
    const { orderId, status } = req.body;

    // Validate input
    if (!orderId || !status) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Find the order
    const order = orders[orderId];
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    // Update order status
    order.status = status;

    // Emit real-time event to notify status update
    io.emit('orderStatusUpdated', order);

    // Respond to the client
    res.status(200).json({ message: 'Order status updated successfully', order });
  } catch (error) {
    console.error('Error updating order status:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * Get the details of a specific order
 * Route Parameter: orderId
 */
app.get('/order/:orderId', (req, res) => {
  try {
    const { orderId } = req.params;

    // Find the order
    const order = orders[orderId];
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    // Respond with order details
    res.status(200).json(order);
  } catch (error) {
    console.error('Error fetching order:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * Get all orders
 */
app.get('/orders', (req, res) => {
  try {
    // Respond with all orders
    res.status(200).json(Object.values(orders));
  } catch (error) {
    console.error('Error fetching orders:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Socket.io connection handler
io.on('connection', (socket) => {
  console.log('A user connected');

  // Handle disconnection
  socket.on('disconnect', () => {
    console.log('A user disconnected');
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
