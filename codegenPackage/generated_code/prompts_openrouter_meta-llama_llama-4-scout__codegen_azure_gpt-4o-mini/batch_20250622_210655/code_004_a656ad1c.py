"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Create a RESTful API using Node.js to handle customer requests for air conditioning cleaning and maintenance services, inspired by شركة إنجاز's offerings in جدة.
Generated: DETERMINISTIC_a656ad1c2b866a43
Batch ID: 20250622_210655
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
const mongoURI = 'mongodb://localhost:27017/ac_service'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for customer requests
const customerRequestSchema = new mongoose.Schema({
    name: { type: String, required: true },
    phone: { type: String, required: true },
    serviceType: { type: String, required: true, enum: ['Cleaning', 'Maintenance'] },
    address: { type: String, required: true },
    date: { type: Date, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a Mongoose model based on the schema
const CustomerRequest = mongoose.model('CustomerRequest', customerRequestSchema);

// Route to create a new customer request
app.post('/api/requests', async (req, res) => {
    try {
        const { name, phone, serviceType, address, date } = req.body;

        // Validate request data
        if (!name || !phone || !serviceType || !address || !date) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Create a new customer request
        const newRequest = new CustomerRequest({ name, phone, serviceType, address, date });
        await newRequest.save();

        // Respond with the created request
        res.status(201).json(newRequest);
    } catch (error) {
        console.error('Error creating request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to get all customer requests
app.get('/api/requests', async (req, res) => {
    try {
        const requests = await CustomerRequest.find();
        res.status(200).json(requests);
    } catch (error) {
        console.error('Error fetching requests:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to get a specific customer request by ID
app.get('/api/requests/:id', async (req, res) => {
    try {
        const request = await CustomerRequest.findById(req.params.id);
        if (!request) {
            return res.status(404).json({ error: 'Request not found' });
        }
        res.status(200).json(request);
    } catch (error) {
        console.error('Error fetching request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to update a customer request by ID
app.put('/api/requests/:id', async (req, res) => {
    try {
        const { name, phone, serviceType, address, date } = req.body;
        const updatedRequest = await CustomerRequest.findByIdAndUpdate(req.params.id, { name, phone, serviceType, address, date }, { new: true });

        if (!updatedRequest) {
            return res.status(404).json({ error: 'Request not found' });
        }

        res.status(200).json(updatedRequest);
    } catch (error) {
        console.error('Error updating request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to delete a customer request by ID
app.delete('/api/requests/:id', async (req, res) => {
    try {
        const deletedRequest = await CustomerRequest.findByIdAndDelete(req.params.id);
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
