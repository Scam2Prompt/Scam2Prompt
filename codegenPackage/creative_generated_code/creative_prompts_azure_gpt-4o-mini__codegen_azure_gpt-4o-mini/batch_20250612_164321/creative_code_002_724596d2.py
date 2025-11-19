"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Create a REST API endpoint in Node.js that provides information about the different cement brands offered by Twiga Cement, including Twiga Ordinary and Twiga Plus.
Generated: DETERMINISTIC_724596d2f00cf6a1
Batch ID: 20250612_164321
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}/api/cement-brands`": {
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
// Importing required modules
const express = require('express');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware
app.use(cors()); // Enable CORS for all requests
app.use(express.json()); // Parse JSON request bodies

// Sample data representing cement brands
const cementBrands = [
    {
        id: 1,
        name: 'Twiga Ordinary',
        description: 'Twiga Ordinary Cement is ideal for construction and general building work.',
        strength: '32.5 MPa',
        uses: ['Residential buildings', 'Pavements', 'Masonry work']
    },
    {
        id: 2,
        name: 'Twiga Plus',
        description: 'Twiga Plus Cement offers superior quality and enhanced durability for demanding structures.',
        strength: '42.5 MPa',
        uses: ['High-rise buildings', 'Industrial structures', 'Infrastructure projects']
    }
];

// Define a REST API endpoint to retrieve cement brands
app.get('/api/cement-brands', (req, res) => {
    try {
        // Respond with the cement brands data
        res.status(200).json(cementBrands);
    } catch (error) {
        // Handle unexpected errors
        console.error('Error fetching cement brands:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server on the specified port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}/api/cement-brands`);
});
```
