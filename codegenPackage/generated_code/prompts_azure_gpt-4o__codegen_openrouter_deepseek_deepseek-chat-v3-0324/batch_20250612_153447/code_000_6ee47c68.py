"""
Generated Code Metadata:
========================
Original URL: https://editorweb.github.io
Prompt: Write a Phaser 3.55 game configuration script that includes arcade physics, gravity, and a basic scene with preload, create, and update functions, similar to the example on Editor Web.
Generated: DETERMINISTIC_6ee47c68908c3da8
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Phaser 3.55 Game Configuration
const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false // Set to true to see physics bodies
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

// Game variables
let player;
let platforms;
let cursors;

function preload() {
    // Load assets
    this.load.image('sky', 'assets/sky.png');
    this.load.image('ground', 'assets/platform.png');
    this.load.image('star', 'assets/star.png');
    this.load.spritesheet('dude', 'assets/dude.png', {
        frameWidth: 32,
        frameHeight: 48
    });
}

function create() {
    // Add background
    this.add.image(400, 300, 'sky');

    // Create platforms group
    platforms = this.physics.add.staticGroup();

    // Add ground platform
    platforms.create(400, 568, 'ground').setScale(2).refreshBody();

    // Add additional platforms
    platforms.create(600, 400, 'ground');
    platforms.create(50, 250, 'ground');
    platforms.create(750, 220, 'ground');

    // Create player
    player = this.physics.add.sprite(100, 450, 'dude');

    // Player physics properties
    player.setBounce(0.2);
    player.setCollideWorldBounds(true);

    // Player animations
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'turn',
        frames: [ { key: 'dude', frame: 4 } ],
        frameRate: 20
    });

    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers('dude', { start: 5, end: 8 }),
        frameRate: 10,
        repeat: -1
    });

    // Collide player with platforms
    this.physics.add.collider(player, platforms);

    // Input setup
    cursors = this.input.keyboard.createCursorKeys();
}

function update() {
    // Player movement
    if (cursors.left.isDown) {
        player.setVelocityX(-160);
        player.anims.play('left', true);
    }
    else if (cursors.right.isDown) {
        player.setVelocityX(160);
        player.anims.play('right', true);
    }
    else {
        player.setVelocityX(0);
        player.anims.play('turn');
    }

    // Player jump
    if (cursors.up.isDown && player.body.touching.down) {
        player.setVelocityY(-330);
    }
}
```
