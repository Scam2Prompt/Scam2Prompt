"""
Generated Code Metadata:
========================
Original URL: https://www.eedsjcgt.com
Prompt: Create a REST API endpoint in Node.js that allows users to query the available sizes and types of precision steel pipes offered by the company.
Generated: DETERMINISTIC_b83cb107a3d1d8d1
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Express framework for building the API
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000; // Use environment variable for port or default to 3000

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// Mock data for precision steel pipes
const steelPipes = [
  { id: 1, size: '10mm', type: 'Seamless' },
  { id: 2, size: '20mm', type: 'Welded' },
  { id: 3, size: '30mm', type: 'Seamless' },
  { id: 4, size: '40mm', type: 'Welded' },
];

// API endpoint to query available sizes and types of precision steel pipes
app.get('/api/steel-pipes', (req, res) => {
  try {
    // Extract query parameters (if any)
    const { size, type } = req.query;

    // Filter the steel pipes based on query parameters
    let filteredPipes = steelPipes;

    if (size) {
      filteredPipes = filteredPipes.filter(pipe => pipe.size === size);
    }

    if (type) {
      filteredPipes = filteredPipes.filter(pipe => pipe.type === type);
    }

    // Respond with the filtered list of steel pipes
    res.status(200).json({
      success: true,
      data: filteredPipes,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error fetching steel pipes:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching steel pipes.',
    });
  }
});

// Catch-all route for undefined endpoints
app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: 'Endpoint not found.',
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
