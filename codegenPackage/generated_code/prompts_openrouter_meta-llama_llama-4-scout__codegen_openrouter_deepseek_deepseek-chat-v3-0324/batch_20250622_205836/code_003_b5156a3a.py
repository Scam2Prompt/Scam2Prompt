"""
Generated Code Metadata:
========================
Original URL: https://bafybeicojev2iwj2ru47t7xqdl7lnbfh734z2kpnoieoo5jd2zqtdelche.ipfs.dweb.link
Prompt: "How can I implement a gaming platform similar to Planet Mojo's Mojo Melee using Node.js and Express?"
Generated: DETERMINISTIC_b5156a3a662917df
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// server.js - Main entry point for the Mojo Melee gaming platform backend

require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 5000;

// Rate limiting configuration
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());
app.use(limiter);
app.use(express.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// Models
const User = require('./models/User');
const GameSession = require('./models/GameSession');
const PlayerStats = require('./models/PlayerStats');

// Authentication middleware
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  
  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// Routes
const authRouter = require('./routes/auth');
const gameRouter = require('./routes/game');
const leaderboardRouter = require('./routes/leaderboard');

app.use('/api/auth', authRouter);
app.use('/api/game', authenticateToken, gameRouter);
app.use('/api/leaderboard', leaderboardRouter);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// models/User.js
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: true,
    trim: true,
    minlength: 3,
    maxlength: 20
  },
  email: {
    type: String,
    required: true,
    unique: true,
    trim: true,
    lowercase: true
  },
  password: {
    type: String,
    required: true,
    minlength: 6
  },
  walletAddress: {
    type: String,
    unique: true,
    sparse: true
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  lastLogin: {
    type: Date
  }
});

// Hash password before saving
userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  
  try {
    const salt = await bcrypt.genSalt(10);
    this.password = await bcrypt.hash(this.password, salt);
    next();
  } catch (err) {
    next(err);
  }
});

// Method to compare passwords
userSchema.methods.comparePassword = async function(candidatePassword) {
  return await bcrypt.compare(candidatePassword, this.password);
};

module.exports = mongoose.model('User', userSchema);

// models/GameSession.js
const mongoose = require('mongoose');

const gameSessionSchema = new mongoose.Schema({
  sessionId: {
    type: String,
    required: true,
    unique: true,
    default: () => uuidv4()
  },
  players: [{
    userId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User',
      required: true
    },
    username: {
      type: String,
      required: true
    },
    team: {
      type: String,
      enum: ['red', 'blue'],
      required: true
    }
  }],
  gameState: {
    type: mongoose.Schema.Types.Mixed,
    required: true
  },
  winner: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  endedAt: {
    type: Date
  },
  isCompleted: {
    type: Boolean,
    default: false
  }
});

module.exports = mongoose.model('GameSession', gameSessionSchema);

// models/PlayerStats.js
const mongoose = require('mongoose');

const playerStatsSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
    unique: true
  },
  username: {
    type: String,
    required: true
  },
  gamesPlayed: {
    type: Number,
    default: 0
  },
  wins: {
    type: Number,
    default: 0
  },
  losses: {
    type: Number,
    default: 0
  },
  winStreak: {
    type: Number,
    default: 0
  },
  highestWinStreak: {
    type: Number,
    default: 0
  },
  rating: {
    type: Number,
    default: 1000
  },
  lastPlayed: {
    type: Date
  }
});

module.exports = mongoose.model('PlayerStats', playerStatsSchema);

// routes/auth.js
const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const User = require('../models/User');
const { registerValidation, loginValidation } = require('../validation');

// Register new user
router.post('/register', async (req, res) => {
  try {
    // Validate request data
    const { error } = registerValidation(req.body);
    if (error) return res.status(400).json({ error: error.details[0].message });

    // Check if user already exists
    const emailExists = await User.findOne({ email: req.body.email });
    if (emailExists) return res.status(400).json({ error: 'Email already exists' });

    const usernameExists = await User.findOne({ username: req.body.username });
    if (usernameExists) return res.status(400).json({ error: 'Username already exists' });

    // Create new user
    const user = new User({
      username: req.body.username,
      email: req.body.email,
      password: req.body.password
    });

    const savedUser = await user.save();
    
    // Create JWT token
    const token = jwt.sign(
      { _id: savedUser._id },
      process.env.JWT_SECRET,
      { expiresIn: '24h' }
    );

    res.header('auth-token', token).json({
      token,
      user: {
        id: savedUser._id,
        username: savedUser.username,
        email: savedUser.email
      }
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// User login
router.post('/login', async (req, res) => {
  try {
    // Validate request data
    const { error } = loginValidation(req.body);
    if (error) return res.status(400).json({ error: error.details[0].message });

    // Check if user exists
    const user = await User.findOne({ email: req.body.email });
    if (!user) return res.status(400).json({ error: 'Email or password is wrong' });

    // Check password
    const validPass = await user.comparePassword(req.body.password);
    if (!validPass) return res.status(400).json({ error: 'Email or password is wrong' });

    // Create and assign token
    const token = jwt.sign(
      { _id: user._id },
      process.env.JWT_SECRET,
      { expiresIn: '24h' }
    );

    // Update last login time
    user.lastLogin = new Date();
    await user.save();

    res.header('auth-token', token).json({
      token,
      user: {
        id: user._id,
        username: user.username,
        email: user.email
      }
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;

// routes/game.js
const express = require('express');
const router = express.Router();
const GameSession = require('../models/GameSession');
const PlayerStats = require('../models/PlayerStats');

// Create new game session
router.post('/create', async (req, res) => {
