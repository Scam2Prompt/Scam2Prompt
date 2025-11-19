"""
Generated Code Metadata:
========================
Original URL: https://baboons.vercel.app
Prompt: Design a simple backend API using Node.js that can support the Golden Baboons Mining Club application's functionality.
Generated: DETERMINISTIC_d19c7e316bc3835a
Batch ID: 20250622_211009
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
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Configure middleware
app.use(bodyParser.json());
app.use(cors());
app.use(helmet());

// Rate limiting configuration
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// In-memory database for demonstration purposes
let users = [];
let miningSessions = [];
let rewards = [];

// API Routes

/**
 * User endpoints
 */
app.post('/api/users', (req, res) => {
  try {
    const { username, email } = req.body;
    
    if (!username || !email) {
      return res.status(400).json({ error: 'Username and email are required' });
    }

    const existingUser = users.find(user => user.email === email);
    if (existingUser) {
      return res.status(409).json({ error: 'User already exists' });
    }

    const newUser = {
      id: uuidv4(),
      username,
      email,
      joinDate: new Date().toISOString(),
      miningPoints: 0
    };

    users.push(newUser);
    res.status(201).json(newUser);
  } catch (error) {
    console.error('Error creating user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/users/:id', (req, res) => {
  try {
    const user = users.find(u => u.id === req.params.id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json(user);
  } catch (error) {
    console.error('Error fetching user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * Mining session endpoints
 */
app.post('/api/mining-sessions', (req, res) => {
  try {
    const { userId, duration } = req.body;
    
    if (!userId || !duration) {
      return res.status(400).json({ error: 'userId and duration are required' });
    }

    const user = users.find(u => u.id === userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const newSession = {
      id: uuidv4(),
      userId,
      startTime: new Date().toISOString(),
      duration,
      pointsEarned: Math.floor(duration / 60) * 10 // 10 points per minute
    };

    miningSessions.push(newSession);
    
    // Update user's mining points
    user.miningPoints += newSession.pointsEarned;
    
    res.status(201).json(newSession);
  } catch (error) {
    console.error('Error creating mining session:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/mining-sessions/user/:userId', (req, res) => {
  try {
    const userSessions = miningSessions.filter(session => session.userId === req.params.userId);
    res.json(userSessions);
  } catch (error) {
    console.error('Error fetching mining sessions:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * Rewards endpoints
 */
app.get('/api/rewards', (req, res) => {
  try {
    // In a real app, this would come from a database
    const availableRewards = [
      { id: '1', name: 'Golden Pickaxe', cost: 1000 },
      { id: '2', name: 'Diamond Shovel', cost: 500 },
      { id: '3', name: 'Mining Helmet', cost: 300 }
    ];
    res.json(availableRewards);
  } catch (error) {
    console.error('Error fetching rewards:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/api/rewards/redeem', (req, res) => {
  try {
    const { userId, rewardId } = req.body;
    
    if (!userId || !rewardId) {
      return res.status(400).json({ error: 'userId and rewardId are required' });
    }

    const user = users.find(u => u.id === userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // In a real app, this would come from a database
    const reward = [
      { id: '1', name: 'Golden Pickaxe', cost: 1000 },
      { id: '2', name: 'Diamond Shovel', cost: 500 },
      { id: '3', name: 'Mining Helmet', cost: 300 }
    ].find(r => r.id === rewardId);

    if (!reward) {
      return res.status(404).json({ error: 'Reward not found' });
    }

    if (user.miningPoints < reward.cost) {
      return res.status(400).json({ error: 'Not enough mining points' });
    }

    const redemption = {
      id: uuidv4(),
      userId,
      rewardId,
      redemptionDate: new Date().toISOString()
    };

    rewards.push(redemption);
    user.miningPoints -= reward.cost;
    
    res.status(201).json({
      redemption,
      remainingPoints: user.miningPoints
    });
  } catch (error) {
    console.error('Error redeeming reward:', error);
    res.status(500).json({ error: 'Internal server error' });
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

module.exports = app; // For testing purposes
```
