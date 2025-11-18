"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://editorweb.github.io
Prompt: Using Phaser 3.55, implement a scoring system where the score increases when stars are collected and resets when all stars are collected, as shown on Editor Web.
Generated: DETERMINISTIC_3d830c5573157d85
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Main game configuration for Phaser 3
const config = {
    type: Phaser.AUTO, // Automatically choose WebGL or Canvas
    width: 800,        // Width of the game canvas
    height: 600,       // Height of the game canvas
    physics: {
        default: 'arcade', // Use arcade physics
        arcade: {
            gravity: { y: 300 }, // Apply gravity to objects
            debug: false         // Disable physics debugging
        }
    },
    scene: {
        preload: preload, // Preload assets
        create: create,   // Set up objects
        update: update    // Game update loop
    }
};

// Global variables for the game
let score = 0;         // Keeps track of the score
let scoreText;         // Displays the score on the screen
let stars;             // Group of collectible star objects

// Initialize the Phaser game instance
const game = new Phaser.Game(config);

/**
 * Preload game assets.
 */
function preload() {
    this.load.image('sky', 'assets/sky.png');      // Load background image
    this.load.image('ground', 'assets/platform.png'); // Load ground platform
    this.load.image('star', 'assets/star.png');    // Load star collectible
    this.load.spritesheet('dude', 'assets/dude.png', {
        frameWidth: 32,
        frameHeight: 48
    }); // Load character sprite
}

/**
 * Create game objects and set up the scene.
 */
function create() {
    // Add a background image
    this.add.image(400, 300, 'sky');

    // Create a static group for platforms
    const platforms = this.physics.add.staticGroup();

    // Add ground platform
    platforms.create(400, 568, 'ground').setScale(2).refreshBody();

    // Add floating platforms
    platforms.create(600, 400, 'ground');
    platforms.create(50, 250, 'ground');
    platforms.create(750, 220, 'ground');

    // Create a player sprite
    const player = this.physics.add.sprite(100, 450, 'dude');
    player.setBounce(0.2); // Adds a slight bounce effect when landing
    player.setCollideWorldBounds(true); // Prevents player from moving outside the game bounds

    // Enable collision between player and platforms
    this.physics.add.collider(player, platforms);

    // Create animation for player movement
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1 // Loop animation
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

    // Set up player controls
    const cursors = this.input.keyboard.createCursorKeys();

    // Create a group of stars
    stars = this.physics.add.group({
        key: 'star',
        repeat: 11, // Number of stars
        setXY: { x: 12, y: 0, stepX: 70 } // Starting position and spacing
    });

    stars.children.iterate((star) => {
        star.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8)); // Random bounce effect
    });

    // Enable collision between stars and platforms
    this.physics.add.collider(stars, platforms);

    // Add overlap check between player and stars
    this.physics.add.overlap(player, stars, collectStar, null, this);

    // Display score text
    scoreText = this.add.text(16, 16, 'Score: 0', {
        fontSize: '32px',
        fill: '#ffffff'
    });

    /**
     * Player movement logic inside the update function.
     */
    this.playerMovement = () => {
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

        if (cursors.up.isDown && player.body.touching.down) {
            player.setVelocityY(-330); // Jump effect
        }
    };
}

/**
 * Game update loop.
 */
function update() {
    if (this.playerMovement) {
        this.playerMovement();
    }
}

/**
 * Callback function for when a star is collected.
 * @param {Phaser.Physics.Arcade.Sprite} player - The player object.
 * @param {Phaser.Physics.Arcade.Sprite} star - The collected star object.
 */
function collectStar(player, star) {
    star.disableBody(true, true); // Hide and deactivate the collected star

    // Increment score when a star is collected
    score += 10;
    scoreText.setText(`Score: ${score}`);

    // Check if all stars have been collected
    if (stars.countActive(true) === 0) {
        // Reset stars and score
        stars.children.iterate((star) => {
            star.enableBody(true, star.x, 0, true, true);
        });
        score = 0;
        scoreText.setText(`Score: ${score}`);
    }
}
```
