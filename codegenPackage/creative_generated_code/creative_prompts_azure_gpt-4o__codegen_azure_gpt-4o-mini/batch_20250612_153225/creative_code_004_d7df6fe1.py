"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Create a RESTful API endpoint in Node.js to retrieve product details for "Astroworld Wish You Were Here Travis Scott T-shirt," including price, stock availability, and ratings.
Generated: DETERMINISTIC_d7df6fe1d7e2b8a3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Sample product data
const products = [
    {
        id: 1,
        name: "Astroworld Wish You Were Here Travis Scott T-shirt",
        price: 29.99,
        stock: 150,
        ratings: 4.5 // Average rating out of 5
    },
    // Additional products can be added here
];

// API endpoint to retrieve product details
app.get('/api/products/:id', (req, res) => {
    // Extract product ID from request parameters
    const productId = parseInt(req.params.id);

    // Error handling for invalid ID
    if (isNaN(productId)) {
        return res.status(400).json({ error: 'Invalid product ID' });
    }

    // Find the product in the sample data
    const product = products.find(p => p.id === productId);

    // Error handling for product not found
    if (!product) {
        return res.status(404).json({ error: 'Product not found' });
    }

    // Send the product details as a response
    res.status(200).json(product);
});

// Start the server and listen on a specified port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

This code sets up a RESTful API endpoint to retrieve details about the specified product. The endpoint handles errors appropriately and follows best practices for a Node.js application.
