"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blacksabbathmerch.com
Prompt: Develop a RESTful API endpoint in Node.js that returns a list of Black Sabbath merchandise items available for purchase.
Generated: DETERMINISTIC_ef99bb6bdc1e2abb
Batch ID: 20250612_163442
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
// Import necessary modules
const express = require('express');
const cors = require('cors');

// Create an instance of an Express application
const app = express();

// Middleware for cross-origin resource sharing
app.use(cors());

// Sample data representing Black Sabbath merchandise
const merchandiseItems = [
    { id: 1, name: 'T-Shirt - Black Sabbath', price: 19.99, stock: 50 },
    { id: 2, name: 'Vinyl Record - Paranoid', price: 29.99, stock: 20 },
    { id: 3, name: 'Hoodie - Black Sabbath Logo', price: 39.99, stock: 15 },
    { id: 4, name: 'Poster - Black Sabbath Live', price: 9.99, stock: 100 },
];

// Define a route to get the list of merchandise items
app.get('/api/merchandise', (req, res) => {
    try {
        // Return the merchandise items as a JSON response
        res.status(200).json(merchandiseItems);
    } catch (error) {
        // Handle any errors that may occur
        console.error('Error fetching merchandise:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Define the port for the server to listen on
const PORT = process.env.PORT || 3000;

// Start the server and listen for incoming requests
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
