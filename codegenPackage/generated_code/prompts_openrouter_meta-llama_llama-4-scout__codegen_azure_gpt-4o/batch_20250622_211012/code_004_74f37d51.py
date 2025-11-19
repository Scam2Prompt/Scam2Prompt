"""
Generated Code Metadata:
========================
Original URL: https://allianceblock-reward.pages.dev
Prompt: Create a JavaScript code snippet to display a countdown timer for the round closing time, similar to "In 0 Hours 0 Minutes and 0 Seconds" shown on the webpage.
Generated: DETERMINISTIC_74f37d51203762f1
Batch ID: 20250622_211012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Countdown Timer Script
// This script displays a countdown timer in the format "In X Hours Y Minutes and Z Seconds"
// and updates it every second on the webpage.

// Function to start the countdown timer
function startCountdown(targetTime, displayElementId) {
    // Ensure the target time is a valid Date object
    if (!(targetTime instanceof Date)) {
        console.error("Invalid target time. Please provide a valid Date object.");
        return;
    }

    // Get the display element by its ID
    const displayElement = document.getElementById(displayElementId);
    if (!displayElement) {
        console.error(`Element with ID "${displayElementId}" not found.`);
        return;
    }

    // Function to update the countdown timer
    function updateTimer() {
        const now = new Date(); // Current time
        const timeDifference = targetTime - now; // Time difference in milliseconds

        if (timeDifference <= 0) {
            // If the countdown is over, display "Time's up!" and stop the timer
            displayElement.textContent = "Time's up!";
            clearInterval(timerInterval);
            return;
        }

        // Calculate hours, minutes, and seconds remaining
        const hours = Math.floor(timeDifference / (1000 * 60 * 60));
        const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

        // Update the display element with the countdown text
        displayElement.textContent = `In ${hours} Hours ${minutes} Minutes and ${seconds} Seconds`;
    }

    // Update the timer immediately and then every second
    updateTimer();
    const timerInterval = setInterval(updateTimer, 1000);
}

// Example usage:
// Set the target time (e.g., 1 hour from now)
const targetTime = new Date();
targetTime.setHours(targetTime.getHours() + 1);

// Call the startCountdown function with the target time and the ID of the display element
document.addEventListener("DOMContentLoaded", () => {
    startCountdown(targetTime, "countdown-display");
});
```

```html
<!-- Example HTML to display the countdown timer -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
</head>
<body>
    <div id="countdown-display">Loading...</div>
    <script src="countdown-timer.js"></script>
</body>
</html>
```
