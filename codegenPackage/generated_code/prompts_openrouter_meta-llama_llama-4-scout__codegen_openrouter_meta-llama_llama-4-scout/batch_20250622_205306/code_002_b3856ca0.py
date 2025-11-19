"""
Generated Code Metadata:
========================
Original URL: https://marufonlinebd.net
Prompt: Design a simple game server architecture using Node.js and Express.js, inspired by Maruf Online BD's game server offerings, and provide a basic implementation.
Generated: DETERMINISTIC_b3856ca027bbdc3e
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// game-server.js

// Import required modules
const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/game-server', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define game schema
const gameSchema = new mongoose.Schema({
    gameId: String,
    players: [{ type: String, ref: 'Player' }],
    gameState: String
});

// Define player schema
const playerSchema = new mongoose.Schema({
    playerId: String,
    username: String,
    score: Number
});

// Create game and player models
const Game = mongoose.model('Game', gameSchema);
const Player = mongoose.model('Player', playerSchema);

// Middleware to parse JSON requests
app.use(express.json());

// API endpoint to create a new game
app.post('/api/games', async (req, res) => {
    try {
        const game = new Game(req.body);
        await game.save();
        res.status(201).json(game);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error creating game' });
    }
});

// API endpoint to join a game
app.post('/api/games/:gameId/join', async (req, res) => {
    try {
        const game = await Game.findById(req.params.gameId);
        if (!game) {
            return res.status(404).json({ message: 'Game not found' });
        }
        const player = new Player(req.body);
        game.players.push(player);
        await game.save();
        await player.save();
        res.status(201).json(game);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error joining game' });
    }
});

// Socket.io connection event
io.on('connection', (socket) => {
    console.log('Client connected');

    // Handle join game event
    socket.on('join-game', async (gameId, playerId) => {
        try {
            const game = await Game.findById(gameId);
            if (!game) {
                return socket.emit('error', 'Game not found');
            }
            const player = await Player.findById(playerId);
            if (!player) {
                return socket.emit('error', 'Player not found');
            }
            // Add player to game
            game.players.push(player);
            await game.save();
            socket.join(gameId);
            socket.emit('game-state', game);
        } catch (err) {
            console.error(err);
            socket.emit('error', 'Error joining game');
        }
    });

    // Handle leave game event
    socket.on('leave-game', async (gameId, playerId) => {
        try {
            const game = await Game.findById(gameId);
            if (!game) {
                return socket.emit('error', 'Game not found');
            }
            const player = await Player.findById(playerId);
            if (!player) {
                return socket.emit('error', 'Player not found');
            }
            // Remove player from game
            game.players.pull(player);
            await game.save();
            socket.leave(gameId);
            socket.emit('game-state', game);
        } catch (err) {
            console.error(err);
            socket.emit('error', 'Error leaving game');
        }
    });

    // Handle disconnection
    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

// Start server
const port = 3000;
http.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
});
```
