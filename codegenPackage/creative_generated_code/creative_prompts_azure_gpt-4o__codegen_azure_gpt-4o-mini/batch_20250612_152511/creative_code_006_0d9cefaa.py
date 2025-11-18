"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-app.pages.dev
Prompt: Write JavaScript code to display a countdown timer for the next Everyworld drawing, dynamically updating based on the provided GMT+4 timestamp.
Generated: DETERMINISTIC_0d9cefaa5db36bf6
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for Everyworld Drawing
 * This script calculates the time remaining until the next Everyworld drawing 
 * based on a provided GMT+4 timestamp and updates the display every second.
 */

// Function to start the countdown timer
function startCountdown(targetTime) {
    // Validate the targetTime input
    if (isNaN(targetTime)) {
        console.error('Invalid timestamp provided. Please provide a valid GMT+4 timestamp.');
        return;
    }

    // Function to update the countdown display
    function updateCountdown() {
        const now = new Date().getTime(); // Current time in milliseconds
        const distance = targetTime - now; // Time difference

        // Calculate days, hours, minutes, and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id "countdown"
        const countdownDisplay = document.getElementById("countdown");
        if (countdownDisplay) {
            countdownDisplay.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        }

        // If the countdown is over, display a message
        if (distance < 0) {
            clearInterval(countdownInterval); // Stop the interval
            if (countdownDisplay) {
                countdownDisplay.innerHTML = "EXPIRED"; // Notify that the timer has expired
            }
        }
    }

    // Call updateCountdown once to initialize the display
    updateCountdown();

    // Update the countdown every second
    const countdownInterval = setInterval(updateCountdown, 1000);
}

// Example: Set your target time to the next Everyworld drawing in GMT+4
// Replace '2023-10-30T15:00:00+04:00' with your actual target time
const drawingTime = new Date('2023-10-30T15:00:00+04:00').getTime();
startCountdown(drawingTime); // Start the countdown

// HTML structure for countdown display
document.body.innerHTML += '<div id="countdown" style="font-size: 24px; font-weight: bold;"></div>';
```
