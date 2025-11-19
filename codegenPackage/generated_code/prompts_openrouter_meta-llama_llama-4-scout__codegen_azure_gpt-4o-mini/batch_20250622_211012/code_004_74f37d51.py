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
// Countdown Timer for Round Closing Time
class CountdownTimer {
    constructor(endTime) {
        this.endTime = new Date(endTime).getTime(); // Convert end time to milliseconds
        this.timerId = null; // Store the timer ID for clearing it later
        this.updateDisplay(); // Initial display update
    }

    // Start the countdown timer
    start() {
        this.timerId = setInterval(() => {
            this.updateDisplay();
        }, 1000); // Update every second
    }

    // Update the display of the countdown timer
    updateDisplay() {
        const now = new Date().getTime(); // Get current time
        const timeRemaining = this.endTime - now; // Calculate time remaining

        // If the countdown is finished, clear the timer and display a message
        if (timeRemaining < 0) {
            clearInterval(this.timerId);
            document.getElementById('countdown').innerHTML = "Round Closed";
            return;
        }

        // Calculate hours, minutes, and seconds remaining
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Update the countdown display
        document.getElementById('countdown').innerHTML = `In ${hours} Hours ${minutes} Minutes and ${seconds} Seconds`;
    }

    // Stop the countdown timer
    stop() {
        clearInterval(this.timerId);
    }
}

// Example usage
const endTime = '2023-10-31T23:59:59'; // Set your round closing time here
const countdownTimer = new CountdownTimer(endTime);
countdownTimer.start(); // Start the countdown timer

// HTML element to display the countdown
document.body.innerHTML += '<div id="countdown"></div>';
```
