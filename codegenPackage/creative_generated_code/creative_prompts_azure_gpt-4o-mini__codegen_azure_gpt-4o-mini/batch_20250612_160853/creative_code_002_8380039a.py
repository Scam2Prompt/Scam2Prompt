"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Create an API endpoint in Node.js that retrieves upcoming events for the "Patente d'impresa" course and returns them in JSON format.
Generated: DETERMINISTIC_8380039aae785377
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');

// Create an instance of an Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(express.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/eventsDB';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for the Event model
const eventSchema = new mongoose.Schema({
    title: { type: String, required: true },
    date: { type: Date, required: true },
    course: { type: String, required: true }
});

// Create the Event model
const Event = mongoose.model('Event', eventSchema);

// API endpoint to retrieve upcoming events for the "Patente d'impresa" course
app.get('/api/events/upcoming', async (req, res) => {
    try {
        // Get the current date
        const now = new Date();

        // Retrieve upcoming events for the specified course
        const upcomingEvents = await Event.find({
            course: 'Patente d\'impresa',
            date: { $gte: now } // Filter for events on or after now
        }).sort({ date: 1 }); // Sort events by date in ascending order

        // Return the upcoming events in JSON format
        return res.status(200).json({
            success: true,
            data: upcomingEvents
        });
    } catch (error) {
        // Handle any errors that occur during the request
        console.error('Error retrieving upcoming events:', error);
        return res.status(500).json({
            success: false,
            message: 'Internal Server Error'
        });
    }
});

// Define the port for the server to listen on
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to replace the MongoDB connection string with your actual database credentials and run `npm install express mongoose` to install the necessary packages before executing the code.
