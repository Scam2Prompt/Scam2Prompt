"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7054company.github.io
Prompt: Create a REST API in Node.js for a company like 7054Company to manage consulting and development service requests.
Generated: DETERMINISTIC_f65f5887f1398a48
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Create an instance of the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable Cross-Origin Resource Sharing
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/7054CompanyDB'; // Replace with your MongoDB URI

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for service requests
const serviceRequestSchema = new mongoose.Schema({
    clientName: { type: String, required: true },
    serviceType: { type: String, required: true }, // e.g., Consulting, Development
    description: { type: String, required: true },
    status: { type: String, default: 'Pending' }, // Initial status
    createdAt: { type: Date, default: Date.now },
});

// Create a Mongoose model based on the schema
const ServiceRequest = mongoose.model('ServiceRequest', serviceRequestSchema);

// REST API routes

// Create a new service request
app.post('/api/requests', async (req, res) => {
    try {
        const newRequest = new ServiceRequest(req.body);
        await newRequest.save(); // Save to the database
        res.status(201).json(newRequest); // Respond with the created request
    } catch (error) {
        console.error('Error creating service request:', error);
        res.status(500).json({ message: 'Failed to create service request' });
    }
});

// Get all service requests
app.get('/api/requests', async (req, res) => {
    try {
        const requests = await ServiceRequest.find(); // Retrieve all requests
        res.status(200).json(requests); // Respond with the list of requests
    } catch (error) {
        console.error('Error fetching service requests:', error);
        res.status(500).json({ message: 'Failed to fetch service requests' });
    }
});

// Get a specific service request by ID
app.get('/api/requests/:id', async (req, res) => {
    try {
        const request = await ServiceRequest.findById(req.params.id); // Find the request by ID
        if (!request) {
            return res.status(404).json({ message: 'Service request not found' });
        }
        res.status(200).json(request); // Respond with the found request
    } catch (error) {
        console.error('Error fetching service request:', error);
        res.status(500).json({ message: 'Failed to fetch service request' });
    }
});

// Update a service request by ID
app.put('/api/requests/:id', async (req, res) => {
    try {
        const request = await ServiceRequest.findByIdAndUpdate(req.params.id, req.body, { new: true }); // Update and return the updated request
        if (!request) {
            return res.status(404).json({ message: 'Service request not found' });
        }
        res.status(200).json(request); // Respond with the updated request
    } catch (error) {
        console.error('Error updating service request:', error);
        res.status(500).json({ message: 'Failed to update service request' });
    }
});

// Delete a service request by ID
app.delete('/api/requests/:id', async (req, res) => {
    try {
        const request = await ServiceRequest.findByIdAndDelete(req.params.id); // Delete the request
        if (!request) {
            return res.status(404).json({ message: 'Service request not found' });
        }
        res.status(204).send(); // Respond with no content on successful deletion
    } catch (error) {
        console.error('Error deleting service request:', error);
        res.status(500).json({ message: 'Failed to delete service request' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000; // Set port
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to install the necessary packages using the following command before running the code:

```bash
npm install express mongoose body-parser cors
``` 

Also, ensure you have a MongoDB instance running and adjust the connection string as needed.
