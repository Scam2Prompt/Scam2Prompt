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
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

// Environment variables
const PORT = process.env.PORT || 3000;
const NODE_ENV = process.env.NODE_ENV || 'development';

// Rate limiting configuration
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});

// Middleware setup
app.use(helmet());
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(limiter);

if (NODE_ENV === 'production') {
  app.use(express.static(path.join(__dirname, 'public')));
}

// Game state management
const games = new Map();
const players = new Map();

// Game model
class Game {
  constructor(id, name, maxPlayers) {
    this.id = id;
    this.name = name;
    this.maxPlayers = maxPlayers;
    this.players = new Map();
    this.state = 'waiting'; // waiting, playing, finished
    this.createdAt = new Date();
  }

  addPlayer(player) {
    if (this.players.size >= this.maxPlayers) {
      throw new Error('Game is full');
    }
    this.players.set(player.id, player);
    return this;
  }

  removePlayer(playerId) {
    this.players.delete(playerId);
    return this;
  }

  start() {
    this.state = 'playing';
    return this;
  }

  end() {
    this.state = 'finished';
    return this;
  }
}

// Player model
class Player {
  constructor(id, name, socketId) {
    this.id = id;
    this.name = name;
    this.socketId = socketId;
    this.score = 0;
    this.connected = true;
  }

  updateScore(points) {
    this.score += points;
    return this;
  }
}

// API Routes
app.get('/api/games', (req, res) => {
  try {
    const gameList = Array.from(games.values()).map(game => ({
      id: game.id,
      name: game.name,
      players: game.players.size,
      maxPlayers: game.maxPlayers,
      state: game.state
    }));
    res.json(gameList);
  } catch (err) {
    console.error('Error fetching games:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/api/games', (req, res) => {
  try {
    const { name, maxPlayers } = req.body;
    if (!name || !maxPlayers) {
      return res.status(400).json({ error: 'Name and maxPlayers are required' });
    }

    const id = uuidv4();
    const game = new Game(id, name, maxPlayers);
    games.set(id, game);

    res.status(201).json({
      id: game.id,
      name: game.name,
      maxPlayers: game.maxPlayers,
      state: game.state
    });
  } catch (err) {
    console.error('Error creating game:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Socket.io connection handling
io.on('connection', (socket) => {
  console.log(`New connection: ${socket.id}`);

  socket.on('joinGame', ({ gameId, playerName }, callback) => {
    try {
      if (!gameId || !playerName) {
        throw new Error('Game ID and player name are required');
      }

      const game = games.get(gameId);
      if (!game) {
        throw new Error('Game not found');
      }

      const playerId = uuidv4();
      const player = new Player(playerId, playerName, socket.id);
      game.addPlayer(player);
      players.set(playerId, player);

      socket.join(gameId);
      socket.emit('playerJoined', { playerId, gameId });
      io.to(gameId).emit('gameUpdate', game);

      callback({ success: true, playerId, gameId });
    } catch (err) {
      console.error('Error joining game:', err);
      callback({ success: false, error: err.message });
    }
  });

  socket.on('leaveGame', ({ gameId, playerId }, callback) => {
    try {
      const game = games.get(gameId);
      if (!game) {
        throw new Error('Game not found');
      }

      game.removePlayer(playerId);
      players.delete(playerId);
      socket.leave(gameId);

      io.to(gameId).emit('gameUpdate', game);
      callback({ success: true });
    } catch (err) {
      console.error('Error leaving game:', err);
      callback({ success: false, error: err.message });
    }
  });

  socket.on('disconnect', () => {
    console.log(`Client disconnected: ${socket.id}`);
    // Handle player disconnection logic
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT} in ${NODE_ENV} mode`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully...');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});
```
