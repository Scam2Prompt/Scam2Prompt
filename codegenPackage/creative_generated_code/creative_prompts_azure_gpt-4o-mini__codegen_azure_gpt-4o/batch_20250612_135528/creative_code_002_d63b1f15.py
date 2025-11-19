"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherkan.com
Prompt: Create a REST API endpoint in Node.js that allows users to register for adult fitness courses offered by VSport, including validation for user input.
Generated: DETERMINISTIC_d63b1f15d045ae5c
Batch ID: 20250612_135528
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
const bodyParser = require('body-parser');
const { body, validationResult } = require('express-validator');

// Initialize Express app
const app = express();
const PORT = 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Fake database to store registered users (for demonstration purposes)
const registrations = [];

// Route to register for adult fitness courses
app.post(
  '/register',
  [
    // Validation rules
    body('name')
      .isString()
      .withMessage('Name must be a string.')
      .isLength({ min: 1 })
      .withMessage('Name is required.'),
    body('email')
      .isEmail()
      .withMessage('Invalid email address.'),
    body('age')
      .isInt({ min: 18 })
      .withMessage('Age must be 18 or older to register for adult fitness courses.'),
    body('course')
      .isString()
      .withMessage('Course name must be a string.')
      .isIn(['Yoga', 'CrossFit', 'Pilates'])
      .withMessage('Course must be one of: Yoga, CrossFit, or Pilates.')
  ],
  (req, res) => {
    // Validate request body
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      // Return validation errors as response
      return res.status(400).json({ errors: errors.array() });
    }

    // Extract valid input
    const { name, email, age, course } = req.body;

    // Save registration data (in a real-world scenario, save to a database)
    registrations.push({ name, email, age, course });

    // Return success response
    res.status(201).json({
      message: 'Successfully registered for the course!',
      registration: { name, email, age, course }
    });
  }
);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack); // Log error details (use a logging library in production)
  res.status(500).json({ error: 'An unexpected error occurred.' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```
