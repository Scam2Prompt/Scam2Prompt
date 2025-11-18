"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacm.pages.dev
Prompt: Write JavaScript code to create a countdown timer for an event, similar to the "Airdrop Season 3 Ends" timer on the Pacmoon website.
Generated: DETERMINISTIC_3f71bae70f6ce8c8
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer Script

// Function to calculate the remaining time until a target date
function calculateTimeLeft(targetDate) {
  const now = new Date(); // Get the current date and time
  const timeDifference = targetDate - now; // Difference in milliseconds

  if (timeDifference <= 0) {
    // Return zeros if the target date has passed
    return {
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 0
    };
  }

  // Convert milliseconds to days, hours, minutes, and seconds
  const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  return {
    days,
    hours,
    minutes,
    seconds
  };
}

// Function to update the countdown timer in the DOM
function updateCountdownTimer(targetDate, timerElementId) {
  const timeLeft = calculateTimeLeft(targetDate);

  // Update the timer element's text content
  const timerElement = document.getElementById(timerElementId);
  if (timerElement) {
    timerElement.textContent = `${timeLeft.days}d ${timeLeft.hours}h ${timeLeft.minutes}m ${timeLeft.seconds}s`;
  } else {
    console.error(`Element with ID '${timerElementId}' not found.`);
  }
}

// Initialize the countdown timer
function startCountdown(targetDateString, timerElementId) {
  // Parse the target date string into a Date object
  const targetDate = new Date(targetDateString);
  
  // Check if the date is valid
  if (isNaN(targetDate)) {
    console.error('Invalid target date format. Please use a valid date string.');
    return;
  }

  // Call updateCountdownTimer every second
  setInterval(() => updateCountdownTimer(targetDate, timerElementId), 1000);
}

// Example usage:
// 1. Add an HTML element with an ID to display the timer, e.g., <div id="countdown-timer"></div>
// 2. Set the target date in the format "YYYY-MM-DDTHH:MM:SS"
startCountdown('2023-11-01T00:00:00', 'countdown-timer');
```

Make sure you include an HTML element with the ID `countdown-timer` where you want the countdown to appear:
```html
<div id="countdown-timer"></div>
```
