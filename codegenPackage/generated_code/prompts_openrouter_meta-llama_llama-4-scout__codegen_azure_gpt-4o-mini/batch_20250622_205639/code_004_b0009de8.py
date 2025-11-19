"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Develop a basic API using Node.js to retrieve information about successful PPI claims and their corresponding compensation amounts from a database, similar to Financial Recovery Solutions' services.
Generated: DETERMINISTIC_b0009de8f4eb0901
Batch ID: 20250622_205639
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

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/ppiClaimsDB'; // Update with your MongoDB URI

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for PPI claims
const ppiClaimSchema = new mongoose.Schema({
    claimantName: { type: String, required: true },
    claimAmount: { type: Number, required: true },
    compensationAmount: { type: Number, required: true },
    dateClaimed: { type: Date, default: Date.now }
});

// Create a model based on the schema
const PPIClaim = mongoose.model('PPIClaim', ppiClaimSchema);

// API endpoint to retrieve all successful PPI claims
app.get('/api/claims', async (req, res) => {
    try {
        const claims = await PPIClaim.find(); // Fetch all claims from the database
        res.status(200).json(claims); // Send the claims as a JSON response
    } catch (error) {
        console.error('Error retrieving claims:', error);
        res.status(500).json({ message: 'Internal server error' }); // Handle errors
    }
});

// API endpoint to retrieve a specific claim by ID
app.get('/api/claims/:id', async (req, res) => {
    try {
        const claim = await PPIClaim.findById(req.params.id); // Fetch claim by ID
        if (!claim) {
            return res.status(404).json({ message: 'Claim not found' }); // Handle not found
        }
        res.status(200).json(claim); // Send the claim as a JSON response
    } catch (error) {
        console.error('Error retrieving claim:', error);
        res.status(500).json({ message: 'Internal server error' }); // Handle errors
    }
});

// API endpoint to create a new PPI claim
app.post('/api/claims', async (req, res) => {
    const { claimantName, claimAmount, compensationAmount } = req.body;

    // Validate request body
    if (!claimantName || !claimAmount || !compensationAmount) {
        return res.status(400).json({ message: 'All fields are required' }); // Handle validation errors
    }

    try {
        const newClaim = new PPIClaim({ claimantName, claimAmount, compensationAmount });
        await newClaim.save(); // Save the new claim to the database
        res.status(201).json(newClaim); // Send the created claim as a JSON response
    } catch (error) {
        console.error('Error creating claim:', error);
        res.status(500).json({ message: 'Internal server error' }); // Handle errors
    }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default to 3000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`); // Log server start
});
```
