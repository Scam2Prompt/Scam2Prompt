"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: Recommend a Node.js library for managing customer inquiries about PVC termopanels and aluminum windows, and demonstrate how to set up a basic API endpoint for handling these inquiries.
Generated: DETERMINISTIC_a8a82dd6ec81eeeb
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((error) => console.error('Error connecting to MongoDB:', error));

// Define schema for inquiry model
const inquirySchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  phone: { type: String, required: true },
  message: { type: String, required: true },
  product: { type: String, required: true }, // PVC termopanels or aluminum windows
});

// Create inquiry model
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Set up middleware for parsing JSON requests
app.use(express.json());

// Define API endpoint for creating new inquiries
app.post('/inquiries', async (req, res) => {
  try {
    const { name, email, phone, message, product } = req.body;
    if (!name || !email || !phone || !message || !product) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    const inquiry = new Inquiry({ name, email, phone, message, product });
    await inquiry.save();
    res.status(201).json({ message: 'Inquiry created successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error creating inquiry' });
  }
});

// Define API endpoint for retrieving all inquiries
app.get('/inquiries', async (req, res) => {
  try {
    const inquiries = await Inquiry.find().exec();
    res.json(inquiries);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error retrieving inquiries' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Close MongoDB connection when server exits
process.on('exit', () => {
  mongoose.disconnect();
});
```
