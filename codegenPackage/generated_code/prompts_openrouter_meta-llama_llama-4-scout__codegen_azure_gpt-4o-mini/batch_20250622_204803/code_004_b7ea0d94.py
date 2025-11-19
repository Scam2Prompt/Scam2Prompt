"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.net
Prompt: Create a RESTful API in Node.js to manage environmental policies and goals for an organization focused on Umweltschutz, incorporating features similar to those implied on the website.
Generated: DETERMINISTIC_b7ea0d940644c4f8
Batch ID: 20250622_204803
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
const mongoURI = 'mongodb://localhost:27017/environmentalPolicies'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for environmental policies
const policySchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    goals: [{ type: String }],
    createdAt: { type: Date, default: Date.now }
});

// Create a model based on the schema
const Policy = mongoose.model('Policy', policySchema);

// RESTful API routes

// Create a new policy
app.post('/api/policies', async (req, res) => {
    try {
        const policy = new Policy(req.body);
        await policy.save();
        res.status(201).json(policy);
    } catch (error) {
        res.status(400).json({ error: 'Error creating policy: ' + error.message });
    }
});

// Get all policies
app.get('/api/policies', async (req, res) => {
    try {
        const policies = await Policy.find();
        res.status(200).json(policies);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching policies: ' + error.message });
    }
});

// Get a specific policy by ID
app.get('/api/policies/:id', async (req, res) => {
    try {
        const policy = await Policy.findById(req.params.id);
        if (!policy) {
            return res.status(404).json({ error: 'Policy not found' });
        }
        res.status(200).json(policy);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching policy: ' + error.message });
    }
});

// Update a specific policy by ID
app.put('/api/policies/:id', async (req, res) => {
    try {
        const policy = await Policy.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!policy) {
            return res.status(404).json({ error: 'Policy not found' });
        }
        res.status(200).json(policy);
    } catch (error) {
        res.status(400).json({ error: 'Error updating policy: ' + error.message });
    }
});

// Delete a specific policy by ID
app.delete('/api/policies/:id', async (req, res) => {
    try {
        const policy = await Policy.findByIdAndDelete(req.params.id);
        if (!policy) {
            return res.status(404).json({ error: 'Policy not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        res.status(500).json({ error: 'Error deleting policy: ' + error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
