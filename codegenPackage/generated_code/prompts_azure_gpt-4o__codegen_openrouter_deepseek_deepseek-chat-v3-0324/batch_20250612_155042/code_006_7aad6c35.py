"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Write a Node.js API endpoint that integrates with the SIMemes game to track and update player actions, such as farming, stealing, and leveling up.
Generated: DETERMINISTIC_7aad6c350cb87304
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/simemes', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => console.log('Connected to MongoDB'));

// Player Schema
const playerSchema = new mongoose.Schema({
    playerId: { type: String, required: true, unique: true, default: uuidv4 },
    username: { type: String, required: true, unique: true },
    level: { type: Number, default: 1 },
    experience: { type: Number, default: 0 },
    coins: { type: Number, default: 100 },
    lastActionTime: { type: Date, default: Date.now },
    inventory: {
        memes: { type: Number, default: 0 },
        crops: { type: Number, default: 0 }
    },
    stats: {
        farms: { type: Number, default: 0 },
        steals: { type: Number, default: 0 },
        defends: { type: Number, default: 0 }
    }
});

const Player = mongoose.model('Player', playerSchema);

// Helper function to calculate required XP for next level
function getRequiredXP(currentLevel) {
    return Math.floor(100 * Math.pow(1.2, currentLevel - 1));
}

// API Endpoints

/**
 * @route POST /api/players
 * @desc Create a new player
 */
app.post('/api/players', async (req, res) => {
    try {
        const { username } = req.body;
        
        if (!username) {
            return res.status(400).json({ error: 'Username is required' });
        }

        const existingPlayer = await Player.findOne({ username });
        if (existingPlayer) {
            return res.status(400).json({ error: 'Username already exists' });
        }

        const player = new Player({ username });
        await player.save();

        res.status(201).json(player);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Server error' });
    }
});

/**
 * @route GET /api/players/:playerId
 * @desc Get player details
 */
app.get('/api/players/:playerId', async (req, res) => {
    try {
        const player = await Player.findOne({ playerId: req.params.playerId });
        if (!player) {
            return res.status(404).json({ error: 'Player not found' });
        }
        res.json(player);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Server error' });
    }
});

/**
 * @route POST /api/players/:playerId/farm
 * @desc Perform farming action
 */
app.post('/api/players/:playerId/farm', async (req, res) => {
    try {
        const player = await Player.findOne({ playerId: req.params.playerId });
        if (!player) {
            return res.status(404).json({ error: 'Player not found' });
        }

        // Check cooldown (5 minutes)
        const now = new Date();
        const lastAction = new Date(player.lastActionTime);
        const diffMinutes = (now - lastAction) / (1000 * 60);

        if (diffMinutes < 5) {
            const remaining = Math.ceil(5 - diffMinutes);
            return res.status(429).json({ 
                error: `Action on cooldown. Try again in ${remaining} minute(s)`
            });
        }

        // Update player stats
        const xpGain = 10;
        const coinsGain = Math.floor(Math.random() * 20) + 5;
        const cropsGain = Math.floor(Math.random() * 3) + 1;

        player.experience += xpGain;
        player.coins += coinsGain;
        player.inventory.crops += cropsGain;
        player.stats.farms += 1;
        player.lastActionTime = now;

        // Check for level up
        const requiredXP = getRequiredXP(player.level);
        if (player.experience >= requiredXP) {
            player.level += 1;
            player.experience -= requiredXP;
        }

        await player.save();
        res.json(player);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Server error' });
    }
});

/**
 * @route POST /api/players/:playerId/steal/:targetId
 * @desc Attempt to steal from another player
 */
app.post('/api/players/:playerId/steal/:targetId', async (req, res) => {
    try {
        const [player, target] = await Promise.all([
            Player.findOne({ playerId: req.params.playerId }),
            Player.findOne({ playerId: req.params.targetId })
        ]);

        if (!player || !target) {
            return res.status(404).json({ error: 'Player or target not found' });
        }

        // Check cooldown (10 minutes)
        const now = new Date();
        const lastAction = new Date(player.lastActionTime);
        const diffMinutes = (now - lastAction) / (1000 * 60);

        if (diffMinutes < 10) {
            const remaining = Math.ceil(10 - diffMinutes);
            return res.status(429).json({ 
                error: `Action on cooldown. Try again in ${remaining} minute(s)`
            });
        }

        // Calculate success chance (30% base + 5% per level difference)
        const levelDiff = player.level - target.level;
        const successChance = Math.min(0.3 + (0.05 * levelDiff), 0.8);
        const isSuccess = Math.random() < successChance;

        let result = {};
        if (isSuccess) {
            // Successful steal
            const stolenAmount = Math.min(
                Math.floor(target.coins * 0.2),
                target.coins
            );
            
            player.coins += stolenAmount;
            target.coins -= stolenAmount;
            player.stats.steals += 1;
            target.stats.defends += 0; // Not a defense
            
            result = {
                success: true,
                message: `Successfully stole ${stolenAmount} coins!`,
                stolenAmount
            };
        } else {
            // Failed steal
            const penalty = Math.floor(player.coins * 0.1);
            player.coins -= penalty;
            target.stats.defends += 1;
            
            result = {
                success: false,
                message: `Steal attempt failed! Lost ${penalty} coins.`,
                penalty
            };
        }

        player.lastActionTime = now;
        await Promise.all([player.save(), target.save()]);
        
        res.json({
            player,
            target,
            result
        });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Server error' });
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```
