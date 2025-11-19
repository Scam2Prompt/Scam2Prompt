"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Create a REST API endpoint in Node.js that provides information about the different cement brands offered by Twiga Cement, including Twiga Ordinary and Twiga Plus.
Generated: DETERMINISTIC_724596d2f00cf6a1
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for building REST APIs
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

// Initialize the Express app
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Port configuration
const PORT = process.env.PORT || 3000;

// Mock data for cement brand information
const cementBrands = [
  {
    id: 1,
    name: 'Twiga Ordinary',
    description: 'Twiga Ordinary is a high-quality cement ideal for general construction work.',
    features: ['High strength', 'Durability', 'Versatility'],
  },
  {
    id: 2,
    name: 'Twiga Plus',
    description: 'Twiga Plus is specifically designed for heavy-duty applications.',
    features: ['Extra strength', 'Improved workability', 'Long-lasting performance'],
  },
];

// Route: GET /api/cement-brands
// Description: Fetch all available cement brands
app.get('/api/cement-brands', (req, res) => {
  try {
    // Respond with the list of cement brands
    res.status(200).json({
      success: true,
      data: cementBrands,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error fetching cement brands:', error);
    res.status(500).json({
      success: false,
      message: 'Internal Server Error',
    });
  }
});

// Route: GET /api/cement-brands/:id
// Description: Fetch details of a specific cement brand by ID
app.get('/api/cement-brands/:id', (req, res) => {
  try {
    const { id } = req.params; // Extract ID from route parameters
    const cementBrand = cementBrands.find((brand) => brand.id === parseInt(id, 10)); // Find the brand by ID

    if (!cementBrand) {
      // If brand is not found, return a 404 response
      return res.status(404).json({
        success: false,
        message: 'Cement brand not found',
      });
    }

    // Respond with the found cement brand
    res.status(200).json({
      success: true,
      data: cementBrand,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error(`Error fetching cement brand with ID ${req.params.id}:`, error);
    res.status(500).json({
      success: false,
      message: 'Internal Server Error',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app (useful for testing or extending functionality)
module.exports = app;
```
