"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Create a RESTful API endpoint in Node.js that allows users to submit requests for polygraph tests related to fidelity verification.
Generated: DETERMINISTIC_38db552f4be1f647
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Create an Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose.connect('mongodb://localhost:27017/polygraphTests', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('MongoDB connected successfully');
}).catch(err => {
    console.error('Database connection error:', err);
});

// Define a schema for polygraph test requests
const polygraphTestSchema = new mongoose.Schema({
    userId: { type: String, required: true },
    requestDate: { type: Date, default: Date.now },
    status: { type: String, enum: ['pending', 'completed'], default: 'pending' },
    notes: String,
});

// Create a model based on the schema
const PolygraphTest = mongoose.model('PolygraphTest', polygraphTestSchema);

// RESTful API endpoint to submit a polygraph test request
app.post('/api/polygraph-requests', async (req, res) => {
    try {
        const { userId, notes } = req.body;

        // Validate request data
        if (!userId) {
            return res.status(400).json({ error: 'User ID is required' });
        }

        // Create a new polygraph test request
        const polygraphTestRequest = new PolygraphTest({ userId, notes });
        await polygraphTestRequest.save();

        // Respond with the created request
        res.status(201).json(polygraphTestRequest);
    } catch (error) {
        console.error('Error creating polygraph test request:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
