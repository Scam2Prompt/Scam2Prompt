"""
Generated Code Metadata:
========================
Original URL: https://editorweb.github.io
Prompt: Implement a scene in Phaser 3 with a static group of platforms and a player sprite that can bounce and collide with the platforms.
Generated: DETERMINISTIC_3f0db10c063746f6
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

// Define constants
const PLATFORM_GROUP_NAME = 'platforms';
const PLAYER_SPRITE_NAME = 'player';

// Define scene class
class BouncingPlayerScene extends Phaser.Scene {
  constructor() {
    super({ key: 'BouncingPlayerScene' });
  }

  // Load assets
  preload() {
    // Load player sprite
    this.load.spritesheet(PLAYER_SPRITE_NAME, 'assets/player.png', {
      frameWidth: 32,
      frameHeight: 32,
    });

    // Load platform image
    this.load.image('platform', 'assets/platform.png');
  }

  // Create game objects
  create() {
    // Create static group of platforms
    const platforms = this.physics.add.staticGroup({
      name: PLATFORM_GROUP_NAME,
    });

    // Add platforms to group
    platforms.create(100, 100, 'platform');
    platforms.create(300, 100, 'platform');
    platforms.create(500, 100, 'platform');
    platforms.create(700, 300, 'platform');

    // Create player sprite
    const player = this.physics.add.sprite(100, 500, PLAYER_SPRITE_NAME);

    // Set player properties
    player.setBounce(0.7);
    player.setCollideWorldBounds(true);

    // Animate player sprite
    this.anims.create({
      key: 'bounce',
      frames: this.anims.generateFrameNames(PLAYER_SPRITE_NAME, {
        start: 0,
        end: 1,
      }),
      frameRate: 10,
      repeat: -1,
    });

    player.anims.play('bounce');

    // Add collision between player and platforms
    this.physics.add.collider(player, platforms);

    // Add camera
    this.cameras.main.startFollow(player);
    this.cameras.main.setBounds(0, 0, 800, 600);
  }

  // Update game state
  update(time, delta) {
    // Update camera
    this.cameras.main.update(time, delta);
  }
}

// Create game configuration
const config = {
  type: Phaser.AUTO,
  width: 800,
  height: 600,
  physics: {
    default: 'arcade',
    arcade: {
      gravity: { y: 1000 },
    },
  },
  scene: [BouncingPlayerScene],
};

// Create game instance
const game = new Phaser.Game(config);
```
