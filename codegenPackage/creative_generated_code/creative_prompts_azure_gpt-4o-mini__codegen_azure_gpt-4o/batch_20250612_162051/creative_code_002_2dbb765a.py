"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ratnarajfoods.in
Prompt: Create a RESTful API endpoint in Node.js that allows users to search for spices offered by Ratnaraj Foods based on specific criteria such as type and quality.
Generated: DETERMINISTIC_2dbb765a0f2ddf1e
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

// Initialize the Express application
const app = express();

// Use bodyParser to parse JSON request bodies
app.use(bodyParser.json());

// Simulated database of spices
const spices = [
  { id: 1, name: 'Turmeric', type: 'Powder', quality: 'Premium' },
  { id: 2, name: 'Cumin', type: 'Whole', quality: 'Standard' },
  { id: 3, name: 'Cinnamon', type: 'Stick', quality: 'Premium' },
  { id: 4, name: 'Black Pepper', type: 'Whole', quality: 'Standard' },
  { id: 5, name: 'Cardamom', type: 'Pod', quality: 'Premium' },
];

// GET endpoint to search for spices based on criteria
app.get('/api/spices/search', (req, res) => {
  try {
    // Extract query parameters
    const { type, quality } = req.query;

    // Filter spices based on provided search criteria
    const filteredSpices = spices.filter((spice) => {
      // Match type if provided
      const matchesType = type ? spice.type.toLowerCase() === type.toLowerCase() : true;

      // Match quality if provided
      const matchesQuality = quality ? spice.quality.toLowerCase() === quality.toLowerCase() : true;

      return matchesType && matchesQuality;
    });

    // Send filtered spices in the response
    res.status(200).json({
      success: true,
      data: filteredSpices,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error while searching for spices:', error.message);
    res.status(500).json({
      success: false,
      message: 'An error occurred while searching for spices. Please try again later.',
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

```
