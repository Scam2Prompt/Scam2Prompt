"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://editorweb.github.io
Prompt: Write a Phaser 3.55 game configuration script that includes arcade physics, gravity, and a basic scene with preload, create, and update functions, similar to the example on Editor Web.
Generated: DETERMINISTIC_6ee47c68908c3da8
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Phaser library
import Phaser from 'phaser';

// Game configuration object
const config = {
    type: Phaser.AUTO, // Automatically choose WebGL or Canvas rendering
    width: 800, // Width of the game canvas
    height: 600, // Height of the game canvas
    physics: {
        default: 'arcade', // Enable Arcade physics
        arcade: {
            gravity: { y: 300 }, // Vertical gravity
            debug: false // Disable debug mode for production
        }
    },
    scene: {
        preload: preload, // Scene preload method
        create: create,   // Scene create method
        update: update    // Scene update method
    }
};

// Create a new Phaser game instance
const game = new Phaser.Game(config);

// Game variables (these will be used across the scene)
let player;
let platforms;

// Preload function: used to load assets
function preload() {
    // Load the background image
    this.load.image('sky', 'assets/sky.png');

    // Load the platform image
    this.load.image('ground', 'assets/platform.png');

    // Load the player sprite sheet
    this.load.spritesheet('dude', 'assets/dude.png', {
        frameWidth: 32,
        frameHeight: 48
    });
}

// Create function: used to set up the game objects
function create() {
    // Add background image to the scene
    this.add.image(400, 300, 'sky');

    // Create a static group of platforms
    platforms = this.physics.add.staticGroup();

    // Create ground platform
    platforms.create(400, 568, 'ground').setScale(2).refreshBody();

    // Create a floating platform
    platforms.create(600, 400, 'ground');
    platforms.create(50, 250, 'ground');
    platforms.create(750, 220, 'ground');

    // Create the player sprite and enable physics on it
    player = this.physics.add.sprite(100, 450, 'dude');

    // Prevent the player from leaving the game bounds
    player.setCollideWorldBounds(true);

    // Set bounce physics property for the player
    player.setBounce(0.2);

    // Add animations for the player character
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1 // Repeat forever
    });

    this.anims.create({
        key: 'turn',
        frames: [{ key: 'dude', frame: 4 }],
        frameRate: 20
    });

    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers('dude', { start: 5, end: 8 }),
        frameRate: 10,
        repeat: -1 // Repeat forever
    });

    // Enable collision between the player and platforms
    this.physics.add.collider(player, platforms);

    // Create cursor keys for player input
    this.cursors = this.input.keyboard.createCursorKeys();
}

// Update function: runs every frame
function update() {
    // Arrow keys movement logic
    if (this.cursors.left.isDown) {
        player.setVelocityX(-160); // Move left
        player.anims.play('left', true); // Play left animation
    } else if (this.cursors.right.isDown) {
        player.setVelocityX(160); // Move right
        player.anims.play('right', true); // Play right animation
    } else {
        player.setVelocityX(0); // Stop movement
        player.anims.play('turn'); // Play idle animation
    }

    // Jump logic: player can only jump if touching a platform
    if (this.cursors.up.isDown && player.body.touching.down) {
        player.setVelocityY(-330); // Jump up
    }
}
```
