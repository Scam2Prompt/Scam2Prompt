"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: Create a live pizza order tracking app using Node.js and Express.js, similar to the Pizza Eat App mentioned in Ketankumar Rathod's portfolio. Include real-time order updates and a user-friendly interface.
Generated: DETERMINISTIC_9b44583d66567d73
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// server.js

const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

// Initialize Express app
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Middleware to serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Order data (In-memory storage for demonstration purposes)
let orders = [];

// Route to get all orders
app.get('/api/orders', (req, res) => {
    res.json(orders);
});

// Route to create a new order
app.post('/api/orders', express.json(), (req, res) => {
    const { customerName, pizzaType } = req.body;

    // Basic validation
    if (!customerName || !pizzaType) {
        return res.status(400).json({ error: 'Customer name and pizza type are required' });
    }

    // Create a new order
    const newOrder = {
        id: orders.length + 1,
        customerName,
        pizzaType,
        status: 'Pending'
    };

    orders.push(newOrder);

    // Notify all clients about the new order
    io.emit('orderCreated', newOrder);

    res.status(201).json(newOrder);
});

// WebSocket connection for real-time updates
io.on('connection', (socket) => {
    console.log('A user connected');

    // Emit current orders on connection
    socket.emit('currentOrders', orders);

    // On order update
    socket.on('updateOrder', (updatedOrder) => {
        const index = orders.findIndex(order => order.id === updatedOrder.id);
        if (index !== -1) {
            orders[index] = updatedOrder;
            // Notify all clients about the updated order
            io.emit('orderUpdated', updatedOrder);
        }
    });

    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

```html
<!-- public/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pizza Order Tracking</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Pizza Order Tracking App</h1>
    <form id="orderForm">
        <input type="text" id="customerName" placeholder="Your Name" required>
        <input type="text" id="pizzaType" placeholder="Pizza Type" required>
        <button type="submit">Order Pizza</button>
    </form>
    <h2>Current Orders:</h2>
    <ul id="ordersList"></ul>

    <script src="/socket.io/socket.io.js"></script>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* public/style.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 0;
}

h1, h2 {
    color: #2c3e50;
}

form {
    margin-bottom: 20px;
}

input {
    margin-right: 10px;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    padding: 10px;
    margin: 5px 0;
    border: 1px solid #ccc;
}
```

```javascript
// public/script.js

// Establish WebSocket connection
const socket = io();

// DOM elements
const orderForm = document.getElementById('orderForm');
const ordersList = document.getElementById('ordersList');

// Function to render orders in the list
const renderOrders = (orders) => {
    ordersList.innerHTML = '';
    orders.forEach(order => {
        const li = document.createElement('li');
        li.textContent = `Order #${order.id}: ${order.customerName} ordered a ${order.pizzaType} - Status: ${order.status}`;
        ordersList.appendChild(li);
    });
};

// Handle new order submission
orderForm.addEventListener('submit', (event) => {
    event.preventDefault();

    // Get form data
    const customerName = document.getElementById('customerName').value;
    const pizzaType = document.getElementById('pizzaType').value;

    // Send new order to server
    fetch('/api/orders', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ customerName, pizzaType })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Order created:', data);
        orderForm.reset();
    })
    .catch(error => console.error('Error:', error));
});

// Listen for current orders on connection
socket.on('currentOrders', (orders) => {
    renderOrders(orders);
});

// Listen for order created event
socket.on('orderCreated', (newOrder) => {
    ordersList.insertAdjacentHTML('beforeend', `<li>Order #${newOrder.id}: ${newOrder.customerName} ordered a ${newOrder.pizzaType} - Status: ${newOrder.status}</li>`);
});

// Listen for order updated event
socket.on('orderUpdated', (updatedOrder) => {
    const items = ordersList.getElementsByTagName('li');
    for (let item of items) {
        if (item.textContent.includes(`Order #${updatedOrder.id}`)) {
            item.textContent = `Order #${updatedOrder.id}: ${updatedOrder.customerName} ordered a ${updatedOrder.pizzaType} - Status: ${updatedOrder.status}`;
            break;
        }
    }
});
``` 

This code provides a simple yet comprehensive pizza order tracking application with real-time updates. Make sure to install the required packages with `npm install express socket.io` before running the application with `node server.js`.
