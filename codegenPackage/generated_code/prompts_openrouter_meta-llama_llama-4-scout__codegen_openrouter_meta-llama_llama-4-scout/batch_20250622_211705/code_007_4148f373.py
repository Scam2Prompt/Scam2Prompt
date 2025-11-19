"""
Generated Code Metadata:
========================
Original URL: https://receitaslucrativas.digital
Prompt: "Create a simple e-commerce API using Node.js and Express.js to manage sales of luxury crochet products, similar to the ones described in the Receitas Lucrativas course."
Generated: DETERMINISTIC_4148f3738cd8a2b2
Batch ID: 20250622_211705
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
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/luxury-crochet', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for products
const productSchema = new mongoose.Schema({
    name: String,
    description: String,
    price: Number,
    image: String
});

// Define schema for users
const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String
});

// Define schema for orders
const orderSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    productId: { type: mongoose.Schema.Types.ObjectId, ref: 'Product' },
    quantity: Number,
    totalPrice: Number
});

// Compile schemas into models
const Product = mongoose.model('Product', productSchema);
const User = mongoose.model('User', userSchema);
const Order = mongoose.model('Order', orderSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new user
app.post('/register', async (req, res) => {
    try {
        const hashedPassword = await bcrypt.hash(req.body.password, 10);
        const user = new User({
            name: req.body.name,
            email: req.body.email,
            password: hashedPassword
        });
        await user.save();
        res.status(201).send({ message: 'User created successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error creating user', error: err.message });
    }
});

// Login a user
app.post('/login', async (req, res) => {
    try {
        const user = await User.findOne({ email: req.body.email });
        if (!user) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const isValidPassword = await bcrypt.compare(req.body.password, user.password);
        if (!isValidPassword) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
        res.send({ token });
    } catch (err) {
        res.status(400).send({ message: 'Error logging in', error: err.message });
    }
});

// Get all products
app.get('/products', async (req, res) => {
    try {
        const products = await Product.find();
        res.send(products);
    } catch (err) {
        res.status(500).send({ message: 'Error fetching products', error: err.message });
    }
});

// Get a product by ID
app.get('/products/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id);
        if (!product) {
            return res.status(404).send({ message: 'Product not found' });
        }
        res.send(product);
    } catch (err) {
        res.status(400).send({ message: 'Error fetching product', error: err.message });
    }
});

// Create a new order
app.post('/orders', authenticateToken, async (req, res) => {
    try {
        const userId = req.user.userId;
        const product = await Product.findById(req.body.productId);
        if (!product) {
            return res.status(404).send({ message: 'Product not found' });
        }
        const order = new Order({
            userId,
            productId: req.body.productId,
            quantity: req.body.quantity,
            totalPrice: product.price * req.body.quantity
        });
        await order.save();
        res.status(201).send({ message: 'Order created successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error creating order', error: err.message });
    }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send({ message: 'Access denied' });
    try {
        const verified = jwt.verify(token, 'secretkey');
        req.user = verified;
        next();
    } catch (err) {
        res.status(400).send({ message: 'Invalid token', error: err.message });
    }
}

// Start server
app.listen(port, () => console.log(`Server started on port ${port}`));
```
