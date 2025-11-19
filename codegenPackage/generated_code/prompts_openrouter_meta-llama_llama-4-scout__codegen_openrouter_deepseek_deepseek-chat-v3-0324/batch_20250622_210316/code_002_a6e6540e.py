"""
Generated Code Metadata:
========================
Original URL: https://activesport.cz
Prompt: "Generate a RESTful API endpoint in Node.js to manage orders for an outdoor equipment store, considering the product categories available on activesport.cz."
Generated: DETERMINISTIC_a6e6540efb2ba0ab
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
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demonstration
let orders = [];
const productCategories = [
  'cycling',
  'running',
  'hiking',
  'winter-sports',
  'water-sports',
  'fitness',
  'outdoor',
  'climbing'
];

// Validate order data
const validateOrder = (order) => {
  if (!order.customerName || typeof order.customerName !== 'string') {
    throw new Error('Invalid customer name');
  }
  if (!order.items || !Array.isArray(order.items) || order.items.length === 0) {
    throw new Error('Order must contain at least one item');
  }
  
  for (const item of order.items) {
    if (!item.productId || typeof item.productId !== 'string') {
      throw new Error('Invalid product ID');
    }
    if (!item.quantity || typeof item.quantity !== 'number' || item.quantity <= 0) {
      throw new Error('Invalid quantity');
    }
    if (!item.category || !productCategories.includes(item.category)) {
      throw new Error('Invalid product category');
    }
  }
};

// Create a new order
app.post('/api/orders', (req, res) => {
  try {
    const order = req.body;
    validateOrder(order);
    
    const newOrder = {
      id: uuidv4(),
      ...order,
      createdAt: new Date().toISOString(),
      status: 'pending'
    };
    
    orders.push(newOrder);
    res.status(201).json(newOrder);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Get all orders
app.get('/api/orders', (req, res) => {
  try {
    res.status(200).json(orders);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve orders' });
  }
});

// Get order by ID
app.get('/api/orders/:id', (req, res) => {
  try {
    const order = orders.find(o => o.id === req.params.id);
    if (!order) {
      return res.status(404).json({ error: 'Order not found' });
    }
    res.status(200).json(order);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve order' });
  }
});

// Update order status
app.patch('/api/orders/:id/status', (req, res) => {
  try {
    const { status } = req.body;
    const validStatuses = ['pending', 'processing', 'shipped', 'delivered', 'cancelled'];
    
    if (!validStatuses.includes(status)) {
      return res.status(400).json({ error: 'Invalid status' });
    }
    
    const orderIndex = orders.findIndex(o => o.id === req.params.id);
    if (orderIndex === -1) {
      return res.status(404).json({ error: 'Order not found' });
    }
    
    orders[orderIndex].status = status;
    res.status(200).json(orders[orderIndex]);
  } catch (error) {
    res.status(500).json({ error: 'Failed to update order status' });
  }
});

// Delete an order
app.delete('/api/orders/:id', (req, res) => {
  try {
    const orderIndex = orders.findIndex(o => o.id === req.params.id);
    if (orderIndex === -1) {
      return res.status(404).json({ error: 'Order not found' });
    }
    
    orders = orders.filter(o => o.id !== req.params.id);
    res.status(204).send();
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete order' });
  }
});

// Get orders by category
app.get('/api/orders/category/:category', (req, res) => {
  try {
    const category = req.params.category;
    if (!productCategories.includes(category)) {
      return res.status(400).json({ error: 'Invalid category' });
    }
    
    const filteredOrders = orders.filter(order => 
      order.items.some(item => item.category === category)
    );
    
    res.status(200).json(filteredOrders);
  } catch (error) {
    res.status(500).json({ error: 'Failed to filter orders by category' });
  }
});

// Error handling middleware
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
