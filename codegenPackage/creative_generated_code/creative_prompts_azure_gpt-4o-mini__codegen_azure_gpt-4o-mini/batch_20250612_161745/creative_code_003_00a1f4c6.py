"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Develop a RESTful API endpoint in Node.js for managing orders, similar to the order management system mentioned on ebrasilbrazz.
Generated: DETERMINISTIC_00a1f4c6b57fcd1f
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Create an instance of express
const app = express();

// Middleware for parsing application/json
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/order_management', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected...'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for orders
const orderSchema = new mongoose.Schema({
    customerId: { type: String, required: true },
    items: [{ 
        productId: String, 
        quantity: { type: Number, required: true } 
    }],
    totalAmount: { type: Number, required: true },
    status: { type: String, default: 'pending' }
});

// Create a model for orders
const Order = mongoose.model('Order', orderSchema);

// Create a new order
app.post('/api/orders', async (req, res) => {
    try {
        const { customerId, items, totalAmount } = req.body;
        const newOrder = new Order({ customerId, items, totalAmount });
        const savedOrder = await newOrder.save();
        res.status(201).json(savedOrder);
    } catch (error) {
        res.status(500).json({ message: 'Error creating order', error: error.message });
    }
});

// Get all orders
app.get('/api/orders', async (req, res) => {
    try {
        const orders = await Order.find();
        res.status(200).json(orders);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching orders', error: error.message });
    }
});

// Get an order by ID
app.get('/api/orders/:id', async (req, res) => {
    const { id } = req.params;
    try {
        const order = await Order.findById(id);
        if (!order) {
            return res.status(404).json({ message: 'Order not found' });
        }
        res.status(200).json(order);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching order', error: error.message });
    }
});

// Update an order by ID
app.put('/api/orders/:id', async (req, res) => {
    const { id } = req.params;
    try {
        const updatedOrder = await Order.findByIdAndUpdate(id, req.body, { new: true });
        if (!updatedOrder) {
            return res.status(404).json({ message: 'Order not found' });
        }
        res.status(200).json(updatedOrder);
    } catch (error) {
        res.status(500).json({ message: 'Error updating order', error: error.message });
    }
});

// Delete an order by ID
app.delete('/api/orders/:id', async (req, res) => {
    const { id } = req.params;
    try {
        const deletedOrder = await Order.findByIdAndDelete(id);
        if (!deletedOrder) {
            return res.status(404).json({ message: 'Order not found' });
        }
        res.status(204).send(); // No content to return
    } catch (error) {
        res.status(500).json({ message: 'Error deleting order', error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
