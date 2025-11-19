"""
Generated Code Metadata:
========================
Original URL: https://balloon-gomble-io.pages.dev
Prompt: "Design a simple backend API using Node.js to manage user interactions with a game like Balloon Gomble, including tracking progress and issuing rewards."
Generated: DETERMINISTIC_42977f3d6a040db2
Batch ID: 20250622_210856
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

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define User Schema
const userSchema = new mongoose.Schema({
    userId: { type: String, required: true, unique: true },
    username: { type: String, required: true },
    score: { type: Number, default: 0 },
    level: { type: Number, default: 1 },
    rewards: [{ type: String }],
    createdAt: { type: Date, default: Date.now }
});

// Define Reward Schema
const rewardSchema = new mongoose.Schema({
    rewardId: { type: String, required: true, unique: true },
    name: { type: String, required: true },
    description: { type: String },
    pointsRequired: { type: Number, required: true }
});

// Create models
const User = mongoose.model('User', userSchema);
const Reward = mongoose.model('Reward', rewardSchema);

// API Routes

// Create a new user
app.post('/api/users', async (req, res) => {
    try {
        const { userId, username } = req.body;
        
        if (!userId || !username) {
            return res.status(400).json({ error: 'userId and username are required' });
        }

        const existingUser = await User.findOne({ userId });
        if (existingUser) {
            return res.status(400).json({ error: 'User already exists' });
        }

        const user = new User({ userId, username });
        await user.save();
        
        res.status(201).json(user);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Get user by ID
app.get('/api/users/:userId', async (req, res) => {
    try {
        const user = await User.findOne({ userId: req.params.userId });
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }
        res.json(user);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Update user score
app.patch('/api/users/:userId/score', async (req, res) => {
    try {
        const { score } = req.body;
        if (typeof score !== 'number') {
            return res.status(400).json({ error: 'Score must be a number' });
        }

        const user = await User.findOneAndUpdate(
            { userId: req.params.userId },
            { $inc: { score } },
            { new: true }
        );

        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }

        res.json(user);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Level up user
app.patch('/api/users/:userId/level-up', async (req, res) => {
    try {
        const user = await User.findOneAndUpdate(
            { userId: req.params.userId },
            { $inc: { level: 1 } },
            { new: true }
        );

        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }

        res.json(user);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Add reward to user
app.post('/api/users/:userId/rewards', async (req, res) => {
    try {
        const { rewardId } = req.body;
        if (!rewardId) {
            return res.status(400).json({ error: 'rewardId is required' });
        }

        const reward = await Reward.findOne({ rewardId });
        if (!reward) {
            return res.status(404).json({ error: 'Reward not found' });
        }

        const user = await User.findOneAndUpdate(
            { userId: req.params.userId },
            { $addToSet: { rewards: rewardId } },
            { new: true }
        );

        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }

        res.json(user);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Create a new reward
app.post('/api/rewards', async (req, res) => {
    try {
        const { rewardId, name, description, pointsRequired } = req.body;
        
        if (!rewardId || !name || !pointsRequired) {
            return res.status(400).json({ error: 'rewardId, name, and pointsRequired are required' });
        }

        const existingReward = await Reward.findOne({ rewardId });
        if (existingReward) {
            return res.status(400).json({ error: 'Reward already exists' });
        }

        const reward = new Reward({ rewardId, name, description, pointsRequired });
        await reward.save();
        
        res.status(201).json(reward);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Get all rewards
app.get('/api/rewards', async (req, res) => {
    try {
        const rewards = await Reward.find();
        res.json(rewards);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```
