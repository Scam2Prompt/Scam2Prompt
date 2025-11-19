"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Create a RESTful API endpoint in Node.js that allows users to submit requests for polygraph tests related to fidelity verification.
Generated: DETERMINISTIC_38db552f4be1f647
Batch ID: 20250612_162050
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/polygraph', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a schema for polygraph test requests
const polygraphRequestSchema = new mongoose.Schema({
    userId: { type: String, required: true },
    requestDate: { type: Date, default: Date.now },
    status: { type: String, enum: ['pending', 'completed', 'canceled'], default: 'pending' },
    details: { type: String, required: true },
});

// Create a model based on the schema
const PolygraphRequest = mongoose.model('PolygraphRequest', polygraphRequestSchema);

// Define the API endpoint to submit a polygraph test request
app.post('/api/polygraph-requests', async (req, res) => {
    try {
        // Validate request body
        const { userId, details } = req.body;
        if (!userId || !details) {
            return res.status(400).json({ error: 'userId and details are required' });
        }

        // Create a new polygraph request
        const newRequest = new PolygraphRequest({ userId, details });
        await newRequest.save();

        // Respond with the created request
        res.status(201).json(newRequest);
    } catch (error) {
        console.error('Error creating polygraph request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Define a port for the server to listen on
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
