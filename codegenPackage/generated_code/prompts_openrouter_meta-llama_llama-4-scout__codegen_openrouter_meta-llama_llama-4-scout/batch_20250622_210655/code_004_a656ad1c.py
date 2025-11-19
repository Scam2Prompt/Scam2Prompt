"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Create a RESTful API using Node.js to handle customer requests for air conditioning cleaning and maintenance services, inspired by شركة إنجاز's offerings in جدة.
Generated: DETERMINISTIC_a656ad1c2b866a43
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
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/ac_cleaning', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for customers
const customerSchema = new mongoose.Schema({
    name: String,
    email: String,
    phone: String,
    password: String
});

// Define schema for services
const serviceSchema = new mongoose.Schema({
    type: String,
    description: String,
    price: Number
});

// Define schema for requests
const requestSchema = new mongoose.Schema({
    customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'Customer' },
    serviceId: { type: mongoose.Schema.Types.ObjectId, ref: 'Service' },
    status: String
});

// Compile schemas into models
const Customer = mongoose.model('Customer', customerSchema);
const Service = mongoose.model('Service', serviceSchema);
const Request = mongoose.model('Request', requestSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register customer
app.post('/customers', async (req, res) => {
    try {
        const hashedPassword = await bcrypt.hash(req.body.password, 10);
        const customer = new Customer({
            name: req.body.name,
            email: req.body.email,
            phone: req.body.phone,
            password: hashedPassword
        });
        await customer.save();
        res.status(201).send({ message: 'Customer created successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error creating customer', error: err.message });
    }
});

// Login customer
app.post('/login', async (req, res) => {
    try {
        const customer = await Customer.findOne({ email: req.body.email });
        if (!customer) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const isValidPassword = await bcrypt.compare(req.body.password, customer.password);
        if (!isValidPassword) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const token = jwt.sign({ customerId: customer._id }, 'secretkey', { expiresIn: '1h' });
        res.send({ token });
    } catch (err) {
        res.status(400).send({ message: 'Error logging in', error: err.message });
    }
});

// Get all services
app.get('/services', async (req, res) => {
    try {
        const services = await Service.find();
        res.send(services);
    } catch (err) {
        res.status(500).send({ message: 'Error fetching services', error: err.message });
    }
});

// Create service request
app.post('/requests', authenticateToken, async (req, res) => {
    try {
        const request = new Request({
            customerId: req.customerId,
            serviceId: req.body.serviceId,
            status: 'pending'
        });
        await request.save();
        res.status(201).send({ message: 'Request created successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error creating request', error: err.message });
    }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send({ message: 'Access denied' });
    try {
        const decoded = jwt.verify(token, 'secretkey');
        req.customerId = decoded.customerId;
        next();
    } catch (err) {
        res.status(400).send({ message: 'Invalid token', error: err.message });
    }
}

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
