"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Develop a RESTful API endpoint in Node.js that allows users to request plumbing inspections and maintenance services, ensuring it includes location-based filtering for Graham, TX.
Generated: DETERMINISTIC_b48054194a6ae3a6
Batch ID: 20250612_164035
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
mongoose.connect('mongodb://localhost:27017/plumbingServices', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a schema for plumbing service requests
const serviceRequestSchema = new mongoose.Schema({
    name: { type: String, required: true },
    address: { type: String, required: true },
    city: { type: String, required: true, default: 'Graham' },
    serviceType: { type: String, required: true },
    dateRequested: { type: Date, default: Date.now },
});

// Create a model based on the schema
const ServiceRequest = mongoose.model('ServiceRequest', serviceRequestSchema);

// API endpoint to request plumbing services
app.post('/api/service-requests', async (req, res) => {
    try {
        // Validate request body
        const { name, address, serviceType } = req.body;
        if (!name || !address || !serviceType) {
            return res.status(400).json({ error: 'Name, address, and service type are required.' });
        }

        // Create a new service request
        const newRequest = new ServiceRequest({
            name,
            address,
            serviceType,
            city: 'Graham', // Ensure city is set to Graham
        });

        // Save the request to the database
        await newRequest.save();
        res.status(201).json({ message: 'Service request created successfully.', request: newRequest });
    } catch (error) {
        console.error('Error creating service request:', error);
        res.status(500).json({ error: 'An error occurred while creating the service request.' });
    }
});

// API endpoint to get service requests filtered by location
app.get('/api/service-requests', async (req, res) => {
    try {
        // Filter requests by city
        const requests = await ServiceRequest.find({ city: 'Graham' });
        res.status(200).json(requests);
    } catch (error) {
        console.error('Error fetching service requests:', error);
        res.status(500).json({ error: 'An error occurred while fetching service requests.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
