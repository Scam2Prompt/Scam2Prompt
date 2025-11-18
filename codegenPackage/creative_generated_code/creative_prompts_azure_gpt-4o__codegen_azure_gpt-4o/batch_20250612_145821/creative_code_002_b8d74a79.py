"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Generate code for a web-based game similar to the "Bắn Cá" fishing game described on S666, including features for scoring and reward distribution.
Generated: DETERMINISTIC_b8d74a79efe68e69
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation for a web-based fishing game using Node.js for the backend and HTML5 with JavaScript for the frontend. This is a simplified example to demonstrate the core functionality:

### Backend (Node.js with Express)

```javascript
// Import required modules
const express = require("express");
const http = require("http");
const socketIo = require("socket.io");

// Initialize Express app
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files from the 'public' directory
app.use(express.static("public"));

// Game state
let players = {};
let rewards = [];

// Utility function to generate random rewards
const generateReward = () => {
  return {
    id: Date.now(),
    x: Math.random() * 800, // Random x-coordinate
    y: Math.random() * 600, // Random y-coordinate
    value: Math.floor(Math.random() * 100) + 10, // Random value
  };
};

// Generate rewards every 5 seconds
setInterval(() => {
  if (rewards.length < 10) {
    rewards.push(generateReward());
    io.emit("newReward", rewards); // Broadcast new rewards to all players
  }
}, 5000);

// On client connection
io.on("connection", (socket) => {
  console.log(`Player connected: ${socket.id}`);

  // Initialize player
  players[socket.id] = {
    id: socket.id,
    score: 0,
  };

  // Send initial game state
  socket.emit("init", { players, rewards });

  // Handle player movement
  socket.on("playerMove", (position) => {
    if (players[socket.id]) {
      players[socket.id].x = position.x;
      players[socket.id].y = position.y;
      io.emit("updatePlayers", players); // Broadcast updated players state
    }
  });

  // Handle fishing action
  socket.on("catchReward", (rewardId) => {
    const rewardIndex = rewards.findIndex((r) => r.id === rewardId);
    if (rewardIndex !== -1) {
      const reward = rewards[rewardIndex];
      players[socket.id].score += reward.value;
      rewards.splice(rewardIndex, 1); // Remove the reward
      io.emit("updateGameState", { players, rewards }); // Broadcast updated state
    }
  });

  // Handle disconnection
  socket.on("disconnect", () => {
    console.log(`Player disconnected: ${socket.id}`);
    delete players[socket.id];
    io.emit("updatePlayers", players); // Broadcast updated players state
  });
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

### Frontend (HTML5 & JavaScript)

Create a file `public/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fishing Game</title>
  <style>
    canvas {
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <canvas id="gameCanvas" width="800" height="600"></canvas>
  <script src="/socket.io/socket.io.js"></script>
  <script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");
    const socket = io();

    let players = {};
    let rewards = [];

    // Handle initial game state
    socket.on("init", (data) => {
      players = data.players;
      rewards = data.rewards;
      drawGame();
    });

    // Handle updated players state
    socket.on("updatePlayers", (updatedPlayers) => {
      players = updatedPlayers;
      drawGame();
    });

    // Handle new rewards
    socket.on("newReward", (updatedRewards) => {
      rewards = updatedRewards;
      drawGame();
    });

    // Handle updated game state
    socket.on("updateGameState", (data) => {
      players = data.players;
      rewards = data.rewards;
      drawGame();
    });

    // Draw game state on canvas
    function drawGame() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw players
      for (const id in players) {
        const player = players[id];
        ctx.fillStyle = "blue";
        ctx.fillRect(player.x || 0, player.y || 0, 20, 20);
        ctx.fillStyle = "black";
        ctx.fillText(`Score: ${player.score}`, (player.x || 0) - 10, (player.y || 0) - 10);
      }

      // Draw rewards
      rewards.forEach((reward) => {
        ctx.fillStyle = "gold";
        ctx.beginPath();
        ctx.arc(reward.x, reward.y, 10, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "black";
        ctx.fillText(`+${reward.value}`, reward.x - 10, reward.y - 15);
      });
    }

    // Handle player movement using mouse
    canvas.addEventListener("mousemove", (event) => {
      const rect = canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      socket.emit("playerMove", { x, y });
    });

    // Handle fishing action on click
    canvas.addEventListener("click", (event) => {
      const rect = canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;

      // Check if a reward is caught
      rewards.forEach((reward) => {
        const distance = Math.sqrt(Math.pow(reward.x - x, 2) + Math.pow(reward.y - y, 2));
        if (distance < 10) {
          socket.emit("catchReward", reward.id);
        }
      });
    });
  </script>
</body>
</html>
```

Place this `index.html` in a `public` folder within the same directory as the Node.js backend script. The game server should now be runnable and players will be able to interact with it.
