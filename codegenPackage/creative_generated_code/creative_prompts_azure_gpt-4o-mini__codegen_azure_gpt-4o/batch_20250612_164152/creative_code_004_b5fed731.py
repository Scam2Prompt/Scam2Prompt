"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum24market.ru
Prompt: Develop a REST API endpoint that allows users to submit inquiries to a legal center, based on the contact functionality seen on the Arbitrum website.
Generated: DETERMINISTIC_b5fed7316e8f3159
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready implementation of a REST API endpoint using `Express.js` (Node.js) to allow users to submit inquiries to a legal center.

```javascript
// Import required modules
const express = require('express'); // Framework for building web applications
const bodyParser = require('body-parser'); // Middleware for parsing JSON request bodies
const Joi = require('joi'); // Library for input validation
const fs = require('fs'); // File system module for logging inquiries (optional)

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000; // Port for the server to listen on

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Define validation schema for inquiries
const inquirySchema = Joi.object({
  name: Joi.string().min(2).max(100).required(), // Name field: required, 2-100 chars
  email: Joi.string().email().required(), // Email field: required, must be a valid email
  message: Joi.string().min(10).max(1000).required(), // Message field: required, 10-1000 chars
});

// POST route to handle inquiries
app.post('/api/inquiries', async (req, res) => {
  try {
    // Validate the request body against the schema
    const { error, value } = inquirySchema.validate(req.body);
    if (error) {
      // If validation fails, return a 400 Bad Request response
      return res.status(400).json({ error: error.details[0].message });
    }

    // Extract validated data
    const { name, email, message } = value;

    // Log the inquiry for demonstration purposes (replace with database storage in production)
    const logEntry = `Inquiry received: ${new Date().toISOString()} - Name: ${name}, Email: ${email}, Message: ${message}\n`;
    fs.appendFile('inquiries.log', logEntry, (err) => {
      if (err) console.error('Error logging inquiry:', err);
    });

    // Respond with a success message
    res.status(200).json({
      message: 'Inquiry submitted successfully.',
      data: { name, email },
    });
  } catch (err) {
    // Handle unexpected errors
    console.error('Error handling inquiry:', err);
    res.status(500).json({ error: 'An unexpected error occurred. Please try again later.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- This implementation uses **Joi** for request validation to ensure the input meets the required format.
- **Error handling** is included for both validation and unexpected server errors.
- Inquiries are logged to a file named `inquiries.log` for demonstration purposes, but in production, they should be stored in a database.
- The API endpoint is exposed at `/api/inquiries`.
- The server runs on port `3000` by default, but you can set a custom port using the `PORT` environment variable.
