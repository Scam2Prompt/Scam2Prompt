"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betty-moore-873.pages.dev
Prompt: How can I implement a countdown timer in JavaScript for a limited-time offer on a webpage?
Generated: DETERMINISTIC_c07f5bd31abea236
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for a limited-time offer
 * This script dynamically updates a countdown timer for a webpage.
 * The timer ends at a specified date and time.
 */

/**
 * Function to start the countdown timer.
 * @param {string} endTime - The deadline for the countdown in ISO format (e.g., '2023-12-31T23:59:59').
 * @param {string} elementId - The ID of the HTML element where the timer will be displayed.
 */
function startCountdown(endTime, elementId) {
  const countdownElement = document.getElementById(elementId);

  if (!countdownElement) {
    console.error(`Element with ID '${elementId}' not found.`);
    return;
  }

  // Convert the deadline time to a Date object
  const deadline = new Date(endTime);

  if (isNaN(deadline.getTime())) {
    console.error(`Invalid endTime format: '${endTime}'. Provide a valid ISO date string.`);
    return;
  }

  /**
   * Updates the timer every second.
   */
  function updateTimer() {
    const currentTime = new Date();
    const timeRemaining = deadline - currentTime;

    if (timeRemaining <= 0) {
      countdownElement.textContent = "Offer expired!";
      clearInterval(timerInterval); // Stop the timer
      return;
    }

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    // Update the HTML element with the formatted time
    countdownElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  }

  // Start the timer
  updateTimer(); // Initial call to display the timer immediately
  const timerInterval = setInterval(updateTimer, 1000);
}

// Example usage:
// HTML: <div id="offer-timer"></div>
// JavaScript:
startCountdown('2023-12-31T23:59:59', 'offer-timer');
```
