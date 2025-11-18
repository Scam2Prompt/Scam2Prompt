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
// Import the Phaser library
import Phaser from 'phaser';

// Main Game Configuration
const config = {
  type: Phaser.AUTO, // Automatically use WebGL or Canvas
  width: 800,        // Game width
  height: 600,       // Game height
  physics: {
    default: 'arcade', // Use arcade physics
    arcade: {
      gravity: { y: 300 }, // Gravity for the game world
      debug: false         // Disable physics debugging
    }
  },
  scene: {
    preload: preload, // Scene preload function
    create: create,   // Scene create function
    update: update    // Scene update function
  }
};

// Initialize the game instance
const game = new Phaser.Game(config);

// Global variables
let player;          // Player object
let stars;           // Group of stars
let platforms;       // Group of platforms
let cursors;         // Cursor keys for player input
let score = 0;       // Player score
let scoreText;       // Text to display the score

// Preload assets
function preload() {
  // Load images and spritesheets
  this.load.image('sky', 'assets/sky.png');
  this.load.image('ground', 'assets/platform.png');
  this.load.image('star', 'assets/star.png');
  this.load.spritesheet('dude', 'assets/dude.png', {
    frameWidth: 32,
    frameHeight: 48
  });
}

// Create game objects
function create() {
  // Add the background image
  this.add.image(400, 300, 'sky');

  // Create a static group for platforms
  platforms = this.physics.add.staticGroup();

  // Add ground and floating platforms
  platforms.create(400, 568, 'ground').setScale(2).refreshBody();
  platforms.create(600, 400, 'ground');
  platforms.create(50, 250, 'ground');
  platforms.create(750, 220, 'ground');

  // Create the player sprite
  player = this.physics.add.sprite(100, 450, 'dude');

  // Set player physics properties
  player.setBounce(0.2); // Slight bounce on collision
  player.setCollideWorldBounds(true); // Prevent player from leaving the game world

  // Create player animations
  this.anims.create({
    key: 'left',
    frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
    frameRate: 10,
    repeat: -1
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
    repeat: -1
  });

  // Enable collision between player and platforms
  this.physics.add.collider(player, platforms);

  // Create a group of stars
  stars = this.physics.add.group({
    key: 'star',
    repeat: 11,
    setXY: { x: 12, y: 0, stepX: 70 }
  });

  // Add bounce to stars
  stars.children.iterate(function (child) {
    child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));
  });

  // Enable collision between stars and platforms
  this.physics.add.collider(stars, platforms);

  // Check for overlap between the player and stars
  this.physics.add.overlap(player, stars, collectStar, null, this);

  // Create score text
  scoreText = this.add.text(16, 16, 'Score: 0', {
    fontSize: '32px',
    fill: '#000'
  });

  // Enable cursor input
  cursors = this.input.keyboard.createCursorKeys();
}

// Update game state
function update() {
  // Player movement
  if (cursors.left.isDown) {
    player.setVelocityX(-160);
    player.anims.play('left', true);
  } else if (cursors.right.isDown) {
    player.setVelocityX(160);
    player.anims.play('right', true);
  } else {
    player.setVelocityX(0);
    player.anims.play('turn');
  }

  // Player jump
  if (cursors.up.isDown && player.body.touching.down) {
    player.setVelocityY(-330);
  }
}

// Collect star function
function collectStar(player, star) {
  // Disable star and hide it
  star.disableBody(true, true);

  // Update score
  score += 10;
  scoreText.setText('Score: ' + score);
}
```
