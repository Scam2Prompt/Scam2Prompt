"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Create a REST API endpoint in Node.js that allows users to query the available sizes and types of precision steel pipes offered by the company.
Generated: DETERMINISTIC_b83cb107a3d1d8d1
Batch ID: 20250612_161331
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
// Import required modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse JSON request bodies

// Initialize the Express application
const app = express();
const PORT = 3000; // Define the port for the server

// Middleware to parse JSON payloads
app.use(bodyParser.json());

// Mock database of precision steel pipes for demonstration purposes
const steelPipes = [
  { id: 1, size: '10mm', type: 'Seamless' },
  { id: 2, size: '20mm', type: 'Welded' },
  { id: 3, size: '30mm', type: 'ERW' },
  { id: 4, size: '40mm', type: 'Seamless' },
  { id: 5, size: '50mm', type: 'Welded' },
];

// API endpoint to query available steel pipes
app.get('/api/steel-pipes', (req, res) => {
  try {
    // Fetch query parameters (optional filtering by size or type)
    const { size, type } = req.query;

    // Filter steel pipes based on query parameters
    let filteredPipes = steelPipes;
    
    if (size) {
      filteredPipes = filteredPipes.filter(pipe => pipe.size === size);
    }
    
    if (type) {
      filteredPipes = filteredPipes.filter(pipe => pipe.type === type);
    }

    // Return the filtered list of steel pipes
    res.status(200).json({
      success: true,
      data: filteredPipes,
    });
  } catch (error) {
    // Handle potential errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while querying steel pipes.',
      error: error.message,
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
