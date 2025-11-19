"""
Generated Code Metadata:
========================
Original URL: https://fareadda.com
Prompt: Create a Node.js application to set up a basic e-commerce backend for a domain like FareAdda.com, including user authentication and product management.
Generated: DETERMINISTIC_2f86cf71cd79f67d
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**FareAdda Backend**
======================

### Dependencies

*   `express`: ^4.18.2
*   `mongodb`: ^4.3.1
*   `mongoose`: ^6.5.2
*   `bcrypt`: ^5.0.1
*   `jsonwebtoken`: ^8.5.1

### Installation

```bash
npm install express mongodb mongoose bcrypt jsonwebtoken
```

### Code

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/fareadda', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define user schema
const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String,
    role: { type: String, enum: ['admin', 'customer'], default: 'customer' },
});

// Define product schema
const productSchema = new mongoose.Schema({
    name: String,
    description: String,
    price: Number,
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Product = mongoose.model('Product', productSchema);

// Create express app
const app = express();
app.use(express.json());

// Register user
app.post('/register', async (req, res) => {
    try {
        const { name, email, password } = req.body;
        const hashedPassword = await bcrypt.hash(password, 10);
        const user = new User({ name, email, password: hashedPassword });
        await user.save();
        res.status(201).json({ message: 'User created successfully' });
    } catch (err) {
        res.status(400).json({ message: 'Error creating user', error: err.message });
    }
});

// Login user
app.post('/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(401).json({ message: 'Invalid email or password' });
        }
        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) {
            return res.status(401).json({ message: 'Invalid email or password' });
        }
        const token = jwt.sign({ userId: user._id, role: user.role }, 'secretkey', {
            expiresIn: '1h',
        });
        res.json({ token });
    } catch (err) {
        res.status(400).json({ message: 'Error logging in', error: err.message });
    }
});

// Verify token middleware
const authenticate = async (req, res, next) => {
    try {
        const token = req.header('Authorization').replace('Bearer ', '');
        const decoded = jwt.verify(token, 'secretkey');
        req.user = await User.findById(decoded.userId);
        next();
    } catch (err) {
        res.status(401).json({ message: 'Please authenticate' });
    }
};

// Get all products
app.get('/products', authenticate, async (req, res) => {
    try {
        const products = await Product.find();
        res.json(products);
    } catch (err) {
        res.status(500).json({ message: 'Error fetching products', error: err.message });
    }
});

// Create product (admin only)
app.post('/products', authenticate, async (req, res) => {
    try {
        if (req.user.role !== 'admin') {
            return res.status(403).json({ message: 'Forbidden' });
        }
        const { name, description, price } = req.body;
        const product = new Product({ name, description, price });
        await product.save();
        res.status(201).json({ message: 'Product created successfully' });
    } catch (err) {
        res.status(400).json({ message: 'Error creating product', error: err.message });
    }
});

// Update product (admin only)
app.patch('/products/:id', authenticate, async (req, res) => {
    try {
        if (req.user.role !== 'admin') {
            return res.status(403).json({ message: 'Forbidden' });
        }
        const product = await Product.findByIdAndUpdate(req.params.id, req.body, {
            new: true,
        });
        if (!product) {
            return res.status(404).json({ message: 'Product not found' });
        }
        res.json({ message: 'Product updated successfully' });
    } catch (err) {
        res.status(400).json({ message: 'Error updating product', error: err.message });
    }
});

// Delete product (admin only)
app.delete('/products/:id', authenticate, async (req, res) => {
    try {
        if (req.user.role !== 'admin') {
            return res.status(403).json({ message: 'Forbidden' });
        }
        await Product.findByIdAndRemove(req.params.id);
        res.json({ message: 'Product deleted successfully' });
    } catch (err) {
        res.status(400).json({ message: 'Error deleting product', error: err.message });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
