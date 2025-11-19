"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saldiana.com.br
Prompt: Create a RESTful API endpoint in Node.js that allows users to query the Sal Diana product offerings specifically for the food and textile industries.
Generated: DETERMINISTIC_00041e5b2e82891e
Batch ID: 20250612_162051
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
const bodyParser = require('body-parser');
const cors = require('cors');

// Create an instance of an Express application
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());
app.use(cors());

// Sample data representing Sal Diana product offerings
const products = [
    {
        id: 1,
        name: 'Organic Cotton Fabric',
        industry: 'Textile',
        description: 'High-quality organic cotton fabric suitable for clothing',
        price: 15.99
    },
    {
        id: 2,
        name: 'Biodegradable Packaging',
        industry: 'Food',
        description: 'Eco-friendly packaging for food products',
        price: 0.25
    },
    {
        id: 3,
        name: 'Recycled Polyester Fabric',
        industry: 'Textile',
        description: 'Durable recycled polyester fabric for various applications',
        price: 12.50
    },
    {
        id: 4,
        name: 'Sustainable Utensils',
        industry: 'Food',
        description: 'Compostable utensils for food service',
        price: 0.05
    }
];

// RESTful API endpoint to fetch products based on industry
app.get('/api/products', (req, res) => {
    // Get the industry query parameter
    const { industry } = req.query;

    // Validate the industry parameter
    if (!industry) {
        return res.status(400).json({ error: 'Industry query parameter is required' });
    }

    // Filter products by the specified industry
    const filteredProducts = products.filter(product => product.industry.toLowerCase() === industry.toLowerCase());

    // Check if no products were found
    if (filteredProducts.length === 0) {
        return res.status(404).json({ message: 'No products found for the specified industry' });
    }

    // Return the filtered products
    return res.status(200).json(filteredProducts);
});

// Define the port for the server to listen on
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
