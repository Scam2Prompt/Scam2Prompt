"""
Generated Code Metadata:
========================
Original URL: https://notrop.com
Prompt: Create a Node.js script to verify and process Notcoin airdrop claims for users on a platform like Smartsupp.
Generated: DETERMINISTIC_3a1523e9f0996e11
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const { MongoClient } = require('mongodb');
const jwt = require('jsonwebtoken');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');
const cors = require('cors');

// Configuration
const config = {
  port: process.env.PORT || 3000,
  mongoUri: process.env.MONGO_URI || 'mongodb://localhost:27017',
  dbName: process.env.DB_NAME || 'notcoin_airdrop',
  jwtSecret: process.env.JWT_SECRET || 'your-secret-key',
  airdropAmount: process.env.AIRDROP_AMOUNT || 1000,
  rateLimitWindowMs: 15 * 60 * 1000, // 15 minutes
  rateLimitMax: 100 // limit each IP to 100 requests per windowMs
};

// Initialize Express app
const app = express();

// Middleware
app.use(helmet());
app.use(cors());
app.use(bodyParser.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: config.rateLimitWindowMs,
  max: config.rateLimitMax,
  message: 'Too many requests, please try again later.'
});
app.use(limiter);

// MongoDB connection
let db;
let usersCollection;
let airdropClaimsCollection;

async function connectToDatabase() {
  try {
    const client = new MongoClient(config.mongoUri);
    await client.connect();
    db = client.db(config.dbName);
    usersCollection = db.collection('users');
    airdropClaimsCollection = db.collection('airdrop_claims');
    console.log('Connected to MongoDB');
  } catch (err) {
    console.error('Database connection error:', err);
    process.exit(1);
  }
}

// JWT verification middleware
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) return res.sendStatus(401);

  jwt.verify(token, config.jwtSecret, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
}

// Routes

/**
 * POST /claim
 * Claims Notcoin airdrop for authenticated user
 */
app.post('/claim', authenticateToken, async (req, res) => {
  try {
    const userId = req.user.userId;

    // Check if user exists
    const user = await usersCollection.findOne({ _id: userId });
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Check if user has already claimed airdrop
    const existingClaim = await airdropClaimsCollection.findOne({ userId });
    if (existingClaim) {
      return res.status(400).json({ error: 'Airdrop already claimed' });
    }

    // Create airdrop claim record
    const claimId = uuidv4();
    const claimData = {
      _id: claimId,
      userId,
      amount: config.airdropAmount,
      timestamp: new Date(),
      status: 'completed'
    };

    await airdropClaimsCollection.insertOne(claimData);

    // Update user balance (simplified example)
    await usersCollection.updateOne(
      { _id: userId },
      { $inc: { balance: config.airdropAmount } }
    );

    res.status(200).json({
      success: true,
      message: 'Airdrop claimed successfully',
      claimId,
      amount: config.airdropAmount
    });
  } catch (err) {
    console.error('Error processing airdrop claim:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * GET /claims/:userId
 * Get airdrop claim history for a user (admin only)
 */
app.get('/claims/:userId', authenticateToken, async (req, res) => {
  try {
    // In a real app, you would check if the requester has admin privileges
    const userId = req.params.userId;
    const claims = await airdropClaimsCollection.find({ userId }).toArray();
    
    res.status(200).json(claims);
  } catch (err) {
    console.error('Error fetching claim history:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

// Start server
async function startServer() {
  await connectToDatabase();
  app.listen(config.port, () => {
    console.log(`Server running on port ${config.port}`);
  });
}

startServer().catch(err => {
  console.error('Failed to start server:', err);
  process.exit(1);
});
```
