"""
Generated Code Metadata:
========================
Original URL: https://larpradar.com
Prompt: Design an API endpoint in Node.js that allows users to search for LARP events by location and category, similar to the features on Larp Radar.
Generated: DETERMINISTIC_6975d35c71122a63
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/larp_events', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a schema for LARP events
const larpEventSchema = new mongoose.Schema({
    name: { type: String, required: true },
    location: { type: String, required: true },
    category: { type: String, required: true },
    date: { type: Date, required: true },
});

// Create a model for LARP events
const LarpEvent = mongoose.model('LarpEvent', larpEventSchema);

// API endpoint to search for LARP events by location and category
app.get('/api/events', async (req, res) => {
    const { location, category } = req.query;

    // Validate query parameters
    if (!location || !category) {
        return res.status(400).json({ error: 'Location and category are required.' });
    }

    try {
        // Search for events matching the location and category
        const events = await LarpEvent.find({ location, category });

        // Check if any events were found
        if (events.length === 0) {
            return res.status(404).json({ message: 'No events found for the specified location and category.' });
        }

        // Return the found events
        res.status(200).json(events);
    } catch (error) {
        // Handle any errors that occur during the search
        console.error('Error fetching events:', error);
        res.status(500).json({ error: 'An error occurred while fetching events.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
