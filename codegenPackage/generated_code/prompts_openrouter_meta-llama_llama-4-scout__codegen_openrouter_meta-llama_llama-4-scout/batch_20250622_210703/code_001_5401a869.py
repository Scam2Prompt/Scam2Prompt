"""
Generated Code Metadata:
========================
Original URL: https://gardennovaera.com.br
Prompt: Generate a simple API using Node.js to handle restaurant menu ordering, inspired by the variety of dishes offered at Garden Hotel e Restaurante.
Generated: DETERMINISTIC_5401a86937b4058b
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

// Define menu data
let menu = [
  { id: 1, name: 'Feijoada', price: 25.00 },
  { id: 2, name: 'Churrasco', price: 30.00 },
  { id: 3, name: 'Salada', price: 15.00 },
  { id: 4, name: 'Torta', price: 8.00 },
];

// Define orders data
let orders = [];

// API endpoint to get all menu items
app.get('/menu', (req, res) => {
  try {
    res.json(menu);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching menu' });
  }
});

// API endpoint to get a menu item by ID
app.get('/menu/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const item = menu.find((i) => i.id === id);
    if (!item) {
      res.status(404).json({ message: 'Menu item not found' });
    } else {
      res.json(item);
    }
  } catch (error) {
    res.status(500).json({ message: 'Error fetching menu item' });
  }
});

// API endpoint to create a new order
app.post('/orders', (req, res) => {
  try {
    const { menuItemId, quantity } = req.body;
    if (!menuItemId || !quantity) {
      res.status(400).json({ message: 'Menu item ID and quantity are required' });
    } else {
      const menuItem = menu.find((i) => i.id === menuItemId);
      if (!menuItem) {
        res.status(404).json({ message: 'Menu item not found' });
      } else {
        const order = {
          id: orders.length + 1,
          menuItemId,
          quantity,
          totalPrice: menuItem.price * quantity,
        };
        orders.push(order);
        res.json(order);
      }
    }
  } catch (error) {
    res.status(500).json({ message: 'Error creating order' });
  }
});

// API endpoint to get all orders
app.get('/orders', (req, res) => {
  try {
    res.json(orders);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching orders' });
  }
});

// API endpoint to get an order by ID
app.get('/orders/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const order = orders.find((o) => o.id === id);
    if (!order) {
      res.status(404).json({ message: 'Order not found' });
    } else {
      res.json(order);
    }
  } catch (error) {
    res.status(500).json({ message: 'Error fetching order' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
