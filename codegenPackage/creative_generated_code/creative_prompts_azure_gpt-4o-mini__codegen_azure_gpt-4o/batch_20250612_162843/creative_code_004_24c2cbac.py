"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Construct a RESTful API endpoint in Node.js that provides details about the history and purpose of the Armourers & Brasiers' Company, including its impact on Materials Science education.
Generated: DETERMINISTIC_24c2cbacb9991977
Batch ID: 20250612_162843
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

// Initialize the Express application
const app = express();

// Define the port the server will run on
const PORT = process.env.PORT || 3000;

// Middleware to parse incoming JSON requests
app.use(express.json());

// Endpoint: GET /api/armourers-brasiers
// Purpose: Provide details about the Armourers & Brasiers' Company
// including its history, purpose, and impact on Materials Science education.
app.get('/api/armourers-brasiers', (req, res) => {
  try {
    // Data about the Armourers & Brasiers' Company
    const companyDetails = {
      history: `The Armourers & Brasiers' Company is one of the historic livery companies of the City of London, originally founded to represent workers who crafted arms and armor. Over time, the focus shifted toward supporting advancements in science and education.`,
      purpose: `The company is dedicated to promoting excellence in Materials Science, fostering education, and supporting research and innovation in the field.`,
      impactOnMaterialsScience: `The Armourers & Brasiers' Company has made significant contributions to Materials Science education through scholarships, grants, and partnerships with leading institutions. It also organizes events and initiatives aimed at inspiring young scientists and engineers to pursue careers in the field.`,
    };

    // Send the JSON response
    res.status(200).json({
      success: true,
      data: companyDetails,
    });
  } catch (error) {
    // Handle any unexpected errors
    console.error('Error fetching company details:', error);

    // Send a generic error response
    res.status(500).json({
      success: false,
      message: 'An error occurred while retrieving company details. Please try again later.',
    });
  }
});

// Handle undefined routes with a 404 response
app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: 'Endpoint not found.',
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
