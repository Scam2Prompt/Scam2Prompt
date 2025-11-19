"""
Generated Code Metadata:
========================
Original URL: https://editorweb.github.io
Prompt: Create a Phaser 3.55 game script that includes animations for a player sprite moving left, right, and turning, as demonstrated on Editor Web.
Generated: DETERMINISTIC_030b0aaa41fed7de
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Phaser 3.55 Game with Player Animations
// This script creates a simple game with a player sprite that has animations for moving left, right, and turning.

// Game configuration
const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

// Create the game instance
const game = new Phaser.Game(config);

// Global variables
let player;
let cursors;
let lastDirection = 'right';

function preload() {
    // Load player sprite sheet
    this.load.spritesheet('player', 'assets/player.png', {
        frameWidth: 32,
        frameHeight: 48
    });
}

function create() {
    // Create player sprite
    player = this.physics.add.sprite(400, 300, 'player');
    player.setCollideWorldBounds(true);

    // Create animations
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('player', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'turn',
        frames: [{ key: 'player', frame: 4 }],
        frameRate: 20
    });

    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers('player', { start: 5, end: 8 }),
        frameRate: 10,
        repeat: -1
    });

    // Set up keyboard input
    cursors = this.input.keyboard.createCursorKeys();
}

function update() {
    // Reset player velocity when no keys are pressed
    player.setVelocity(0);

    // Horizontal movement
    if (cursors.left.isDown) {
        player.setVelocityX(-160);
        player.anims.play('left', true);
        lastDirection = 'left';
    } else if (cursors.right.isDown) {
        player.setVelocityX(160);
        player.anims.play('right', true);
        lastDirection = 'right';
    } else {
        // Play idle animation when not moving
        player.anims.play('turn', true);
    }

    // Vertical movement (optional)
    if (cursors.up.isDown) {
        player.setVelocityY(-160);
    } else if (cursors.down.isDown) {
        player.setVelocityY(160);
    }

    // Maintain facing direction when stopping
    if (player.body.velocity.x === 0 && player.body.velocity.y === 0) {
        player.anims.play('turn', true);
    }
}
```
