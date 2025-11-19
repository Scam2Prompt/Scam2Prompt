"""
Generated Code Metadata:
========================
Original URL: https://d-510.pages.dev
Prompt: "Generate a Node.js API to interact with the Lingo token's rewards ecosystem, allowing users to earn points and claim rewards across 3,000+ brands."
Generated: DETERMINISTIC_aafae8c03b197a35
Batch ID: 20250622_211405
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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

// Initialize Express app
const app = express();

// Environment variables
require('dotenv').config();
const PORT = process.env.PORT || 3000;
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/lingo-rewards';
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

// Middleware
app.use(cors());
app.use(helmet());
app.use(bodyParser.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect(MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Models
const User = mongoose.model('User', new mongoose.Schema({
  userId: { type: String, unique: true, default: uuidv4 },
  email: { type: String, unique: true, required: true },
  password: { type: String, required: true },
  points: { type: Number, default: 0 },
  rewards: [{
    rewardId: String,
    brandId: String,
    claimed: { type: Boolean, default: false },
    dateClaimed: Date
  }],
  createdAt: { type: Date, default: Date.now }
}));

const Brand = mongoose.model('Brand', new mongoose.Schema({
  brandId: { type: String, unique: true, default: uuidv4 },
  name: { type: String, required: true },
  description: String,
  rewards: [{
    rewardId: { type: String, default: uuidv4 },
    name: String,
    pointsRequired: Number,
    description: String,
    expiryDate: Date
  }],
  createdAt: { type: Date, default: Date.now }
}));

// JWT Authentication Middleware
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  
  if (!token) return res.sendStatus(401);

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// Routes

// User Registration
app.post('/api/register', async (req, res) => {
  try {
    const { email, password } = req.body;
    
    if (!email || !password) {
      return res.status(400).json({ error: 'Email and password are required' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ email, password: hashedPassword });
    await user.save();

    const token = jwt.sign({ userId: user.userId, email: user.email }, JWT_SECRET, { expiresIn: '1h' });
    
    res.status(201).json({ token });
  } catch (error) {
    if (error.code === 11000) {
      return res.status(400).json({ error: 'Email already exists' });
    }
    res.status(500).json({ error: 'Internal server error' });
  }
});

// User Login
app.post('/api/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    
    if (!email || !password) {
      return res.status(400).json({ error: 'Email and password are required' });
    }

    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const token = jwt.sign({ userId: user.userId, email: user.email }, JWT_SECRET, { expiresIn: '1h' });
    
    res.json({ token });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get User Points
app.get('/api/user/points', authenticateToken, async (req, res) => {
  try {
    const user = await User.findOne({ userId: req.user.userId });
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json({ points: user.points });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Earn Points
app.post('/api/user/earn', authenticateToken, async (req, res) => {
  try {
    const { points, brandId } = req.body;
    
    if (!points || !brandId) {
      return res.status(400).json({ error: 'Points and brandId are required' });
    }

    const user = await User.findOne({ userId: req.user.userId });
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    user.points += parseInt(points);
    await user.save();

    res.json({ points: user.points });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get Available Rewards
app.get('/api/rewards', authenticateToken, async (req, res) => {
  try {
    const brands = await Brand.find({});
    const rewards = brands.flatMap(brand => 
      brand.rewards.map(reward => ({
        rewardId: reward.rewardId,
        brandId: brand.brandId,
        brandName: brand.name,
        name: reward.name,
        pointsRequired: reward.pointsRequired,
        description: reward.description,
        expiryDate: reward.expiryDate
      }))
    );
    res.json(rewards);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Claim Reward
app.post('/api/rewards/claim', authenticateToken, async (req, res) => {
  try {
    const { rewardId, brandId } = req.body;
    
    if (!rewardId || !brandId) {
      return res.status(400).json({ error: 'rewardId and brandId are required' });
    }

    const brand = await Brand.findOne({ brandId });
    if (!brand) {
      return res.status(404).json({ error: 'Brand not found' });
    }

    const reward = brand.rewards.find(r => r.rewardId === rewardId);
    if (!reward) {
      return res.status(404).json({ error: 'Reward not found' });
    }

    const user = await User.findOne({ userId: req.user.userId });
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    if (user.points < reward.pointsRequired) {
      return res.status(400).json({ error: 'Insufficient points' });
    }

    user.points -= reward.pointsRequired;
    user.rewards.push({
      rewardId,
      brandId,
      claimed: true,
      dateClaimed: new Date()
    });
    await user.save();

    res.json({ 
      message: 'Reward claimed successfully',
      points: user.points,
      reward: {
        rewardId,
        brandId,
        name: reward.name,
        pointsRequired: reward.pointsRequired
      }
    });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
