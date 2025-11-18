"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-claim.pages.dev
Prompt: Create a function in JavaScript to display the countdown timer for the next price increase in the WienerAI presale, based on the provided time data.
Generated: DETERMINISTIC_89ca9f3e035c347f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display a countdown timer for the next price increase in the WienerAI presale.
 * @param {Date} targetTime - The target date and time for the price increase.
 */
function displayCountdownTimer(targetTime) {
  // Ensure the provided targetTime is a valid Date object
  if (!(targetTime instanceof Date) || isNaN(targetTime)) {
    throw new Error("Invalid targetTime: Please provide a valid Date object.");
  }

  // Get the HTML element where the timer will be displayed
  const timerElement = document.getElementById("countdown-timer");
  if (!timerElement) {
    throw new Error("Element with id 'countdown-timer' not found in the DOM.");
  }

  // Function to calculate and display the remaining time
  function updateTimer() {
    const now = new Date();
    const timeDifference = targetTime - now;

    // If the countdown is over, display a message and stop the timer
    if (timeDifference <= 0) {
      timerElement.textContent = "The price has increased!";
      clearInterval(timerInterval);
      return;
    }

    // Calculate days, hours, minutes, and seconds remaining
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    // Update the text content of the timerElement with the formatted countdown
    timerElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s until the next price increase`;
  }

  // Initialize the timer with the first update
  updateTimer();

  // Set up an interval to update the timer every second
  const timerInterval = setInterval(updateTimer, 1000);
}

// Example usage:
// Create a Date object for the target time (e.g., 2023-12-31 23:59:59)
const nextPriceIncreaseTime = new Date("2023-12-31T23:59:59");

// Call the function with the target time
displayCountdownTimer(nextPriceIncreaseTime);
```

**Note:** Ensure you have an HTML element with the ID `countdown-timer` in your document for this script to work. Example:
```html
<div id="countdown-timer"></div>
```
