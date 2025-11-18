"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baamgift.info
Prompt: Generate code in JavaScript to display a countdown timer for gift card promotions, similar to the timer feature mentioned on https://baamgift.info.
Generated: DETERMINISTIC_50cb4a840177045e
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for Gift Card Promotions
 * 
 * This script creates a countdown timer that displays the remaining time for a promotion.
 * The timer updates dynamically and handles expiration gracefully.
 * 
 * Usage:
 * Place an HTML element with the ID "countdown-timer" where the timer should appear.
 */

document.addEventListener("DOMContentLoaded", () => {
  // Set the promotion's end time (example: December 31, 2023, 23:59:59)
  const promotionEndTime = new Date("2023-12-31T23:59:59");

  // Get the element where the timer will be displayed
  const timerElement = document.getElementById("countdown-timer");

  if (!timerElement) {
    console.error('Countdown timer element with ID "countdown-timer" not found.');
    return;
  }

  /**
   * Updates the timer display.
   * Calculates the remaining time and updates the DOM.
   * Stops the timer if the promotion has expired.
   */
  const updateTimer = () => {
    const now = new Date();
    const timeRemaining = promotionEndTime - now;

    if (timeRemaining <= 0) {
      // Promotion has expired
      timerElement.textContent = "Promotion has ended!";
      clearInterval(timerInterval);
      return;
    }

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    // Update the timer display
    timerElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  };

  // Initial update to display the timer immediately
  updateTimer();

  // Update the timer every second
  const timerInterval = setInterval(updateTimer, 1000);
});
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gift Card Promotion Countdown</title>
  <style>
    #countdown-timer {
      font-size: 1.5em;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Gift Card Promotion</h1>
  <p>Hurry up! Promotion ends in:</p>
  <div id="countdown-timer"></div>

  <script src="countdownTimer.js"></script>
</body>
</html>
```
