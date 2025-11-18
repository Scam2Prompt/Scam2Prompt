"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://editorweb.github.io
Prompt: Create a Phaser 3.55 game script that includes animations for a player sprite moving left, right, and turning, as demonstrated on Editor Web.
Generated: DETERMINISTIC_030b0aaa41fed7de
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Phaser 3.55 Game Script with Animations for Player Sprite

// Import Phaser library (required in non-browser environments, skip if running directly in browser)
// import Phaser from 'phaser';

// Configuration for the Phaser game
const config = {
  type: Phaser.AUTO, // Automatically choose WebGL or Canvas
  width: 800, // Game width
  height: 600, // Game height
  physics: {
    default: 'arcade', // Physics engine
    arcade: {
      gravity: { y: 0 }, // Disable gravity for top-down movement
      debug: false, // Set to true for debugging
    },
  },
  scene: {
    preload: preload, // Preload assets
    create: create, // Create the game world
    update: update, // Game loop updates
  },
};

// Initialize the game with the provided configuration
const game = new Phaser.Game(config);

// Variables
let player;
let cursors;

// Preload function to load assets
function preload() {
  // Load the player sprite sheet (48x48 pixels per frame)
  this.load.spritesheet('player', 'path/to/player_spritesheet.png', {
    frameWidth: 48, 
    frameHeight: 48,
  });
}

// Create function to initialize the game world
function create() {
  // Add the player sprite to the scene (positioned at the center)
  player = this.physics.add.sprite(400, 300, 'player');

  // Set player properties
  player.setCollideWorldBounds(true); // Prevent player from leaving the screen
  
  // Create animations
  this.anims.create({
    key: 'move-left', // Animation key for left movement
    frames: this.anims.generateFrameNumbers('player', { start: 0, end: 2 }),
    frameRate: 10, // Speed of animation
    repeat: -1, // Loop the animation
  });

  this.anims.create({
    key: 'move-right', // Animation key for right movement
    frames: this.anims.generateFrameNumbers('player', { start: 3, end: 5 }),
    frameRate: 10,
    repeat: -1,
  });

  this.anims.create({
    key: 'turn', // Animation key for idle/turning
    frames: [{ key: 'player', frame: 6 }],
    frameRate: 20,
  });

  // Enable keyboard input
  cursors = this.input.keyboard.createCursorKeys();
}

// Update function for game logic
function update() {
  // Reset player velocity
  player.setVelocity(0);

  // Movement logic
  if (cursors.left.isDown) {
    player.setVelocityX(-200); // Move left
    player.anims.play('move-left', true); // Play left animation
  } else if (cursors.right.isDown) {
    player.setVelocityX(200); // Move right
    player.anims.play('move-right', true); // Play right animation
  } else {
    player.anims.play('turn', true); // Default animation (idle/turning)
  }
}
```

> **Note:** Replace `'path/to/player_spritesheet.png'` with the actual path to your sprite sheet file. Make sure the sprite sheet follows the expected frame layout (e.g., `0-2` for left, `3-5` for right, and `6` for turning/idle).
