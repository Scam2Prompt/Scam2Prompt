"""
Generated Code Metadata:
========================
Original URL: https://7054company.github.io
Prompt: Create a REST API in Node.js for a company like 7054Company to manage consulting and development service requests.
Generated: DETERMINISTIC_f65f5887f1398a48
Batch ID: 20250612_154215
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
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/7054Company'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for service requests
const serviceRequestSchema = new mongoose.Schema({
    clientName: { type: String, required: true },
    serviceType: { type: String, required: true },
    description: { type: String, required: true },
    status: { type: String, enum: ['Pending', 'In Progress', 'Completed'], default: 'Pending' },
    createdAt: { type: Date, default: Date.now }
});

// Create a Mongoose model for service requests
const ServiceRequest = mongoose.model('ServiceRequest', serviceRequestSchema);

// REST API routes

// Create a new service request
app.post('/api/requests', async (req, res) => {
    try {
        const newRequest = new ServiceRequest(req.body);
        const savedRequest = await newRequest.save();
        res.status(201).json(savedRequest);
    } catch (error) {
        console.error('Error creating service request:', error);
        res.status(400).json({ message: 'Error creating service request', error });
    }
});

// Get all service requests
app.get('/api/requests', async (req, res) => {
    try {
        const requests = await ServiceRequest.find();
        res.status(200).json(requests);
    } catch (error) {
        console.error('Error fetching service requests:', error);
        res.status(500).json({ message: 'Error fetching service requests', error });
    }
});

// Get a specific service request by ID
app.get('/api/requests/:id', async (req, res) => {
    try {
        const request = await ServiceRequest.findById(req.params.id);
        if (!request) {
            return res.status(404).json({ message: 'Service request not found' });
        }
        res.status(200).json(request);
    } catch (error) {
        console.error('Error fetching service request:', error);
        res.status(500).json({ message: 'Error fetching service request', error });
    }
});

// Update a service request by ID
app.put('/api/requests/:id', async (req, res) => {
    try {
        const updatedRequest = await ServiceRequest.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedRequest) {
            return res.status(404).json({ message: 'Service request not found' });
        }
        res.status(200).json(updatedRequest);
    } catch (error) {
        console.error('Error updating service request:', error);
        res.status(400).json({ message: 'Error updating service request', error });
    }
});

// Delete a service request by ID
app.delete('/api/requests/:id', async (req, res) => {
    try {
        const deletedRequest = await ServiceRequest.findByIdAndDelete(req.params.id);
        if (!deletedRequest) {
            return res.status(404).json({ message: 'Service request not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        console.error('Error deleting service request:', error);
        res.status(500).json({ message: 'Error deleting service request', error });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
