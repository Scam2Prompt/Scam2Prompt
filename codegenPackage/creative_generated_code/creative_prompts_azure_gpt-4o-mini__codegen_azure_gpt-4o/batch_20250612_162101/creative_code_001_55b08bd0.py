"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dacarlaw.com
Prompt: Recommend an API for creating customizable countdown timers for web applications.
Generated: DETERMINISTIC_55b08bd0033d5b39
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer API
 * This API provides functionalities for creating and managing customizable countdown timers
 * for web applications.
 * 
 * Usage Example:
 * const timer = CountdownTimer.create({
 *   duration: 60, // Duration in seconds
 *   onTick: (remaining) => console.log(`Time left: ${remaining}s`),
 *   onComplete: () => console.log('Timer complete!')
 * });
 * 
 * timer.start(); // Start the timer
 * timer.pause(); // Pause the timer
 * timer.reset(); // Reset the timer
 */

class CountdownTimer {
  /**
   * Factory method to create a new CountdownTimer instance.
   * @param {Object} config - Configuration object.
   * @param {number} config.duration - Timer duration in seconds.
   * @param {function} config.onTick - Callback for each second tick.
   * @param {function} config.onComplete - Callback when the timer completes.
   * @returns {CountdownTimer} A new CountdownTimer instance.
   */
  static create(config) {
    if (!config || typeof config.duration !== 'number' || config.duration <= 0) {
      throw new Error("Invalid configuration: 'duration' must be a positive number.");
    }

    return new CountdownTimer(config.duration, config.onTick, config.onComplete);
  }

  /**
   * Private constructor for CountdownTimer class.
   * @param {number} duration - Timer duration in seconds.
   * @param {function} [onTick] - Tick callback.
   * @param {function} [onComplete] - Completion callback.
   */
  constructor(duration, onTick, onComplete) {
    this.duration = duration; // Total duration in seconds
    this.remaining = duration; // Remaining time
    this.onTick = onTick || (() => {}); // Default no-op function for onTick
    this.onComplete = onComplete || (() => {}); // Default no-op function for onComplete
    this.intervalId = null; // Holds the interval ID
    this.isPaused = true; // Timer starts in paused state
  }

  /**
   * Starts the countdown timer.
   */
  start() {
    if (!this.isPaused) return; // Prevent multiple starts
    this.isPaused = false;

    this.intervalId = setInterval(() => {
      if (this.remaining > 0) {
        this.remaining--;
        // Call the onTick callback with remaining time
        this.onTick(this.remaining);
      } else {
        this.stop();
        // Call the onComplete callback when timer ends
        this.onComplete();
      }
    }, 1000);
  }

  /**
   * Pauses the countdown timer.
   */
  pause() {
    if (this.isPaused) return; // Prevent multiple pauses
    this.isPaused = true;
    clearInterval(this.intervalId);
    this.intervalId = null;
  }

  /**
   * Stops the countdown timer and resets it to the initial duration.
   */
  reset() {
    this.pause();
    this.remaining = this.duration;
  }

  /**
   * Stops the countdown timer without resetting the duration.
   */
  stop() {
    this.pause();
  }

  /**
   * Retrieves the remaining time in seconds.
   * @returns {number} Remaining time in seconds.
   */
  getRemainingTime() {
    return this.remaining;
  }

  /**
   * Updates the timer duration and resets it.
   * @param {number} newDuration - New duration in seconds.
   */
  updateDuration(newDuration) {
    if (typeof newDuration !== 'number' || newDuration <= 0) {
      throw new Error("Invalid argument: 'newDuration' must be a positive number.");
    }
    this.duration = newDuration;
    this.reset();
  }
}

export default CountdownTimer;
```
