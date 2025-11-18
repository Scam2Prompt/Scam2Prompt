"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Create a REST API endpoint in Node.js for fetching product details such as "HyaloCare Gel" and "Removedor de Adhesivo Médico en Spray" based on their unique product IDs.
Generated: DETERMINISTIC_6054189c10522b5d
Batch ID: 20250612_152426
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Sample product data (in a real application, this could come from a database)
const products = {
    '1': { id: '1', name: 'HyaloCare Gel', description: 'Moisturizing gel for skin care.' },
    '2': { id: '2', name: 'Removedor de Adhesivo Médico en Spray', description: 'Medical adhesive remover spray.' }
};

// Define a REST API endpoint to fetch product details by ID
app.get('/api/products/:id', (req, res) => {
    const productId = req.params.id;

    // Validate the product ID
    if (!products[productId]) {
        return res.status(404).json({ error: 'Product not found' });
    }

    // Respond with the product details
    res.status(200).json(products[productId]);
});

// Global error handler for uncaught exceptions
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack
    res.status(500).json({ error: 'Internal Server Error' }); // Respond with a 500 status
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
