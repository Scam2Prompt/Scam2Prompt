"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Generate a JavaScript function to display a countdown timer for the $WING presale price increase, as shown on the Dopawing website.
Generated: DETERMINISTIC_161f79bae0249444
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for $WING Presale Price Increase
 * Displays a countdown timer that updates every second.
 * @param {Date} endTime - The end time for the countdown (ISO string format or JavaScript Date object).
 * @param {string} elementId - The ID of the HTML element where the timer will be rendered.
 */
function displayCountdownTimer(endTime, elementId) {
  // Ensure endTime is a valid Date object
  const targetTime = new Date(endTime);
  if (isNaN(targetTime.getTime())) {
    console.error("Invalid date format for endTime. Please provide a valid ISO string or Date object.");
    return;
  }

  // Ensure the specified element exists in the DOM
  const timerElement = document.getElementById(elementId);
  if (!timerElement) {
    console.error(`Element with ID '${elementId}' not found in the DOM.`);
    return;
  }

  // Function to update the countdown
  function updateTimer() {
    const currentTime = new Date();
    const timeDifference = targetTime - currentTime;

    if (timeDifference <= 0) {
      // Countdown has ended
      timerElement.textContent = "Price has increased!";
      clearInterval(timerInterval);
      return;
    }

    // Calculate remaining time components
    const seconds = Math.floor((timeDifference / 1000) % 60);
    const minutes = Math.floor((timeDifference / (1000 * 60)) % 60);
    const hours = Math.floor((timeDifference / (1000 * 60 * 60)) % 24);
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));

    // Display formatted countdown
    timerElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  }

  // Start the countdown timer
  updateTimer(); // Initial display
  const timerInterval = setInterval(updateTimer, 1000);

  // Cleanup interval if the element is removed from the DOM
  timerElement.addEventListener("DOMNodeRemoved", () => {
    clearInterval(timerInterval);
  });
}

// Example usage:
// displayCountdownTimer("2023-10-31T23:59:59Z", "countdown-timer");
```

Ensure you have an HTML element with the corresponding `elementId` (e.g., `<div id="countdown-timer"></div>`) before calling the function.
