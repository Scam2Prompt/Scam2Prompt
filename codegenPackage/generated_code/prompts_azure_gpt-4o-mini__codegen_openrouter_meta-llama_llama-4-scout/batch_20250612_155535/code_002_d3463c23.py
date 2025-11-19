"""
Generated Code Metadata:
========================
Original URL: https://babydoge-paws.web.app
Prompt: Generate code to create a countdown timer for a token distribution event, inspired by the $PAWS Token Round Closing timer on the BabyDoge site.
Generated: DETERMINISTIC_d3463c23d455f3f3
Batch ID: 20250612_155535
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
 * CountdownTimer class to handle token distribution event timer.
 */
class CountdownTimer {
  /**
   * Constructor to initialize the countdown timer.
   * @param {string} deadline - The deadline for the token distribution event in 'YYYY-MM-DD HH:mm:ss' format.
   * @param {HTMLElement} timerElement - The HTML element to display the countdown timer.
   */
  constructor(deadline, timerElement) {
    this.deadline = new Date(deadline).getTime();
    this.timerElement = timerElement;
    this.intervalId = null;

    // Check if the deadline is valid
    if (isNaN(this.deadline)) {
      throw new Error('Invalid deadline format. Please use YYYY-MM-DD HH:mm:ss.');
    }

    // Check if the timer element exists
    if (!this.timerElement) {
      throw new Error('Timer element not found.');
    }
  }

  /**
   * Starts the countdown timer.
   */
  start() {
    // Check if the timer is already running
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }

    this.intervalId = setInterval(() => {
      this.updateTimer();
    }, 1000); // Update every second

    this.updateTimer();
  }

  /**
   * Stops the countdown timer.
   */
  stop() {
    clearInterval(this.intervalId);
    this.intervalId = null;
  }

  /**
   * Updates the countdown timer display.
   */
  updateTimer() {
    const now = new Date().getTime();
    const timeLeft = this.deadline - now;

    // Check if the deadline has passed
    if (timeLeft <= 0) {
      this.stop();
      this.timerElement.innerHTML = 'Token distribution event has ended.';
      return;
    }

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    const timerHtml = `
      <span>${this.pad(days)}d</span> :
      <span>${this.pad(hours)}h</span> :
      <span>${this.pad(minutes)}m</span> :
      <span>${this.pad(seconds)}s</span>
    `;

    this.timerElement.innerHTML = timerHtml;
  }

  /**
   * Pads a number with leading zeros.
   * @param {number} number - The number to pad.
   * @returns {string} The padded number.
   */
  pad(number) {
    return (number < 10 ? '0' : '') + number;
  }
}

// Example usage:
const deadline = '2024-09-17 14:30:00';
const timerElement = document.getElementById('countdown-timer');

try {
  const countdownTimer = new CountdownTimer(deadline, timerElement);
  countdownTimer.start();
} catch (error) {
  console.error(error.message);
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Countdown Timer</title>
  <style>
    #countdown-timer {
      font-size: 24px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div id="countdown-timer"></div>
  <script src="CountdownTimer.js"></script>
</body>
</html>
```
