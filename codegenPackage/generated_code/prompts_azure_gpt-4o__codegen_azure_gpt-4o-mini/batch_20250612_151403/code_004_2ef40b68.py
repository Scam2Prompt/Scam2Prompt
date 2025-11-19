"""
Generated Code Metadata:
========================
Original URL: https://gprobolsa.com
Prompt: Create a REST API endpoint in Node.js that allows businesses to request quotes for eco-friendly promotional products, referencing Grupo ProBolsa's focus on sustainability.
Generated: DETERMINISTIC_2ef40b689f48cff6
Batch ID: 20250612_151403
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
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// Sample data for eco-friendly promotional products
const ecoFriendlyProducts = [
    { id: 1, name: 'Bamboo Pen', price: 1.50, description: 'Eco-friendly bamboo pen' },
    { id: 2, name: 'Recycled Tote Bag', price: 3.00, description: 'Durable tote bag made from recycled materials' },
    { id: 3, name: 'Seed Paper Business Card', price: 0.10, description: 'Business card that can be planted to grow flowers' },
];

// Endpoint to request a quote for eco-friendly promotional products
app.post('/api/quotes', (req, res) => {
    const { productId, quantity } = req.body;

    // Validate request body
    if (!productId || !quantity) {
        return res.status(400).json({ error: 'Product ID and quantity are required.' });
    }

    // Find the requested product
    const product = ecoFriendlyProducts.find(p => p.id === productId);
    if (!product) {
        return res.status(404).json({ error: 'Product not found.' });
    }

    // Calculate total price
    const totalPrice = product.price * quantity;

    // Create quote response
    const quote = {
        product: product.name,
        quantity: quantity,
        totalPrice: totalPrice.toFixed(2),
        message: 'Thank you for your interest in eco-friendly products!'
    };

    // Send the quote response
    return res.status(200).json(quote);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
