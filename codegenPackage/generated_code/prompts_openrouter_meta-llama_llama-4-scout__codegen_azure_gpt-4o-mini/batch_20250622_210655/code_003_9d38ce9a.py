"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Develop a RESTful API using Node.js and Express.js to manage customer requests for home maintenance services, including services like gas installation and painting.
Generated: DETERMINISTIC_9d38ce9a0923025a
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

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace 'your_connection_string' with your actual connection string)
mongoose.connect('your_connection_string', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for customer requests
const requestSchema = new mongoose.Schema({
    customerName: { type: String, required: true },
    serviceType: { type: String, required: true, enum: ['Gas Installation', 'Painting'] },
    description: { type: String, required: true },
    status: { type: String, default: 'Pending', enum: ['Pending', 'In Progress', 'Completed'] },
    createdAt: { type: Date, default: Date.now }
});

// Create a model based on the schema
const Request = mongoose.model('Request', requestSchema);

// Route to create a new customer request
app.post('/api/requests', async (req, res) => {
    try {
        const newRequest = new Request(req.body);
        const savedRequest = await newRequest.save();
        res.status(201).json(savedRequest);
    } catch (error) {
        res.status(400).json({ message: 'Error creating request', error: error.message });
    }
});

// Route to get all customer requests
app.get('/api/requests', async (req, res) => {
    try {
        const requests = await Request.find();
        res.status(200).json(requests);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching requests', error: error.message });
    }
});

// Route to get a specific customer request by ID
app.get('/api/requests/:id', async (req, res) => {
    try {
        const request = await Request.findById(req.params.id);
        if (!request) {
            return res.status(404).json({ message: 'Request not found' });
        }
        res.status(200).json(request);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching request', error: error.message });
    }
});

// Route to update a customer request by ID
app.put('/api/requests/:id', async (req, res) => {
    try {
        const updatedRequest = await Request.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedRequest) {
            return res.status(404).json({ message: 'Request not found' });
        }
        res.status(200).json(updatedRequest);
    } catch (error) {
        res.status(400).json({ message: 'Error updating request', error: error.message });
    }
});

// Route to delete a customer request by ID
app.delete('/api/requests/:id', async (req, res) => {
    try {
        const deletedRequest = await Request.findByIdAndDelete(req.params.id);
        if (!deletedRequest) {
            return res.status(404).json({ message: 'Request not found' });
        }
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: 'Error deleting request', error: error.message });
    }
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
