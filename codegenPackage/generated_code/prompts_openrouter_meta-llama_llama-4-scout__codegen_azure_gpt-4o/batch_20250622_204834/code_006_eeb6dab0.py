"""
Generated Code Metadata:
========================
Original URL: https://mememogulsclaim.pages.dev
Prompt: "What are the key considerations for building a play-to-earn platform like Meme Moguls, and how would you architect the system using Node.js and MongoDB?"
Generated: DETERMINISTIC_eeb6dab0e47eb602
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const mongoose = require('mongoose'); // MongoDB object modeling tool
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const dotenv = require('dotenv'); // For environment variable management

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('MongoDB connected successfully');
  } catch (error) {
    console.error('Error connecting to MongoDB:', error.message);
    process.exit(1); // Exit process with failure
  }
};

// Call the database connection function
connectDB();

// Define MongoDB schemas and models
// User schema: Represents players in the platform
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  balance: { type: Number, default: 0 }, // Earnings balance
  createdAt: { type: Date, default: Date.now },
});

const User = mongoose.model('User', userSchema);

// Game schema: Represents games available on the platform
const gameSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String },
  rewardRate: { type: Number, required: true }, // Earnings per play
  createdAt: { type: Date, default: Date.now },
});

const Game = mongoose.model('Game', gameSchema);

// Transaction schema: Represents earnings transactions
const transactionSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  gameId: { type: mongoose.Schema.Types.ObjectId, ref: 'Game', required: true },
  amount: { type: Number, required: true },
  createdAt: { type: Date, default: Date.now },
});

const Transaction = mongoose.model('Transaction', transactionSchema);

// API routes
// Route: Register a new user
app.post('/api/users/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;

    // Validate input
    if (!username || !email || !password) {
      return res.status(400).json({ message: 'All fields are required' });
    }

    // Check if user already exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({ message: 'User already exists' });
    }

    // Create new user
    const newUser = new User({ username, email, password });
    await newUser.save();

    res.status(201).json({ message: 'User registered successfully', user: newUser });
  } catch (error) {
    console.error('Error registering user:', error.message);
    res.status(500).json({ message: 'Server error' });
  }
});

// Route: List all games
app.get('/api/games', async (req, res) => {
  try {
    const games = await Game.find();
    res.status(200).json(games);
  } catch (error) {
    console.error('Error fetching games:', error.message);
    res.status(500).json({ message: 'Server error' });
  }
});

// Route: Play a game and earn rewards
app.post('/api/games/play', async (req, res) => {
  try {
    const { userId, gameId } = req.body;

    // Validate input
    if (!userId || !gameId) {
      return res.status(400).json({ message: 'User ID and Game ID are required' });
    }

    // Fetch user and game details
    const user = await User.findById(userId);
    const game = await Game.findById(gameId);

    if (!user || !game) {
      return res.status(404).json({ message: 'User or Game not found' });
    }

    // Calculate reward and update user balance
    const reward = game.rewardRate;
    user.balance += reward;
    await user.save();

    // Record transaction
    const transaction = new Transaction({ userId, gameId, amount: reward });
    await transaction.save();

    res.status(200).json({ message: 'Game played successfully', reward, balance: user.balance });
  } catch (error) {
    console.error('Error playing game:', error.message);
    res.status(500).json({ message: 'Server error' });
  }
});

// Route: Get user transactions
app.get('/api/users/:userId/transactions', async (req, res) => {
  try {
    const { userId } = req.params;

    // Fetch transactions for the user
    const transactions = await Transaction.find({ userId }).populate('gameId', 'name');
    res.status(200).json(transactions);
  } catch (error) {
    console.error('Error fetching transactions:', error.message);
    res.status(500).json({ message: 'Server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Notes:
- Ensure you have a `.env` file with `MONGO_URI` and `PORT` defined.
- Use a library like `bcrypt` for password hashing and `jsonwebtoken` for authentication in production.
- Add rate limiting and input validation for enhanced security.
