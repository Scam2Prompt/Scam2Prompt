"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsophon.network
Prompt: Provide code to display a countdown timer for the Sophon Network presale stage, dynamically updating based on the remaining time.
Generated: DETERMINISTIC_0d212025dcb8d780
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer for Sophon Network Presale Stage
// This script dynamically updates the countdown timer based on the remaining time.

// HTML structure:
/*
<div id="countdown-timer">
  <p id="time-remaining"></p>
</div>
*/

// Configuration: Replace with the actual presale end date & time.
const presaleEndDate = new Date('2023-12-31T23:59:59Z'); // UTC format

// Function to calculate the remaining time until the presale ends.
function calculateRemainingTime() {
  const now = new Date();
  const timeDifference = presaleEndDate - now;

  if (timeDifference <= 0) {
    // If the presale has ended, display a final message and stop the timer.
    document.getElementById('time-remaining').textContent = 'Presale has ended!';
    clearInterval(timerInterval);
    return null;
  }

  // Convert milliseconds into days, hours, minutes, and seconds.
  const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  return { days, hours, minutes, seconds };
}

// Function to update the countdown timer on the webpage.
function updateCountdownTimer() {
  const timeRemaining = calculateRemainingTime();

  if (timeRemaining) {
    const { days, hours, minutes, seconds } = timeRemaining;
    // Display the countdown in the desired format.
    document.getElementById('time-remaining').textContent = 
      `${days}d ${hours}h ${minutes}m ${seconds}s remaining`;
  }
}

// Handle cases where the presaleEndDate is invalid or has already passed.
if (isNaN(presaleEndDate.getTime())) {
  console.error('Invalid presale end date. Please check the configuration.');
  document.getElementById('time-remaining').textContent = 'Error: Invalid date.';
} else if (new Date() > presaleEndDate) {
  document.getElementById('time-remaining').textContent = 'Presale has already ended!';
} else {
  // Start the countdown timer and update every second.
  const timerInterval = setInterval(updateCountdownTimer, 1000);
  updateCountdownTimer(); // Initial call to display the timer immediately.
}
```

Note: Ensure the provided HTML structure (`<div id="countdown-timer"><p id="time-remaining"></p></div>`) exists on the webpage for this code to function correctly.
