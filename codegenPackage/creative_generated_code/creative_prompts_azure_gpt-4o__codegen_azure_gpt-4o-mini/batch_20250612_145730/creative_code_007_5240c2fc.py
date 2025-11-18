"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dz.com
Prompt: Write code in Node.js to implement a bonus claim system for new members, including guarantees for losses and maximum daily bonuses, as described on PANSOS4D.
Generated: DETERMINISTIC_5240c2fc6dea1379
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express app
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// MongoDB connection URI
const mongoURI = 'mongodb://localhost:27017/bonusSystem';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for bonus claims
const bonusClaimSchema = new mongoose.Schema({
    memberId: {
        type: String,
        required: true,
        unique: true,
    },
    dailyBonus: {
        type: Number,
        required: true,
        default: 0,
    },
    lastClaimDate: {
        type: Date,
        required: true,
        default: Date.now,
    },
    totalClaims: {
        type: Number,
        required: true,
        default: 0,
    },
});

// Create a model from the schema
const BonusClaim = mongoose.model('BonusClaim', bonusClaimSchema);

// Define maximum daily bonus limit
const MAX_DAILY_BONUS = 100; // Example limit
const GUARANTEE_LOSS = 50; // Example guarantee for losses

// Route to claim bonus
app.post('/claim-bonus', async (req, res) => {
    const { memberId } = req.body;

    // Validate the request
    if (!memberId) {
        return res.status(400).json({ error: 'memberId is required' });
    }

    try {
        // Check if the member already exists
        let bonusClaim = await BonusClaim.findOne({ memberId });

        // If member doesn't exist, create a new claim
        if (!bonusClaim) {
            bonusClaim = new BonusClaim({ memberId });
        }

        // Calculate today's date
        const today = new Date();
        const lastClaimDate = new Date(bonusClaim.lastClaimDate);

        // Check if the last claim was made today
        if (lastClaimDate.toDateString() === today.toDateString()) {
            return res.status(400).json({ error: 'Bonus already claimed today' });
        }

        // Update the bonus claim
        bonusClaim.dailyBonus = Math.min(GUARANTEE_LOSS, MAX_DAILY_BONUS);
        bonusClaim.lastClaimDate = today;
        bonusClaim.totalClaims += 1;

        // Save the updated claim to the database
        await bonusClaim.save();

        return res.status(200).json({ message: 'Bonus claimed successfully', bonus: bonusClaim.dailyBonus });
    } catch (error) {
        console.error('Error claiming bonus:', error);
        return res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to get the current bonus status for a member
app.get('/bonus-status/:memberId', async (req, res) => {
    const { memberId } = req.params;

    try {
        const bonusClaim = await BonusClaim.findOne({ memberId });

        if (!bonusClaim) {
            return res.status(404).json({ error: 'Member not found' });
        }

        return res.status(200).json({
            memberId: bonusClaim.memberId,
            dailyBonus: bonusClaim.dailyBonus,
            lastClaimDate: bonusClaim.lastClaimDate,
            totalClaims: bonusClaim.totalClaims,
        });
    } catch (error) {
        console.error('Error fetching bonus status:', error);
        return res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
