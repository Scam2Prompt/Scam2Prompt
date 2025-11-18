"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitechcareindia.com
Prompt: Write a Node.js and MongoDB web application for e-commerce development, referencing the services offered by DigiTech Care India.
Generated: DETERMINISTIC_ea79f86ca86bba75
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework
const mongoose = require('mongoose'); // MongoDB ODM
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

// Initialize Express app
const app = express();

// Middleware
app.use(bodyParser.json()); // Parse JSON payloads from incoming requests

// MongoDB connection string (replace with your own connection string)
const mongoURI = 'mongodb://localhost:27017/digitechcareindia'; // Update with production-grade URI if deploying
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas and models
// User schema and model
const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
});

const User = mongoose.model('User', userSchema);

// Product schema and model
const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    price: { type: Number, required: true },
    stock: { type: Number, required: true },
});

const Product = mongoose.model('Product', productSchema);

// Order schema and model
const orderSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    products: [
        {
            productId: { type: mongoose.Schema.Types.ObjectId, ref: 'Product', required: true },
            quantity: { type: Number, required: true },
        },
    ],
    totalAmount: { type: Number, required: true },
    status: { type: String, enum: ['Pending', 'Shipped', 'Delivered'], default: 'Pending' },
});

const Order = mongoose.model('Order', orderSchema);

// Routes
// Health check route
app.get('/api/health', (req, res) => {
    res.json({ status: 'OK', message: 'DigiTech Care India API is running.' });
});

// Register a new user
app.post('/api/users/register', async (req, res) => {
    try {
        const { name, email, password } = req.body;
        const user = new User({ name, email, password }); // Password should be hashed in real applications
        await user.save();
        res.status(201).json({ message: 'User registered successfully', user });
    } catch (err) {
        res.status(400).json({ error: 'Unable to register user', details: err.message });
    }
});

// Add a new product
app.post('/api/products', async (req, res) => {
    try {
        const { name, description, price, stock } = req.body;
        const product = new Product({ name, description, price, stock });
        await product.save();
        res.status(201).json({ message: 'Product added successfully', product });
    } catch (err) {
        res.status(400).json({ error: 'Unable to add product', details: err.message });
    }
});

// Create an order
app.post('/api/orders', async (req, res) => {
    try {
        const { userId, products } = req.body;

        // Calculate total amount
        let totalAmount = 0;
        for (const productInfo of products) {
            const product = await Product.findById(productInfo.productId);
            if (!product) {
                return res.status(404).json({ error: `Product with ID ${productInfo.productId} not found.` });
            }
            totalAmount += product.price * productInfo.quantity;
        }

        const order = new Order({ userId, products, totalAmount });
        await order.save();
        res.status(201).json({ message: 'Order created successfully', order });
    } catch (err) {
        res.status(400).json({ error: 'Unable to create order', details: err.message });
    }
});

// List all products
app.get('/api/products', async (req, res) => {
    try {
        const products = await Product.find();
        res.json(products);
    } catch (err) {
        res.status(500).json({ error: 'Unable to fetch products', details: err.message });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Internal Server Error' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
