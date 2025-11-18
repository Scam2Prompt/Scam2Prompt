"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-aevo-97y.pages.dev
Prompt: Provide a code example for displaying a countdown timer (e.g., "END OF FARM BOOST 7D 8H 15M 45S") using JavaScript, as seen on the Aevo website.
Generated: DETERMINISTIC_99fa411fee057f24
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer
 * Displays a countdown timer in the format "END OF FARM BOOST 7D 8H 15M 45S".
 * This example assumes a target end time and updates the display dynamically.
 */

// Function to calculate and format the remaining time
function formatCountdown(targetDate) {
  const now = new Date();
  const timeDiff = targetDate - now;

  if (timeDiff <= 0) {
    // Return "Expired" when the countdown is over
    return "END OF FARM BOOST EXPIRED";
  }

  // Calculate days, hours, minutes, and seconds remaining
  const days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);

  // Return formatted string
  return `END OF FARM BOOST ${days}D ${hours}H ${minutes}M ${seconds}S`;
}

// Function to initialize and update the countdown timer
function startCountdown(targetDate, elementId) {
  const targetElement = document.getElementById(elementId);

  if (!targetElement) {
    console.error("Element with the provided ID not found.");
    return;
  }

  // Update the countdown every second
  const interval = setInterval(() => {
    const formattedTime = formatCountdown(targetDate);
    targetElement.textContent = formattedTime;

    // Stop the interval when the countdown ends
    if (formattedTime === "END OF FARM BOOST EXPIRED") {
      clearInterval(interval);
    }
  }, 1000);
}

// Example usage
// Set the target date (e.g., 7 days from now)
const targetDate = new Date();
targetDate.setDate(targetDate.getDate() + 7);

// Start the countdown and display it in an element with ID "countdown-timer"
startCountdown(targetDate, "countdown-timer");
```

```html
<!-- Example HTML for displaying the countdown -->
<div id="countdown-timer"></div>
```
