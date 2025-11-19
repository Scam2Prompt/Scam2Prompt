"""
Generated Code Metadata:
========================
Original URL: https://private-gomble.pages.dev
Prompt: Write JavaScript code for a simple event-based game where users can "heat a balloon" and track its height, inspired by the mechanics described in GOMBLE's "Heat the Balloon" game.
Generated: DETERMINISTIC_2ff97f4bcf99347b
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Heat the Balloon Game
 * A simple event-based game where users heat a balloon to make it rise.
 */

class BalloonGame {
  constructor() {
    this.height = 0;
    this.maxHeight = 1000;
    this.heatLevel = 0;
    this.maxHeat = 10;
    this.isPopped = false;
    this.gameActive = false;
    this.score = 0;
    this.gameDuration = 30000; // 30 seconds
    this.gameInterval = null;
    this.heatInterval = null;
    this.eventListeners = {
      heat: [],
      pop: [],
      heightChange: [],
      gameStart: [],
      gameEnd: []
    };
  }

  /**
   * Start the game
   */
  startGame() {
    if (this.gameActive) return;

    this.resetGame();
    this.gameActive = true;
    this.emit('gameStart');

    // Main game loop
    this.gameInterval = setInterval(() => {
      this.updateHeight();
      this.emit('heightChange', this.height);
    }, 100);

    // Game timer
    setTimeout(() => {
      this.endGame();
    }, this.gameDuration);
  }

  /**
   * End the game
   */
  endGame() {
    if (!this.gameActive) return;

    clearInterval(this.gameInterval);
    clearInterval(this.heatInterval);
    this.gameActive = false;
    this.emit('gameEnd', this.score);
  }

  /**
   * Reset game state
   */
  resetGame() {
    this.height = 0;
    this.heatLevel = 0;
    this.isPopped = false;
    this.score = 0;
    clearInterval(this.gameInterval);
    clearInterval(this.heatInterval);
  }

  /**
   * Apply heat to the balloon
   */
  applyHeat() {
    if (!this.gameActive || this.isPopped) return;

    if (this.heatLevel < this.maxHeat) {
      this.heatLevel++;
      this.emit('heat', this.heatLevel);
    }

    // Heat decays over time
    if (this.heatInterval) clearInterval(this.heatInterval);
    this.heatInterval = setInterval(() => {
      if (this.heatLevel > 0) {
        this.heatLevel--;
        this.emit('heat', this.heatLevel);
      } else {
        clearInterval(this.heatInterval);
      }
    }, 500);
  }

  /**
   * Update balloon height based on heat level
   */
  updateHeight() {
    if (this.isPopped) return;

    // Increase height based on heat level
    const heightIncrease = this.heatLevel * 0.5;
    this.height += heightIncrease;
    this.score = Math.floor(this.height);

    // Random chance to pop based on heat level
    if (this.heatLevel > 7 && Math.random() < 0.05) {
      this.popBalloon();
      return;
    }

    // Cap the maximum height
    if (this.height > this.maxHeight) {
      this.height = this.maxHeight;
      this.endGame();
    }
  }

  /**
   * Pop the balloon
   */
  popBalloon() {
    this.isPopped = true;
    this.heatLevel = 0;
    this.emit('pop');
    this.endGame();
  }

  /**
   * Add event listener
   * @param {string} event - Event name
   * @param {function} callback - Callback function
   */
  on(event, callback) {
    if (this.eventListeners[event]) {
      this.eventListeners[event].push(callback);
    }
  }

  /**
   * Emit event to all listeners
   * @param {string} event - Event name
   * @param {*} data - Data to pass to listeners
   */
  emit(event, data = null) {
    if (this.eventListeners[event]) {
      this.eventListeners[event].forEach(callback => {
        callback(data);
      });
    }
  }
}

// Example usage:
/*
const game = new BalloonGame();

game.on('gameStart', () => {
  console.log('Game started!');
});

game.on('heat', (level) => {
  console.log(`Heat level: ${level}`);
});

game.on('heightChange', (height) => {
  console.log(`Balloon height: ${Math.floor(height)}m`);
});

game.on('pop', () => {
  console.log('Balloon popped!');
});

game.on('gameEnd', (score) => {
  console.log(`Game over! Final score: ${score}`);
});

// Start the game
game.startGame();

// Simulate heating (in a real game, this would be triggered by user input)
setInterval(() => {
  game.applyHeat();
}, 300);
*/
```
