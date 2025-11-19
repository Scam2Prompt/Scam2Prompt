"""
Generated Code Metadata:
========================
Original URL: https://www.igadvocacia.com
Prompt: Construct an API endpoint in Node.js that allows users to submit inquiries about labor law issues, highlighting the dual focus on labor and previdenciary law as seen in IG Advocacia's services.
Generated: DETERMINISTIC_ecfa808a4c18233a
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Define the port for the server
const PORT = process.env.PORT || 3000;

// In-memory storage for inquiries (for demonstration purposes)
// In production, use a database like MongoDB, PostgreSQL, etc.
const inquiries = [];

/**
 * POST /api/inquiries
 * Endpoint to submit inquiries about labor and previdenciary law issues.
 * Request body should include:
 * - name: string (required)
 * - email: string (required)
 * - message: string (required)
 */
app.post('/api/inquiries', (req, res) => {
  try {
    const { name, email, message } = req.body;

    // Validate request body
    if (!name || !email || !message) {
      return res.status(400).json({
        error: 'Missing required fields: name, email, and message are mandatory.',
      });
    }

    // Create a new inquiry object
    const newInquiry = {
      id: inquiries.length + 1, // Simple ID generation (use UUIDs in production)
      name,
      email,
      message,
      submittedAt: new Date(),
    };

    // Store the inquiry
    inquiries.push(newInquiry);

    // Respond with success
    res.status(201).json({
      message: 'Inquiry submitted successfully.',
      inquiry: newInquiry,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error processing inquiry:', error);
    res.status(500).json({
      error: 'An internal server error occurred. Please try again later.',
    });
  }
});

/**
 * GET /api/inquiries
 * Endpoint to retrieve all submitted inquiries.
 * For demonstration purposes only. In production, implement authentication and authorization.
 */
app.get('/api/inquiries', (req, res) => {
  try {
    res.status(200).json({
      message: 'List of all inquiries.',
      inquiries,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error retrieving inquiries:', error);
    res.status(500).json({
      error: 'An internal server error occurred. Please try again later.',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

This code creates a simple API with two endpoints: one for submitting inquiries and another for retrieving all inquiries. It includes validation, error handling, and follows best practices for a Node.js application.
