"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Create an API endpoint in Node.js that provides information on private equity investment opportunities, reflecting the expertise and services offered by Alghanim Capital in the private equity domain.
Generated: DETERMINISTIC_a36588b3bed35de6
Batch ID: 20250612_162811
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
// Import the required modules
const express = require('express'); // Web framework for building the API
const bodyParser = require('body-parser'); // Middleware to parse JSON requests
const helmet = require('helmet'); // Helps secure Express apps by setting HTTP headers
const { v4: uuidv4 } = require('uuid'); // Module for generating unique IDs

// Initialize the Express application
const app = express();

// Middleware for security and JSON parsing
app.use(helmet());
app.use(bodyParser.json());

// Port on which the server will run
const PORT = process.env.PORT || 3000;

// Mock database for storing investment opportunities
const investmentOpportunities = [
  {
    id: uuidv4(),
    name: 'Tech Growth Fund',
    description: 'A fund focusing on high-growth technology startups.',
    minimumInvestment: 1000000, // USD
    region: 'North America',
    riskLevel: 'Medium',
    expectedReturn: '15-20%',
  },
  {
    id: uuidv4(),
    name: 'Healthcare Innovations Fund',
    description: 'Investments in pioneering healthcare technologies.',
    minimumInvestment: 2000000, // USD
    region: 'Global',
    riskLevel: 'Low',
    expectedReturn: '10-12%',
  },
];

// Route: GET /api/private-equity-opportunities
// Purpose: Fetch all private equity investment opportunities
app.get('/api/private-equity-opportunities', (req, res) => {
  try {
    // Respond with the list of investment opportunities
    res.status(200).json({
      success: true,
      data: investmentOpportunities,
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching investment opportunities.',
    });
  }
});

// Route: GET /api/private-equity-opportunities/:id
// Purpose: Fetch details of a specific investment opportunity
app.get('/api/private-equity-opportunities/:id', (req, res) => {
  const { id } = req.params; // Extract the id from the request parameters

  try {
    // Find the investment opportunity by ID
    const opportunity = investmentOpportunities.find((opp) => opp.id === id);

    if (!opportunity) {
      // If not found, respond with a 404 status
      return res.status(404).json({
        success: false,
        message: 'Investment opportunity not found.',
      });
    }

    // Respond with the details of the investment opportunity
    res.status(200).json({
      success: true,
      data: opportunity,
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching the investment opportunity.',
    });
  }
});

// Route: POST /api/private-equity-opportunities
// Purpose: Add a new private equity investment opportunity
app.post('/api/private-equity-opportunities', (req, res) => {
  const { name, description, minimumInvestment, region, riskLevel, expectedReturn } = req.body;

  // Validate request payload
  if (!name || !description || !minimumInvestment || !region || !riskLevel || !expectedReturn) {
    return res.status(400).json({
      success: false,
      message: 'All fields are required to add a new investment opportunity.',
    });
  }

  try {
    // Create a new investment opportunity object
    const newOpportunity = {
      id: uuidv4(),
      name,
      description,
      minimumInvestment,
      region,
      riskLevel,
      expectedReturn,
    };

    // Add the new opportunity to the mock database
    investmentOpportunities.push(newOpportunity);

    // Respond with the newly created investment opportunity
    res.status(201).json({
      success: true,
      data: newOpportunity,
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while adding the investment opportunity.',
    });
  }
});

// Route: DELETE /api/private-equity-opportunities/:id
// Purpose: Remove an investment opportunity by ID
app.delete('/api/private-equity-opportunities/:id', (req, res) => {
  const { id } = req.params; // Extract the id from the request parameters

  try {
    // Find the index of the investment opportunity by ID
    const index = investmentOpportunities.findIndex((opp) => opp.id === id);

    if (index === -1) {
      // If not found, respond with a 404 status
      return res.status(404).json({
        success: false,
        message: 'Investment opportunity not found.',
      });
    }

    // Remove the investment opportunity from the mock database
    investmentOpportunities.splice(index, 1);

    // Respond with success status
    res.status(200).json({
      success: true,
      message: 'Investment opportunity successfully deleted.',
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while deleting the investment opportunity.',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

```
