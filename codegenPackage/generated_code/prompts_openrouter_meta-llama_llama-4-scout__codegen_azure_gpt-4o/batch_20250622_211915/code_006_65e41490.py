"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Develop a JavaScript code snippet to implement a countdown timer for a VZ99 promotion, including features for displaying the remaining time and updating the UI in real-time.
Generated: DETERMINISTIC_65e41490cf0477fb
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer for VZ99 Promotion
 * This script creates a real-time countdown timer that updates the UI to display
 * the remaining time until the promotion ends.
 */

// Function to format time as HH:MM:SS
function formatTime(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  // Ensure double digits for hours, minutes, and seconds
  return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
}

// Countdown Timer Function
function startCountdown(endTime, displayElementId) {
  const displayElement = document.getElementById(displayElementId);

  if (!displayElement) {
    console.error(`Element with ID "${displayElementId}" not found.`);
    return;
  }

  // Update the timer every second
  const intervalId = setInterval(() => {
    const currentTime = new Date().getTime();
    const timeRemaining = Math.floor((endTime - currentTime) / 1000);

    if (timeRemaining <= 0) {
      clearInterval(intervalId);
      displayElement.textContent = "Promotion has ended!";
      return;
    }

    // Update the UI with the formatted time
    displayElement.textContent = formatTime(timeRemaining);
  }, 1000);
}

// Example Usage
document.addEventListener("DOMContentLoaded", () => {
  // Set the end time for the promotion (e.g., 1 hour from now)
  const promotionEndTime = new Date().getTime() + 3600 * 1000; // 1 hour in milliseconds

  // Start the countdown timer and update the UI element with ID "countdown-timer"
  startCountdown(promotionEndTime, "countdown-timer");
});
```

```html
<!-- Example HTML to display the countdown timer -->
<div id="countdown-timer">Loading...</div>
```
