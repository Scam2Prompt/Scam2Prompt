"""
Generated Code Metadata:
========================
Original URL: https://therealrathore.in
Prompt: Write a Node.js application for managing a pizza order system, incorporating real-time tracking and Express.js, as highlighted in Ketankumar Rathod's Pizza Eat App.
Generated: DETERMINISTIC_dc52b33b1c7ddc20
Batch ID: 20250612_151459
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
const http = require('http');
const socketIo = require('socket.io');
const bodyParser = require('body-parser');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// In-memory storage for orders
let orders = {};

// Order status constants
const ORDER_STATUS = {
  RECEIVED: 'Order Received',
  PREPARING: 'Preparing',
  BAKING: 'Baking',
  READY: 'Ready for Delivery',
  DELIVERED: 'Delivered'
};

// Routes
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API Endpoints
app.post('/api/orders', (req, res) => {
  try {
    const { customerName, pizzaType, quantity, address } = req.body;
    
    if (!customerName || !pizzaType || !quantity || !address) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const orderId = uuidv4();
    const order = {
      id: orderId,
      customerName,
      pizzaType,
      quantity,
      address,
      status: ORDER_STATUS.RECEIVED,
      createdAt: new Date()
    };

    orders[orderId] = order;
    
    // Emit new order to all connected clients
    io.emit('newOrder', order);
    
    res.status(201).json(order);
  } catch (error) {
    console.error('Error creating order:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/orders', (req, res) => {
  try {
    res.json(Object.values(orders));
  } catch (error) {
    console.error('Error fetching orders:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/orders/:id', (req, res) => {
  try {
    const order = orders[req.params.id];
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }
    res.json(order);
  } catch (error) {
    console.error('Error fetching order:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.put('/api/orders/:id/status', (req, res) => {
  try {
    const { status } = req.body;
    const order = orders[req.params.id];
    
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }

    if (!Object.values(ORDER_STATUS).includes(status)) {
      return res.status(400).json({ error: 'Invalid status' });
    }

    order.status = status;
    order.updatedAt = new Date();
    
    // Emit status update to all connected clients
    io.emit('statusUpdate', order);
    
    res.json(order);
  } catch (error) {
    console.error('Error updating order status:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Socket.io connection handler
io.on('connection', (socket) => {
  console.log('New client connected');
  
  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

```html
<!-- public/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pizza Order System</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f5f5f5;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .section {
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1, h2 {
      color: #e74c3c;
    }
    form {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, select {
      width: 100%;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    button {
      background-color: #e74c3c;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
      grid-column: span 2;
    }
    button:hover {
      background-color: #c0392b;
    }
    .order-list {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 15px;
    }
    .order-card {
      border: 1px solid #ddd;
      padding: 15px;
      border-radius: 8px;
      background: white;
    }
    .status {
      padding: 5px 10px;
      border-radius: 4px;
      color: white;
      font-weight: bold;
      display: inline-block;
      margin-top: 10px;
    }
    .status-received { background-color: #3498db; }
    .status-preparing { background-color: #f39c12; }
    .status-baking { background-color: #e67e22; }
    .status-ready { background-color: #2ecc71; }
    .status-delivered { background-color: #27ae60; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Pizza Order System</h1>
    
    <div class="section">
      <h2>Place New Order</h2>
      <form id="orderForm">
        <div>
          <label for="customerName">Customer Name</label>
          <input type="text" id="customerName" required>
        </div>
        <div>
          <label for="pizzaType">Pizza Type</label>
          <select id="pizzaType" required>
            <option value="">Select a pizza</option>
            <option value="Margherita">Margherita</option>
            <option value="Pepperoni">Pepperoni</option>
            <option value="Vegetarian">Vegetarian</option>
            <option value="Hawaiian">Hawaiian</option>
          </select>
        </div>
        <div>
          <label for="quantity">Quantity</label>
          <input type="number" id="quantity" min="1" value="1" required>
        </div>
        <div>
          <label for="address">Delivery Address</label>
          <input type="text" id="address" required>
        </div>
        <button type="submit">Place Order</button>
      </form>
    </div>
    
    <div class="section">
      <h2>Order Status Dashboard</h2>
      <div class="order-list" id="orderList"></div>
    </div>
  </div>

  <script src="/socket.io/socket.io.js"></script>
  <script>
    const socket = io();
    const orderForm = document.getElementById('orderForm');
    const orderList = document.getElementById('orderList');
    
    // Handle form submission
    orderForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const order = {
        customerName: document.getElementById('customerName').value,
        pizzaType: document.getElementById('pizzaType').value,
        quantity: parseInt(document.getElementById('quantity').value),
        address: document.getElementById('address').value
      };
      
      try {
        const response = await fetch('/api/orders', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(order)
        });
        
        if (response.ok) {
          orderForm.reset();
        } else {
          alert('Failed
