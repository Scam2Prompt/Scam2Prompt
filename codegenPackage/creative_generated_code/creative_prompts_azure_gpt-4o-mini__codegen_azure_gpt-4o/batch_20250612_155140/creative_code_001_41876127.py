"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharon-robinson-662.pages.dev
Prompt: Write a function in JavaScript that displays a countdown timer for a limited-time offer on a friendship-themed product.
Generated: DETERMINISTIC_418761273b9f2e77
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
 * Displays a countdown timer for a limited-time offer.
 * The timer will count down to a specified end time and update the display every second.
 * Once the timer reaches zero, it will show a message indicating the offer has expired.
 *
 * @param {string} endTime - The end time for the countdown in ISO 8601 format (e.g., '2023-12-31T23:59:59Z').
 * @param {string} displayElementId - The ID of the HTML element where the countdown will be displayed.
 */
function displayCountdownTimer(endTime, displayElementId) {
    try {
        // Validate the endTime and displayElementId
        if (!endTime || !Date.parse(endTime)) {
            throw new Error("Invalid endTime. Please provide a valid ISO 8601 date string.");
        }

        const displayElement = document.getElementById(displayElementId);
        if (!displayElement) {
            throw new Error(`Element with ID "${displayElementId}" not found.`);
        }

        const countdownInterval = setInterval(() => {
            const now = new Date();
            const endDate = new Date(endTime);
            const remainingTime = endDate - now;

            if (remainingTime <= 0) {
                clearInterval(countdownInterval);
                displayElement.textContent = "The offer has expired!";
                return;
            }

            // Calculate days, hours, minutes, and seconds remaining
            const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
            const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

            // Update the displayElement with the countdown timer
            displayElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s remaining!`;
        }, 1000);

    } catch (error) {
        console.error("Error displaying countdown timer:", error.message);
    }
}

// Example usage:
// 1. Add an HTML element with ID `countdown-timer`
//    <div id="countdown-timer"></div>
// 2. Call the function with the desired end time and element ID
//    displayCountdownTimer('2023-12-31T23:59:59Z', 'countdown-timer');
```
