"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Create a RESTful API endpoint in Node.js to submit sweepstakes entries with details like name, address, and email, considering the requirements from thedaybrightener.com.
Generated: DETERMINISTIC_833acd2eb1609cf6
Batch ID: 20250622_205236
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
const validator = require('validator');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/sweepstakes', { useNewUrlParser: true, useUnifiedTopology: true });

// Define the sweepstakes entry schema
const sweepstakesEntrySchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  address: {
    type: String,
    required: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    trim: true,
    validate: {
      validator: (email) => validator.isEmail(email),
      message: 'Invalid email address'
    }
  }
});

// Create a model for sweepstakes entries
const SweepstakesEntry = mongoose.model('SweepstakesEntry', sweepstakesEntrySchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Define the RESTful API endpoint to submit sweepstakes entries
app.post('/api/sweepstakes/entries', async (req, res) => {
  try {
    // Validate request body
    if (!req.body.name || !req.body.address || !req.body.email) {
      return res.status(400).json({ error: 'Name, address, and email are required' });
    }

    // Create a new sweepstakes entry
    const entry = new SweepstakesEntry(req.body);

    // Save the entry to the database
    await entry.save();

    // Return a success response
    res.status(201).json({ message: 'Sweepstakes entry submitted successfully' });
  } catch (error) {
    // Handle validation errors
    if (error.name === 'ValidationError') {
      return res.status(400).json({ error: error.message });
    }

    // Handle server errors
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
