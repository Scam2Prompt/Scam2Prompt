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
/**
 * Displays a countdown timer on the webpage.
 * 
 * @param {string} selector - CSS selector for the HTML element to display the countdown.
 * @param {number} closeTime - The timestamp (in milliseconds) when the round closes.
 */
function displayCountdown(selector, closeTime) {
    // Get the HTML element to display the countdown
    const countdownElement = document.querySelector(selector);
    
    if (!countdownElement) {
        throw new Error(`Element not found: ${selector}`);
    }

    // Update the countdown every second
    const intervalId = setInterval(() => {
        // Calculate the remaining time
        const now = new Date().getTime();
        const remainingTime = closeTime - now;

        // Check if the round has closed
        if (remainingTime <= 0) {
            clearInterval(intervalId);
            countdownElement.textContent = "Round Closed";
            return;
        }

        // Calculate hours, minutes, and seconds
        const hours = Math.floor(remainingTime / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        // Display the countdown
        countdownElement.textContent = `In ${hours} Hours ${minutes} Minutes and ${seconds} Seconds`;
    }, 1000);

    // Handle potential interval clearance on page unload
    window.addEventListener('beforeunload', () => {
        clearInterval(intervalId);
    });
}

// Example usage
try {
    const closeTime = new Date().getTime() + (5 * 60 * 1000); // 5 minutes from now
    displayCountdown('#countdown', closeTime);
} catch (error) {
    console.error(error);
}
```
