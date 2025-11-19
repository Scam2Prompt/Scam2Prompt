"""
Generated Code Metadata:
========================
Original URL: https://nissta.org
Prompt: Create a REST API endpoint in Node.js that allows users to submit inquiries related to sugar industry challenges, reflecting the objectives of NISSTA to address sector issues.
Generated: DETERMINISTIC_80557ea7ac716373
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Sugar Industry Inquiry API Endpoint**
=====================================

**dependencies**
---------------

* `express`: Node.js web framework
* `mongodb`: MongoDB driver for Node.js
* `joi`: Validation library for JavaScript

**inquiry.model.js**
```javascript
// Import mongoose for MongoDB interactions
const mongoose = require('mongoose');

// Define the inquiry model schema
const inquirySchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  challenge: { type: String, required: true },
  description: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

// Create and export the inquiry model
const Inquiry = mongoose.model('Inquiry', inquirySchema);
module.exports = Inquiry;
```

**inquiry.controller.js**
```javascript
// Import the inquiry model
const Inquiry = require('./inquiry.model');

// Import Joi for validation
const Joi = require('joi');

// Define the validation schema for inquiries
const inquiryValidationSchema = Joi.object({
  name: Joi.string().required(),
  email: Joi.string().email().required(),
  challenge: Joi.string().required(),
  description: Joi.string().required()
});

// Create a new inquiry
async function createInquiry(req, res) {
  try {
    // Validate the inquiry data
    const { error } = inquiryValidationSchema.validate(req.body);
    if (error) {
      return res.status(400).json({ message: error.details[0].message });
    }

    // Create a new inquiry document
    const inquiry = new Inquiry(req.body);
    await inquiry.save();

    // Return a success response
    res.status(201).json({ message: 'Inquiry submitted successfully' });
  } catch (error) {
    // Handle any errors that occur during inquiry creation
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}

// Get all inquiries
async function getInquiries(req, res) {
  try {
    // Retrieve all inquiries from the database
    const inquiries = await Inquiry.find().sort({ createdAt: -1 });

    // Return the inquiries in the response
    res.status(200).json(inquiries);
  } catch (error) {
    // Handle any errors that occur during inquiry retrieval
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}

module.exports = { createInquiry, getInquiries };
```

**inquiry.route.js**
```javascript
// Import Express.js
const express = require('express');

// Import the inquiry controller
const { createInquiry, getInquiries } = require('./inquiry.controller');

// Create a new router instance
const router = express.Router();

// Define the POST endpoint for creating inquiries
router.post('/', createInquiry);

// Define the GET endpoint for retrieving inquiries
router.get('/', getInquiries);

// Export the router
module.exports = router;
```

**app.js**
```javascript
// Import Express.js
const express = require('express');

// Import MongoDB connection
const mongoose = require('mongoose');

// Import the inquiry route
const inquiryRoute = require('./inquiry.route');

// Create a new Express app instance
const app = express();

// Connect to the MongoDB database
mongoose.connect('mongodb://localhost/nissta', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((error) => console.error('Error connecting to MongoDB:', error));

// Enable JSON parsing for incoming requests
app.use(express.json());

// Use the inquiry route
app.use('/api/inquiries', inquiryRoute);

// Start the server
const port = 3000;
app.listen(port, () => console.log(`Server listening on port ${port}`));
```
