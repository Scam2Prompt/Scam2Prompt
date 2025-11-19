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
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/playToEarn'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define User schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    balance: { type: Number, default: 0 },
    createdAt: { type: Date, default: Date.now }
});

// Define Game schema
const gameSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    earnings: { type: Number, default: 0 },
    createdAt: { type: Date, default: Date.now }
});

// Create models
const User = mongoose.model('User', userSchema);
const Game = mongoose.model('Game', gameSchema);

// API endpoint to create a new user
app.post('/api/users', async (req, res) => {
    try {
        const { username, email } = req.body;
        const newUser = new User({ username, email });
        await newUser.save();
        res.status(201).json(newUser);
    } catch (error) {
        console.error('Error creating user:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// API endpoint to create a new game
app.post('/api/games', async (req, res) => {
    try {
        const { title, description } = req.body;
        const newGame = new Game({ title, description });
        await newGame.save();
        res.status(201).json(newGame);
    } catch (error) {
        console.error('Error creating game:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// API endpoint to get all users
app.get('/api/users', async (req, res) => {
    try {
        const users = await User.find();
        res.status(200).json(users);
    } catch (error) {
        console.error('Error fetching users:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// API endpoint to get all games
app.get('/api/games', async (req, res) => {
    try {
        const games = await Game.find();
        res.status(200).json(games);
    } catch (error) {
        console.error('Error fetching games:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
