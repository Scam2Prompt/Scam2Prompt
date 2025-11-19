"""
Generated Code Metadata:
========================
Original URL: https://pollossukaoalcarbon.com
Prompt: "Generate a RESTful API endpoint in Node.js to handle CRUD operations for menu items, including creating, reading, updating, and deleting items on a restaurant's menu."
Generated: DETERMINISTIC_7ffe300761da37a4
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB (replace 'your_connection_string' with your actual connection string)
mongoose.connect('your_connection_string', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for menu items
const menuItemSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    price: { type: Number, required: true },
    available: { type: Boolean, default: true }
});

// Create a Mongoose model for menu items
const MenuItem = mongoose.model('MenuItem', menuItemSchema);

// CRUD Operations

// Create a new menu item
app.post('/api/menu-items', async (req, res) => {
    try {
        const newItem = new MenuItem(req.body);
        const savedItem = await newItem.save();
        res.status(201).json(savedItem);
    } catch (error) {
        res.status(400).json({ message: 'Error creating menu item', error });
    }
});

// Read all menu items
app.get('/api/menu-items', async (req, res) => {
    try {
        const items = await MenuItem.find();
        res.status(200).json(items);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving menu items', error });
    }
});

// Read a single menu item by ID
app.get('/api/menu-items/:id', async (req, res) => {
    try {
        const item = await MenuItem.findById(req.params.id);
        if (!item) {
            return res.status(404).json({ message: 'Menu item not found' });
        }
        res.status(200).json(item);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving menu item', error });
    }
});

// Update a menu item by ID
app.put('/api/menu-items/:id', async (req, res) => {
    try {
        const updatedItem = await MenuItem.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedItem) {
            return res.status(404).json({ message: 'Menu item not found' });
        }
        res.status(200).json(updatedItem);
    } catch (error) {
        res.status(400).json({ message: 'Error updating menu item', error });
    }
});

// Delete a menu item by ID
app.delete('/api/menu-items/:id', async (req, res) => {
    try {
        const deletedItem = await MenuItem.findByIdAndDelete(req.params.id);
        if (!deletedItem) {
            return res.status(404).json({ message: 'Menu item not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        res.status(500).json({ message: 'Error deleting menu item', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
