"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "Create a RESTful API using Node.js to handle dumpster rental requests, including customer registration and order management."
Generated: DETERMINISTIC_c8c13155d0bd7ee8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Database connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/dumpster_rentals', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Models
const Customer = mongoose.model('Customer', new mongoose.Schema({
    firstName: { type: String, required: true },
    lastName: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    phone: { type: String, required: true },
    password: { type: String, required: true },
    address: {
        street: { type: String, required: true },
        city: { type: String, required: true },
        state: { type: String, required: true },
        zipCode: { type: String, required: true }
    },
    createdAt: { type: Date, default: Date.now }
}));

const Order = mongoose.model('Order', new mongoose.Schema({
    customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'Customer', required: true },
    dumpsterSize: { type: String, required: true, enum: ['small', 'medium', 'large'] },
    rentalPeriod: { type: Number, required: true, min: 1 },
    deliveryDate: { type: Date, required: true },
    pickupDate: { type: Date, required: true },
    totalPrice: { type: Number, required: true },
    status: { type: String, default: 'pending', enum: ['pending', 'confirmed', 'delivered', 'picked-up', 'cancelled'] },
    createdAt: { type: Date, default: Date.now }
}));

// Authentication middleware
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    
    if (!token) return res.sendStatus(401);

    jwt.verify(token, process.env.JWT_SECRET || 'secret_key', (err, user) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
};

// Routes

// Customer registration
app.post('/api/register', async (req, res) => {
    try {
        const { firstName, lastName, email, phone, password, address } = req.body;
        
        // Validate input
        if (!firstName || !lastName || !email || !phone || !password || !address) {
            return res.status(400).json({ message: 'All fields are required' });
        }

        // Check if customer already exists
        const existingCustomer = await Customer.findOne({ email });
        if (existingCustomer) {
            return res.status(400).json({ message: 'Customer already exists' });
        }

        // Hash password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create new customer
        const customer = new Customer({
            firstName,
            lastName,
            email,
            phone,
            password: hashedPassword,
            address
        });

        await customer.save();

        // Generate JWT token
        const token = jwt.sign(
            { id: customer._id, email: customer.email },
            process.env.JWT_SECRET || 'secret_key',
            { expiresIn: '1h' }
        );

        res.status(201).json({ token });
    } catch (error) {
        console.error('Registration error:', error);
        res.status(500).json({ message: 'Server error' });
    }
});

// Customer login
app.post('/api/login', async (req, res) => {
    try {
        const { email, password } = req.body;

        // Validate input
        if (!email || !password) {
            return res.status(400).json({ message: 'Email and password are required' });
        }

        // Find customer
        const customer = await Customer.findOne({ email });
        if (!customer) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }

        // Check password
        const isMatch = await bcrypt.compare(password, customer.password);
        if (!isMatch) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }

        // Generate JWT token
        const token = jwt.sign(
            { id: customer._id, email: customer.email },
            process.env.JWT_SECRET || 'secret_key',
            { expiresIn: '1h' }
        );

        res.json({ token });
    } catch (error) {
        console.error('Login error:', error);
        res.status(500).json({ message: 'Server error' });
    }
});

// Create order
app.post('/api/orders', authenticateToken, async (req, res) => {
    try {
        const { dumpsterSize, rentalPeriod, deliveryDate, pickupDate, totalPrice } = req.body;

        // Validate input
        if (!dumpsterSize || !rentalPeriod || !deliveryDate || !pickupDate || !totalPrice) {
            return res.status(400).json({ message: 'All fields are required' });
        }

        // Create new order
        const order = new Order({
            customerId: req.user.id,
            dumpsterSize,
            rentalPeriod,
            deliveryDate: new Date(deliveryDate),
            pickupDate: new Date(pickupDate),
            totalPrice
        });

        await order.save();

        res.status(201).json(order);
    } catch (error) {
        console.error('Order creation error:', error);
        res.status(500).json({ message: 'Server error' });
    }
});

// Get customer orders
app.get('/api/orders', authenticateToken, async (req, res) => {
    try {
        const orders = await Order.find({ customerId: req.user.id }).sort({ createdAt: -1 });
        res.json(orders);
    } catch (error) {
        console.error('Orders fetch error:', error);
        res.status(500).json({ message: 'Server error' });
    }
});

// Get single order
app.get('/api/orders/:id', authenticateToken, async (req, res) => {
    try {
        const order = await Order.findOne({ 
            _id: req.params.id, 
            customerId: req.user.id 
        });

        if (!order) {
            return res.status(404).json({ message: 'Order not found' });
        }

        res.json(order);
    } catch (error) {
        console.error('Order fetch error:', error);
        res.status(500).json({ message: 'Server error' });
    }
});

// Update order status
app.patch('/api/orders/:id/status', authenticateToken, async (req, res) => {
    try {
        const { status } = req.body;

        if (!status) {
            return res.status(400).json({ message: 'Status is required' });
        }

        const order = await Order.findOneAndUpdate(
            { _id: req.params.id, customerId: req.user.id },
            { status },
            { new: true }
        );

        if (!order) {
            return res.status(404).json({ message: 'Order not found' });
        }

        res.json(order);
    } catch (error) {
        console.error('Order status update error:', error);
        res.status(500).json({ message: 'Server error' });
    }
});

// Cancel order
app.delete('/api/orders/:id', authenticateToken, async (req, res) => {
    try {
        const order = await Order.findOneAndUpdate(
            { _id: req.params.id, customerId: req.user.id, status: { $in: ['pending', 'confirmed'] } },
            { status: 'cancelled' },
            { new: true }
        );

        if (!order) {
            return res.status(404).json({ message: 'Order not found or cannot be cancelled' });
        }

        res.json({ message: 'Order cancelled successfully' });
    } catch (error) {
        console.error('Order cancellation error:', error);
        res.status(500).json({ message: 'Server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
