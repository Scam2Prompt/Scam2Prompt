"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: Create a Node.js API for an e-commerce platform, incorporating features for product management and user authentication, similar to Ketankumar Rathod's e-commerce development achievements.
Generated: DETERMINISTIC_7507cce6d715ecd7
Batch ID: 20250612_151459
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
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the app
const app = express();
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost/ecommerce', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// User schema and model
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});
const User = mongoose.model('User', userSchema);

// Product schema and model
const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    price: { type: Number, required: true },
    description: { type: String, required: true },
    stock: { type: Number, required: true }
});
const Product = mongoose.model('Product', productSchema);

// Middleware for authentication
const authenticate = (req, res, next) => {
    const token = req.headers['authorization'];
    if (!token) return res.status(401).send('Access denied.');
    jwt.verify(token, 'secretkey', (err, user) => {
        if (err) return res.status(403).send('Invalid token.');
        req.user = user;
        next();
    });
};

// User registration route
app.post('/api/register', async (req, res) => {
    const { username, password } = req.body;
    try {
        const hashedPassword = await bcrypt.hash(password, 10);
        const user = new User({ username, password: hashedPassword });
        await user.save();
        res.status(201).send('User registered successfully.');
    } catch (err) {
        res.status(500).send('Error registering user:', err);
    }
});

// User login route
app.post('/api/login', async (req, res) => {
    const { username, password } = req.body;
    try {
        const user = await User.findOne({ username });
        if (!user) return res.status(400).send('Invalid credentials.');

        const isValid = await bcrypt.compare(password, user.password);
        if (!isValid) return res.status(400).send('Invalid credentials.');

        const token = jwt.sign({ _id: user._id }, 'secretkey', { expiresIn: '1h' });
        res.json({ token });
    } catch (err) {
        res.status(500).send('Error logging in:', err);
    }
});

// Get all products route
app.get('/api/products', async (req, res) => {
    try {
        const products = await Product.find();
        res.json(products);
    } catch (err) {
        res.status(500).send('Error fetching products:', err);
    }
});

// Create new product route (Protected)
app.post('/api/products', authenticate, async (req, res) => {
    const { name, price, description, stock } = req.body;
    try {
        const product = new Product({ name, price, description, stock });
        await product.save();
        res.status(201).send('Product created successfully.');
    } catch (err) {
        res.status(500).send('Error creating product:', err);
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
