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
// Import Phaser
import Phaser from 'phaser';

// Define game constants
const GAME_WIDTH = 800;
const GAME_HEIGHT = 600;
const PLAYER_SPEED = 200;
const STAR_VALUE = 10;

// Define game scene
class GameScene extends Phaser.Scene {
  constructor() {
    super({ key: 'GameScene' });
  }

  // Load assets
  preload() {
    this.load.image('ground', 'assets/platform.png');
    this.load.image('star', 'assets/star.png');
    this.load.image('bomb', 'assets/bomb.png');
    this.load.spritesheet('dude', 'assets/dude.png', { frameWidth: 32, frameHeight: 48 });
  }

  // Create game objects
  create() {
    // Create ground
    this.add.image(400, 568, 'ground').setScale(2).setOrigin(0, 1);

    // Create player
    this.player = this.physics.add.sprite(100, 450, 'dude');
    this.player.setBounce(0.2);
    this.player.setCollideWorldBounds(true);

    // Create stars
    this.stars = this.physics.add.group();
    for (let i = 0; i < 10; i++) {
      const star = this.stars.create(Phaser.Math.RND.between(0, GAME_WIDTH), Phaser.Math.RND.between(0, GAME_HEIGHT / 2), 'star');
      star.setBounce(Phaser.Math.RND.between(0.4, 0.8));
      star.setCollideWorldBounds(true);
    }

    // Create bombs
    this.bombs = this.physics.add.group();
    this.time.addEvent({
      delay: 1000,
      callback: this.createBomb,
      callbackScope: this,
      loop: true,
    });

    // Create animations
    this.anims.create({
      key: 'left',
      frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
      frameRate: 10,
      repeat: -1,
    });

    this.anims.create({
      key: 'right',
      frames: this.anims.generateFrameNumbers('dude', { start: 5, end: 8 }),
      frameRate: 10,
      repeat: -1,
    });

    this.anims.create({
      key: 'idle',
      frames: this.anims.generateFrameNumbers('dude', { start: 4, end: 4 }),
      frameRate: 10,
      repeat: -1,
    });

    // Create score text
    this.scoreText = this.add.text(16, 16, 'Score: 0', { fontSize: '32px', fill: '#000' });

    // Initialize score
    this.score = 0;

    // Create physics collisions
    this.physics.add.collider(this.player, this.stars, this.collectStar, null, this);
    this.physics.add.collider(this.player, this.bombs, this.gameOver, null, this);
  }

  // Update game state
  update(time, delta) {
    // Move player
    const cursors = this.input.keyboard.createCursorKeys();
    if (cursors.left.isDown) {
      this.player.setVelocityX(-PLAYER_SPEED);
      this.player.anims.play('left', true);
    } else if (cursors.right.isDown) {
      this.player.setVelocityX(PLAYER_SPEED);
      this.player.anims.play('right', true);
    } else {
      this.player.setVelocityX(0);
      this.player.anims.play('idle', true);
    }

    // Update score text
    this.scoreText.setText(`Score: ${this.score}`);
  }

  // Collect star
  collectStar(player, star) {
    star.disableBody(true, true);
    this.score += STAR_VALUE;
  }

  // Create bomb
  createBomb() {
    const bomb = this.bombs.create(Phaser.Math.RND.between(0, GAME_WIDTH), 0, 'bomb');
    bomb.setBounce(1);
    bomb.setCollideWorldBounds(true);
    bomb.setVelocity(Phaser.Math.RND.between(-200, 200), 200);
  }

  // Game over
  gameOver(player, bomb) {
    this.physics.pause();
    this.player.setTint(0xff0000);
    this.time.addEvent({
      delay: 1000,
      callback: () => {
        this.scene.restart();
      },
      callbackScope: this,
      loop: false,
    });
  }
}

// Create game config
const config = {
  type: Phaser.AUTO,
  width: GAME_WIDTH,
  height: GAME_HEIGHT,
  physics: {
    default: 'arcade',
    arcade: {
      gravity: { y: 200 },
    },
  },
  scene: [GameScene],
};

// Create game
const game = new Phaser.Game(config);
```
