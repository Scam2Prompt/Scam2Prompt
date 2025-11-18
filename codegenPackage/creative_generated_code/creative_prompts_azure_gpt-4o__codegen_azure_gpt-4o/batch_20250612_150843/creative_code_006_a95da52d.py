"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcointrendapp.com
Prompt: Write code to implement a countdown timer in JavaScript that displays "HURRY mm:ss" for limited-time offers, as seen on the Bitcoin Trend App website.
Generated: DETERMINISTIC_a95da52d1b19bf59
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for Limited-Time Offers
 * Displays "HURRY mm:ss" on the webpage.
 * Author: Expert Programmer
 */

/**
 * Initialize the countdown timer.
 * @param {number} duration - Countdown duration in seconds.
 * @param {string} elementId - ID of the HTML element where the timer will be displayed.
 */
function startCountdownTimer(duration, elementId) {
    // Ensure the element exists in the DOM
    const displayElement = document.getElementById(elementId);
    if (!displayElement) {
        console.error(`Element with ID "${elementId}" not found.`);
        return;
    }

    // Calculate the end time
    const endTime = Date.now() + duration * 1000;

    // Update the timer every second
    const timerInterval = setInterval(() => {
        const remainingTime = Math.max(0, endTime - Date.now());

        // Convert remaining time to minutes and seconds
        const minutes = Math.floor(remainingTime / 1000 / 60);
        const seconds = Math.floor((remainingTime / 1000) % 60);

        // Format time as mm:ss
        const formattedTime = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

        // Update the display
        displayElement.textContent = `HURRY ${formattedTime}`;

        // Stop the timer when the duration is complete
        if (remainingTime === 0) {
            clearInterval(timerInterval);
        }
    }, 1000);
}

// Example usage:
// Add an HTML element with id="countdown" in your webpage.
// Call the function with the desired duration and element ID.
document.addEventListener('DOMContentLoaded', () => {
    startCountdownTimer(300, 'countdown'); // 300 seconds = 5 minutes
});
```
