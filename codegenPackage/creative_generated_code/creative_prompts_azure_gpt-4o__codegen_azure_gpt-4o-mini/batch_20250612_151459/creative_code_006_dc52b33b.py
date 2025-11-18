"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: Write a Node.js application for managing a pizza order system, incorporating real-time tracking and Express.js, as highlighted in Ketankumar Rathod's Pizza Eat App.
Generated: DETERMINISTIC_dc52b33b1c7ddc20
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const http = require('http'); // HTTP module for creating server
const socketIo = require('socket.io'); // Real-time communication library
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const cors = require('cors'); // Middleware for enabling CORS

// Create an instance of the express app
const app = express();
const server = http.createServer(app);
const io = socketIo(server); // Attach Socket.io to the server

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(bodyParser.urlencoded({ extended: true })); // Parse URL-encoded request bodies

// In-memory storage for pizza orders (for demonstration purposes)
let orders = [];

/**
 * Route to create a new pizza order
 */
app.post('/api/orders', (req, res) => {
    const { customerName, pizzaType } = req.body;

    // Basic validation
    if (!customerName || !pizzaType) {
        return res.status(400).json({ error: 'Customer name and pizza type are required.' });
    }

    const newOrder = {
        id: orders.length + 1,
        customerName,
        pizzaType,
        status: 'Ordered'
    };

    orders.push(newOrder); // Store the new order
    io.emit('orderPlaced', newOrder); // Real-time notification for new order

    res.status(201).json(newOrder); // Respond with the created order
});

/**
 * Route to get all orders
 */
app.get('/api/orders', (req, res) => {
    res.status(200).json(orders); // Respond with the orders array
});

/**
 * Route to update the status of an order
 */
app.put('/api/orders/:id', (req, res) => {
    const { id } = req.params;
    const { status } = req.body;

    // Validate order ID and status
    const order = orders.find(o => o.id == id);
    if (!order) {
        return res.status(404).json({ error: 'Order not found.' });
    }
    if (!status) {
        return res.status(400).json({ error: 'Status is required.' });
    }

    order.status = status; // Update the order status
    io.emit('orderUpdated', order); // Notify clients of the status update

    res.status(200).json(order); // Respond with the updated order
});

/**
 * Real-time connection handling
 */
io.on('connection', (socket) => {
    console.log('A user connected:', socket.id);

    socket.on('disconnect', () => {
        console.log('User disconnected:', socket.id);
    });
});

// Set the server to listen on port 3000
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
