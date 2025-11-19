"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: "Create a RESTful API in Node.js for managing public sector contracts, including licitation and outsourcing processes, inspired by Licitare's services."
Generated: DETERMINISTIC_57d44b10e38aad45
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
const mongoURI = 'mongodb://localhost:27017/public_sector_contracts'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for contracts
const contractSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    value: { type: Number, required: true },
    startDate: { type: Date, required: true },
    endDate: { type: Date, required: true },
    status: { type: String, enum: ['active', 'completed', 'cancelled'], default: 'active' },
}, { timestamps: true });

// Create a model for contracts
const Contract = mongoose.model('Contract', contractSchema);

// RESTful API routes

// Create a new contract
app.post('/contracts', async (req, res) => {
    try {
        const contract = new Contract(req.body);
        const savedContract = await contract.save();
        res.status(201).json(savedContract);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Get all contracts
app.get('/contracts', async (req, res) => {
    try {
        const contracts = await Contract.find();
        res.status(200).json(contracts);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Get a contract by ID
app.get('/contracts/:id', async (req, res) => {
    try {
        const contract = await Contract.findById(req.params.id);
        if (!contract) {
            return res.status(404).json({ error: 'Contract not found' });
        }
        res.status(200).json(contract);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Update a contract by ID
app.put('/contracts/:id', async (req, res) => {
    try {
        const contract = await Contract.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!contract) {
            return res.status(404).json({ error: 'Contract not found' });
        }
        res.status(200).json(contract);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Delete a contract by ID
app.delete('/contracts/:id', async (req, res) => {
    try {
        const contract = await Contract.findByIdAndDelete(req.params.id);
        if (!contract) {
            return res.status(404).json({ error: 'Contract not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
