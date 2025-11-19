"""
Generated Code Metadata:
========================
Original URL: https://ton-station-2.gitbook.io
Prompt: Write code to implement a "Tomato Takedown" game mechanic, inspired by TON Station's Season 2 event, using Web3 gaming libraries.
Generated: DETERMINISTIC_ab786ae550cd6a60
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required Web3 and gaming libraries
const { ethers } = require('ethers');
const { Web3 } = require('web3');
const Phaser = require('phaser');

// Game configuration
const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create,
        update: update
    },
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },
            debug: false
        }
    }
};

// Initialize game
const game = new Phaser.Game(config);

// Web3 configuration
const web3 = new Web3(window.ethereum);
const contractAddress = '0x...'; // Replace with actual contract address
const contractABI = [...]; // Replace with actual contract ABI
let tomatoContract;

// Player and game state
let player;
let tomatoes = [];
let score = 0;
let scoreText;
let isConnected = false;

// Preload assets
function preload() {
    this.load.image('background', 'assets/background.png');
    this.load.image('player', 'assets/player.png');
    this.load.image('tomato', 'assets/tomato.png');
}

// Create game objects
function create() {
    // Add background
    this.add.image(400, 300, 'background');
    
    // Create player
    player = this.physics.add.sprite(400, 300, 'player');
    player.setCollideWorldBounds(true);
    
    // Setup controls
    cursors = this.input.keyboard.createCursorKeys();
    
    // Initialize Web3 connection
    initWeb3();
    
    // Score display
    scoreText = this.add.text(16, 16, 'Score: 0', { 
        fontSize: '32px', 
        fill: '#fff' 
    });
    
    // Spawn tomatoes periodically
    this.time.addEvent({
        delay: 1000,
        callback: spawnTomato,
        callbackScope: this,
        loop: true
    });
}

// Update game state
function update() {
    // Player movement
    if (cursors.left.isDown) {
        player.setVelocityX(-160);
    } else if (cursors.right.isDown) {
        player.setVelocityX(160);
    } else {
        player.setVelocityX(0);
    }

    if (cursors.up.isDown) {
        player.setVelocityY(-160);
    } else if (cursors.down.isDown) {
        player.setVelocityY(160);
    } else {
        player.setVelocityY(0);
    }
    
    // Check for tomato collisions
    this.physics.overlap(player, tomatoes, collectTomato, null, this);
}

// Initialize Web3 connection
async function initWeb3() {
    try {
        if (window.ethereum) {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            web3.setProvider(window.ethereum);
            tomatoContract = new web3.eth.Contract(contractABI, contractAddress);
            isConnected = true;
            console.log('Web3 connected successfully');
        } else {
            console.warn('MetaMask not detected, running in local mode');
        }
    } catch (error) {
        console.error('Error connecting to Web3:', error);
    }
}

// Spawn a new tomato
function spawnTomato() {
    const x = Phaser.Math.Between(50, 750);
    const y = Phaser.Math.Between(50, 550);
    const tomato = this.physics.add.sprite(x, y, 'tomato');
    tomatoes.push(tomato);
}

// Handle tomato collection
function collectTomato(player, tomato) {
    // Remove tomato from game
    tomato.destroy();
    tomatoes = tomatoes.filter(t => t !== tomato);
    
    // Update score
    score += 10;
    scoreText.setText('Score: ' + score);
    
    // If connected to Web3, update on-chain score
    if (isConnected) {
        updateOnChainScore(score);
    }
}

// Update score on blockchain
async function updateOnChainScore(newScore) {
    try {
        const accounts = await web3.eth.getAccounts();
        await tomatoContract.methods.updateScore(newScore).send({ from: accounts[0] });
        console.log('Score updated on chain');
    } catch (error) {
        console.error('Error updating score:', error);
    }
}

// Export for testing if needed
module.exports = {
    game,
    initWeb3,
    spawnTomato,
    collectTomato,
    updateOnChainScore
};
```
