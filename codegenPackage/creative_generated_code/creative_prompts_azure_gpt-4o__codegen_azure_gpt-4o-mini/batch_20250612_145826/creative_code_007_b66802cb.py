"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimxbox.web.app
Prompt: Create a Node.js backend API for verifying assets and managing reward claims in an AlienX-style airdrop system.
Generated: DETERMINISTIC_b66802cb2de8cebc
Batch ID: 20250612_145826
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Express framework for building the API
const mongoose = require('mongoose'); // Mongoose for MongoDB interactions
const bodyParser = require('body-parser'); // Body parser for parsing request bodies
const cors = require('cors'); // Middleware for enabling CORS
const { check, validationResult } = require('express-validator'); // Validation middleware

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(cors()); // Enable CORS
app.use(bodyParser.json()); // Parse JSON bodies

// MongoDB connection setup
const mongoURI = process.env.MONGODB_URI || 'mongodb://localhost:27017/airdropDB';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schema and model for assets
const assetSchema = new mongoose.Schema({
    assetId: { type: String, required: true, unique: true },
    owner: { type: String, required: true },
    verified: { type: Boolean, default: false }
});
const Asset = mongoose.model('Asset', assetSchema);

// Define Mongoose schema and model for reward claims
const claimSchema = new mongoose.Schema({
    assetId: { type: String, required: true },
    claimedAt: { type: Date, default: Date.now }
});
const Claim = mongoose.model('Claim', claimSchema);

// API Endpoint to verify an asset
app.post('/api/verifyAsset', [
    check('assetId').isString().notEmpty(),
    check('owner').isString().notEmpty()
], async (req, res) => {
    // Validate request
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    const { assetId, owner } = req.body;

    try {
        // Check if asset already exists
        let asset = await Asset.findOne({ assetId });

        if (asset) {
            return res.status(400).json({ message: 'Asset already verified' });
        }

        // Create and save the new asset
        asset = new Asset({ assetId, owner, verified: true });
        await asset.save();

        return res.status(201).json({ message: 'Asset verified successfully', asset });
    } catch (error) {
        console.error('Verification error:', error);
        return res.status(500).json({ message: 'Internal Server Error' });
    }
});

// API Endpoint to manage reward claims
app.post('/api/claimReward', [
    check('assetId').isString().notEmpty()
], async (req, res) => {
    // Validate request
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    const { assetId } = req.body;

    try {
        // Check if the asset exists and is verified
        const asset = await Asset.findOne({ assetId, verified: true });
        if (!asset) {
            return res.status(404).json({ message: 'Asset not found or not verified' });
        }

        // Check if the reward has already been claimed
        const existingClaim = await Claim.findOne({ assetId });
        if (existingClaim) {
            return res.status(400).json({ message: 'Reward already claimed for this asset' });
        }

        // Create and save the new claim
        const claim = new Claim({ assetId });
        await claim.save();

        return res.status(201).json({ message: 'Reward claimed successfully', claim });
    } catch (error) {
        console.error('Claim error:', error);
        return res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
