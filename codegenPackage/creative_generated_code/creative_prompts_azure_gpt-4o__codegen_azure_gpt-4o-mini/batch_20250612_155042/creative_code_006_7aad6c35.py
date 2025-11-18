"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Write a Node.js API endpoint that integrates with the SIMemes game to track and update player actions, such as farming, stealing, and leveling up.
Generated: DETERMINISTIC_7aad6c350cb87304
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/simemes'; // Update with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Player Schema and Model
const playerSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    farmingLevel: { type: Number, default: 0 },
    stealingLevel: { type: Number, default: 0 },
    experiencePoints: { type: Number, default: 0 },
});

const Player = mongoose.model('Player', playerSchema);

// API Endpoint to update player actions
app.post('/api/player/action', async (req, res) => {
    const { username, action } = req.body;

    // Validate request body
    if (!username || !action) {
        return res.status(400).json({ error: 'Username and action are required' });
    }

    try {
        // Find the player by username
        let player = await Player.findOne({ username });

        // If player does not exist, create a new player
        if (!player) {
            player = new Player({ username });
        }

        // Update player based on action
        switch (action) {
            case 'farm':
                player.farmingLevel++;
                player.experiencePoints += 10; // Example XP gain
                break;
            case 'steal':
                player.stealingLevel++;
                player.experiencePoints += 5; // Example XP gain
                break;
            case 'levelUp':
                player.experiencePoints += 20; // Example XP gain for leveling up
                break;
            default:
                return res.status(400).json({ error: 'Invalid action' });
        }

        // Save the player data
        await player.save();

        // Respond with updated player data
        res.status(200).json({ message: 'Player action updated', player });
    } catch (err) {
        console.error('Error updating player action:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Graceful shutdown
process.on('SIGINT', async () => {
    await mongoose.connection.close();
    console.log('MongoDB connection closed gracefully');
    process.exit(0);
});
```
