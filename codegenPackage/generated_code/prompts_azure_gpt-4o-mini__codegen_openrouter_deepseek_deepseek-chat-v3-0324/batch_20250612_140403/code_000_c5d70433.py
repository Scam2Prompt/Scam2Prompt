"""
Generated Code Metadata:
========================
Original URL: https://red.game
Prompt: Generate a code snippet for a browser-based game that incorporates surveillance themes similar to those found in RED's TRON concept.
Generated: DETERMINISTIC_c5d70433cfc879a6
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TRON-inspired Surveillance Game
 * A browser-based game where players navigate a grid while avoiding surveillance drones.
 */

// Game configuration
const config = {
    gridSize: 20, // Size of the game grid (N x N)
    cellSize: 30, // Pixel size of each grid cell
    playerSpeed: 300, // Player movement speed in ms
    droneCount: 3, // Number of surveillance drones
    droneSpeed: 500, // Drone movement speed in ms
    scanRadius: 3, // Drone surveillance radius
    gameDuration: 60000 // Game duration in ms (1 minute)
};

// Game state
const state = {
    player: { x: 0, y: 0 },
    drones: [],
    grid: [],
    score: 0,
    gameOver: false,
    startTime: null,
    endTime: null
};

// DOM elements
const gameContainer = document.getElementById('game-container');
const gridElement = document.createElement('div');
gridElement.className = 'grid';
gameContainer.appendChild(gridElement);

const scoreElement = document.createElement('div');
scoreElement.className = 'score';
gameContainer.appendChild(scoreElement);

const timerElement = document.createElement('div');
timerElement.className = 'timer';
gameContainer.appendChild(timerElement);

// Initialize game grid
function initGrid() {
    gridElement.style.width = `${config.gridSize * config.cellSize}px`;
    gridElement.style.height = `${config.gridSize * config.cellSize}px`;
    
    state.grid = Array(config.gridSize).fill().map(() => 
        Array(config.gridSize).fill(0)
    );
    
    // Create grid cells
    for (let y = 0; y < config.gridSize; y++) {
        for (let x = 0; x < config.gridSize; x++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.dataset.x = x;
            cell.dataset.y = y;
            cell.style.width = `${config.cellSize}px`;
            cell.style.height = `${config.cellSize}px`;
            gridElement.appendChild(cell);
        }
    }
}

// Initialize player
function initPlayer() {
    // Place player at random position
    state.player = {
        x: Math.floor(Math.random() * config.gridSize),
        y: Math.floor(Math.random() * config.gridSize)
    };
    updateCell(state.player.x, state.player.y, 'player');
}

// Initialize drones
function initDrones() {
    state.drones = [];
    for (let i = 0; i < config.droneCount; i++) {
        let x, y;
        do {
            x = Math.floor(Math.random() * config.gridSize);
            y = Math.floor(Math.random() * config.gridSize);
        } while (
            (x === state.player.x && y === state.player.y) ||
            state.drones.some(d => d.x === x && d.y === y)
        );
        
        state.drones.push({ x, y, direction: Math.floor(Math.random() * 4) });
        updateCell(x, y, 'drone');
    }
}

// Update cell appearance
function updateCell(x, y, type) {
    const cell = document.querySelector(`.cell[data-x="${x}"][data-y="${y}"]`);
    if (!cell) return;
    
    // Clear previous classes
    cell.className = 'cell';
    
    // Add new class based on type
    if (type === 'player') {
        cell.classList.add('player');
    } else if (type === 'drone') {
        cell.classList.add('drone');
    } else if (type === 'scanned') {
        cell.classList.add('scanned');
    }
}

// Move player
function movePlayer(dx, dy) {
    if (state.gameOver) return;
    
    const newX = state.player.x + dx;
    const newY = state.player.y + dy;
    
    // Check boundaries
    if (newX < 0 || newX >= config.gridSize || newY < 0 || newY >= config.gridSize) {
        return;
    }
    
    // Clear old position
    updateCell(state.player.x, state.player.y, 'empty');
    
    // Update position
    state.player.x = newX;
    state.player.y = newY;
    
    // Update display
    updateCell(newX, newY, 'player');
    
    // Check for drone collision
    checkCollision();
}

// Move drones
function moveDrones() {
    if (state.gameOver) return;
    
    state.drones.forEach(drone => {
        // Clear old position
        updateCell(drone.x, drone.y, 'empty');
        
        // Determine new position based on direction
        let newX = drone.x;
        let newY = drone.y;
        
        // 0: up, 1: right, 2: down, 3: left
        switch (drone.direction) {
            case 0: newY--; break;
            case 1: newX++; break;
            case 2: newY++; break;
            case 3: newX--; break;
        }
        
        // If hitting boundary or another drone, change direction
        if (newX < 0 || newX >= config.gridSize || newY < 0 || newY >= config.gridSize ||
            state.drones.some(d => d.x === newX && d.y === newY)) {
            drone.direction = Math.floor(Math.random() * 4);
            return;
        }
        
        // Update position
        drone.x = newX;
        drone.y = newY;
        
        // Update display
        updateCell(newX, newY, 'drone');
        
        // Perform scan
        performScan(drone);
    });
    
    // Check for drone collision
    checkCollision();
}

// Perform surveillance scan from drone
function performScan(drone) {
    for (let dy = -config.scanRadius; dy <= config.scanRadius; dy++) {
        for (let dx = -config.scanRadius; dx <= config.scanRadius; dx++) {
            const x = drone.x + dx;
            const y = drone.y + dy;
            
            // Check boundaries
            if (x >= 0 && x < config.gridSize && y >= 0 && y < config.gridSize) {
                // Mark as scanned
                updateCell(x, y, 'scanned');
                
                // If player is in scan range, increase score (being detected is bad)
                if (x === state.player.x && y === state.player.y) {
                    state.score -= 10;
                    updateScore();
                }
            }
        }
    }
}

// Check for collisions
function checkCollision() {
    // Check if player is on a drone
    const collision = state.drones.some(d => 
        d.x === state.player.x && d.y === state.player.y
    );
    
    if (collision) {
        endGame(false);
    }
}

// Update score display
function updateScore() {
    scoreElement.textContent = `Score: ${Math.max(0, state.score)}`;
}

// Update timer display
function updateTimer() {
    if (!state.startTime || state.gameOver) return;
    
    const elapsed = Date.now() - state.startTime;
    const remaining = Math.max(0, config.gameDuration - elapsed);
    const seconds = Math.ceil(remaining / 1000);
    
    timerElement.textContent = `Time: ${seconds}s`;
    
    if (remaining <= 0) {
        endGame(true);
    }
}

// End the game
function endGame(success) {
    state.gameOver = true;
    state.endTime = Date.now();
    
    if (success) {
        state.score += Math.floor((config.gameDuration - (state.endTime - state.startTime)) / 1000) * 5;
        updateScore();
        alert(`Game Over! You evaded surveillance! Final Score: ${state.score}`);
    } else {
        alert(`Game Over! You were detected! Final Score: ${state.score}`);
    }
}

// Initialize game
function initGame() {
    initGrid();
    initPlayer();
    initDrones();
    
    state.score = 0;
    state.gameOver = false;
    state.startTime = Date.now();
    
    updateScore();
    updateTimer();
    
    // Set up player controls
    document.addEventListener('keydown', (e) => {
        switch (e.key) {
            case 'ArrowUp': movePlayer(0, -1); break;
            case 'ArrowRight': movePlayer(1, 0); break;
            case 'ArrowDown': movePlayer(0, 1); break;
            case 'ArrowLeft': movePlayer(-1, 0); break;
        }
    });
    
    // Set up game loop
    const playerInterval = setInterval(() => {
        if (state.gameOver) {
            clearInterval(playerInterval);
            clearInterval(droneInterval);
            clearInterval(timerInterval);
            return;
        }
    }, config.playerSpeed);
    
    const droneInterval = setInterval(moveDrones, config.droneSpeed);
    const timerInterval = setInterval(updateTimer, 1000);
}

// Start the game
initGame();
```

```css
