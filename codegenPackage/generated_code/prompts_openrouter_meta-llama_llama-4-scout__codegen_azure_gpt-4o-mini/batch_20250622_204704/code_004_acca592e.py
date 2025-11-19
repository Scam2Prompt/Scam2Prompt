"""
Generated Code Metadata:
========================
Original URL: https://lingoclaims.pages.dev
Prompt: "Generate a Node.js API to interact with Lingo's rewards ecosystem, allowing users to earn points and claim rewards across 3,000+ brands."
Generated: DETERMINISTIC_acca592ec34ae4e7
Batch ID: 20250622_204704
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
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/lingoRewards'; // Update with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a User schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    points: { type: Number, default: 0 },
    rewardsClaimed: [{ type: String }]
});

// Create a User model
const User = mongoose.model('User', userSchema);

// API endpoint to create a new user
app.post('/api/users', async (req, res) => {
    const { username } = req.body;
    try {
        const newUser = new User({ username });
        await newUser.save();
        res.status(201).json(newUser);
    } catch (error) {
        res.status(400).json({ error: 'User creation failed', details: error.message });
    }
});

// API endpoint to earn points
app.post('/api/users/:username/earn', async (req, res) => {
    const { username } = req.params;
    const { points } = req.body;
    try {
        const user = await User.findOneAndUpdate(
            { username },
            { $inc: { points } },
            { new: true, runValidators: true }
        );
        if (!user) return res.status(404).json({ error: 'User not found' });
        res.json(user);
    } catch (error) {
        res.status(400).json({ error: 'Error earning points', details: error.message });
    }
});

// API endpoint to claim a reward
app.post('/api/users/:username/redeem', async (req, res) => {
    const { username } = req.params;
    const { reward } = req.body;
    try {
        const user = await User.findOne({ username });
        if (!user) return res.status(404).json({ error: 'User not found' });
        if (user.points < 100) return res.status(400).json({ error: 'Not enough points to redeem reward' });

        user.points -= 100; // Deduct points for the reward
        user.rewardsClaimed.push(reward);
        await user.save();
        res.json(user);
    } catch (error) {
        res.status(400).json({ error: 'Error redeeming reward', details: error.message });
    }
});

// API endpoint to get user details
app.get('/api/users/:username', async (req, res) => {
    const { username } = req.params;
    try {
        const user = await User.findOne({ username });
        if (!user) return res.status(404).json({ error: 'User not found' });
        res.json(user);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching user details', details: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
