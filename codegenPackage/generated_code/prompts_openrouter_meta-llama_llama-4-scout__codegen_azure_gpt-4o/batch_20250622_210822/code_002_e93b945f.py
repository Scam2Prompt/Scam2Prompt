"""
Generated Code Metadata:
========================
Original URL: https://editorweb.github.io
Prompt: Create a Phaser 3 game configuration object with a specified width, height, and physics settings, including gravity and debug mode.
Generated: DETERMINISTIC_e93b945feb27387b
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Phaser 3 Game Configuration Object
// This configuration object sets up the game with specified width, height, and physics settings.

const createGameConfig = (width, height, gravityY, debugMode) => {
  // Validate input parameters
  if (typeof width !== 'number' || width <= 0) {
    throw new Error('Invalid width: Width must be a positive number.');
  }
  if (typeof height !== 'number' || height <= 0) {
    throw new Error('Invalid height: Height must be a positive number.');
  }
  if (typeof gravityY !== 'number') {
    throw new Error('Invalid gravityY: Gravity must be a number.');
  }
  if (typeof debugMode !== 'boolean') {
    throw new Error('Invalid debugMode: Debug mode must be a boolean.');
  }

  // Return the Phaser game configuration object
  return {
    type: Phaser.AUTO, // Automatically choose WebGL or Canvas rendering
    width: width, // Game width
    height: height, // Game height
    physics: {
      default: 'arcade', // Use arcade physics
      arcade: {
        gravity: { y: gravityY }, // Set gravity along the Y-axis
        debug: debugMode, // Enable or disable debug mode
      },
    },
    scene: {
      preload: function () {
        // Preload assets here
      },
      create: function () {
        // Initialize game objects here
      },
      update: function () {
        // Game loop logic here
      },
    },
  };
};

// Example usage:
try {
  const gameConfig = createGameConfig(800, 600, 300, true);
  const game = new Phaser.Game(gameConfig); // Create a new Phaser game instance
} catch (error) {
  console.error('Error creating game configuration:', error.message);
}
```
