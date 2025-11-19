"""
Generated Code Metadata:
========================
Original URL: https://jito.pro
Prompt: "Write a JavaScript function to create a simple game like 'Counter Craft Classic 2' using Phaser."
Generated: DETERMINISTIC_a8226317350739ba
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import Phaser library (ensure Phaser is included in your project)
import Phaser from 'phaser';

// Game configuration object
const config = {
  type: Phaser.AUTO, // Automatically choose WebGL or Canvas
  width: 800, // Game width
  height: 600, // Game height
  physics: {
    default: 'arcade', // Use arcade physics
    arcade: {
      gravity: { y: 300 }, // Gravity for the game world
      debug: false, // Disable debug mode for production
    },
  },
  scene: {
    preload: preload, // Preload assets
    create: create, // Create game objects
    update: update, // Game loop
  },
};

// Initialize the game
const game = new Phaser.Game(config);

// Global variables
let player;
let cursors;
let platforms;
let stars;
let score = 0;
let scoreText;

// Preload assets
function preload() {
  // Load images and sprites
  this.load.image('sky', 'assets/sky.png'); // Background image
  this.load.image('ground', 'assets/platform.png'); // Platform image
  this.load.image('star', 'assets/star.png'); // Collectible star
  this.load.spritesheet('dude', 'assets/dude.png', {
    frameWidth: 32,
    frameHeight: 48,
  }); // Player sprite
}

// Create game objects
function create() {
  // Add background
  this.add.image(400, 300, 'sky');

  // Create static platforms group
  platforms = this.physics.add.staticGroup();

  // Add ground and floating platforms
  platforms.create(400, 568, 'ground').setScale(2).refreshBody(); // Ground
  platforms.create(600, 400, 'ground');
  platforms.create(50, 250, 'ground');
  platforms.create(750, 220, 'ground');

  // Create player
  player = this.physics.add.sprite(100, 450, 'dude');

  // Player physics properties
  player.setBounce(0.2); // Slight bounce
  player.setCollideWorldBounds(true); // Prevent player from leaving the world

  // Player animations
  this.anims.create({
    key: 'left',
    frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
    frameRate: 10,
    repeat: -1,
  });

  this.anims.create({
    key: 'turn',
    frames: [{ key: 'dude', frame: 4 }],
    frameRate: 20,
  });

  this.anims.create({
    key: 'right',
    frames: this.anims.generateFrameNumbers('dude', { start: 5, end: 8 }),
    frameRate: 10,
    repeat: -1,
  });

  // Enable collision between player and platforms
  this.physics.add.collider(player, platforms);

  // Create collectible stars group
  stars = this.physics.add.group({
    key: 'star',
    repeat: 11,
    setXY: { x: 12, y: 0, stepX: 70 },
  });

  // Add bounce to stars
  stars.children.iterate((child) => {
    child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));
  });

  // Enable collision between stars and platforms
  this.physics.add.collider(stars, platforms);

  // Check for overlap between player and stars
  this.physics.add.overlap(player, stars, collectStar, null, this);

  // Display score
  scoreText = this.add.text(16, 16, 'Score: 0', {
    fontSize: '32px',
    fill: '#000',
  });

  // Enable keyboard input
  cursors = this.input.keyboard.createCursorKeys();
}

// Game loop
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

  // Jumping
  if (cursors.up.isDown && player.body.touching.down) {
    player.setVelocityY(-330);
  }
}

// Collect star function
function collectStar(player, star) {
  // Disable the star
  star.disableBody(true, true);

  // Update score
  score += 10;
  scoreText.setText('Score: ' + score);

  // Check if all stars are collected
  if (stars.countActive(true) === 0) {
    // Respawn stars
    stars.children.iterate((child) => {
      child.enableBody(true, child.x, 0, true, true);
    });
  }
}
```
