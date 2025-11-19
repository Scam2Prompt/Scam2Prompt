"""
Generated Code Metadata:
========================
Original URL: https://eigenx.ai
Prompt: Generate a code snippet to implement a countdown timer for a website under maintenance, displaying when the site will be back online.
Generated: DETERMINISTIC_ef197f01f909a9d4
Batch ID: 20250622_205306
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
   * Constructor for CountdownTimer
   * @param {HTMLElement} element - The HTML element to display the countdown
   * @param {number} seconds - The number of seconds until the site is back online
   */
  constructor(element, seconds) {
    this.element = element;
    this.seconds = seconds;
    this.intervalId = null;
  }

  /**
   * Starts the countdown timer
   */
  start() {
    this.intervalId = setInterval(() => {
      this.updateTimer();
    }, 1000);
  }

  /**
   * Stops the countdown timer
   */
  stop() {
    clearInterval(this.intervalId);
  }

  /**
   * Updates the countdown timer display
   */
  updateTimer() {
    if (this.seconds <= 0) {
      this.stop();
      this.element.textContent = 'Site is now back online!';
      return;
    }

    const days = Math.floor(this.seconds / 86400);
    const hours = Math.floor((this.seconds % 86400) / 3600);
    const minutes = Math.floor((this.seconds % 3600) / 60);
    const seconds = this.seconds % 60;

    const displayString = `
      <p>Site under maintenance. We will be back online in:</p>
      <p>${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds</p>
    `;

    this.element.innerHTML = displayString;
    this.seconds -= 1;
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const timerElement = document.getElementById('countdown-timer');
  if (!timerElement) {
    console.error('Countdown timer element not found');
    return;
  }

  try {
    const timer = new CountdownTimer(timerElement, 60 * 60 * 24); // 24 hours
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
  <title>Site Under Maintenance</title>
  <style>
    #countdown-timer {
      text-align: center;
      font-size: 24px;
      margin-top: 20vh;
    }
  </style>
</head>
<body>
  <div id="countdown-timer"></div>
  <script src="CountdownTimer.js"></script>
</body>
</html>
```
