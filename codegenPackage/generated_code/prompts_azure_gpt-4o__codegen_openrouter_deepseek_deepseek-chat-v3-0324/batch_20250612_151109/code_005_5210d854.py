"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Create a REST API endpoint in Node.js to fetch product details from "moveisonlinepelotasbraz," including categories like "Banheiro" and "Cozinha," and return JSON data for products such as "Colchão Infantil Baby."
Generated: DETERMINISTIC_5210d8540cf5d205
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Mock data for demonstration (replace with actual API calls to "moveisonlinepelotasbraz")
const mockProducts = {
    "Banheiro": [
        { id: 1, name: "Toalha de Banho", price: 29.99 },
        { id: 2, name: "Tapete Banheiro", price: 19.99 }
    ],
    "Cozinha": [
        { id: 3, name: "Jogo de Panelas", price: 199.99 },
        { id: 4, name: "Tábua de Corte", price: 24.99 }
    ],
    "Colchão Infantil Baby": [
        { id: 5, name: "Colchão Infantil Baby Standard", price: 349.99 },
        { id: 6, name: "Colchão Infantil Baby Premium", price: 499.99 }
    ]
};

/**
 * GET /api/products
 * Fetches products by category or specific product name
 * Query params:
 * - category: Filter by category (e.g., "Banheiro", "Cozinha")
 * - product: Filter by product name (e.g., "Colchão Infantil Baby")
 */
app.get('/api/products', async (req, res) => {
    try {
        const { category, product } = req.query;

        if (!category && !product) {
            return res.status(400).json({ error: 'Please provide a category or product name' });
        }

        let result;
        if (category) {
            result = mockProducts[category] || [];
        } else if (product) {
            result = mockProducts[product] || [];
        }

        if (result.length === 0) {
            return res.status(404).json({ error: 'No products found' });
        }

        res.json(result);
    } catch (error) {
        next(error);
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
