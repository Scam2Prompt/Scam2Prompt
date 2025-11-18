"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dmsauto4x4.ro
Prompt: Develop a REST API endpoint in Node.js to fetch details of off-road recovery accessories, such as kinetic straps, steel cables, and towing belts, using the product categories from DMS Auto4x4.ro.
Generated: DETERMINISTIC_e413b63f684acbe5
Batch ID: 20250612_152739
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.auto4x4.ro": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
// Import required modules
const express = require('express');
const axios = require('axios'); // For making HTTP requests
const app = express();

// Define the port for the server
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Base URL for DMS Auto4x4.ro's API (replace with actual endpoint if known)
const DMS_BASE_URL = 'https://api.auto4x4.ro'; // Replace with actual URL if available

// Route: GET /accessories
// Fetch details of off-road recovery accessories
app.get('/accessories', async (req, res) => {
    try {
        // Define product categories for off-road recovery accessories
        const categories = ['kinetic-straps', 'steel-cables', 'towing-belts'];

        // Fetch product details for each category from the external API
        const fetchCategoryPromises = categories.map(async (category) => {
            const response = await axios.get(`${DMS_BASE_URL}/products?category=${category}`);
            return {
                category,
                products: response.data.products
            };
        });

        // Resolve all promises
        const allProducts = await Promise.all(fetchCategoryPromises);

        // Respond with the fetched data
        res.status(200).json({
            success: true,
            data: allProducts
        });
    } catch (error) {
        // Handle errors gracefully
        console.error('Error fetching accessory details:', error.message);
        res.status(500).json({
            success: false,
            message: 'Failed to fetch accessory details. Please try again later.'
        });
    }
});

// Error handling middleware for handling invalid routes
app.use((req, res) => {
    res.status(404).json({
        success: false,
        message: 'Endpoint not found.'
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
