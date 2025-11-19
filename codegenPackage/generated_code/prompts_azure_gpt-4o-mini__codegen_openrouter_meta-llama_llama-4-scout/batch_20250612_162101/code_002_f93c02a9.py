"""
Generated Code Metadata:
========================
Original URL: https://dacarlaw.com
Prompt: Write a code snippet to implement a countdown timer that displays expired days, hours, minutes, and seconds on a webpage.
Generated: DETERMINISTIC_f93c02a962a2a2b2
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// countdown-timer.js

class CountdownTimer {
  /**
   * Creates a new CountdownTimer instance.
   * 
   * @param {string} deadline - The deadline date in 'YYYY-MM-DD HH:mm:ss' format.
   * @param {string} displayElementId - The ID of the HTML element to display the countdown.
   */
  constructor(deadline, displayElementId) {
    this.deadline = new Date(deadline).getTime();
    this.displayElement = document.getElementById(displayElementId);
    if (!this.displayElement) {
      throw new Error(`Element with ID '${displayElementId}' not found.`);
    }
  }

  /**
   * Starts the countdown timer.
   */
  start() {
    this.updateCountdown();
    setInterval(() => this.updateCountdown(), 1000);
  }

  /**
   * Updates the countdown display.
   */
  updateCountdown() {
    const now = new Date().getTime();
    const distance = this.deadline - now;

    if (distance < 0) {
      // Countdown has expired, display 'Expired'
      this.displayElement.textContent = 'Expired';
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    const formattedCountdown = `${this.pad(days)}d ${this.pad(hours)}h ${this.pad(minutes)}m ${this.pad(seconds)}s`;
    this.displayElement.textContent = formattedCountdown;
  }

  /**
   * Pads a number with a leading zero if it's less than 10.
   * 
   * @param {number} number - The number to pad.
   * @returns {string} The padded number.
   */
  pad(number) {
    return (number < 10 ? '0' : '') + number;
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  try {
    const timer = new CountdownTimer('2024-12-31 23:59:59', 'countdown-display');
    timer.start();
  } catch (error) {
    console.error('Error starting countdown timer:', error);
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
    #countdown-display {
      font-size: 24px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div id="countdown-display"></div>
  <script src="countdown-timer.js"></script>
</body>
</html>
```
