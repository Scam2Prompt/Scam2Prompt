"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todaythegames.com
Prompt: Create a backend API using Node.js to manage user accounts, virtual credits, and game statistics for a platform similar to todaythegames.com.
Generated: DETERMINISTIC_f841f6cf3ea8a681
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize the Express app
const app = express();

// Middleware setup
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Error connecting to MongoDB:', err.message);
    process.exit(1); // Exit the application if database connection fails
  });

// Define Mongoose schemas and models

// User schema and model
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true }, // In production, store hashed passwords
  virtualCredits: { type: Number, default: 0 },
  createdAt: { type: Date, default: Date.now },
});

const User = mongoose.model('User', userSchema);

// Game statistics schema and model
const gameStatsSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  gamesPlayed: { type: Number, default: 0 },
  totalScore: { type: Number, default: 0 },
});

const GameStats = mongoose.model('GameStats', gameStatsSchema);

// API Endpoints

// Register a new user
app.post('/api/users/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;

    // Validate input data
    if (!username || !email || !password) {
      return res.status(400).json({ error: 'All fields are required.' });
    }

    const newUser = new User({ username, email, password });
    await newUser.save();

    res.status(201).json({ message: 'User registered successfully.', userId: newUser._id });
  } catch (err) {
    if (err.code === 11000) {
      // Handle duplicate key errors (e.g., duplicate username or email)
      return res.status(400).json({ error: 'Username or email already exists.' });
    }
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Get user details
app.get('/api/users/:userId', async (req, res) => {
  try {
    const user = await User.findById(req.params.userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found.' });
    }

    res.status(200).json({ user });
  } catch (err) {
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Update virtual credits for a user
app.put('/api/users/:userId/credits', async (req, res) => {
  try {
    const { virtualCredits } = req.body;

    if (typeof virtualCredits !== 'number') {
      return res.status(400).json({ error: 'Invalid virtualCredits value.' });
    }

    const user = await User.findByIdAndUpdate(
      req.params.userId,
      { virtualCredits },
      { new: true }
    );

    if (!user) {
      return res.status(404).json({ error: 'User not found.' });
    }

    res.status(200).json({ message: 'Credits updated successfully.', user });
  } catch (err) {
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Record game statistics for a user
app.post('/api/gamestats', async (req, res) => {
  try {
    const { userId, gamesPlayed, totalScore } = req.body;

    // Validate input data
    if (!userId || typeof gamesPlayed !== 'number' || typeof totalScore !== 'number') {
      return res.status(400).json({ error: 'Invalid input data.' });
    }

    const userExists = await User.findById(userId);
    if (!userExists) {
      return res.status(404).json({ error: 'User not found.' });
    }

    const gameStats = new GameStats({ userId, gamesPlayed, totalScore });
    await gameStats.save();

    res.status(201).json({ message: 'Game statistics recorded successfully.', gameStats });
  } catch (err) {
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Notes:
1. This code assumes MongoDB is running and the connection string is provided via `process.env.MONGO_URI`.
2. Passwords are stored in plaintext for simplicity in this demo. In production, use hashing (e.g., bcrypt) for password storage.
