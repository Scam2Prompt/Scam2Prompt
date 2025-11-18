"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sundancespasadvantage.com
Prompt: Create a REST API endpoint in Node.js to handle dealer inquiries about the Sundance Spas Retail Advantage program, including fields for name, email, and company information.
Generated: DETERMINISTIC_026e185710fcc61d
Batch ID: 20250612_153246
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
const { check, validationResult } = require('express-validator');

// Create an instance of Express
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Define a port for the server to listen on
const PORT = process.env.PORT || 3000;

// Define the inquiry route
app.post('/api/inquiries', [
    // Validate and sanitize input fields
    check('name').isString().notEmpty().withMessage('Name is required.'),
    check('email').isEmail().withMessage('Valid email is required.'),
    check('company').isString().optional().trim().escape(),
], (req, res) => {
    // Handle validation errors
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    // Extract data from the request body
    const { name, email, company } = req.body;

    // Ideally, you would save this data to a database here
    // For demonstration, we'll just log it to the console
    console.log('Dealer Inquiry:', { name, email, company });

    // Send a success response
    return res.status(201).json({
        message: 'Inquiry submitted successfully.',
        data: { name, email, company },
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```
