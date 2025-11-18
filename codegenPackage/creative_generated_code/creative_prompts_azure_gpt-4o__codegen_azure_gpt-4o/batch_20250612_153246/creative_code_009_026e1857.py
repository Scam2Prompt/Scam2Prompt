"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sundancespasadvantage.com
Prompt: Create a REST API endpoint in Node.js to handle dealer inquiries about the Sundance Spas Retail Advantage program, including fields for name, email, and company information.
Generated: DETERMINISTIC_026e185710fcc61d
Batch ID: 20250612_153246
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

// Initialize Express application
const app = express();
const PORT = 3000;

// Middleware for parsing JSON request bodies
app.use(bodyParser.json());

// Route to handle dealer inquiries about Sundance Spas Retail Advantage program
app.post('/api/dealer-inquiry', (req, res) => {
  try {
    // Extract fields from the request body
    const { name, email, company } = req.body;

    // Validate required fields
    if (!name || !email || !company) {
      return res.status(400).json({
        error: 'Missing required fields: name, email, or company.',
      });
    }

    // Simulate successful inquiry submission (replace with actual logic, e.g., database save)
    const inquiry = {
      name,
      email,
      company,
      submittedAt: new Date(),
    };

    // Respond with success message
    return res.status(200).json({
      message: 'Inquiry submitted successfully!',
      inquiry,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error handling dealer inquiry:', error);
    return res.status(500).json({
      error: 'An unexpected error occurred. Please try again later.',
    });
  }
});

// Start Express server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

Ensure you have `express` and `body-parser` installed in your Node.js project to run this code:

```bash
npm install express body-parser
```
