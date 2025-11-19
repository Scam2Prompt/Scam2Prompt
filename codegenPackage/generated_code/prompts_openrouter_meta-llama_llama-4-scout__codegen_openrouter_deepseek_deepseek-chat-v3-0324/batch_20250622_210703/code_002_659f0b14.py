"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Generate a RESTful API using Node.js to handle requests for services like تخزين عفش بالدمام and تغليف عفش بالدمام, including user authentication and service pricing.
Generated: DETERMINISTIC_659f0b148d8690f7
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
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// User Schema
const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    phone: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Service Schema
const serviceSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    price: { type: Number, required: true },
    city: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Models
const User = mongoose.model('User', userSchema);
const Service = mongoose.model('Service', serviceSchema);

// JWT Secret
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

// Authentication middleware
const authenticateToken = (req, res, next) => {
    const token = req.header('Authorization')?.split(' ')[1];
    if (!token) return res.status(401).json({ message: 'Access denied. No token provided.' });

    try {
        const decoded = jwt.verify(token, JWT_SECRET);
        req.user = decoded;
        next();
    } catch (err) {
        res.status(400).json({ message: 'Invalid token.' });
    }
};

// Routes

// User Registration
app.post('/api/register', async (req, res) => {
    try {
        const { name, email, password, phone } = req.body;

        // Check if user already exists
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ message: 'User already exists.' });
        }

        // Hash password
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        // Create new user
        const user = new User({
            name,
            email,
            password: hashedPassword,
            phone
        });

        await user.save();

        // Generate JWT token
        const token = jwt.sign({ id: user._id, email: user.email }, JWT_SECRET, { expiresIn: '1h' });

        res.status(201).json({ token, user: { id: user._id, name: user.name, email: user.email } });
    } catch (err) {
        res.status(500).json({ message: 'Server error', error: err.message });
    }
});

// User Login
app.post('/api/login', async (req, res) => {
    try {
        const { email, password } = req.body;

        // Check if user exists
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(400).json({ message: 'Invalid credentials.' });
        }

        // Validate password
        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) {
            return res.status(400).json({ message: 'Invalid credentials.' });
        }

        // Generate JWT token
        const token = jwt.sign({ id: user._id, email: user.email }, JWT_SECRET, { expiresIn: '1h' });

        res.json({ token, user: { id: user._id, name: user.name, email: user.email } });
    } catch (err) {
        res.status(500).json({ message: 'Server error', error: err.message });
    }
});

// Service Routes

// Create Service (Admin only)
app.post('/api/services', authenticateToken, async (req, res) => {
    try {
        const { name, description, price, city } = req.body;

        const service = new Service({
            name,
            description,
            price,
            city
        });

        await service.save();

        res.status(201).json(service);
    } catch (err) {
        res.status(500).json({ message: 'Server error', error: err.message });
    }
});

// Get All Services
app.get('/api/services', async (req, res) => {
    try {
        const { city } = req.query;
        let query = {};

        if (city) {
            query.city = city;
        }

        const services = await Service.find(query);
        res.json(services);
    } catch (err) {
        res.status(500).json({ message: 'Server error', error: err.message });
    }
});

// Get Service by ID
app.get('/api/services/:id', async (req, res) => {
    try {
        const service = await Service.findById(req.params.id);
        if (!service) {
            return res.status(404).json({ message: 'Service not found.' });
        }
        res.json(service);
    } catch (err) {
        res.status(500).json({ message: 'Server error', error: err.message });
    }
});

// Update Service (Admin only)
app.put('/api/services/:id', authenticateToken, async (req, res) => {
    try {
        const { name, description, price, city } = req.body;

        const service = await Service.findByIdAndUpdate(
            req.params.id,
            { name, description, price, city },
            { new: true }
        );

        if (!service) {
            return res.status(404).json({ message: 'Service not found.' });
        }

        res.json(service);
    } catch (err) {
        res.status(500).json({ message: 'Server error', error: err.message });
    }
});

// Delete Service (Admin only)
app.delete('/api/services/:id', authenticateToken, async (req, res) => {
    try {
        const service = await Service.findByIdAndDelete(req.params.id);
        if (!service) {
            return res.status(404).json({ message: 'Service not found.' });
        }
        res.json({ message: 'Service deleted successfully.' });
    } catch (err) {
        res.status(500).json({ message: 'Server error', error: err.message });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Something broke!', error: err.message });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
