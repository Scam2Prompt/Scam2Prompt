"""
Generated Code Metadata:
========================
Original URL: https://status.ttec.smartteam.chat
Prompt: Create a REST API endpoint using Node.js to fetch and return the status updates of the TTEC STC Cluster for a given time period (e.g., last 7 days, last 30 days).
Generated: DETERMINISTIC_1100c8232d903f00
Batch ID: 20250622_212152
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
const mongoose = require('mongoose');
const moment = require('moment');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// MongoDB connection string (replace with your own)
const mongoURI = 'mongodb://localhost:27017/ttec-stc-cluster';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for status updates
const statusUpdateSchema = new mongoose.Schema({
    status: String,
    timestamp: { type: Date, default: Date.now }
});

// Create a model for status updates
const StatusUpdate = mongoose.model('StatusUpdate', statusUpdateSchema);

/**
 * Fetch status updates for a given time period.
 * @param {string} period - The time period to fetch updates for (e.g., '7d', '30d').
 * @returns {Array} - An array of status updates.
 */
app.get('/api/status-updates', async (req, res) => {
    const { period } = req.query;

    // Validate the period parameter
    if (!period || !['7d', '30d'].includes(period)) {
        return res.status(400).json({ error: 'Invalid period. Use "7d" or "30d".' });
    }

    // Calculate the start date based on the period
    const startDate = moment().subtract(parseInt(period), 'days').toDate();

    try {
        // Fetch status updates from the database
        const updates = await StatusUpdate.find({ timestamp: { $gte: startDate } }).sort({ timestamp: -1 });

        // Return the status updates
        return res.status(200).json(updates);
    } catch (error) {
        console.error('Error fetching status updates:', error);
        return res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
