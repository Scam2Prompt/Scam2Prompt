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
// Import the Phaser library
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

// Initialize a new Phaser game instance
const game = new Phaser.Game(config);

let score = 0; // Variable to track the score
let scoreText; // Text object to display the score
let stars; // Group for the stars
const totalStars = 12; // Total number of stars to collect

function preload() {
    // Load the star image
    this.load.image('star', 'assets/star.png');
}

function create() {
    // Initialize the stars group
    stars = this.physics.add.group({
        key: 'star',
        repeat: totalStars - 1,
        setXY: { x: 12, y: 0, stepX: 70 }
    });

    // Enable collision detection for the stars
    stars.children.iterate(star => {
        star.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8)); // Set bounce for stars
    });

    // Create the score text
    scoreText = this.add.text(16, 16, 'Score: 0', { fontSize: '32px', fill: '#fff' });

    // Set up cursor keys for player movement
    this.input.keyboard.on('keydown', onCollectStar, this);
}

function update() {
    // Update game logic continuously if needed
}

function onCollectStar(event) {
    // Check if the event corresponds to a star collection
    stars.children.iterate(star => {
        // Assuming some collision detection mechanism here
        if (star.getBounds().contains(event.x, event.y)) {
            star.setAlpha(0); // Hide the collected star
            score += 10; // Increment score
            scoreText.setText('Score: ' + score); // Update score text

            if (score === totalStars * 10) {
                // Reset score if all stars are collected
                score = 0; 
                scoreText.setText('Score: ' + score); // Reset score display
                resetStars(); // Reset stars for the next round
            }
        }
    });
}

function resetStars() {
    // Reset the stars group to visible and reposition them
    stars.children.iterate(star => {
        star.setAlpha(1); // Make all stars visible again
        star.setPosition(Phaser.Math.Between(0, 800), Phaser.Math.Between(0, 600)); // Randomly reposition stars
    });
}
```
