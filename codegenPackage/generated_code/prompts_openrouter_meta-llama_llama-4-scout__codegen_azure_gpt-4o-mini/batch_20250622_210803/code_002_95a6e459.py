"""
Generated Code Metadata:
========================
Original URL: https://calanguteescorts.com
Prompt: Generate a RESTful API endpoint using Node.js and Express.js to create, read, update, and delete (CRUD) escort listings, inspired by the content and structure of https://calanguteescorts.com.
Generated: DETERMINISTIC_95a6e45923950a47
Batch ID: 20250622_210803
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

// Connect to MongoDB (replace with your own connection string)
mongoose.connect('mongodb://localhost:27017/escortListings', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define the Escort schema
const escortSchema = new mongoose.Schema({
    name: { type: String, required: true },
    age: { type: Number, required: true },
    description: { type: String, required: true },
    services: { type: [String], required: true },
    location: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create the Escort model
const Escort = mongoose.model('Escort', escortSchema);

// Create a new escort listing
app.post('/api/escorts', async (req, res) => {
    try {
        const newEscort = new Escort(req.body);
        const savedEscort = await newEscort.save();
        res.status(201).json(savedEscort);
    } catch (error) {
        res.status(400).json({ message: 'Error creating escort listing', error });
    }
});

// Get all escort listings
app.get('/api/escorts', async (req, res) => {
    try {
        const escorts = await Escort.find();
