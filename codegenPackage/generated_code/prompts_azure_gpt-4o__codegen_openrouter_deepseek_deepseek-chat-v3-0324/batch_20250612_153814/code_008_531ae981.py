"""
Generated Code Metadata:
========================
Original URL: https://phantomdistro.com
Prompt: Create an API endpoint in Node.js for verifying and storing user-provided business information, including Vape License Numbers and Federal EINs, inspired by PhantomDistro.com.
Generated: DETERMINISTIC_531ae9814bd0c632
Batch ID: 20250612_153814
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
const { v4: uuidv4 } = require('uuid');
const validator = require('validator');
const mongoose = require('mongoose');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/businessVerification', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

// Business Schema
const BusinessSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4 },
  businessName: { type: String, required: true },
  ownerName: { type: String, required: true },
  email: { 
    type: String, 
    required: true,
    validate: {
      validator: validator.isEmail,
      message: 'Invalid email format'
    }
  },
  phone: { 
    type: String, 
    required: true,
    validate: {
      validator: (value) => validator.isMobilePhone(value, 'any'),
      message: 'Invalid phone number'
    }
  },
  vapeLicenseNumber: { 
    type: String, 
    required: true,
    validate: {
      validator: (value) => /^[A-Za-z0-9-]{8,20}$/.test(value),
      message: 'Invalid vape license format (8-20 alphanumeric characters)'
    }
  },
  federalEIN: { 
    type: String, 
    required: true,
    validate: {
      validator: (value) => /^\d{2}-\d{7}$/.test(value),
      message: 'Invalid EIN format (XX-XXXXXXX)'
    }
  },
  address: {
    street: { type: String, required: true },
    city: { type: String, required: true },
    state: { type: String, required: true, maxlength: 2 },
    zipCode: { 
      type: String, 
      required: true,
      validate: {
        validator: (value) => /^\d{5}(-\d{4})?$/.test(value),
        message: 'Invalid ZIP code format'
      }
    }
  },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Business Model
const Business = mongoose.model('Business', BusinessSchema);

// API Endpoint for Business Verification
app.post('/api/verify-business', async (req, res) => {
  try {
    // Validate required fields
    const requiredFields = ['businessName', 'ownerName', 'email', 'phone', 'vapeLicenseNumber', 'federalEIN', 'address'];
    for (const field of requiredFields) {
      if (!req.body[field]) {
        return res.status(400).json({ error: `${field} is required` });
      }
    }

    // Create new business record
    const business = new Business(req.body);
    await business.save();

    // Return success response
    res.status(201).json({
      success: true,
      message: 'Business information verified and stored successfully',
      businessId: business.id
    });
  } catch (error) {
    // Handle validation errors
    if (error.name === 'ValidationError') {
      const errors = {};
      Object.keys(error.errors).forEach((key) => {
        errors[key] = error.errors[key].message;
      });
      return res.status(400).json({ error: 'Validation failed', details: errors });
    }

    // Handle other errors
    console.error('Error verifying business:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get Business by ID
app.get('/api/business/:id', async (req, res) => {
  try {
    const business = await Business.findOne({ id: req.params.id });
    if (!business) {
      return res.status(404).json({ error: 'Business not found' });
    }
    res.json(business);
  } catch (error) {
    console.error('Error fetching business:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```
