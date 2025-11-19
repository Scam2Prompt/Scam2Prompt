"""
Generated Code Metadata:
========================
Original URL: https://editorweb.github.io
Prompt: Write a Phaser 3 game that includes a player character that can move left and right, and collect stars while avoiding bombs.
Generated: DETERMINISTIC_8d6ab185e7baac2c
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import Phaser library
import Phaser from 'phaser';

// Game configuration
const config = {
  type: Phaser.AUTO, // Automatically choose WebGL or Canvas
  width: 800, // Game width
  height: 600, // Game height
  physics: {
    default: 'arcade', // Use arcade physics
    arcade: {
      gravity: { y: 300 }, // Gravity for the game world
      debug: false, // Disable debug mode
    },
  },
  scene: {
    preload: preload, // Preload assets
    create: create, // Create game objects
    update: update, // Update game logic
  },
};

// Initialize the game
const game = new Phaser.Game(config);

// Global variables
let player; // Player character
let stars; // Group of collectible stars
let bombs; // Group of bombs
let cursors; // Keyboard input
let score = 0; // Player score
let scoreText; // Text to display score

// Preload assets
function preload() {
  // Load images
  this.load.image('sky', 'assets/sky.png');
  this.load.image('ground', 'assets/platform.png');
  this.load.image('star', 'assets/star.png');
  this.load.image('bomb', 'assets/bomb.png');

  // Load sprite sheet for player
  this.load.spritesheet('dude', 'assets/dude.png', {
    frameWidth: 32,
    frameHeight: 48,
  });
}

// Create game objects
function create() {
  // Add background
  this.add.image(400, 300, 'sky');

  // Create static platforms group
  const platforms = this.physics.add.staticGroup();

  // Add ground platform
  platforms.create(400, 568, 'ground').setScale(2).refreshBody();

  // Add floating platforms
  platforms.create(600, 400, 'ground');
  platforms.create(50, 250, 'ground');
  platforms.create(750, 220, 'ground');

  // Create player character
  player = this.physics.add.sprite(100, 450, 'dude');
  player.setBounce(0.2); // Slight bounce on landing
  player.setCollideWorldBounds(true); // Prevent player from leaving the game world

  // Add player animations
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

  // Create group of stars
  stars = this.physics.add.group({
    key: 'star',
    repeat: 11, // Number of stars
    setXY: { x: 12, y: 0, stepX: 70 }, // Position and spacing
  });

  // Add bounce to stars
  stars.children.iterate((child) => {
    child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));
  });

  // Enable collision between stars and platforms
  this.physics.add.collider(stars, platforms);

  // Allow player to collect stars
  this.physics.add.overlap(player, stars, collectStar, null, this);

  // Create group of bombs
  bombs = this.physics.add.group();

  // Enable collision between bombs and platforms
  this.physics.add.collider(bombs, platforms);

  // Enable collision between player and bombs
  this.physics.add.collider(player, bombs, hitBomb, null, this);

  // Display score
  scoreText = this.add.text(16, 16, 'Score: 0', {
    fontSize: '32px',
    fill: '#000',
  });

  // Enable keyboard input
  cursors = this.input.keyboard.createCursorKeys();
}

// Update game logic
function update() {
  // Player movement
  if (cursors.left.isDown) {
    player.setVelocityX(-160); // Move left
    player.anims.play('left', true); // Play left animation
  } else if (cursors.right.isDown) {
    player.setVelocityX(160); // Move right
    player.anims.play('right', true); // Play right animation
  } else {
    player.setVelocityX(0); // Stop moving
    player.anims.play('turn'); // Play idle animation
  }

  // Allow player to jump if touching the ground
  if (cursors.up.isDown && player.body.touching.down) {
    player.setVelocityY(-330); // Jump
  }
}

// Collect star
function collectStar(player, star) {
  star.disableBody(true, true); // Remove star from game

  // Update score
  score += 10;
  scoreText.setText('Score: ' + score);

  // Check if all stars are collected
  if (stars.countActive(true) === 0) {
    // Respawn stars
    stars.children.iterate((child) => {
      child.enableBody(true, child.x, 0, true, true);
    });

    // Spawn a bomb
    const x =
      player.x < 400
        ? Phaser.Math.Between(400, 800)
        : Phaser.Math.Between(0, 400);
    const bomb = bombs.create(x, 16, 'bomb');
    bomb.setBounce(1); // Bomb bounces
    bomb.setCollideWorldBounds(true); // Prevent bomb from leaving the game world
    bomb.setVelocity(Phaser.Math.Between(-200, 200), 20); // Random velocity
  }
}

// Handle player hitting a bomb
function hitBomb(player, bomb) {
  // Stop the game
  this.physics.pause();

  // Change player tint to red
  player.setTint(0xff0000);

  // Play death animation
  player.anims.play('turn');

  // End the game
  gameOver = true;
}
```
