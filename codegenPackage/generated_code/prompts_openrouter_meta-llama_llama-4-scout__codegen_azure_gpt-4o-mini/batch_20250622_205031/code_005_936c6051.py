"""
Generated Code Metadata:
========================
Original URL: https://www.coupangeatsplus.info
Prompt: Design a simple backend API using Node.js to manage customer applications and support requests for a service like 쿠팡이츠플러스, including handling of additional zone charges.
Generated: DETERMINISTIC_936c6051515c71f9
Batch ID: 20250622_205031
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
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/customerSupport'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for customer applications and support requests
const requestSchema = new mongoose.Schema({
    customerName: { type: String, required: true },
    requestType: { type: String, enum: ['application', 'support'], required: true },
    description: { type: String, required: true },
    zoneCharge: { type: Number, default: 0 },
    createdAt: { type: Date, default: Date.now }
});

// Create a model based on the schema
const Request = mongoose.model('Request', requestSchema);

// API endpoint to create a new request
app.post('/api/requests', async (req, res) => {
    try {
        const { customerName, requestType, description, zoneCharge } = req.body;

        // Validate request data
        if (!customerName || !requestType || !description) {
            return res.status(400).json({ error: 'Customer name, request type, and description are required.' });
        }

        // Create a new request
        const newRequest = new Request({ customerName, requestType, description, zoneCharge });
        await newRequest.save();

        // Respond with the created request
        res.status(201).json(newRequest);
    } catch (error) {
        console.error('Error creating request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to get all requests
app.get('/api/requests', async (req, res) => {
    try {
        const requests = await Request.find();
        res.status(200).json(requests);
    } catch (error) {
        console.error('Error fetching requests:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to get a specific request by ID
app.get('/api/requests/:id', async (req, res) => {
    try {
        const request = await Request.findById(req.params.id);
        if (!request) {
            return res.status(404).json({ error: 'Request not found' });
        }
        res.status(200).json(request);
    } catch (error) {
        console.error('Error fetching request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to update a request by ID
app.put('/api/requests/:id', async (req, res) => {
    try {
        const { customerName, requestType, description, zoneCharge } = req.body;
        const updatedRequest = await Request.findByIdAndUpdate(req.params.id, { customerName, requestType, description, zoneCharge }, { new: true });

        if (!updatedRequest) {
            return res.status(404).json({ error: 'Request not found' });
        }

        res.status(200).json(updatedRequest);
    } catch (error) {
        console.error('Error updating request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to delete a request by ID
app.delete('/api/requests/:id', async (req, res) => {
    try {
        const deletedRequest = await Request.findByIdAndDelete(req.params.id);
        if (!deletedRequest) {
            return res.status(404).json({ error: 'Request not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        console.error('Error deleting request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
