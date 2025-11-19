"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Create a RESTful API using Node.js to manage industrial part cleaning requests, including ultrasonic cleaning, and provide estimates for cleaning time and cost."
Generated: DETERMINISTIC_7760e3436c685498
Batch ID: 20250622_212534
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
mongoose.connect('mongodb://localhost:27017/cleaningRequests', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define a schema for cleaning requests
const cleaningRequestSchema = new mongoose.Schema({
    partName: { type: String, required: true },
    cleaningType: { type: String, enum: ['ultrasonic', 'manual'], required: true },
    estimatedTime: { type: Number, required: true }, // in minutes
    estimatedCost: { type: Number, required: true }, // in dollars
    createdAt: { type: Date, default: Date.now },
});

// Create a model based on the schema
const CleaningRequest = mongoose.model('CleaningRequest', cleaningRequestSchema);

// Create a new cleaning request
app.post('/api/cleaning-requests', async (req, res) => {
    try {
        const { partName, cleaningType } = req.body;

        // Estimate time and cost based on cleaning type
        let estimatedTime, estimatedCost;
        if (cleaningType === 'ultrasonic') {
            estimatedTime = 30; // Example: 30 minutes for ultrasonic cleaning
            estimatedCost = 50; // Example: $50 for ultrasonic cleaning
        } else {
            estimatedTime = 60; // Example: 60 minutes for manual cleaning
            estimatedCost = 80; // Example: $80 for manual cleaning
        }

        // Create a new cleaning request
        const cleaningRequest = new CleaningRequest({
            partName,
            cleaningType,
            estimatedTime,
            estimatedCost,
        });

        // Save the request to the database
        await cleaningRequest.save();
        res.status(201).json(cleaningRequest);
    } catch (error) {
        console.error('Error creating cleaning request:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Get all cleaning requests
app.get('/api/cleaning-requests', async (req, res) => {
    try {
        const requests = await CleaningRequest.find();
        res.status(200).json(requests);
    } catch (error) {
        console.error('Error fetching cleaning requests:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Get a specific cleaning request by ID
app.get('/api/cleaning-requests/:id', async (req, res) => {
    try {
        const request = await CleaningRequest.findById(req.params.id);
        if (!request) {
            return res.status(404).json({ message: 'Cleaning request not found' });
        }
        res.status(200).json(request);
    } catch (error) {
        console.error('Error fetching cleaning request:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Update a cleaning request by ID
app.put('/api/cleaning-requests/:id', async (req, res) => {
    try {
        const { partName, cleaningType } = req.body;
        const request = await CleaningRequest.findByIdAndUpdate(
            req.params.id,
            { partName, cleaningType },
            { new: true, runValidators: true }
        );

        if (!request) {
            return res.status(404).json({ message: 'Cleaning request not found' });
        }

        // Recalculate estimates
        let estimatedTime, estimatedCost;
        if (cleaningType === 'ultrasonic') {
            estimatedTime = 30;
            estimatedCost = 50;
        } else {
            estimatedTime = 60;
            estimatedCost = 80;
        }

        request.estimatedTime = estimatedTime;
        request.estimatedCost = estimatedCost;
        await request.save();

        res.status(200).json(request);
    } catch (error) {
        console.error('Error updating cleaning request:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Delete a cleaning request by ID
app.delete('/api/cleaning-requests/:id', async (req, res) => {
    try {
        const request = await CleaningRequest.findByIdAndDelete(req.params.id);
        if (!request) {
            return res.status(404).json({ message: 'Cleaning request not found' });
        }
        res.status(204).send(); // No content
    } catch (error) {
        console.error('Error deleting cleaning request:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
