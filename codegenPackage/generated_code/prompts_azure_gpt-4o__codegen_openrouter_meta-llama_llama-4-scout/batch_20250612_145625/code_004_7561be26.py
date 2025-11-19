"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.web.app
Prompt: Write code in JavaScript to implement a countdown timer for a presale widget, similar to the one on the Popo website, displaying days, hours, minutes, and seconds until the token price increases.
Generated: DETERMINISTIC_7561be260309ff8e
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CountdownTimer.js

/**
 * CountdownTimer class for presale widget.
 * Displays days, hours, minutes, and seconds until the token price increases.
 */
class CountdownTimer {
  /**
   * Constructor for CountdownTimer.
   * @param {HTMLElement} container - The container element for the countdown timer.
   * @param {number} endTime - The end time in milliseconds.
   */
  constructor(container, endTime) {
    this.container = container;
    this.endTime = endTime;
    this.intervalId = null;

    // Initialize the timer display
    this.display = document.createElement('div');
    this.display.classList.add('countdown-timer');
    this.container.appendChild(this.display);

    // Start the countdown
    this.start();
  }

  /**
   * Starts the countdown timer.
   */
  start() {
    // Check if the end time has already passed
    if (this.endTime < Date.now()) {
      this.display.textContent = 'Presale has ended';
      return;
    }

    // Update the timer display immediately
    this.updateDisplay();

    // Start the interval
    this.intervalId = setInterval(() => {
      this.updateDisplay();
    }, 1000);
  }

  /**
   * Updates the countdown timer display.
   */
  updateDisplay() {
    const timeRemaining = this.endTime - Date.now();

    // Check if the countdown has reached zero
    if (timeRemaining <= 0) {
      clearInterval(this.intervalId);
      this.display.textContent = 'Presale has ended';
      return;
    }

    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    this.display.textContent = `
      <span class="countdown-days">${this.pad(days)}d</span>
      <span class="countdown-hours">${this.pad(hours)}h</span>
      <span class="countdown-minutes">${this.pad(minutes)}m</span>
      <span class="countdown-seconds">${this.pad(seconds)}s</span>
    `;
  }

  /**
   * Pads a number with a leading zero if necessary.
   * @param {number} num - The number to pad.
   * @returns {string} The padded number.
   */
  pad(num) {
    return num.toString().padStart(2, '0');
  }

  /**
   * Destroys the countdown timer.
   */
  destroy() {
    clearInterval(this.intervalId);
    this.container.removeChild(this.display);
  }
}

// Example usage
const container = document.getElementById('countdown-timer-container');
const endTime = new Date('2024-09-17T14:30:00.000Z').getTime();
const countdownTimer = new CountdownTimer(container, endTime);
```

```css
/* styles.css */

.countdown-timer {
  font-size: 24px;
  font-weight: bold;
}

.countdown-days,
.countdown-hours,
.countdown-minutes,
.countdown-seconds {
  display: inline-block;
  margin: 0 10px;
}

.countdown-days::after,
.countdown-hours::after,
.countdown-minutes::after,
.countdown-seconds::after {
  content: ':';
  margin: 0 5px;
}

.countdown-seconds::after {
  content: '';
}
```
