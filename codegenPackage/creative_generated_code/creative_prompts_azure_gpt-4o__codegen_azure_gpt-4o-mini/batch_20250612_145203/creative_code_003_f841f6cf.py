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
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware
app.use(cors()); // Allow cross-origin requests
app.use(bodyParser.json()); // Parse JSON bodies

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/gamingPlatform', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('MongoDB Connected');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// User Schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    credits: { type: Number, default: 0 },
    statistics: {
        gamesPlayed: { type: Number, default: 0 },
        wins: { type: Number, default: 0 },
        losses: { type: Number, default: 0 }
    }
});

// User Model
const User = mongoose.model('User', userSchema);

// API Endpoints

// Create a new user
app.post('/api/users', async (req, res) => {
    try {
        const { username, password } = req.body;
        const newUser = new User({ username, password });
        await newUser.save();
        res.status(201).json(newUser);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Get user by username
app.get('/api/users/:username', async (req, res) => {
    try {
        const user = await User.findOne({ username: req.params.username });
        if (user) {
            res.json(user);
        } else {
            res.status(404).json({ message: 'User not found' });
        }
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Update user credits
app.patch('/api/users/:username/credits', async (req, res) => {
    try {
        const { credits } = req.body;
        const user = await User.findOneAndUpdate(
            { username: req.params.username },
            { $inc: { credits: credits } },
            { new: true }
        );
        if (user) {
            res.json(user);
        } else {
            res.status(404).json({ message: 'User not found' });
        }
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Update game statistics
app.patch('/api/users/:username/statistics', async (req, res) => {
    try {
        const { gamesPlayed, wins, losses } = req.body;
        const user = await User.findOneAndUpdate(
            { username: req.params.username },
            { 
                $inc: { 
                    'statistics.gamesPlayed': gamesPlayed || 0,
                    'statistics.wins': wins || 0,
                    'statistics.losses': losses || 0
                } 
            },
            { new: true }
        );
        if (user) {
            res.json(user);
        } else {
            res.status(404).json({ message: 'User not found' });
        }
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
