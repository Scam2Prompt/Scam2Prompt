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
 * Event Countdown Timer Class
 */
class EventCountdownTimer {
  /**
   * Constructor for EventCountdownTimer
   * @param {Object} events - Object containing event names and their end timestamps
   * @param {Function} callback - Callback function to execute when an event countdown ends
   */
  constructor(events, callback) {
    this.events = events;
    this.callback = callback;
    this.countdowns = {};

    // Initialize countdowns
    Object.keys(events).forEach((eventName) => {
      this.countdowns[eventName] = this.getCountdownInterval(eventName);
    });
  }

  /**
   * Get the countdown interval for a specific event
   * @param {String} eventName - Name of the event
   * @returns {Number} Interval ID
   */
  getCountdownInterval(eventName) {
    const endTime = this.events[eventName];
    const intervalId = setInterval(() => {
      const timeLeft = this.getTimeLeft(endTime);
      if (timeLeft <= 0) {
        clearInterval(intervalId);
        this.callback(eventName);
      } else {
        this.displayCountdown(eventName, timeLeft);
      }
    }, 1000); // Update every second
    return intervalId;
  }

  /**
   * Get the time left until a specific timestamp
   * @param {Number} endTime - End timestamp
   * @returns {Number} Time left in seconds
   */
  getTimeLeft(endTime) {
    const now = Math.floor(Date.now() / 1000);
    return endTime - now;
  }

  /**
   * Display the countdown for a specific event
   * @param {String} eventName - Name of the event
   * @param {Number} timeLeft - Time left in seconds
   */
  displayCountdown(eventName, timeLeft) {
    const days = Math.floor(timeLeft / (60 * 60 * 24));
    const hours = Math.floor((timeLeft % (60 * 60 * 24)) / (60 * 60));
    const minutes = Math.floor((timeLeft % (60 * 60)) / 60);
    const seconds = timeLeft % 60;

    console.log(`Event: ${eventName} - ${days}d ${hours}h ${minutes}m ${seconds}s`);
    // You can replace this with your own display logic (e.g., update HTML element)
  }

  /**
   * Stop a specific event countdown
   * @param {String} eventName - Name of the event
   */
  stopCountdown(eventName) {
    clearInterval(this.countdowns[eventName]);
  }
}

// Example usage:
const events = {
  pacmoonAirdrop: Math.floor(Date.now() / 1000) + 60 * 60 * 24, // 1 day from now
  anotherEvent: Math.floor(Date.now() / 1000) + 30 * 60, // 30 minutes from now
};

const callback = (eventName) => {
  console.log(`Event ${eventName} has ended!`);
};

const timer = new EventCountdownTimer(events, callback);
```
