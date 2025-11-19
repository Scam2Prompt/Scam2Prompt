"""
Generated Code Metadata:
========================
Original URL: https://mambowood.ir
Prompt: Generate a RESTful API endpoint in Node.js to manage orders and payments for an online store selling wooden decorative items, with a focus on security and scalability.
Generated: DETERMINISTIC_a684122f4278fadb
Batch ID: 20250622_210655
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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware for security and parsing
app.use(helmet());
app.use(cors());
app.use(bodyParser.json());

// Rate limiting to prevent abuse
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100 // Limit each IP to 100 requests per windowMs
});
app.use(limiter);

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/wooden_store', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('MongoDB connected');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// Order schema definition
const orderSchema = new mongoose.Schema({
    customerName: { type: String, required: true },
    items: [{ 
        itemId: { type: mongoose.Schema.Types.ObjectId, required: true },
        quantity: { type: Number, required: true }
    }],
    totalAmount: { type: Number, required: true },
    paymentStatus: { type: String, enum: ['Pending', 'Completed', 'Failed'], default: 'Pending' },
    createdAt: { type: Date, default: Date.now }
});

// Order model
const Order = mongoose.model('Order', orderSchema);

// Create a new order
app.post('/api/orders', async (req, res) => {
    try {
        const { customerName, items, totalAmount } = req.body;

        // Validate request body
        if (!customerName || !items || !totalAmount) {
            return res.status(400).json({ message: 'Invalid order data' });
        }

        const newOrder = new Order({ customerName, items, totalAmount });
        await newOrder.save();
        res.status(201).json(newOrder);
    } catch (error) {
        console.error('Error creating order:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Get all orders
app.get('/api/orders', async (req, res) => {
    try {
        const orders = await Order.find();
        res.status(200).json(orders);
    } catch (error) {
        console.error('Error fetching orders:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Update payment status of an order
app.patch('/api/orders/:id/payment', async (req, res) => {
    try {
        const { id } = req.params;
        const { paymentStatus } = req.body;

        // Validate request body
        if (!paymentStatus || !['Pending', 'Completed', 'Failed'].includes(paymentStatus)) {
            return res.status(400).json({ message: 'Invalid payment status' });
        }

        const updatedOrder = await Order.findByIdAndUpdate(id, { paymentStatus }, { new: true });
        if (!updatedOrder) {
            return res.status(404).json({ message: 'Order not found' });
        }

        res.status(200).json(updatedOrder);
    } catch (error) {
        console.error('Error updating payment status:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
