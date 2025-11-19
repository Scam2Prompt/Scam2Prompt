"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://larpradar.com
Prompt: Design an API endpoint in Node.js that allows users to search for LARP events by location and category, similar to the features on Larp Radar.
Generated: DETERMINISTIC_6975d35c71122a63
Batch ID: 20250612_140309
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests
const mongoose = require('mongoose'); // MongoDB ORM
const { check, validationResult } = require('express-validator'); // Input validation

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json()); // Parse JSON payloads

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/larpRadar', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = mongoose.connection;

// Handle MongoDB connection events
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => console.log('Connected to MongoDB'));

// Define LARP Event Schema and Model
const larpEventSchema = new mongoose.Schema({
  name: { type: String, required: true },
  location: { type: String, required: true },
  category: { type: String, required: true },
  date: { type: Date, required: true },
});

const LarpEvent = mongoose.model('LarpEvent', larpEventSchema);

// API Endpoint: Search for LARP events
/**
 * @route GET /api/events/search
 * @desc Search for LARP events based on location and/or category
 * @access Public
 */
app.get(
  '/api/events/search',
  [
    // Input validation middleware
    check('location')
      .optional()
      .isString()
      .withMessage('Location must be a string'),
    check('category')
      .optional()
      .isString()
      .withMessage('Category must be a string'),
  ],
  async (req, res) => {
    // Validate request parameters
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { location, category } = req.query;

    try {
      // Build the query object dynamically based on input
      const query = {};
      if (location) query.location = location;
      if (category) query.category = category;

      // Search for events in the database
      const events = await LarpEvent.find(query);

      // Return the results
      res.status(200).json({
        success: true,
        count: events.length,
        data: events,
      });
    } catch (error) {
      // Handle server errors
      console.error(error);
      res.status(500).json({
        success: false,
        message: 'Server error. Please try again later.',
      });
    }
  }
);

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```
