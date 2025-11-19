"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donna-lopez-376.pages.dev
Prompt: Write a JavaScript function that displays a countdown timer for a limited-time offer on a webpage.
Generated: DETERMINISTIC_8feebf393933e4e7
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
 * Displays a countdown timer for a limited-time offer on a webpage.
 * @param {string} elementId - The ID of the HTML element where the timer will be displayed.
 * @param {Date} endTime - The end time for the countdown (as a Date object).
 */
function displayCountdownTimer(elementId, endTime) {
  // Ensure the provided endTime is a valid Date object
  if (!(endTime instanceof Date) || isNaN(endTime)) {
    throw new Error("Invalid endTime provided. Please provide a valid Date object.");
  }

  // Select the target HTML element by its ID
  const timerElement = document.getElementById(elementId);
  if (!timerElement) {
    throw new Error(`Element with ID "${elementId}" not found.`);
  }

  /**
   * Updates the timer display every second.
   */
  function updateTimer() {
    const currentTime = new Date();
    const timeRemaining = endTime - currentTime;

    if (timeRemaining <= 0) {
      // If the countdown is over, display "Offer Expired" and stop updating the timer
      timerElement.textContent = "Offer Expired";
      clearInterval(timerInterval);
      return;
    }

    // Calculate remaining time components
    const seconds = Math.floor((timeRemaining / 1000) % 60);
    const minutes = Math.floor((timeRemaining / 1000 / 60) % 60);
    const hours = Math.floor((timeRemaining / 1000 / 60 / 60) % 24);
    const days = Math.floor(timeRemaining / 1000 / 60 / 60 / 24);

    // Format the remaining time and update the timer element
    timerElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  }

  // Start the timer and update every second
  updateTimer(); // Initial call to display immediately
  const timerInterval = setInterval(updateTimer, 1000);
}

// Example usage:
// HTML: <div id="countdown"></div>
// JavaScript:
const offerEndTime = new Date("2023-10-31T23:59:59"); // Replace with your desired end time
displayCountdownTimer("countdown", offerEndTime);
```
ML element with ID 'countdown' exists
const offerEndTime = new Date("2023-12-31T23:59:59"); // Replace with your desired end time
displayCountdownTimer("countdown", offerEndTime);
```
