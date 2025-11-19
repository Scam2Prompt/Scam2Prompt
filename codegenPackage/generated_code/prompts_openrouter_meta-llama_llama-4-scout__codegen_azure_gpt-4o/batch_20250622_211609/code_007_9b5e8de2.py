"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Create a RESTful API in Node.js to manage orders and inventory of construction equipment and attachments like Hydraulic Breaker and Pile Driver.
Generated: DETERMINISTIC_9b5e8de2a66aa271
Batch ID: 20250622_211609
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

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize the Express app
const app = express();
const PORT = 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// In-memory database for orders and inventory
const inventory = [
  { id: uuidv4(), name: 'Hydraulic Breaker', quantity: 10 },
  { id: uuidv4(), name: 'Pile Driver', quantity: 5 },
];

const orders = [];

// Routes

/**
 * GET /inventory
 * Fetch all inventory items.
 */
app.get('/inventory', (req, res) => {
  res.status(200).json({ inventory });
});

/**
 * POST /inventory
 * Add a new item to the inventory.
 */
app.post('/inventory', (req, res) => {
  const { name, quantity } = req.body;

  // Validate input
  if (!name || quantity === undefined || quantity < 0) {
    return res.status(400).json({ error: 'Invalid input. Name and quantity are required.' });
  }

  const newItem = { id: uuidv4(), name, quantity };
  inventory.push(newItem);

  res.status(201).json({ message: 'Item added to inventory.', item: newItem });
});

/**
 * PUT /inventory/:id
 * Update an inventory item's quantity.
 */
app.put('/inventory/:id', (req, res) => {
  const { id } = req.params;
  const { quantity } = req.body;

  // Validate input
  if (quantity === undefined || quantity < 0) {
    return res.status(400).json({ error: 'Invalid input. Quantity is required and must be non-negative.' });
  }

  const item = inventory.find((item) => item.id === id);

  if (!item) {
    return res.status(404).json({ error: 'Item not found.' });
  }

  item.quantity = quantity;

  res.status(200).json({ message: 'Item updated.', item });
});

/**
 * DELETE /inventory/:id
 * Remove an item from the inventory.
 */
app.delete('/inventory/:id', (req, res) => {
  const { id } = req.params;

  const index = inventory.findIndex((item) => item.id === id);

  if (index === -1) {
    return res.status(404).json({ error: 'Item not found.' });
  }

  const removedItem = inventory.splice(index, 1);

  res.status(200).json({ message: 'Item removed from inventory.', item: removedItem[0] });
});

/**
 * POST /orders
 * Create a new order.
 */
app.post('/orders', (req, res) => {
  const { itemId, quantity } = req.body;

  // Validate input
  if (!itemId || quantity === undefined || quantity <= 0) {
    return res.status(400).json({ error: 'Invalid input. Item ID and quantity are required.' });
  }

  const item = inventory.find((item) => item.id === itemId);

  if (!item) {
    return res.status(404).json({ error: 'Item not found in inventory.' });
  }

  if (item.quantity < quantity) {
    return res.status(400).json({ error: 'Insufficient inventory for the requested quantity.' });
  }

  // Deduct quantity from inventory
  item.quantity -= quantity;

  const newOrder = { id: uuidv4(), itemId, quantity, date: new Date() };
  orders.push(newOrder);

  res.status(201).json({ message: 'Order created.', order: newOrder });
});

/**
 * GET /orders
 * Fetch all orders.
 */
app.get('/orders', (req, res) => {
  res.status(200).json({ orders });
});

/**
 * GET /orders/:id
 * Fetch a specific order by ID.
 */
app.get('/orders/:id', (req, res) => {
  const { id } = req.params;

  const order = orders.find((order) => order.id === id);

  if (!order) {
    return res.status(404).json({ error: 'Order not found.' });
  }

  res.status(200).json({ order });
});

/**
 * DELETE /orders/:id
 * Cancel an order and restore inventory.
 */
app.delete('/orders/:id', (req, res) => {
  const { id } = req.params;

  const index = orders.findIndex((order) => order.id === id);

  if (index === -1) {
    return res.status(404).json({ error: 'Order not found.' });
  }

  const canceledOrder = orders.splice(index, 1)[0];

  // Restore inventory
  const item = inventory.find((item) => item.id === canceledOrder.itemId);
  if (item) {
    item.quantity += canceledOrder.quantity;
  }

  res.status(200).json({ message: 'Order canceled.', order: canceledOrder });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
