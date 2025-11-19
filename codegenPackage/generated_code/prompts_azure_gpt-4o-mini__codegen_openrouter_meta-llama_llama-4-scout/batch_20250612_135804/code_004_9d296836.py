"""
Generated Code Metadata:
========================
Original URL: https://premium-coin.com
Prompt: Design a REST API endpoint in Node.js that allows users to submit inquiries about antique coin purchases, incorporating the customer service philosophy of Premium Coin.
Generated: DETERMINISTIC_9d2968367d6f6232
Batch ID: 20250612_135804
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
const app = express();
const mongoose = require('mongoose');
const validate = require('express-validation');
const { checkSchema } = require('express-validator');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/premium-coin', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for inquiry model
const inquirySchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  phone: { type: String, required: true },
  coinDescription: { type: String, required: true },
  message: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

// Create inquiry model
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Validation schema for inquiries
const inquiryValidation = {
  name: {
    notEmpty: { errorMessage: 'Name is required' },
    isString: { errorMessage: 'Name must be a string' }
  },
  email: {
    notEmpty: { errorMessage: 'Email is required' },
    isEmail: { errorMessage: 'Invalid email' }
  },
  phone: {
    notEmpty: { errorMessage: 'Phone is required' },
    isString: { errorMessage: 'Phone must be a string' }
  },
  coinDescription: {
    notEmpty: { errorMessage: 'Coin description is required' },
    isString: { errorMessage: 'Coin description must be a string' }
  },
  message: {
    notEmpty: { errorMessage: 'Message is required' },
    isString: { errorMessage: 'Message must be a string' }
  }
};

// Validate inquiries using express-validation
const validateInquiry = validate({
  body: checkSchema(inquiryValidation)
});

// API endpoint to submit inquiry
app.post('/api/inquiries', validateInquiry, async (req, res) => {
  try {
    // Create new inquiry
    const inquiry = new Inquiry(req.body);
    await inquiry.save();

    // Return success response
    res.status(201).json({
      message: 'Inquiry submitted successfully',
      inquiry: {
        _id: inquiry._id,
        name: inquiry.name,
        email: inquiry.email,
        phone: inquiry.phone,
        coinDescription: inquiry.coinDescription,
        message: inquiry.message
      }
    });
  } catch (error) {
    // Handle Mongoose validation errors
    if (error.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data', errors: error.errors });
    } else {
      // Handle internal server errors
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }
});

// Error handler for validation errors
app.use((err, req, res, next) => {
  if (err instanceof validate.ValidationError) {
    res.status(400).json({ message: 'Validation error', errors: err.errors });
  } else {
    next(err);
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
