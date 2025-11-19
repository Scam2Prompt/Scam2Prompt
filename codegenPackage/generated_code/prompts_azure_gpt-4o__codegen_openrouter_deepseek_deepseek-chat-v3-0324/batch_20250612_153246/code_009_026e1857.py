"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Create a REST API endpoint in Node.js to handle dealer inquiries about the Sundance Spas Retail Advantage program, including fields for name, email, and company information.
Generated: DETERMINISTIC_026e185710fcc61d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { validationResult, check } = require('express-validator');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Validation rules
const inquiryValidationRules = [
  check('name').notEmpty().withMessage('Name is required'),
  check('email').isEmail().withMessage('Valid email is required'),
  check('company').notEmpty().withMessage('Company name is required'),
  check('phone').optional().isMobilePhone().withMessage('Valid phone number is required if provided'),
  check('message').optional().isLength({ max: 500 }).withMessage('Message must be less than 500 characters')
];

// In-memory storage for demo purposes (replace with database in production)
let inquiries = [];

// POST endpoint for dealer inquiries
app.post('/api/inquiries', inquiryValidationRules, (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const { name, email, company, phone, message } = req.body;
    
    const newInquiry = {
      id: inquiries.length + 1,
      name,
      email,
      company,
      phone: phone || null,
      message: message || null,
      createdAt: new Date().toISOString()
    };

    inquiries.push(newInquiry);
    
    // In production, you would save to a database here
    // await saveToDatabase(newInquiry);

    res.status(201).json({
      success: true,
      message: 'Inquiry submitted successfully',
      data: newInquiry
    });
  } catch (error) {
    console.error('Error processing inquiry:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while processing your inquiry'
    });
  }
});

// GET endpoint to retrieve all inquiries (for admin purposes)
app.get('/api/inquiries', (req, res) => {
  try {
    res.status(200).json({
      success: true,
      data: inquiries
    });
  } catch (error) {
    console.error('Error fetching inquiries:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching inquiries'
    });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    success: false,
    message: 'Internal server error'
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
