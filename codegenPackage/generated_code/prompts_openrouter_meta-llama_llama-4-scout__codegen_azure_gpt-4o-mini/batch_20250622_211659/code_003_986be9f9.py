"""
Generated Code Metadata:
========================
Original URL: https://popcorn.claims
Prompt: "Design a RESTful API in Node.js for managing claims, including endpoints for submission, review, and approval, with considerations for data privacy."
Generated: DETERMINISTIC_986be9f92261a958
Batch ID: 20250622_211659
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
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define Claim schema
const claimSchema = new mongoose.Schema({
    claimantName: { type: String, required: true },
    claimDetails: { type: String, required: true },
    status: { type: String, enum: ['submitted', 'under_review', 'approved', 'rejected'], default: 'submitted' },
    createdAt: { type: Date, default: Date.now }
});

// Create Claim model
const Claim = mongoose.model('Claim', claimSchema);

// Endpoint to submit a new claim
app.post('/api/claims', async (req, res) => {
    try {
        const { claimantName, claimDetails } = req.body;
        const newClaim = new Claim({ claimantName, claimDetails });
        await newClaim.save();
        res.status(201).json({ message: 'Claim submitted successfully', claim: newClaim });
    } catch (error) {
        console.error('Error submitting claim:', error);
        res.status(500).json({ message: 'Error submitting claim', error: error.message });
    }
});

// Endpoint to get all claims
app.get('/api/claims', async (req, res) => {
    try {
        const claims = await Claim.find();
        res.status(200).json(claims);
    } catch (error) {
        console.error('Error fetching claims:', error);
        res.status(500).json({ message: 'Error fetching claims', error: error.message });
    }
});

// Endpoint to review a claim
app.put('/api/claims/:id/review', async (req, res) => {
    try {
        const { id } = req.params;
        const { status } = req.body;

        if (!['under_review', 'approved', 'rejected'].includes(status)) {
            return res.status(400).json({ message: 'Invalid status' });
        }

        const updatedClaim = await Claim.findByIdAndUpdate(id, { status }, { new: true });
        if (!updatedClaim) {
            return res.status(404).json({ message: 'Claim not found' });
        }

        res.status(200).json({ message: 'Claim status updated', claim: updatedClaim });
    } catch (error) {
        console.error('Error updating claim status:', error);
        res.status(500).json({ message: 'Error updating claim status', error: error.message });
    }
});

// Endpoint to get a specific claim by ID
app.get('/api/claims/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const claim = await Claim.findById(id);
        if (!claim) {
            return res.status(404).json({ message: 'Claim not found' });
        }
        res.status(200).json(claim);
    } catch (error) {
        console.error('Error fetching claim:', error);
        res.status(500).json({ message: 'Error fetching claim', error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### .env file example
```
MONGODB_URI=mongodb://<username>:<password>@localhost:27017/claimsdb
PORT=3000
```

### Note
- Ensure to replace `<username>` and `<password>` with your MongoDB credentials.
- This code assumes you have MongoDB running and accessible at the specified URI.
