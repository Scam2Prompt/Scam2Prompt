"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://editorweb.github.io
Prompt: Generate code for a Phaser 3.55 game where the player can move left, right, and jump using keyboard input, and the score updates when stars are collected, based on the example on Editor Web.
Generated: DETERMINISTIC_086508b27927d2ae
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Phaser library
const { Scene, Game, Physics } = require('phaser');

// Configuration for the game
const config = {
    type: Phaser.AUTO, // Use WebGL or Canvas
    width: 800, // Game width
    height: 600, // Game height
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 }, // No gravity in the X direction
            debug: false // Set to true to see debug information
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

// Create a new Phaser Game
const game = new Game(config);

// Variables to hold game elements
let player;
let stars;
let score = 0;
let scoreText;

// Load assets
function preload() {
    this.load.image('sky', 'assets/sky.png'); // Background
    this.load.image('ground', 'assets/platform.png'); // Platforms
    this.load.image('star', 'assets/star.png'); // Stars
    this.load.spritesheet('dude', 'assets/dude.png', { frameWidth: 32, frameHeight: 48 }); // Player sprite
}

// Create game objects
function create() {
    // Set background
    this.add.image(400, 300, 'sky');

    // Create platforms group
    const platforms = this.physics.add.staticGroup();

    // Add ground and platforms
    platforms.create(400, 568, 'ground').setScale(2).refreshBody();
    platforms.create(600, 400, 'ground');
    platforms.create(50, 250, 'ground');
    platforms.create(750, 220, 'ground');

    // Create the player
    player = this.physics.add.sprite(100, 450, 'dude');

    // Configure player physics
    player.setBounce(0.2); // Bounce when hitting ground
    player.setCollideWorldBounds(true); // Prevent leaving the world

    // Create collision between player and platforms
    this.physics.add.collider(player, platforms);

    // Create stars group
    stars = this.physics.add.group({
        key: 'star',
        repeat: 11,
        setXY: { x: 12, y: 0, stepX: 70 }
    });

    // Enable collision between stars and platforms
    stars.children.iterate(function (child) {
        child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));
    });

    // Create collision between stars and platforms
    this.physics.add.collider(stars, platforms);

    // Create overlap detection between player and stars
    this.physics.add.overlap(player, stars, collectStar, null, this);

    // Create score text
    scoreText = this.add.text(16, 16, 'Score: 0', { fontSize: '32px', fill: '#fff' });

    // Input events for player movement
    this.cursors = this.input.keyboard.createCursorKeys();
}

// Update game state
function update() {
    // Handle player movement
    if (this.cursors.left.isDown) {
        player.setVelocityX(-160); // Move left
    } else if (this.cursors.right.isDown) {
        player.setVelocityX(160); // Move right
    } else {
        player.setVelocityX(0); // Stop movement
    }

    // Handle jumping
    if (this.cursors.up.isDown && player.body.touching.down) {
        player.setVelocityY(-330); // Jump
    }
}

// Function to collect stars and update score
function collectStar(player, star) {
    // Remove the collected star from the scene
    star.disableBody(true, true);

    // Update score
    score += 10; // Increase score by 10
    scoreText.setText('Score: ' + score); // Update score text

    // If all stars are collected
    if (stars.countActive(true) === 0) {
        // Reset stars for next round
        stars.children.iterate(function (child) {
            child.enableBody(true, child.x, 0, true, true);
        });
    }
}
``` 

Make sure to replace the asset paths (`sky.png`, `platform.png`, `star.png`, `dude.png`) with your own asset paths when running the game.
