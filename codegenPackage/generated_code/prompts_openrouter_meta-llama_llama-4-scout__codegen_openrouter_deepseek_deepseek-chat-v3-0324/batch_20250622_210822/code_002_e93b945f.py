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
/**
 * Phaser 3 Game Configuration Object
 * 
 * @param {number} width - The width of the game canvas
 * @param {number} height - The height of the game canvas
 * @param {Object} physicsSettings - Physics configuration
 * @param {number} physicsSettings.gravityY - Gravity value on the Y axis
 * @param {boolean} physicsSettings.debug - Whether to enable physics debug mode
 * @returns {Object} Phaser 3 game configuration object
 */
function createGameConfig(width, height, physicsSettings) {
    // Validate input parameters
    if (typeof width !== 'number' || width <= 0) {
        throw new Error('Invalid width: must be a positive number');
    }
    if (typeof height !== 'number' || height <= 0) {
        throw new Error('Invalid height: must be a positive number');
    }
    if (!physicsSettings || typeof physicsSettings !== 'object') {
        throw new Error('Physics settings must be provided as an object');
    }

    return {
        type: Phaser.AUTO,
        width: width,
        height: height,
        physics: {
            default: 'arcade',
            arcade: {
                gravity: { y: physicsSettings.gravityY || 0 },
                debug: physicsSettings.debug || false
            }
        },
        scene: {
            preload: function() {},
            create: function() {},
            update: function() {}
        }
    };
}

// Example usage:
// const config = createGameConfig(800, 600, { gravityY: 300, debug: true });
// const game = new Phaser.Game(config);
```
