"""
Generated Code Metadata:
========================
Original URL: https://europarquets.be
Prompt: Generate a RESTful API in Node.js for managing orders and services offered by a company that restores wooden surfaces using aerogommage techniques.
Generated: DETERMINISTIC_13e74512a389b4ff
Batch ID: 20250622_212043
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/aerogommage'; // Update with your MongoDB URI

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define Order schema
const orderSchema = new mongoose.Schema({
    customerName: { type: String, required: true },
    serviceType: { type: String, required: true },
    orderDate: { type: Date, default: Date.now },
    status: { type: String, enum: ['pending', 'completed', 'canceled'], default: 'pending' }
});

// Create Order model
const Order = mongoose.model('Order', orderSchema);

// RESTful API routes

// Create a new order
app.post('/api/orders', async (req, res) => {
    try {
        const order = new Order(req.body);
        await order.save();
        res.status(201).json(order);
    } catch (error) {
        res.status(400).json({ message: 'Error creating order', error });
    }
});

// Get all orders
app.get('/api/orders', async (req, res) => {
    try {
        const orders = await Order.find();
        res.status(200).json(orders);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching orders', error });
    }
});

// Get a specific order by ID
app.get('/api/orders/:id', async (req, res) => {
    try {
        const order = await Order.findById(req.params.id);
        if (!order) {
            return res.status(404).json({ message: 'Order not found' });
        }
        res.status(200).json(order);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching order', error });
    }
});

// Update an order by ID
app.put('/api/orders/:id', async (req, res) => {
    try {
        const order = await Order.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!order) {
            return res.status(404).json({ message: 'Order not found' });
        }
        res.status(200).json(order);
    } catch (error) {
        res.status(400).json({ message: 'Error updating order', error });
    }
});

// Delete an order by ID
app.delete('/api/orders/:id', async (req, res) => {
    try {
        const order = await Order.findByIdAndDelete(req.params.id);
        if (!order) {
            return res.status(404).json({ message: 'Order not found' });
        }
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: 'Error deleting order', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
