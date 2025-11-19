"""
Generated Code Metadata:
========================
Original URL: https://dacarlaw.com
Prompt: Generate a countdown timer using JavaScript that can be integrated into a website template.
Generated: DETERMINISTIC_955a0d6c083f16f0
Batch ID: 20250612_162101
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
 * Countdown Timer class.
 */
class CountdownTimer {
  /**
   * Constructor for CountdownTimer.
   * @param {HTMLElement} element - The HTML element to display the timer in.
   * @param {number} seconds - The number of seconds to count down from.
   */
  constructor(element, seconds) {
    this.element = element;
    this.seconds = seconds;
    this.intervalId = null;

    // Check if element and seconds are valid
    if (!element || typeof seconds !== 'number' || seconds < 0) {
      throw new Error('Invalid input');
    }
  }

  /**
   * Starts the countdown timer.
   */
  start() {
    // Check if timer is already running
    if (this.intervalId !== null) {
      throw new Error('Timer is already running');
    }

    this.intervalId = setInterval(() => {
      this.updateTimer();
    }, 1000); // Update every second
  }

  /**
   * Stops the countdown timer.
   */
  stop() {
    // Check if timer is running
    if (this.intervalId === null) {
      throw new Error('Timer is not running');
    }

    clearInterval(this.intervalId);
    this.intervalId = null;
  }

  /**
   * Updates the timer display.
   */
  updateTimer() {
    // Calculate remaining time
    const remainingTime = this.seconds--;

    // Check if time is up
    if (remainingTime < 0) {
      this.stop();
      this.element.textContent = 'Time\'s up!';
      return;
    }

    // Format time
    const minutes = Math.floor(remainingTime / 60);
    const seconds = remainingTime % 60;
    const formattedTime = `${this.padZero(minutes)}:${this.padZero(seconds)}`;

    // Update display
    this.element.textContent = formattedTime;
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

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const timerElement = document.getElementById('timer');
  const timer = new CountdownTimer(timerElement, 60); // 1 minute

  try {
    timer.start();
  } catch (error) {
    console.error(error);
  }
});
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
    #timer {
      font-size: 48px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Countdown Timer</h1>
  <p id="timer"></p>

  <script src="CountdownTimer.js"></script>
</body>
</html>
```
