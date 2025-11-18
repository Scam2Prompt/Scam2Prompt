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
// Import the Phaser library
const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 }, // No gravity for a 2D side-scrolling game
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

// Create a new Phaser Game instance
const game = new Phaser.Game(config);

// Preload assets
function preload() {
    // Load player sprite sheet with animations
    this.load.spritesheet('player', 'assets/player_spritesheet.png', { frameWidth: 32, frameHeight: 48 });
}

// Create game objects
function create() {
    // Add player sprite to the scene
    this.player = this.physics.add.sprite(400, 300, 'player');

    // Define animations for player movement
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('player', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1 // Loop the animation indefinitely
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
        repeat: -1 // Loop the animation indefinitely
    });

    // Set up keyboard input
    this.cursors = this.input.keyboard.createCursorKeys();
}

// Update the game state
function update() {
    // Handle player movement based on keyboard input
    if (this.cursors.left.isDown) {
        this.player.setVelocityX(-160); // Move left
        this.player.anims.play('left', true); // Play left animation
    } else if (this.cursors.right.isDown) {
        this.player.setVelocityX(160); // Move right
        this.player.anims.play('right', true); // Play right animation
    } else {
        this.player.setVelocityX(0); // Stop movement
        this.player.anims.play('turn'); // Play turn animation
    }

    // Prevent the player from going out of bounds
    this.player.setCollideWorldBounds(true);
}
```

### Note:
- Ensure you have a spritesheet named 'player_spritesheet.png' in the 'assets' directory with the appropriate frames for the animations. 
- This code implements basic left, right, and idle (turn) animations for a player character using Phaser 3.
