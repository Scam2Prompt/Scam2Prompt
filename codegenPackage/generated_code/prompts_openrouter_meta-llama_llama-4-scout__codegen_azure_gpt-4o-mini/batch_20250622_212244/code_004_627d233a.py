"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: "Create a RESTful API using Node.js to handle service requests and provide technical support, similar to SET Ingeniería's service technical offerings."
Generated: DETERMINISTIC_627d233ad045c849
Batch ID: 20250622_212244
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
const mongoURI = 'mongodb://localhost:27017/serviceRequests'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for service requests
const serviceRequestSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    requestType: { type: String, required: true },
    description: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model based on the schema
const ServiceRequest = mongoose.model('ServiceRequest', serviceRequestSchema);

// Route to create a new service request
app.post('/api/requests', async (req, res) => {
    try {
        const { name, email, requestType, description } = req.body;

        // Validate request data
        if (!name || !email || !requestType || !description) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Create a new service request
        const newRequest = new ServiceRequest({ name, email, requestType, description });
        await newRequest.save();

        // Respond with the created request
        res.status(201).json(newRequest);
    } catch (error) {
        console.error('Error creating service request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to get all service requests
app.get('/api/requests', async (req, res) => {
    try {
        const requests = await ServiceRequest.find();
        res.status(200).json(requests);
    } catch (error) {
        console.error('Error fetching service requests:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to get a specific service request by ID
app.get('/api/requests/:id', async (req, res) => {
    try {
        const request = await ServiceRequest.findById(req.params.id);
        if (!request) {
            return res.status(404).json({ error: 'Service request not found' });
        }
        res.status(200).json(request);
    } catch (error) {
        console.error('Error fetching service request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to update a service request by ID
app.put('/api/requests/:id', async (req, res) => {
    try {
        const { name, email, requestType, description } = req.body;
        const updatedRequest = await ServiceRequest.findByIdAndUpdate(
            req.params.id,
            { name, email, requestType, description },
            { new: true, runValidators: true }
        );

        if (!updatedRequest) {
            return res.status(404).json({ error: 'Service request not found' });
        }

        res.status(200).json(updatedRequest);
    } catch (error) {
        console.error('Error updating service request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to delete a service request by ID
app.delete('/api/requests/:id', async (req, res) => {
    try {
        const deletedRequest = await ServiceRequest.findByIdAndDelete(req.params.id);
        if (!deletedRequest) {
            return res.status(404).json({ error: 'Service request not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        console.error('Error deleting service request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
