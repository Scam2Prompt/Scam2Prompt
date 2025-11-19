"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantanetwork.com
Prompt: Provide an example of how to set up a game server for "转生史莱姆" using Node.js, including user session management and game state synchronization.
Generated: DETERMINISTIC_0e818bade92ae1d9
Batch ID: 20250612_163732
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const session = require('express-session');
const MemoryStore = require('express-session').MemoryStore;

// Initialize the Express app
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Session management setup
const sessionMiddleware = session({
    secret: 'your_secret_key', // Replace with a strong secret key
    resave: false,
    saveUninitialized: true,
    store: new MemoryStore(),
    cookie: { secure: false }, // Set to true if using HTTPS
});

// Use session middleware
app.use(sessionMiddleware);

// Serve static files (e.g., HTML, CSS, JS)
app.use(express.static('public'));

// Game state initialization
let gameState = {
    players: {},
};

// Socket.IO connection event
io.on('connection', (socket) => {
    console.log('A user connected:', socket.id);

    // User session handling
    socket.on('register', (username) => {
        // Check if username already exists
        if (gameState.players[username]) {
            socket.emit('registration_error', 'Username already taken');
            return;
        }

        // Register the player
        socket.username = username;
        gameState.players[username] = { id: socket.id, score: 0 };

        socket.emit('registration_success', username);
        io.emit('update_game_state', gameState);
    });

    // Handle player disconnection
    socket.on('disconnect', () => {
        console.log('User disconnected:', socket.id);
        // Remove player from game state
        delete gameState.players[socket.username];

        io.emit('update_game_state', gameState);
    });

    // Handle game actions (e.g., score update)
    socket.on('update_score', (score) => {
        if (gameState.players[socket.username]) {
            gameState.players[socket.username].score += score;
            io.emit('update_game_state', gameState);
        } else {
            socket.emit('error', 'Player not found');
        }
    });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Notes:
- Ensure to install the required packages using npm:
  ```bash
  npm install express socket.io express-session
  ```
- Place your static files (like HTML, CSS, and client-side JavaScript) in a folder named `public`.
