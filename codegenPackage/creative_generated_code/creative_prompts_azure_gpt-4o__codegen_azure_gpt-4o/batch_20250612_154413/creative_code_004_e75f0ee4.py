"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Develop a REST API in Node.js that allows users to search for fabric types from Shaoxing Eagles Textile Co., Ltd. by properties such as stretchability, weight (e.g., 180g or 240g), and intended use (e.g., swim fabric or hoodie fabric).
Generated: DETERMINISTIC_e75f0ee46c3e7d1f
Batch ID: 20250612_154413
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

// Initialize the application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(cors()); // Enable Cross-Origin Resource Sharing

// Sample fabric dataset (In a real-world scenario, this would be fetched from a database)
const fabrics = [
  {
    id: 1,
    name: 'Stretchable Swim Fabric',
    stretchability: 'High',
    weight: '180g',
    intendedUse: 'Swim fabric',
  },
  {
    id: 2,
    name: 'Heavy Hoodie Fabric',
    stretchability: 'Medium',
    weight: '240g',
    intendedUse: 'Hoodie fabric',
  },
  {
    id: 3,
    name: 'Lightweight Stretch Fabric',
    stretchability: 'Low',
    weight: '150g',
    intendedUse: 'Shirt fabric',
  },
];

// Endpoint to search for fabrics
app.get('/api/fabrics/search', (req, res) => {
  try {
    // Extract query parameters from the request
    const { stretchability, weight, intendedUse } = req.query;

    // Filter fabrics based on query parameters
    let results = fabrics;

    if (stretchability) {
      results = results.filter((fabric) =>
        fabric.stretchability.toLowerCase() === stretchability.toLowerCase()
      );
    }
    if (weight) {
      results = results.filter((fabric) => fabric.weight === weight);
    }
    if (intendedUse) {
      results = results.filter((fabric) =>
        fabric.intendedUse.toLowerCase().includes(intendedUse.toLowerCase())
      );
    }

    // Return matching results
    res.status(200).json({
      success: true,
      data: results,
    });
  } catch (error) {
    // Handle any errors that occur during execution
    console.error('Error searching fabrics:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while searching for fabrics.',
    });
  }
});

// Default error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled Error:', err);
  res.status(500).json({
    success: false,
    message: 'An unexpected error occurred.',
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
Production-Ready Features:
1. Proper query parameter handling for searching fabrics.
2. Error handling for unexpected cases.
3. Uses middleware for JSON parsing and CORS.
4. Modular and maintainable structure.
5. Ready for integration with a database for dynamic fabric data in real-world applications.
*/
```
