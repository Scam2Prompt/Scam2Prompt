"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Develop a backend service in Node.js to manage and serve MFO data, including features like sorting offers by interest rates and filtering by client region, as described on nocreditcheck.online.
Generated: DETERMINISTIC_baac814e3b6bb3cd
Batch ID: 20250612_145727
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
const express = require('express');
const bodyParser = require('body-parser');

// Initialize Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Sample data: Array of MFO (Microfinance Organization) offers
const mfoOffers = [
  { id: 1, name: "MFO Alpha", interestRate: 5.5, region: "North" },
  { id: 2, name: "MFO Beta", interestRate: 3.0, region: "South" },
  { id: 3, name: "MFO Gamma", interestRate: 7.2, region: "East" },
  { id: 4, name: "MFO Delta", interestRate: 4.8, region: "North" },
  { id: 5, name: "MFO Epsilon", interestRate: 6.0, region: "West" },
];

// Utility function to validate query parameters
function validateQueryParams(query) {
  const allowedSortFields = ['interestRate', 'name'];
  const allowedRegions = ['North', 'South', 'East', 'West'];

  if (query.sort && !allowedSortFields.includes(query.sort)) {
    return `Invalid sort field. Allowed fields: ${allowedSortFields.join(', ')}`;
  }

  if (query.region && !allowedRegions.includes(query.region)) {
    return `Invalid region. Allowed regions: ${allowedRegions.join(', ')}`;
  }

  return null;
}

// Route to get filtered and sorted MFO data
app.get('/api/mfo-offers', (req, res) => {
  try {
    const { sort, region } = req.query;

    // Validate query parameters
    const validationError = validateQueryParams(req.query);
    if (validationError) {
      return res.status(400).json({ error: validationError });
    }

    let filteredOffers = [...mfoOffers];

    // Filter by region if specified
    if (region) {
      filteredOffers = filteredOffers.filter(offer => offer.region === region);
    }

    // Sort by specified field if provided
    if (sort) {
      filteredOffers.sort((a, b) => {
        if (typeof a[sort] === 'string') {
          // Alphabetical sorting for strings
          return a[sort].localeCompare(b[sort]);
        }
        // Numerical sorting for numbers
        return a[sort] - b[sort];
      });
    }

    // Return the filtered and sorted offers
    return res.json(filteredOffers);

  } catch (error) {
    // Handle unexpected server errors
    console.error('Error fetching MFO offers:', error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Fallback route for undefined endpoints
app.use((req, res) => {
  res.status(404).json({ error: 'Endpoint not found' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
