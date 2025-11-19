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
// Import required modules
const express = require('express');
const mongoose = require('mongoose');

// Initialize the Express app
const app = express();

// Middleware for parsing JSON requests
app.use(express.json());

// Connect to MongoDB (replace with your own connection string)
const mongoUri = 'mongodb://localhost:27017/larp-events';
mongoose.connect(mongoUri, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define the Event schema
const eventSchema = new mongoose.Schema({
    title: { type: String, required: true },
    location: { type: String, required: true },
    category: { type: String, required: true },
    date: { type: Date, required: true },
});

// Create the Event model
const Event = mongoose.model('Event', eventSchema);

// API endpoint to search for LARP events by location and category
app.get('/api/events/search', async (req, res) => {
    try {
        // Extract query parameters for location and category
        const { location, category } = req.query;

        // Validate query parameters
        if (!location && !category) {
            return res.status(400).json({ error: 'Location or category must be provided.' });
        }

        // Build the query object
        const query = {};
        if (location) {
            query.location = new RegExp(location, 'i'); // Case-insensitive regex search
        }
        if (category) {
            query.category = new RegExp(category, 'i'); // Case-insensitive regex search
        }

        // Fetch events from the database based on the query
        const events = await Event.find(query);

        // Return the found events
        return res.status(200).json(events);
    } catch (error) {
        // Handle errors and respond with an appropriate message
        console.error('Error searching events:', error);
        return res.status(500).json({ error: 'Internal server error.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Notes:
- Ensure you replace the MongoDB connection string with your own.
- Consider adding additional error handling and logging as needed for your specific production environment.
- The API is designed to handle searches based on location and category using regex for case-insensitivity.
