"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Create a REST API endpoint in Node.js that provides information about the MBA programs at the School of Management, including curriculum details and concentration areas.
Generated: DETERMINISTIC_a3425798493b30a1
Batch ID: 20250612_162945
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${port}`": {
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
const cors = require('cors');

// Initialize the Express application
const app = express();
const port = process.env.PORT || 3000;

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON bodies

// Sample data for MBA programs
const mbaPrograms = [
    {
        id: 1,
        name: 'Full-Time MBA',
        curriculum: [
            'Core Courses: Finance, Marketing, Operations Management',
            'Electives: Data Analytics, International Business',
        ],
        concentrations: [
            'Finance',
            'Marketing',
            'Operations',
            'Entrepreneurship',
        ],
    },
    {
        id: 2,
        name: 'Part-Time MBA',
        curriculum: [
            'Core Courses: Leadership, Strategic Management',
            'Electives: Digital Marketing, E-commerce',
        ],
        concentrations: [
            'Healthcare Management',
            'Supply Chain Management',
        ],
    },
];

// REST API endpoint to get MBA programs information
app.get('/api/mba-programs', (req, res) => {
    try {
        // Return the list of MBA programs
        res.status(200).json(mbaPrograms);
    } catch (error) {
        // Handle any potential errors
        console.error('Error fetching MBA programs:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
```
