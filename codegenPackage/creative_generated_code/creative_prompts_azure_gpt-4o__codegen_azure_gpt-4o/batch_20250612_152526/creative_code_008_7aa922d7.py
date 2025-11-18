"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baazaars.com
Prompt: Create a JavaScript function to implement a countdown timer for special deals like "Luxury & Trendy Watches – Up to 50% OFF!" on the website.
Generated: DETERMINISTIC_7aa922d7084ba4df
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for Special Deals
 * Displays a countdown timer for promotions like "Luxury & Trendy Watches – Up to 50% OFF!"
 * @param {string} endTime - The ISO 8601 string representing the end time of the deal.
 * @param {string} displayElementId - The ID of the HTML element to display the countdown timer.
 */
function startCountdownTimer(endTime, displayElementId) {
    // Parse the endTime into a Date object
    const dealEndDate = new Date(endTime);

    // Validate the provided date
    if (isNaN(dealEndDate)) {
        console.error('Invalid end time. Please provide a valid ISO 8601 date string.');
        return;
    }

    // Get the display element for showing the timer
    const displayElement = document.getElementById(displayElementId);
    if (!displayElement) {
        console.error(`Element with ID "${displayElementId}" not found.`);
        return;
    }

    /**
     * Updates the countdown timer display.
     */
    function updateTimer() {
        const now = new Date();
        const timeRemaining = dealEndDate - now;

        if (timeRemaining <= 0) {
            // Timer has expired, show "Deal Ended" message
            displayElement.textContent = "Deal Ended!";
            clearInterval(timerInterval); // Stop further updates
            return;
        }

        // Calculate time components
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Update the display element with the formatted time
        displayElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }

    // Initialize the timer
    updateTimer();

    // Set an interval to update the timer every second
    const timerInterval = setInterval(updateTimer, 1000);
}

// Example usage:
// Assuming there is an HTML element with ID "countdownTimer".
// <div id="countdownTimer"></div>
startCountdownTimer("2023-12-31T23:59:59Z", "countdownTimer");
```
