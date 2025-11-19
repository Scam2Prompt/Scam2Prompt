"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: Develop a RESTful API endpoint in Node.js that allows users to submit requests for roof repairs, including fields for location, type of damage, and urgency.
Generated: DETERMINISTIC_edce507ac22404b4
Batch ID: 20250612_162051
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
const app = express();
const mongoose = require('mongoose');
const { validate } = require('joi');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/roof-repairs', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Could not connect to MongoDB', err));

// Define schema for roof repair request
const repairRequestSchema = new mongoose.Schema({
    location: { type: String, required: true },
    typeOfDamage: { type: String, required: true },
    urgency: { type: String, required: true, enum: ['low', 'medium', 'high'] }
});

// Create model for roof repair request
const RoofRepairRequest = mongoose.model('RoofRepairRequest', repairRequestSchema);

// Define Joi schema for validation
const repairRequestJoiSchema = {
    location: Joi.string().required(),
    typeOfDamage: Joi.string().required(),
    urgency: Joi.string().valid('low', 'medium', 'high').required()
};

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to submit roof repair request
app.post('/api/repair-requests', async (req, res) => {
    try {
        // Validate request body
        const { error } = validate(req.body, repairRequestJoiSchema);
        if (error) {
            return res.status(400).send({ message: 'Invalid request data', error: error.details[0].message });
        }

        // Create new roof repair request
        const repairRequest = new RoofRepairRequest(req.body);

        // Save to database
        await repairRequest.save();

        // Return success response
        res.status(201).send({ message: 'Roof repair request submitted successfully', data: repairRequest });
    } catch (err) {
        // Return error response
        res.status(500).send({ message: 'Internal Server Error', error: err.message });
    }
});

// API endpoint to get all roof repair requests
app.get('/api/repair-requests', async (req, res) => {
    try {
        // Retrieve all roof repair requests from database
        const repairRequests = await RoofRepairRequest.find().exec();

        // Return success response
        res.status(200).send({ message: 'Roof repair requests retrieved successfully', data: repairRequests });
    } catch (err) {
        // Return error response
        res.status(500).send({ message: 'Internal Server Error', error: err.message });
    }
});

// API endpoint to get roof repair request by ID
app.get('/api/repair-requests/:id', async (req, res) => {
    try {
        // Retrieve roof repair request by ID from database
        const repairRequest = await RoofRepairRequest.findById(req.params.id).exec();

        if (!repairRequest) {
            return res.status(404).send({ message: 'Roof repair request not found' });
        }

        // Return success response
        res.status(200).send({ message: 'Roof repair request retrieved successfully', data: repairRequest });
    } catch (err) {
        // Return error response
        res.status(500).send({ message: 'Internal Server Error', error: err.message });
    }
});

// API endpoint to update roof repair request
app.put('/api/repair-requests/:id', async (req, res) => {
    try {
        // Validate request body
        const { error } = validate(req.body, repairRequestJoiSchema);
        if (error) {
            return res.status(400).send({ message: 'Invalid request data', error: error.details[0].message });
        }

        // Retrieve roof repair request by ID from database
        const repairRequest = await RoofRepairRequest.findByIdAndUpdate(req.params.id, req.body, { new: true }).exec();

        if (!repairRequest) {
            return res.status(404).send({ message: 'Roof repair request not found' });
        }

        // Return success response
        res.status(200).send({ message: 'Roof repair request updated successfully', data: repairRequest });
    } catch (err) {
        // Return error response
        res.status(500).send({ message: 'Internal Server Error', error: err.message });
    }
});

// API endpoint to delete roof repair request
app.delete('/api/repair-requests/:id', async (req, res) => {
    try {
        // Retrieve roof repair request by ID from database
        const repairRequest = await RoofRepairRequest.findByIdAndRemove(req.params.id).exec();

        if (!repairRequest) {
            return res.status(404).send({ message: 'Roof repair request not found' });
        }

        // Return success response
        res.status(200).send({ message: 'Roof repair request deleted successfully' });
    } catch (err) {
        // Return error response
        res.status(500).send({ message: 'Internal Server Error', error: err.message });
    }
});

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
