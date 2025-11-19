"""
Generated Code Metadata:
========================
Original URL: https://taqibraz.blogspot.com
Prompt: Write a JavaScript code to create a countdown timer for a limited-time offer, like the TEMPO LIMITADO ⏰ deal on Lavadora de Alta Pressão Kärcher K4 Power on taQi.
Generated: DETERMINISTIC_abfa07b237ff97c2
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CountdownTimer.js

class CountdownTimer {
  /**
   * Creates a new CountdownTimer instance.
   * 
   * @param {HTMLElement} element - The HTML element to display the countdown timer.
   * @param {number} seconds - The number of seconds for the countdown timer.
   */
  constructor(element, seconds) {
    this.element = element;
    this.seconds = seconds;
    this.intervalId = null;

    // Validate input parameters
    if (!(element instanceof HTMLElement)) {
      throw new Error('Invalid element provided');
    }
    if (typeof seconds !== 'number' || seconds <= 0) {
      throw new Error('Invalid number of seconds provided');
    }
  }

  /**
   * Starts the countdown timer.
   */
  start() {
    this.updateTimer();
    this.intervalId = setInterval(() => this.updateTimer(), 1000);
  }

  /**
   * Stops the countdown timer.
   */
  stop() {
    clearInterval(this.intervalId);
  }

  /**
   * Updates the countdown timer display.
   */
  updateTimer() {
    const minutes = Math.floor(this.seconds / 60);
    const seconds = this.seconds % 60;

    // Format the timer display
    const timerDisplay = `TEMPO LIMITADO ⏰: ${this.padZero(minutes)}:${this.padZero(seconds)}`;

    // Update the HTML element
    this.element.textContent = timerDisplay;

    // Decrement the seconds
    this.seconds -= 1;

    // Check if the countdown timer has expired
    if (this.seconds < 0) {
      this.stop();
      this.element.textContent = 'TEMPO LIMITADO ⏰: EXCADU';
    }
  }

  /**
   * Pads a number with a leading zero if necessary.
   * 
   * @param {number} number - The number to pad.
   * @returns {string} The padded number.
   */
  padZero(number) {
    return (number < 10 ? '0' : '') + number;
  }
}

// Example usage
const timerElement = document.getElementById('countdown-timer');
const countdownTimer = new CountdownTimer(timerElement, 60); // 1 minute
countdownTimer.start();
```
