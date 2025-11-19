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
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for user progress
const userProgressSchema = new mongoose.Schema({
  userId: String,
  gamesPlayed: Number,
  score: Number,
  level: Number,
  rewardsClaimed: [{ type: String }]
});

// Define schema for rewards
const rewardSchema = new mongoose.Schema({
  rewardId: String,
  rewardName: String,
  rewardDescription: String,
  rewardValue: Number
});

// Create models
const UserProgress = mongoose.model('UserProgress', userProgressSchema);
const Reward = mongoose.model('Reward', rewardSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to create a new user progress entry
app.post('/api/user-progress', async (req, res) => {
  try {
    const { userId } = req.body;
    if (!userId) {
      return res.status(400).json({ error: 'User ID is required' });
    }
    const existingProgress = await UserProgress.findOne({ userId });
    if (existingProgress) {
      return res.status(400).json({ error: 'User progress already exists' });
    }
    const userProgress = new UserProgress({
      userId,
      gamesPlayed: 0,
      score: 0,
      level: 1,
      rewardsClaimed: []
    });
    await userProgress.save();
    res.json({ message: 'User progress created successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error creating user progress' });
  }
});

// API endpoint to update user progress
app.put('/api/user-progress/:userId', async (req, res) => {
  try {
    const { userId } = req.params;
    const { gamesPlayed, score, level } = req.body;
    if (!userId) {
      return res.status(400).json({ error: 'User ID is required' });
    }
    const userProgress = await UserProgress.findOneAndUpdate({ userId }, {
      $inc: { gamesPlayed },
      $set: { score, level }
    }, { new: true });
    if (!userProgress) {
      return res.status(404).json({ error: 'User progress not found' });
    }
    res.json(userProgress);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error updating user progress' });
  }
});

// API endpoint to claim a reward
app.post('/api/rewards/:rewardId/claim', async (req, res) => {
  try {
    const { rewardId } = req.params;
    const { userId } = req.body;
    if (!rewardId || !userId) {
      return res.status(400).json({ error: 'Reward ID and User ID are required' });
    }
    const reward = await Reward.findById(rewardId);
    if (!reward) {
      return res.status(404).json({ error: 'Reward not found' });
    }
    const userProgress = await UserProgress.findOne({ userId });
    if (!userProgress) {
      return res.status(404).json({ error: 'User progress not found' });
    }
    if (userProgress.rewardsClaimed.includes(rewardId)) {
      return res.status(400).json({ error: 'Reward already claimed' });
    }
    userProgress.rewardsClaimed.push(rewardId);
    await userProgress.save();
    res.json({ message: 'Reward claimed successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error claiming reward' });
  }
});

// API endpoint to create a new reward
app.post('/api/rewards', async (req, res) => {
  try {
    const { rewardId, rewardName, rewardDescription, rewardValue } = req.body;
    if (!rewardId || !rewardName || !rewardDescription || !rewardValue) {
      return res.status(400).json({ error: 'Reward details are required' });
    }
    const existingReward = await Reward.findOne({ rewardId });
    if (existingReward) {
      return res.status(400).json({ error: 'Reward already exists' });
    }
    const reward = new Reward({
      rewardId,
      rewardName,
      rewardDescription,
      rewardValue
    });
    await reward.save();
    res.json({ message: 'Reward created successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error creating reward' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
