"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: "Create a RESTful API in Node.js for managing insurance policies, including endpoints for creating, reading, updating, and deleting policies, inspired by the services offered by Recuperación JC."
Generated: DETERMINISTIC_7c0324b2e540ad95
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
const app = express();
const mongoose = require('mongoose');
const policyModel = require('./models/Policy');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/insuranceDB', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Could not connect to MongoDB', err));

// Middleware to parse JSON bodies
app.use(express.json());

// Policy Model
// ===========

// In models/Policy.js
// const mongoose = require('mongoose');
// const policySchema = new mongoose.Schema({
//     policyNumber: String,
//     customerName: String,
//     policyType: String,
//     startDate: Date,
//     endDate: Date,
//     premium: Number
// });
// module.exports = mongoose.model('Policy', policySchema);

// API Endpoints
// ===========

// Get all policies
app.get('/api/policies', async (req, res) => {
    try {
        const policies = await policyModel.find().exec();
        res.json(policies);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Get policy by ID
app.get('/api/policies/:id', async (req, res) => {
    try {
        const policy = await policyModel.findById(req.params.id).exec();
        if (!policy) {
            res.status(404).json({ message: 'Policy not found' });
        } else {
            res.json(policy);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Create a new policy
app.post('/api/policies', async (req, res) => {
    try {
        const policy = new policyModel(req.body);
        await policy.save();
        res.status(201).json(policy);
    } catch (err) {
        console.error(err);
        if (err.name === 'ValidationError') {
            res.status(400).json({ message: 'Invalid request data' });
        } else {
            res.status(500).json({ message: 'Internal Server Error' });
        }
    }
});

// Update a policy
app.put('/api/policies/:id', async (req, res) => {
    try {
        const policy = await policyModel.findByIdAndUpdate(req.params.id, req.body, { new: true }).exec();
        if (!policy) {
            res.status(404).json({ message: 'Policy not found' });
        } else {
            res.json(policy);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Delete a policy
app.delete('/api/policies/:id', async (req, res) => {
    try {
        await policyModel.findByIdAndRemove(req.params.id).exec();
        res.status(204).json({ message: 'Policy deleted successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
```

```javascript
// models/Policy.js
const mongoose = require('mongoose');

const policySchema = new mongoose.Schema({
    policyNumber: {
        type: String,
        required: true,
        unique: true
    },
    customerName: {
        type: String,
        required: true
    },
    policyType: {
        type: String,
        required: true
    },
    startDate: {
        type: Date,
        required: true
    },
    endDate: {
        type: Date,
        required: true
    },
    premium: {
        type: Number,
        required: true
    }
});

module.exports = mongoose.model('Policy', policySchema);
```
