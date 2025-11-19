"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Develop a RESTful API using Node.js and Express.js to manage membership information for a professional organization like the Colegio de Psicologos de Oruro.
Generated: DETERMINISTIC_aa3654022a9b2b40
Batch ID: 20250622_212724
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

// Initialize the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/membershipDB'; // Update with your MongoDB URI

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Membership schema
const membershipSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    membershipType: { type: String, required: true },
    joinDate: { type: Date, default: Date.now }
});

// Create a Membership model
const Membership = mongoose.model('Membership', membershipSchema);

// API endpoint to create a new membership
app.post('/api/members', async (req, res) => {
    try {
        const newMember = new Membership(req.body);
        const savedMember = await newMember.save();
        res.status(201).json(savedMember);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// API endpoint to get all members
app.get('/api/members', async (req, res) => {
    try {
        const members = await Membership.find();
        res.status(200).json(members);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// API endpoint to get a member by ID
app.get('/api/members/:id', async (req, res) => {
    try {
        const member = await Membership.findById(req.params.id);
        if (!member) {
            return res.status(404).json({ error: 'Member not found' });
        }
        res.status(200).json(member);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// API endpoint to update a member by ID
app.put('/api/members/:id', async (req, res) => {
    try {
        const updatedMember = await Membership.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedMember) {
            return res.status(404).json({ error: 'Member not found' });
        }
        res.status(200).json(updatedMember);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// API endpoint to delete a member by ID
app.delete('/api/members/:id', async (req, res) => {
    try {
        const deletedMember = await Membership.findByIdAndDelete(req.params.id);
        if (!deletedMember) {
            return res.status(404).json({ error: 'Member not found' });
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
