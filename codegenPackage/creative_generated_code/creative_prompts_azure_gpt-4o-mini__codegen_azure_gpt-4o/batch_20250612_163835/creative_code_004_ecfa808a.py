"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igadvocacia.com
Prompt: Construct an API endpoint in Node.js that allows users to submit inquiries about labor law issues, highlighting the dual focus on labor and previdenciary law as seen in IG Advocacia's services.
Generated: DETERMINISTIC_ecfa808a4c18233a
Batch ID: 20250612_163835
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
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs for inquiries

// Initialize the Express app
const app = express();

// Set the port for the application
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON request bodies
app.use(bodyParser.json());

// In-memory storage for inquiries (for simplicity; replace with a database in production)
const inquiries = [];

/**
 * POST /api/inquiries
 * Endpoint to submit inquiries related to labor and previdenciary law
 */
app.post('/api/inquiries', (req, res) => {
  try {
    const { name, email, phone, subject, message } = req.body;

    // Validate incoming data
    if (!name || !email || !subject || !message) {
      return res.status(400).json({ error: 'All fields (name, email, subject, message) are required.' });
    }

    // Construct the inquiry object
    const newInquiry = {
      id: uuidv4(), // Generate a unique ID for the inquiry
      name,
      email,
      phone: phone || null, // Optional field
      subject,
      message,
      submittedAt: new Date().toISOString() // Timestamp
    };

    // Save inquiry to the in-memory storage
    inquiries.push(newInquiry);

    // Respond with the inquiry ID and success message
    res.status(201).json({
      message: 'Inquiry submitted successfully.',
      inquiryId: newInquiry.id
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error while submitting inquiry:', error);
    res.status(500).json({ error: 'An internal server error occurred. Please try again later.' });
  }
});

/**
 * GET /api/inquiries
 * Endpoint to fetch all submitted inquiries (for admin purposes, example only)
 */
app.get('/api/inquiries', (req, res) => {
  try {
    res.status(200).json(inquiries);
  } catch (error) {
    console.error('Error while fetching inquiries:', error);
    res.status(500).json({ error: 'An internal server error occurred. Please try again later.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

```
