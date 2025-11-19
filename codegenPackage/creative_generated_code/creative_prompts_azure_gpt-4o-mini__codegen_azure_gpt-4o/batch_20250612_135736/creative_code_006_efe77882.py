"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerlab.org
Prompt: Construct a RESTful API endpoint in Node.js that provides information about the various mining plans available on MinerLab.
Generated: DETERMINISTIC_efe77882b825e9c9
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express framework for building RESTful APIs
const bodyParser = require('body-parser'); // Middleware for parsing incoming request bodies
const morgan = require('morgan'); // HTTP request logger middleware

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000; // Use environment variable or default to port 3000

// Middleware
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(morgan('dev')); // Log HTTP requests for debugging

// Mock Data: Mining plans available on MinerLab
const miningPlans = [
  {
    id: 1,
    name: "Basic Plan",
    hashRate: "10 TH/s",
    duration: "6 months",
    price: "$500",
  },
  {
    id: 2,
    name: "Standard Plan",
    hashRate: "50 TH/s",
    duration: "1 year",
    price: "$2000",
  },
  {
    id: 3,
    name: "Premium Plan",
    hashRate: "100 TH/s",
    duration: "2 years",
    price: "$5000",
  },
];

// API Route: GET /api/mining-plans
/**
 * Endpoint to retrieve a list of mining plans available on MinerLab.
 * Responds with JSON containing an array of mining plans.
 */
app.get('/api/mining-plans', (req, res) => {
  try {
    res.status(200).json({
      success: true,
      data: miningPlans,
    });
  } catch (error) {
    console.error("Error retrieving mining plans:", error.message);

    // Send internal server error response
    res.status(500).json({
      success: false,
      message: "An error occurred while retrieving mining plans.",
    });
  }
});

// API Route: GET /api/mining-plans/:id
/**
 * Endpoint to retrieve a specific mining plan by ID.
 * Responds with the details of the requested mining plan if found.
 */
app.get('/api/mining-plans/:id', (req, res) => {
  try {
    const planId = parseInt(req.params.id, 10); // Parse the ID from request params
    const plan = miningPlans.find((p) => p.id === planId); // Find the plan by ID

    if (!plan) {
      // If no plan found, respond with 404
      res.status(404).json({
        success: false,
        message: "Mining plan not found.",
      });
      return;
    }

    res.status(200).json({
      success: true,
      data: plan,
    });
  } catch (error) {
    console.error("Error retrieving mining plan:", error.message);

    // Send internal server error response
    res.status(500).json({
      success: false,
      message: "An error occurred while retrieving the mining plan.",
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing or further integration
module.exports = app;
```
