"""
Generated Code Metadata:
========================
Original URL: https://avabase.vercel.app
Prompt: Generate code to create a countdown timer for a crypto campaign, showing days, hours, minutes, and seconds remaining, similar to the AVAAI Hunt timer.
Generated: DETERMINISTIC_0bb731cbe640e1c6
Batch ID: 20250612_153925
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
   * @param {Date} endDate The date and time at which the countdown ends.
   * @param {HTMLElement} displayElement The HTML element to display the countdown in.
   */
  constructor(endDate, displayElement) {
    this.endDate = endDate;
    this.displayElement = displayElement;
    this.intervalId = null;

    // Validate input parameters
    if (!(endDate instanceof Date) || isNaN(endDate.getTime())) {
      throw new Error('Invalid end date');
    }
    if (!(displayElement instanceof HTMLElement)) {
      throw new Error('Invalid display element');
    }
  }

  /**
   * Starts the countdown timer.
   */
  start() {
    // Update the display immediately
    this.updateDisplay();

    // Calculate the time remaining and update the display every second
    this.intervalId = setInterval(() => {
      this.updateDisplay();
    }, 1000);
  }

  /**
   * Stops the countdown timer.
   */
  stop() {
    clearInterval(this.intervalId);
  }

  /**
   * Updates the countdown display.
   */
  updateDisplay() {
    const now = new Date();
    const timeRemaining = this.calculateTimeRemaining(now);

    if (timeRemaining <= 0) {
      // Countdown has ended, stop the timer and display a message
      this.stop();
      this.displayElement.textContent = 'Countdown ended!';
      return;
    }

    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    this.displayElement.textContent = `
      ${this.padZero(days)}d ${this.padZero(hours)}h ${this.padZero(minutes)}m ${this.padZero(seconds)}s
    `;
  }

  /**
   * Calculates the time remaining until the end date.
   * 
   * @param {Date} now The current date and time.
   * @returns {number} The time remaining in milliseconds.
   */
  calculateTimeRemaining(now) {
    return this.endDate.getTime() - now.getTime();
  }

  /**
   * Pads a number with a leading zero if it's less than 10.
   * 
   * @param {number} number The number to pad.
   * @returns {string} The padded number.
   */
  padZero(number) {
    return (number < 10 ? '0' : '') + number;
  }
}

// Example usage
const endDate = new Date('2024-09-17T14:30:00.000Z'); // Replace with your end date
const displayElement = document.getElementById('countdown-timer'); // Replace with your display element

const countdownTimer = new CountdownTimer(endDate, displayElement);
countdownTimer.start();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Crypto Campaign Countdown Timer</title>
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
