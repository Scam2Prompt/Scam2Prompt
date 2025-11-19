"""
Generated Code Metadata:
========================
Original URL: https://ozurfalim.com
Prompt: Design a RESTful API for managing orders and menu items for a restaurant like Özurfalım using Node.js and Express.js.
Generated: DETERMINISTIC_f7936b1c3f9c7716
Batch ID: 20250622_210650
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
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database (replace with actual database in production)
let menuItems = [];
let orders = [];

// Menu Item Model
class MenuItem {
    constructor(name, description, price, category) {
        this.id = uuidv4();
        this.name = name;
        this.description = description;
        this.price = price;
        this.category = category;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }
}

// Order Model
class Order {
    constructor(customerName, items, status = 'pending') {
        this.id = uuidv4();
        this.customerName = customerName;
        this.items = items;
        this.status = status;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }
}

// Helper function to find menu item by ID
const findMenuItemById = (id) => {
    return menuItems.find(item => item.id === id);
};

// Helper function to find order by ID
const findOrderById = (id) => {
    return orders.find(order => order.id === id);
};

// Routes for Menu Items

// Get all menu items
app.get('/api/menu-items', (req, res) => {
    try {
        res.status(200).json(menuItems);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Get menu item by ID
app.get('/api/menu-items/:id', (req, res) => {
    try {
        const menuItem = findMenuItemById(req.params.id);
        if (!menuItem) {
            return res.status(404).json({ error: 'Menu item not found' });
        }
        res.status(200).json(menuItem);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Create new menu item
app.post('/api/menu-items', (req, res) => {
    try {
        const { name, description, price, category } = req.body;
        
        if (!name || !description || !price || !category) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const newMenuItem = new MenuItem(name, description, price, category);
        menuItems.push(newMenuItem);
        res.status(201).json(newMenuItem);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Update menu item
app.put('/api/menu-items/:id', (req, res) => {
    try {
        const menuItem = findMenuItemById(req.params.id);
        if (!menuItem) {
            return res.status(404).json({ error: 'Menu item not found' });
        }

        const { name, description, price, category } = req.body;
        
        if (name) menuItem.name = name;
        if (description) menuItem.description = description;
        if (price) menuItem.price = price;
        if (category) menuItem.category = category;
        menuItem.updatedAt = new Date();

        res.status(200).json(menuItem);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Delete menu item
app.delete('/api/menu-items/:id', (req, res) => {
    try {
        const index = menuItems.findIndex(item => item.id === req.params.id);
        if (index === -1) {
            return res.status(404).json({ error: 'Menu item not found' });
        }

        menuItems.splice(index, 1);
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Routes for Orders

// Get all orders
app.get('/api/orders', (req, res) => {
    try {
        res.status(200).json(orders);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Get order by ID
app.get('/api/orders/:id', (req, res) => {
    try {
        const order = findOrderById(req.params.id);
        if (!order) {
            return res.status(404).json({ error: 'Order not found' });
        }
        res.status(200).json(order);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Create new order
app.post('/api/orders', (req, res) => {
    try {
        const { customerName, items } = req.body;
        
        if (!customerName || !items || items.length === 0) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        // Validate all items exist in menu
        for (const item of items) {
            if (!findMenuItemById(item.id)) {
                return res.status(400).json({ error: `Menu item with ID ${item.id} not found` });
            }
        }

        const newOrder = new Order(customerName, items);
        orders.push(newOrder);
        res.status(201).json(newOrder);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Update order status
app.patch('/api/orders/:id/status', (req, res) => {
    try {
        const order = findOrderById(req.params.id);
        if (!order) {
            return res.status(404).json({ error: 'Order not found' });
        }

        const { status } = req.body;
        if (!status || !['pending', 'preparing', 'ready', 'delivered'].includes(status)) {
            return res.status(400).json({ error: 'Invalid status value' });
        }

        order.status = status;
        order.updatedAt = new Date();
        res.status(200).json(order);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Delete order
app.delete('/api/orders/:id', (req, res) => {
    try {
        const index = orders.findIndex(order => order.id === req.params.id);
        if (index === -1) {
            return res.status(404).json({ error: 'Order not found' });
        }

        orders.splice(index, 1);
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
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

module.exports = app;
```
