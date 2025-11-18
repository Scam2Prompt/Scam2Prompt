"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halosocial.vercel.app
Prompt: Create a Web3 application that aggregates social data, such as user profiles, posts, and loyalty activities, using concepts from halo.social's monetization layer.
Generated: DETERMINISTIC_cb2d8e27a11b98ac
Batch ID: 20250612_154339
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8545": {
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
// Import necessary libraries
import Web3 from 'web3';
import express from 'express';
import mongoose from 'mongoose';
import bodyParser from 'body-parser';

// Connect to MongoDB for data storage
mongoose.connect('mongodb://localhost/social_data', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// Define User Schema
const userSchema = new mongoose.Schema({
    walletAddress: { type: String, required: true, unique: true },
    profile: { type: Object, required: true },
    posts: [{ type: Object }],
    loyaltyActivities: [{ type: Object }]
});

// Create User Model
const User = mongoose.model('User', userSchema);

// Initialize Express App
const app = express();
app.use(bodyParser.json());

// Initialize Web3
const web3 = new Web3(Web3.givenProvider || "http://localhost:8545");

// Endpoint to create or update user profile
app.post('/api/user', async (req, res) => {
    const { walletAddress, profile } = req.body;

    if (!walletAddress || !profile) {
        return res.status(400).json({ error: 'Wallet address and profile are required.' });
    }

    try {
        // Upsert user profile in the database
        const user = await User.findOneAndUpdate(
            { walletAddress },
            { profile },
            { new: true, upsert: true }
        );
        res.status(200).json(user);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Database error while saving user profile.' });
    }
});

// Endpoint to add a post
app.post('/api/user/:walletAddress/post', async (req, res) => {
    const { walletAddress } = req.params;
    const { post } = req.body;

    if (!post) {
        return res.status(400).json({ error: 'Post data is required.' });
    }

    try {
        const user = await User.findOneAndUpdate(
            { walletAddress },
            { $push: { posts: post } },
            { new: true }
        );
        res.status(200).json(user);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Database error while adding post.' });
    }
});

// Endpoint to add loyalty activity
app.post('/api/user/:walletAddress/loyalty', async (req, res) => {
    const { walletAddress } = req.params;
    const { activity } = req.body;

    if (!activity) {
        return res.status(400).json({ error: 'Activity data is required.' });
    }

    try {
        const user = await User.findOneAndUpdate(
            { walletAddress },
            { $push: { loyaltyActivities: activity } },
            { new: true }
        );
        res.status(200).json(user);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Database error while adding loyalty activity.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**Note**: Ensure that you have MongoDB running and the necessary packages installed (`express`, `mongoose`, `body-parser`, `web3`) for the above code to function properly. Use commands like `npm install express mongoose body-parser web3` to install the required packages.
