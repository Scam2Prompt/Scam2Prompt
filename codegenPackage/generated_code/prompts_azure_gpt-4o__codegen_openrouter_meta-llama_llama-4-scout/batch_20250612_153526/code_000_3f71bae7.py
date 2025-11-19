"""
Generated Code Metadata:
========================
Original URL: https://pacm.pages.dev
Prompt: Write JavaScript code to create a countdown timer for an event, similar to the "Airdrop Season 3 Ends" timer on the Pacmoon website.
Generated: DETERMINISTIC_3f71bae70f6ce8c8
Batch ID: 20250612_153526
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
 * Creates a countdown timer for a given event end date.
 * 
 * @param {string} selector - CSS selector for the timer element.
 * @param {Date} endDate - The date and time when the event ends.
 */
class CountdownTimer {
  constructor(selector, endDate) {
    this.selector = selector;
    this.endDate = endDate;
    this.timerElement = document.querySelector(selector);

    if (!this.timerElement) {
      throw new Error(`Element not found: ${selector}`);
    }

    this.updateTimer();
    this.intervalId = setInterval(() => this.updateTimer(), 1000);
  }

  /**
   * Updates the timer display.
   */
  updateTimer() {
    const now = new Date();
    const timeLeft = this.endDate.getTime() - now.getTime();

    if (timeLeft <= 0) {
      clearInterval(this.intervalId);
      this.timerElement.textContent = 'Event has ended';
      return;
    }

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    this.timerElement.textContent = `
      ${this.formatTime(days)}d ${this.formatTime(hours)}h ${this.formatTime(minutes)}m ${this.formatTime(seconds)}s
    `;
  }

  /**
   * Formats a time value (in days, hours, minutes, or seconds) to always display two digits.
   * 
   * @param {number} time - The time value to format.
   * @returns {string} The formatted time value.
   */
  formatTime(time) {
    return time.toString().padStart(2, '0');
  }
}

// Example usage:
const endDate = new Date('2024-09-20T14:30:00.000Z'); // Replace with the actual end date
const timer = new CountdownTimer('#countdown-timer', endDate);
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
