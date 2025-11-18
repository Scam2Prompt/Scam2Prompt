"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.web.app
Prompt: Write code in JavaScript to implement a countdown timer for a presale widget, similar to the one on the Popo website, displaying days, hours, minutes, and seconds until the token price increases.
Generated: DETERMINISTIC_7561be260309ff8e
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer for Presale Widget
// Author: [Your Name]
// Description: This script implements a countdown timer that displays days, hours, minutes,
// and seconds until the token price increases. The target date/time should be configured
// when initializing the widget.

// IIFE (Immediately Invoked Function Expression) to encapsulate the code
(() => {
  // Target date/time for the countdown (e.g., "2023-12-31T23:59:59Z")
  const targetDate = new Date('2023-12-31T23:59:59Z');

  // Ensure the target date is valid
  if (isNaN(targetDate.getTime())) {
    console.error('Invalid target date. Please provide a valid date.');
    return;
  }

  // DOM Elements for displaying the countdown
  const daysElement = document.getElementById('countdown-days');
  const hoursElement = document.getElementById('countdown-hours');
  const minutesElement = document.getElementById('countdown-minutes');
  const secondsElement = document.getElementById('countdown-seconds');

  // Ensure the elements exist in the DOM
  if (!daysElement || !hoursElement || !minutesElement || !secondsElement) {
    console.error('Countdown DOM elements not found. Ensure the correct IDs are used.');
    return;
  }

  // Function to calculate time remaining and update the timer
  function updateCountdown() {
    const now = new Date();
    const timeRemaining = targetDate - now;

    // If the countdown has ended
    if (timeRemaining <= 0) {
      clearInterval(timerInterval); // Stop the timer
      daysElement.textContent = '0';
      hoursElement.textContent = '00';
      minutesElement.textContent = '00';
      secondsElement.textContent = '00';
      console.log('Countdown ended.');
      return;
    }

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    // Update the DOM elements
    daysElement.textContent = days;
    hoursElement.textContent = hours.toString().padStart(2, '0'); // Add leading zero if needed
    minutesElement.textContent = minutes.toString().padStart(2, '0');
    secondsElement.textContent = seconds.toString().padStart(2, '0');
  }

  // Initialize the countdown immediately
  updateCountdown();

  // Update the countdown every second
  const timerInterval = setInterval(updateCountdown, 1000);
})();
```

**Usage Instructions:**

1. Add the following HTML structure to your webpage:
   ```html
   <div id="presale-countdown">
     <span id="countdown-days"></span> Days 
     <span id="countdown-hours"></span> Hours 
     <span id="countdown-minutes"></span> Minutes 
     <span id="countdown-seconds"></span> Seconds
   </div>
   ```

2. Include the above JavaScript code in your page, either inline or as an external file.
