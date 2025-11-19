"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dacarlaw.com
Prompt: Provide an example of a JavaScript function that updates a countdown timer in real-time on a website.
Generated: DETERMINISTIC_1958e490c00b5773
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Updates a countdown timer in real-time on a website.
 * @param {string} timerId - The ID of the HTML element where the timer will be displayed.
 * @param {Date} endTime - The target end time for the countdown.
 */
function startCountdown(timerId, endTime) {
    // Validate input
    if (!document.getElementById(timerId)) {
        console.error(`Element with ID "${timerId}" not found.`);
        return;
    }
    if (!(endTime instanceof Date)) {
        console.error(`Invalid endTime provided. Must be a valid Date object.`);
        return;
    }

    const timerElement = document.getElementById(timerId);

    /**
     * Formats time values to ensure they always have two digits.
     * @param {number} value - The value to format.
     * @returns {string} - A two-digit formatted string.
     */
    function formatTime(value) {
        return value < 10 ? `0${value}` : `${value}`;
    }

    /**
     * Updates the timer display.
     */
    function updateTimer() {
        const now = new Date();
        const timeRemaining = endTime - now;

        if (timeRemaining <= 0) {
            // Stop the timer if the countdown is complete
            clearInterval(timerInterval);
            timerElement.textContent = "Time's up!";
            return;
        }

        // Calculate remaining time
        const seconds = Math.floor((timeRemaining / 1000) % 60);
        const minutes = Math.floor((timeRemaining / 1000 / 60) % 60);
        const hours = Math.floor((timeRemaining / 1000 / 60 / 60) % 24);
        const days = Math.floor(timeRemaining / 1000 / 60 / 60 / 24);

        // Update the timer element with the formatted time
        timerElement.textContent = `${days}d ${formatTime(hours)}h ${formatTime(minutes)}m ${formatTime(seconds)}s`;
    }

    // Update the timer immediately and then every second
    updateTimer();
    const timerInterval = setInterval(updateTimer, 1000);
}

// Example usage:
// Assuming there is an element <div id="countdown"></div> in the HTML.
// Example: Start a countdown that ends 10 minutes from now.
const tenMinutesFromNow = new Date(new Date().getTime() + 10 * 60 * 1000);
startCountdown("countdown", tenMinutesFromNow);
```
