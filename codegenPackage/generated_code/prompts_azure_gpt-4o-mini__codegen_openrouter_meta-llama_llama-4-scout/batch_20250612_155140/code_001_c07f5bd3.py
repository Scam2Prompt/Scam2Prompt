"""
Generated Code Metadata:
========================
Original URL: https://betty-moore-873.pages.dev
Prompt: How can I implement a countdown timer in JavaScript for a limited-time offer on a webpage?
Generated: DETERMINISTIC_c07f5bd31abea236
Batch ID: 20250612_155140
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
 * CountdownTimer class to handle limited-time offers on a webpage.
 */
class CountdownTimer {
  /**
   * Constructor to initialize the countdown timer.
   * @param {Element} element - The HTML element to display the countdown timer.
   * @param {number} seconds - The number of seconds for the countdown timer.
   */
  constructor(element, seconds) {
    this.element = element;
    this.seconds = seconds;
    this.intervalId = null;

    // Validate input parameters
    if (!(element instanceof HTMLElement)) {
      throw new Error('Invalid HTML element');
    }
    if (typeof seconds !== 'number' || seconds <= 0) {
      throw new Error('Invalid number of seconds');
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
    const formattedTime = `${this.padZero(minutes)}:${this.padZero(seconds)}`;

    this.element.textContent = formattedTime;

    if (this.seconds > 0) {
      this.seconds -= 1;
    } else {
      this.stop();
      this.element.textContent = 'Time\'s up!';
    }
  }

  /**
   * Pads a number with a leading zero if necessary.
   * @param {number} number - The number to pad.
   * @returns {string} The padded number.
   */
  padZero(number) {
    return (number < 10 ? '0' : '') + number;
  }
}

// Example usage:
const timerElement = document.getElementById('countdown-timer');
const countdownTimer = new CountdownTimer(timerElement, 60); // 1-minute countdown
countdownTimer.start();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Limited-Time Offer</title>
  <style>
    #countdown-timer {
      font-size: 24px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Limited-Time Offer</h1>
  <p id="countdown-timer"></p>

  <script src="CountdownTimer.js"></script>
</body>
</html>
```
