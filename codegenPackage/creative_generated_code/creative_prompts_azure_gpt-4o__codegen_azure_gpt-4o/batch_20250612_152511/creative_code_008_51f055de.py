"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Generate code for a countdown timer feature to display limited-time offers on an e-commerce site, similar to the "0 روز 00 ساعت 00 دقیقه 00 ثانیه" timer shown on "ای ار گیفت."
Generated: DETERMINISTIC_51f055de65e0b2be
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Countdown Timer</title>
  <style>
    /* Basic styling for the countdown timer */
    .countdown {
      font-family: Arial, sans-serif;
      font-size: 20px;
      color: #333;
      display: flex;
      gap: 10px;
    }
    .countdown span {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="countdown">
    <span id="days">0</span> روز
    <span id="hours">00</span> ساعت
    <span id="minutes">00</span> دقیقه
    <span id="seconds">00</span> ثانیه
  </div>

  <script>
    /**
     * Countdown Timer Functionality
     * This script dynamically updates the countdown timer for limited-time offers.
     */
    (function () {
      // Set the target deadline (e.g., 3 days from now)
      const deadline = new Date();
      deadline.setDate(deadline.getDate() + 3); // Add 3 days

      // Get references to the timer elements
      const daysElement = document.getElementById('days');
      const hoursElement = document.getElementById('hours');
      const minutesElement = document.getElementById('minutes');
      const secondsElement = document.getElementById('seconds');

      /**
       * Updates the countdown timer values on the page.
       */
      function updateTimer() {
        const now = new Date();
        const timeRemaining = deadline - now;

        // If the countdown is finished, set all values to zero
        if (timeRemaining <= 0) {
          daysElement.textContent = 0;
          hoursElement.textContent = '00';
          minutesElement.textContent = '00';
          secondsElement.textContent = '00';
          clearInterval(timerInterval); // Stop updating once expired
          return;
        }

        // Calculate remaining time components
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Update the HTML elements
        daysElement.textContent = days;
        hoursElement.textContent = hours.toString().padStart(2, '0');
        minutesElement.textContent = minutes.toString().padStart(2, '0');
        secondsElement.textContent = seconds.toString().padStart(2, '0');
      }

      // Set an interval to update the timer every second
      const timerInterval = setInterval(updateTimer, 1000);

      // Initialize the timer display immediately
      updateTimer();
    })();
  </script>
</body>
</html>
```
