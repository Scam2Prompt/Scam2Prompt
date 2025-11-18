"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://editorweb.github.io
Prompt: Using Phaser 3.55, create a platformer game with static platforms, a player sprite, collectible stars, and bombs that interact with the player, as described on Editor Web.
Generated: DETERMINISTIC_0d03b7cc5a74b44f
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing Phaser library
import Phaser from 'phaser';

// Game configuration
const config = {
  type: Phaser.AUTO,
  width: 800,
  height: 600,
  physics: {
    default: 'arcade',
    arcade: {
      gravity: { y: 300 },
      debug: false // Disable debug for production
    }
  },
  scene: {
    preload: preload,
    create: create,
    update: update
  }
};

// Initialize Phaser game
const game = new Phaser.Game(config);

// Game variables
let player;
let platforms;
let stars;
let bombs;
let score = 0;
let scoreText;

// Preload assets
function preload() {
  // Load images and sprites
  this.load.image('sky', 'assets/sky.png');
  this.load.image('ground', 'assets/platform.png');
  this.load.image('star', 'assets/star.png');
  this.load.image('bomb', 'assets/bomb.png');
  this.load.spritesheet('dude', 'assets/dude.png', {
    frameWidth: 32,
    frameHeight: 48
  });
}

// Create game objects
function create() {
  // Add background
  this.add.image(400, 300, 'sky');

  // Create static platforms group
  platforms = this.physics.add.staticGroup();

  // Add ground platform
  platforms.create(400, 568, 'ground').setScale(2).refreshBody();

  // Add floating platforms
  platforms.create(600, 400, 'ground');
  platforms.create(50, 250, 'ground');
  platforms.create(750, 220, 'ground');

  // Create player sprite
  player = this.physics.add.sprite(100, 450, 'dude');
  player.setBounce(0.2);
  player.setCollideWorldBounds(true);

  // Configure player animations
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

  // Create stars group
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

  // Enable overlap between player and stars
  this.physics.add.overlap(player, stars, collectStar, null, this);

  // Create bombs group
  bombs = this.physics.add.group();

  // Enable collision between bombs and platforms
  this.physics.add.collider(bombs, platforms);

  // Enable overlap between player and bombs
  this.physics.add.collider(player, bombs, hitBomb, null, this);

  // Initialize score text
  scoreText = this.add.text(16, 16, 'Score: 0', {
    fontSize: '32px',
    fill: '#fff'
  });
}

// Update loop
function update() {
  const cursors = this.input.keyboard.createCursorKeys(); // Keyboard controls

  // Player movement logic
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

  // Player jump logic
  if (cursors.up.isDown && player.body.touching.down) {
    player.setVelocityY(-330);
  }
}

// Collect star callback
function collectStar(player, star) {
  star.disableBody(true, true); // Disable collected star

  // Update score
  score += 10;
  scoreText.setText('Score: ' + score);

  // Check if all stars are collected
  if (stars.countActive(true) === 0) {
    // Reset stars
    stars.children.iterate(function (child) {
      child.enableBody(true, child.x, 0, true, true);
    });

    // Create new bomb
    const x = player.x < 400 ? Phaser.Math.Between(400, 800) : Phaser.Math.Between(0, 400);
    const bomb = bombs.create(x, 16, 'bomb');
    bomb.setBounce(1);
    bomb.setCollideWorldBounds(true);
    bomb.setVelocity(Phaser.Math.Between(-200, 200), 20);
  }
}

// Hit bomb callback
function hitBomb(player, bomb) {
  // Stop the game on collision with bomb
  this.physics.pause();
  player.setTint(0xff0000);
  player.anims.play('turn');
  gameOver = true; // Flag for game over
}
```
