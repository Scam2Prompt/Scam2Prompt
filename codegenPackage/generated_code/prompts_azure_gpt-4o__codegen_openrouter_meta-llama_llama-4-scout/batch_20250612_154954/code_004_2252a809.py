"""
Generated Code Metadata:
========================
Original URL: https://dacarlaw.com
Prompt: Write JavaScript code to create a responsive countdown timer for a website using the PopularFX theme, as seen on the Dacarlaw site.
Generated: DETERMINISTIC_2252a809ff7501ae
Batch ID: 20250612_154954
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
 * Creates a responsive countdown timer.
 * 
 * @class CountdownTimer
 * @param {HTMLElement} element - The HTML element to render the countdown timer in.
 * @param {number} deadline - The deadline timestamp in seconds.
 */
class CountdownTimer {
  constructor(element, deadline) {
    this.element = element;
    this.deadline = deadline;
    this.intervalId = null;

    // Initialize the timer
    this.init();
  }

  /**
   * Initializes the countdown timer.
   * 
   * @memberof CountdownTimer
   */
  init() {
    // Get the current timestamp
    const currentTime = Math.floor(Date.now() / 1000);

    // Calculate the time difference
    const timeDifference = this.deadline - currentTime;

    // Check if the deadline has passed
    if (timeDifference <= 0) {
      this.element.textContent = 'Time\'s up!';
      return;
    }

    // Render the initial timer
    this.render(timeDifference);

    // Start the interval
    this.intervalId = setInterval(() => {
      // Calculate the updated time difference
      const updatedTimeDifference = this.deadline - Math.floor(Date.now() / 1000);

      // Check if the deadline has passed
      if (updatedTimeDifference <= 0) {
        clearInterval(this.intervalId);
        this.element.textContent = 'Time\'s up!';
        return;
      }

      // Render the updated timer
      this.render(updatedTimeDifference);
    }, 1000);
  }

  /**
   * Renders the countdown timer.
   * 
   * @param {number} time - The time in seconds.
   * @memberof CountdownTimer
   */
  render(time) {
    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(time / 86400);
    const hours = Math.floor((time % 86400) / 3600);
    const minutes = Math.floor((time % 3600) / 60);
    const seconds = time % 60;

    // Format the timer
    const formattedTime = `
      <span class="countdown-days">${this.pad(days)}</span>:
      <span class="countdown-hours">${this.pad(hours)}</span>:
      <span class="countdown-minutes">${this.pad(minutes)}</span>:
      <span class="countdown-seconds">${this.pad(seconds)}</span>
    `;

    // Update the element
    this.element.innerHTML = formattedTime;
  }

  /**
   * Pads a number with leading zeros.
   * 
   * @param {number} number - The number to pad.
   * @returns {string} The padded number.
   * @memberof CountdownTimer
   */
  pad(number) {
    return (number < 10 ? '0' : '') + number;
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const deadline = Math.floor(Date.now() / 1000) + 30 * 24 * 60 * 60; // 30 days from now
  const countdownElement = document.getElementById('countdown-timer');
  const countdownTimer = new CountdownTimer(countdownElement, deadline);
});
```

```css
/* styles.css */

.countdown-days,
.countdown-hours,
.countdown-minutes,
.countdown-seconds {
  font-size: 24px;
  font-weight: bold;
  margin: 0 10px;
}

.countdown-days::after,
.countdown-hours::after,
.countdown-minutes::after {
  content: ':';
  margin: 0 5px;
}

@media only screen and (max-width: 768px) {
  .countdown-days,
  .countdown-hours,
  .countdown-minutes,
  .countdown-seconds {
    font-size: 18px;
  }
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
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="countdown-timer"></div>
  <script src="CountdownTimer.js"></script>
</body>
</html>
```
