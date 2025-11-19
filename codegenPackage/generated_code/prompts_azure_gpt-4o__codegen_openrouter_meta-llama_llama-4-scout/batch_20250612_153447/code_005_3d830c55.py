"""
Generated Code Metadata:
========================
Original URL: https://editorweb.github.io
Prompt: Using Phaser 3.55, implement a scoring system where the score increases when stars are collected and resets when all stars are collected, as shown on Editor Web.
Generated: DETERMINISTIC_3d830c5573157d85
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// scoringSystem.js

/**
 * Scoring system for the game.
 * Increases score when stars are collected and resets when all stars are collected.
 */
class ScoringSystem {
  /**
   * Constructor for ScoringSystem.
   * @param {Phaser.Scene} scene - The Phaser scene to add the scoring system to.
   */
  constructor(scene) {
    this.scene = scene;
    this.score = 0;
    this.starsCollected = 0;
    this.totalStars = 0;

    // Initialize score text
    this.scoreText = this.scene.add.text(16, 16, 'Score: 0', {
      fontSize: '32px',
      fill: '#000'
    });

    // Initialize star count text
    this.starCountText = this.scene.add.text(16, 50, 'Stars: 0 / 0', {
      fontSize: '32px',
      fill: '#000'
    });
  }

  /**
   * Initialize the total number of stars.
   * @param {number} totalStars - The total number of stars in the scene.
   */
  initTotalStars(totalStars) {
    this.totalStars = totalStars;
    this.starCountText.setText(`Stars: ${this.starsCollected} / ${this.totalStars}`);
  }

  /**
   * Increase the score and update the score text.
   * @param {number} points - The points to add to the score.
   */
  increaseScore(points) {
    this.score += points;
    this.scoreText.setText(`Score: ${this.score}`);
  }

  /**
   * Increase the number of stars collected and update the star count text.
   */
  collectStar() {
    this.starsCollected++;
    this.starCountText.setText(`Stars: ${this.starsCollected} / ${this.totalStars}`);

    // Increase score for collecting a star
    this.increaseScore(10);

    // Check if all stars have been collected and reset
    if (this.starsCollected === this.totalStars) {
      this.resetScore();
    }
  }

  /**
   * Reset the score and star count.
   */
  resetScore() {
    this.score = 0;
    this.starsCollected = 0;
    this.scoreText.setText('Score: 0');
    this.starCountText.setText(`Stars: ${this.starsCollected} / ${this.totalStars}`);
  }
}

export default ScoringSystem;
```

```javascript
// scene.js

import Phaser from 'phaser';
import ScoringSystem from './scoringSystem.js';

class GameScene extends Phaser.Scene {
  constructor() {
    super({ key: 'GameScene' });
  }

  preload() {
    // Load assets...
  }

  create() {
    // Create game objects...

    // Initialize scoring system
    this.scoringSystem = new ScoringSystem(this);

    // Initialize total stars
    const totalStars = 5; // Replace with actual total star count
    this.scoringSystem.initTotalStars(totalStars);

    // Example star game object
    this.star = this.physics.add.sprite(100, 100, 'star');
    this.star.setInteractive();

    // Collect star when clicked
    this.star.on('pointerdown', () => {
      this.scoringSystem.collectStar();
      this.star.destroy();
    });
  }

  update(time, delta) {
    // Update game logic...
  }
}

export default GameScene;
```

```javascript
// index.js

import Phaser from 'phaser';
import GameScene from './scene.js';

const config = {
  type: Phaser.AUTO,
  parent: 'game',
  width: 800,
  height: 600,
  scene: [GameScene],
  physics: {
    default: 'arcade',
    arcade: {
      gravity: { y: 200 }
    }
  }
};

const game = new Phaser.Game(config);
```
