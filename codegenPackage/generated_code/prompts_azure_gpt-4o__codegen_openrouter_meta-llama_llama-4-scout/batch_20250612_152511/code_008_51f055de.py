"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Generate code for a countdown timer feature to display limited-time offers on an e-commerce site, similar to the "0 روز 00 ساعت 00 دقیقه 00 ثانیه" timer shown on "ای ار گیفت."
Generated: DETERMINISTIC_51f055de65e0b2be
Batch ID: 20250612_152511
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
   * @param {Element} element - The HTML element to display the timer in.
   * @param {number} deadline - The deadline timestamp in seconds.
   */
  constructor(element, deadline) {
    this.element = element;
    this.deadline = deadline;
    this.intervalId = null;

    // Validate inputs
    if (!(element instanceof HTMLElement)) {
      throw new Error('Invalid element provided');
    }
    if (typeof deadline !== 'number' || deadline <= 0) {
      throw new Error('Invalid deadline provided');
    }
  }

  /**
   * Starts the countdown timer.
   */
  start() {
    this.intervalId = setInterval(() => this.updateTimer(), 1000);
    this.updateTimer();
  }

  /**
   * Stops the countdown timer.
   */
  stop() {
    clearInterval(this.intervalId);
  }

  /**
   * Updates the timer display.
   */
  updateTimer() {
    const now = Math.floor(Date.now() / 1000);
    const timeLeft = this.deadline - now;

    if (timeLeft <= 0) {
      this.stop();
      this.displayTime(0, 0, 0, 0);
      return;
    }

    const days = Math.floor(timeLeft / 86400);
    const hours = Math.floor((timeLeft % 86400) / 3600);
    const minutes = Math.floor((timeLeft % 3600) / 60);
    const seconds = timeLeft % 60;

    this.displayTime(days, hours, minutes, seconds);
  }

  /**
   * Displays the time in the format: "X روزY ساعتZ دقیقهW ثانیه".
   * 
   * @param {number} days - The number of days.
   * @param {number} hours - The number of hours.
   * @param {number} minutes - The number of minutes.
   * @param {number} seconds - The number of seconds.
   */
  displayTime(days, hours, minutes, seconds) {
    const formattedTime = `${this.pad(days)} روز${this.pad(hours)} ساعت${this.pad(minutes)} دقیقه${this.pad(seconds)} ثانیه`;
    this.element.textContent = formattedTime;
  }

  /**
   * Pads a number with a leading zero if it's less than 10.
   * 
   * @param {number} num - The number to pad.
   * @returns {string} The padded number.
   */
  pad(num) {
    return (num < 10 ? '0' : '') + num;
  }
}

// Example usage:
const timerElement = document.getElementById('timer');
const deadline = Math.floor(Date.now() / 1000) + 86400; // 1 day from now

const timer = new CountdownTimer(timerElement, deadline);
timer.start();
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
      font-size: 24px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <p id="timer"></p>
  <script src="CountdownTimer.js"></script>
</body>
</html>
```
