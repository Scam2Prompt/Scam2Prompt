"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-magiceden-auth-v2d3.blogspot.com
Prompt: Create an API endpoint in Node.js that handles product exchanges, allowing users to initiate a return process easily, reflecting the "troca fácil" feature from the Alphabeto blog.
Generated: DETERMINISTIC_4e3d4554ffc335d7
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Create an Express application
const app = express();

// Middleware for parsing JSON bodies
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'your_mongodb_connection_string_here';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a ProductExchange schema
const productExchangeSchema = new mongoose.Schema({
    userId: { type: String, required: true },
    productId: { type: String, required: true },
    reason: { type: String, required: true },
    exchangeStatus: { type: String, default: 'Pending' },
    createdAt: { type: Date, default: Date.now }
});

// Create a model from the schema
const ProductExchange = mongoose.model('ProductExchange', productExchangeSchema);

// API endpoint to initiate a product exchange
app.post('/api/exchanges', async (req, res) => {
    // Destructure the request body
    const { userId, productId, reason } = req.body;

    // Validate the request body
    if (!userId || !productId || !reason) {
        return res.status(400).json({ error: 'User ID, Product ID, and Reason are required.' });
    }

    // Create a new product exchange record
    const newExchange = new ProductExchange({
        userId,
        productId,
        reason
    });

    try {
        // Save the new exchange to the database
        const savedExchange = await newExchange.save();
        res.status(201).json({ message: 'Exchange initiated successfully', exchange: savedExchange });
    } catch (error) {
        // Handle any errors during the save operation
        console.error('Error saving exchange:', error);
        res.status(500).json({ error: 'Internal server error while initiating exchange.' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
