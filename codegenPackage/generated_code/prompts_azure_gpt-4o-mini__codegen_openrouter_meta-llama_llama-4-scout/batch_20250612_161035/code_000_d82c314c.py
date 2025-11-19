"""
Generated Code Metadata:
========================
Original URL: https://prom-app.vercel.app
Prompt: Generate a code snippet for a countdown timer that displays the time remaining until an event, similar to the countdown on Gabe and Adnan's Prom webpage.
Generated: DETERMINISTIC_d82c314cccdfbb85
Batch ID: 20250612_161035
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
   * @param {string} targetDate - The target date and time for the countdown in ISO format (YYYY-MM-DDTHH:MM:SS).
   * @param {string} displayElementId - The ID of the HTML element to display the countdown in.
   */
  constructor(targetDate, displayElementId) {
    this.targetDate = new Date(targetDate);
    this.displayElement = document.getElementById(displayElementId);

    if (!this.displayElement) {
      throw new Error(`Element with ID ${displayElementId} not found.`);
    }

    this.updateCountdown();
    this.intervalId = setInterval(() => this.updateCountdown(), 1000);
  }

  /**
   * Updates the countdown display.
   */
  updateCountdown() {
    const now = new Date();
    const timeRemaining = this.targetDate.getTime() - now.getTime();

    if (timeRemaining <= 0) {
      clearInterval(this.intervalId);
      this.displayElement.textContent = 'Event has started!';
      return;
    }

    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    this.displayElement.textContent = `
      ${this.pad(days)} days, ${this.pad(hours)} hours, ${this.pad(minutes)} minutes, ${this.pad(seconds)} seconds
    `;
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

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
  try {
    const targetDate = '2024-09-20T14:30:00'; // Replace with your target date and time.
    const displayElementId = 'countdown-timer'; // Replace with your display element ID.

    new CountdownTimer(targetDate, displayElementId);
  } catch (error) {
    console.error('Error initializing countdown timer:', error);
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
