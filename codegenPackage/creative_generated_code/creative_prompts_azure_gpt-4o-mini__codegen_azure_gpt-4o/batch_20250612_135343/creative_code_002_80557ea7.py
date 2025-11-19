"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nissta.org
Prompt: Create a REST API endpoint in Node.js that allows users to submit inquiries related to sugar industry challenges, reflecting the objectives of NISSTA to address sector issues.
Generated: DETERMINISTIC_80557ea7ac716373
Batch ID: 20250612_135343
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
const { v4: uuidv4 } = require('uuid');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Port the server will listen to
const PORT = process.env.PORT || 3000;

// Dummy datastore to hold inquiries
const inquiries = [];

/**
 * POST /api/inquiries
 * Endpoint to submit inquiries related to sugar industry challenges.
 * 
 * Request Body:
 * {
 *   "name": "John Doe",       // Name of the user submitting the inquiry
 *   "email": "john@example.com", // Email of the user (for replies)
 *   "subject": "Sugar sector policy issues", // Subject of the inquiry
 *   "message": "Detailed message about the inquiry." // Inquiry details
 * }
 * 
 * Response Body:
 * {
 *   "id": "generated-id",     // Unique ID for the inquiry
 *   "message": "Inquiry submitted successfully."
 * }
 */
app.post('/api/inquiries', (req, res) => {
  try {
    // Validate request body
    const { name, email, subject, message } = req.body;

    if (!name || !email || !subject || !message) {
      return res.status(400).json({
        error: 'All fields (name, email, subject, message) are required.'
      });
    }

    // Create a new inquiry object
    const inquiry = {
      id: uuidv4(), // Generate a unique ID for the inquiry
      name,
      email,
      subject,
      message,
      submittedAt: new Date() // Timestamp of submission
    };

    // Save the inquiry to the datastore
    inquiries.push(inquiry);

    // Respond with success message and inquiry ID
    res.status(201).json({
      id: inquiry.id,
      message: 'Inquiry submitted successfully.'
    });

  } catch (error) {
    // Handle unexpected errors
    console.error('Error processing inquiry:', error.message);
    res.status(500).json({
      error: 'An error occurred while processing your request. Please try again later.'
    });
  }
});

// Endpoint to check server status
app.get('/api/status', (req, res) => {
  res.status(200).json({ message: 'Server is running.' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
