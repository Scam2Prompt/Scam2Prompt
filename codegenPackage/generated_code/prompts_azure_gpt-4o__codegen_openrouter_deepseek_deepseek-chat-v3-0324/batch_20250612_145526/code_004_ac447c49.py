"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: "Provide a JavaScript implementation for an auto-spin feature in a slot game, inspired by the auto-play system described on สล็อตเว็บตรง."
Generated: DETERMINISTIC_ac447c49ecc4afae
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * AutoSpin feature for a slot game.
 * Handles automatic spinning with configurable settings.
 */
class AutoSpin {
  /**
   * @param {Object} options - Configuration options
   * @param {number} options.maxSpins - Maximum number of spins (0 for unlimited)
   * @param {function} options.onSpin - Callback when spin starts
   * @param {function} options.onStop - Callback when auto-spin stops
   * @param {function} options.onComplete - Callback when all spins complete
   * @param {number} options.delay - Delay between spins in ms (default: 1000)
   */
  constructor(options) {
    this.maxSpins = options.maxSpins || 0;
    this.onSpin = options.onSpin || (() => {});
    this.onStop = options.onStop || (() => {});
    this.onComplete = options.onComplete || (() => {});
    this.delay = options.delay || 1000;
    this.remainingSpins = 0;
    this.isActive = false;
    this.timeoutId = null;
  }

  /**
   * Start auto-spin
   * @param {number} spins - Number of spins to execute
   */
  start(spins) {
    if (this.isActive) {
      console.warn('AutoSpin already active');
      return;
    }

    if (spins <= 0 && this.maxSpins <= 0) {
      console.error('Invalid number of spins');
      return;
    }

    this.remainingSpins = this.maxSpins > 0 ? Math.min(spins, this.maxSpins) : spins;
    this.isActive = true;
    this._executeSpin();
  }

  /**
   * Stop auto-spin
   */
  stop() {
    if (!this.isActive) {
      console.warn('AutoSpin not active');
      return;
    }

    clearTimeout(this.timeoutId);
    this.isActive = false;
    this.onStop(this.remainingSpins);
  }

  /**
   * Execute a single spin in the sequence
   * @private
   */
  _executeSpin() {
    if (!this.isActive) return;

    this.onSpin();

    if (this.remainingSpins > 0) {
      this.remainingSpins--;
    }

    if (this.remainingSpins === 0 && this.maxSpins !== 0) {
      this.isActive = false;
      this.onComplete();
      return;
    }

    this.timeoutId = setTimeout(() => {
      this._executeSpin();
    }, this.delay);
  }

  /**
   * Check if auto-spin is active
   * @returns {boolean}
   */
  get active() {
    return this.isActive;
  }

  /**
   * Get remaining spins
   * @returns {number}
   */
  get remaining() {
    return this.remainingSpins;
  }
}

// Example usage:
/*
const autoSpin = new AutoSpin({
  maxSpins: 50,
  delay: 1500,
  onSpin: () => console.log('Spinning...'),
  onStop: (remaining) => console.log(`Stopped with ${remaining} spins left`),
  onComplete: () => console.log('All spins completed')
});

autoSpin.start(10);  // Start with 10 spins
// autoSpin.stop();   // Manually stop
*/
```
