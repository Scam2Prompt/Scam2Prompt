"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "Create a RESTful API using Node.js to manage orders for window and door installations, including endpoints for calculating costs and scheduling installations."
Generated: DETERMINISTIC_751ae2dfa94be0b9
Batch ID: 20250622_210703
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
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Define a class for Order
class Order {
  constructor(id, customerName, windowInstallations, doorInstallations, installationDate) {
    this.id = id;
    this.customerName = customerName;
    this.windowInstallations = windowInstallations;
    this.doorInstallations = doorInstallations;
    this.installationDate = installationDate;
  }
}

// In-memory order storage (replace with a database in production)
let orders = [];
let nextOrderId = 1;

// Calculate cost of window installation
function calculateWindowCost(numWindows) {
  const costPerWindow = 500;
  return numWindows * costPerWindow;
}

// Calculate cost of door installation
function calculateDoorCost(numDoors) {
  const costPerDoor = 750;
  return numDoors * costPerDoor;
}

// Calculate total cost of order
function calculateTotalCost(order) {
  const windowCost = calculateWindowCost(order.windowInstallations);
  const doorCost = calculateDoorCost(order.doorInstallations);
  return windowCost + doorCost;
}

// API endpoint to create a new order
app.post('/orders', (req, res) => {
  try {
    const { customerName, windowInstallations, doorInstallations, installationDate } = req.body;
    if (!customerName || !windowInstallations || !doorInstallations || !installationDate) {
      return res.status(400).send({ error: 'Missing required fields' });
    }
    const order = new Order(nextOrderId++, customerName, windowInstallations, doorInstallations, installationDate);
    orders.push(order);
    res.status(201).send({ id: order.id, message: 'Order created successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// API endpoint to get all orders
app.get('/orders', (req, res) => {
  try {
    res.send(orders);
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// API endpoint to get an order by ID
app.get('/orders/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const order = orders.find((o) => o.id === id);
    if (!order) {
      return res.status(404).send({ error: 'Order not found' });
    }
    res.send(order);
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// API endpoint to calculate order cost
app.post('/orders/:id/calculate-cost', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const order = orders.find((o) => o.id === id);
    if (!order) {
      return res.status(404).send({ error: 'Order not found' });
    }
    const totalCost = calculateTotalCost(order);
    res.send({ totalCost });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// API endpoint to schedule an installation
app.patch('/orders/:id/schedule-installation', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const order = orders.find((o) => o.id === id);
    if (!order) {
      return res.status(404).send({ error: 'Order not found' });
    }
    const { installationDate } = req.body;
    if (!installationDate) {
      return res.status(400).send({ error: 'Missing installation date' });
    }
    order.installationDate = installationDate;
    res.send({ message: 'Installation scheduled successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
