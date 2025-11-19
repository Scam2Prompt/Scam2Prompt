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
// BalloonGame.js

/**
 * Represents a balloon in the game.
 */
class Balloon {
  /**
   * Creates a new balloon.
   * @param {number} initialHeight - The initial height of the balloon.
   */
  constructor(initialHeight = 0) {
    this.height = initialHeight;
    this.maxHeight = 100; // Maximum height the balloon can reach
    this.minHeight = 0; // Minimum height the balloon can have
  }

  /**
   * Increases the height of the balloon by a given amount.
   * @param {number} amount - The amount to increase the height by.
   */
  heat(amount) {
    if (amount < 0) {
      throw new Error("Heat amount cannot be negative.");
    }
    this.height = Math.min(this.height + amount, this.maxHeight);
  }

  /**
   * Decreases the height of the balloon by a given amount.
   * @param {number} amount - The amount to decrease the height by.
   */
  cool(amount) {
    if (amount < 0) {
      throw new Error("Cool amount cannot be negative.");
    }
    this.height = Math.max(this.height - amount, this.minHeight);
  }
}

/**
 * Represents the game.
 */
class Game {
  /**
   * Creates a new game.
   */
  constructor() {
    this.balloon = new Balloon();
    this.listeners = [];
  }

  /**
   * Adds an event listener to the game.
   * @param {function} listener - The listener to add.
   */
  addEventListener(listener) {
    if (typeof listener === "function") {
      this.listeners.push(listener);
    } else {
      throw new Error("Listener must be a function.");
    }
  }

  /**
   * Removes an event listener from the game.
   * @param {function} listener - The listener to remove.
   */
  removeEventListener(listener) {
    if (typeof listener === "function") {
      this.listeners = this.listeners.filter((l) => l !== listener);
    } else {
      throw new Error("Listener must be a function.");
    }
  }

  /**
   * Notifies all listeners of a change in the balloon's height.
   */
  notifyListeners() {
    this.listeners.forEach((listener) => listener(this.balloon.height));
  }

  /**
   * Heats the balloon by a given amount.
   * @param {number} amount - The amount to heat the balloon by.
   */
  heatBalloon(amount) {
    this.balloon.heat(amount);
    this.notifyListeners();
  }

  /**
   * Cools the balloon by a given amount.
   * @param {number} amount - The amount to cool the balloon by.
   */
  coolBalloon(amount) {
    this.balloon.cool(amount);
    this.notifyListeners();
  }
}

// Example usage:
function main() {
  const game = new Game();

  // Add an event listener to track the balloon's height
  game.addEventListener((height) => console.log(`Balloon height: ${height}`));

  // Heat the balloon
  game.heatBalloon(20);
  game.heatBalloon(30);
  game.coolBalloon(10);
}

main();
```
