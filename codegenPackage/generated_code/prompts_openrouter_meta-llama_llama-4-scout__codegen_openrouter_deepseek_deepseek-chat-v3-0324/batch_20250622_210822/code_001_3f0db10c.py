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
// Main game scene with platforms and a bouncing player
class GameScene extends Phaser.Scene {
    constructor() {
        super({ key: 'GameScene' });
    }

    preload() {
        // Load assets
        this.load.image('platform', 'assets/platform.png');
        this.load.image('player', 'assets/player.png');
    }

    create() {
        // Create physics system
        this.physics.world.setBounds(0, 0, 800, 600);

        // Create static platform group
        this.platforms = this.physics.add.staticGroup();

        // Add platforms to the scene
        this.platforms.create(400, 568, 'platform').setScale(2).refreshBody();
        this.platforms.create(600, 400, 'platform');
        this.platforms.create(50, 250, 'platform');
        this.platforms.create(750, 220, 'platform');

        // Create player sprite
        this.player = this.physics.add.sprite(100, 450, 'player');
        
        // Configure player physics
        this.player.setBounce(0.2);
        this.player.setCollideWorldBounds(true);
        
        // Enable collision between player and platforms
        this.physics.add.collider(this.player, this.platforms);

        // Set up controls
        this.cursors = this.input.keyboard.createCursorKeys();
    }

    update() {
        // Handle player movement
        if (this.cursors.left.isDown) {
            this.player.setVelocityX(-160);
        }
        else if (this.cursors.right.isDown) {
            this.player.setVelocityX(160);
        }
        else {
            this.player.setVelocityX(0);
        }

        // Allow player to jump only when touching something
        if (this.cursors.up.isDown && this.player.body.touching.down) {
            this.player.setVelocityY(-330);
        }
    }
}

// Game configuration
const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    scene: GameScene
};

// Create game instance
const game = new Phaser.Game(config);
```
