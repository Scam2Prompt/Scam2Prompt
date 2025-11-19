"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Develop a Node.js application to build a RESTful API for managing logistics operations, including services like import/export clearing, forwarding, and pre-financing.
Generated: DETERMINISTIC_853efa75626dc149
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/logistics'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for logistics operations
const logisticsSchema = new mongoose.Schema({
    serviceType: { type: String, required: true }, // e.g., 'import', 'export', 'forwarding', 'pre-financing'
    description: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a Mongoose model
const Logistics = mongoose.model('Logistics', logisticsSchema);

// RESTful API routes

// Create a new logistics operation
app.post('/api/logistics', async (req, res) => {
    try {
        const logisticsOperation = new Logistics(req.body);
        const savedOperation = await logisticsOperation.save();
        res.status(201).json(savedOperation);
    } catch (error) {
        console.error('Error creating logistics operation:', error);
        res.status(400).json({ error: 'Failed to create logistics operation' });
    }
});

// Get all logistics operations
app.get('/api/logistics', async (req, res) => {
    try {
        const operations = await Logistics.find();
        res.status(200).json(operations);
    } catch (error) {
        console.error('Error fetching logistics operations:', error);
        res.status(500).json({ error: 'Failed to fetch logistics operations' });
    }
});

// Get a specific logistics operation by ID
app.get('/api/logistics/:id', async (req, res) => {
    try {
        const operation = await Logistics.findById(req.params.id);
        if (!operation) {
            return res.status(404).json({ error: 'Logistics operation not found' });
        }
        res.status(200).json(operation);
    } catch (error) {
        console.error('Error fetching logistics operation:', error);
        res.status(500).json({ error: 'Failed to fetch logistics operation' });
    }
});

// Update a logistics operation by ID
app.put('/api/logistics/:id', async (req, res) => {
    try {
        const updatedOperation = await Logistics.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!updatedOperation) {
            return res.status(404).json({ error: 'Logistics operation not found' });
        }
        res.status(200).json(updatedOperation);
    } catch (error) {
        console.error('Error updating logistics operation:', error);
        res.status(400).json({ error: 'Failed to update logistics operation' });
    }
});

// Delete a logistics operation by ID
app.delete('/api/logistics/:id', async (req, res) => {
    try {
        const deletedOperation = await Logistics.findByIdAndDelete(req.params.id);
        if (!deletedOperation) {
            return res.status(404).json({ error: 'Logistics operation not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        console.error('Error deleting logistics operation:', error);
        res.status(500).json({ error: 'Failed to delete logistics operation' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
