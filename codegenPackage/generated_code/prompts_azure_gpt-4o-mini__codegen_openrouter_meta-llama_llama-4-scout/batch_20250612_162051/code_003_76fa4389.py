"""
Generated Code Metadata:
========================
Original URL: https://corfucoastalcollection.com
Prompt: Develop a REST API endpoint in Node.js that allows users to submit inquiries about properties listed on the Corfu Coastal Collection website.
Generated: DETERMINISTIC_76fa43891a4f278c
Batch ID: 20250612_162051
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
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for inquiry model
const inquirySchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  propertyId: { type: String, required: true },
  message: { type: String, required: true },
});

// Create inquiry model
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Define endpoint to submit inquiry
/**
 * @route POST /inquiries
 * @description Submit an inquiry about a property
 * @param {string} name - User's name
 * @param {string} email - User's email
 * @param {string} propertyId - ID of the property
 * @param {string} message - Inquiry message
 */
app.post('/inquiries', async (req, res) => {
  try {
    const { name, email, propertyId, message } = req.body;

    // Validate request body
    if (!name || !email || !propertyId || !message) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    // Create new inquiry
    const inquiry = new Inquiry({ name, email, propertyId, message });

    // Save inquiry to database
    await inquiry.save();

    // Return success response
    res.status(201).json({ message: 'Inquiry submitted successfully' });
  } catch (error) {
    // Return error response
    res.status(500).json({ error: 'Failed to submit inquiry' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
