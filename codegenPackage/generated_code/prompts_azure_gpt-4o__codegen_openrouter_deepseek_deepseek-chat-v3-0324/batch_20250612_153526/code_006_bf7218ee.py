"""
Generated Code Metadata:
========================
Original URL: https://pacm.pages.dev
Prompt: Create a JavaScript function to display real-time countdowns for multiple events, similar to the Pacmoon airdrop timers.
Generated: DETERMINISTIC_bf7218ee6af08692
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * CountdownManager - Manages multiple real-time countdowns
 */
class CountdownManager {
  /**
   * @constructor
   * @param {Object} options - Configuration options
   * @param {string} options.containerId - ID of the container element
   * @param {string} options.countdownClass - CSS class for countdown elements
   * @param {boolean} options.autoStart - Whether to start countdowns immediately
   */
  constructor(options = {}) {
    this.defaultOptions = {
      containerId: 'countdown-container',
      countdownClass: 'countdown-timer',
      autoStart: true,
      refreshInterval: 1000
    };
    this.options = { ...this.defaultOptions, ...options };
    this.countdowns = new Map();
    this.intervalId = null;
    this.container = document.getElementById(this.options.containerId);
    
    if (!this.container) {
      throw new Error(`Container element with ID '${this.options.containerId}' not found`);
    }
    
    if (this.options.autoStart) {
      this.start();
    }
  }

  /**
   * Add a new countdown
   * @param {string} id - Unique identifier for the countdown
   * @param {Date} endTime - End time for the countdown
   * @param {Function} [callback] - Callback when countdown completes
   * @param {Object} [options] - Additional options for this countdown
   * @returns {boolean} True if countdown was added successfully
   */
  addCountdown(id, endTime, callback = null, options = {}) {
    if (this.countdowns.has(id)) {
      console.warn(`Countdown with ID '${id}' already exists`);
      return false;
    }

    if (!(endTime instanceof Date)) {
      throw new Error('endTime must be a Date object');
    }

    const countdownElement = document.createElement('div');
    countdownElement.className = this.options.countdownClass;
    countdownElement.id = `countdown-${id}`;
    this.container.appendChild(countdownElement);

    this.countdowns.set(id, {
      element: countdownElement,
      endTime,
      callback,
      ...options
    });

    this.updateCountdown(id);
    return true;
  }

  /**
   * Remove a countdown
   * @param {string} id - ID of the countdown to remove
   * @returns {boolean} True if countdown was removed
   */
  removeCountdown(id) {
    if (!this.countdowns.has(id)) {
      return false;
    }

    const { element } = this.countdowns.get(id);
    element.remove();
    this.countdowns.delete(id);

    if (this.countdowns.size === 0) {
      this.stop();
    }

    return true;
  }

  /**
   * Start the countdown manager
   */
  start() {
    if (this.intervalId !== null) return;

    this.intervalId = setInterval(() => {
      this.countdowns.forEach((_, id) => this.updateCountdown(id));
    }, this.options.refreshInterval);
  }

  /**
   * Stop the countdown manager
   */
  stop() {
    if (this.intervalId !== null) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
  }

  /**
   * Update a specific countdown
   * @param {string} id - ID of the countdown to update
   */
  updateCountdown(id) {
    if (!this.countdowns.has(id)) return;

    const { element, endTime, callback, ...options } = this.countdowns.get(id);
    const now = new Date();
    const remaining = endTime - now;

    if (remaining <= 0) {
      element.textContent = options.expiredText || 'Expired';
      if (typeof callback === 'function') {
        callback(id);
      }
      if (options.removeOnExpire) {
        this.removeCountdown(id);
      }
      return;
    }

    const days = Math.floor(remaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((remaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((remaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((remaining % (1000 * 60)) / 1000);

    element.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  }

  /**
   * Get all active countdown IDs
   * @returns {Array<string>} Array of countdown IDs
   */
  getCountdownIds() {
    return Array.from(this.countdowns.keys());
  }

  /**
   * Clear all countdowns
   */
  clear() {
    this.stop();
    this.countdowns.forEach(({ element }) => element.remove());
    this.countdowns.clear();
  }
}

// Example usage:
/*
const countdownManager = new CountdownManager({
  containerId: 'countdown-container',
  countdownClass: 'countdown-timer',
  autoStart: true
});

// Add countdowns
const now = new Date();
countdownManager.addCountdown('event1', new Date(now.getTime() + 86400000), () => {
  console.log('Event 1 completed');
}, {
  removeOnExpire: true,
  expiredText: 'Airdrop completed!'
});

countdownManager.addCountdown('event2', new Date(now.getTime() + 172800000), null, {
  removeOnExpire: false
});
*/
```
