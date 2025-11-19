"""
Generated Code Metadata:
========================
Original URL: https://baamgift.info
Prompt: Write a JavaScript function to implement a countdown timer for limited-time offers on gift cards, similar to the one displayed on بام گیفت.
Generated: DETERMINISTIC_b1f95f51d7a30095
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer for Limited-Time Offers
 * 
 * This function creates a countdown timer that updates the remaining time
 * for a limited-time offer on gift cards. It displays the time in the format
 * HH:MM:SS and stops when the timer reaches zero.
 * 
 * @param {string} endTime - The end time of the offer in ISO 8601 format (e.g., "2023-12-31T23:59:59").
 * @param {string} displayElementId - The ID of the HTML element where the timer will be displayed.
 */
function startCountdownTimer(endTime, displayElementId) {
    // Validate input parameters
    if (!endTime || !displayElementId) {
        console.error("Invalid parameters: endTime and displayElementId are required.");
        return;
    }

    // Parse the end time
    const endDate = new Date(endTime);
    if (isNaN(endDate.getTime())) {
        console.error("Invalid endTime format. Please provide a valid ISO 8601 date string.");
        return;
    }

    // Get the display element
    const displayElement = document.getElementById(displayElementId);
    if (!displayElement) {
        console.error(`Element with ID "${displayElementId}" not found.`);
        return;
    }

    // Function to calculate and update the remaining time
    function updateTimer() {
        const now = new Date();
        const timeRemaining = endDate - now;

        if (timeRemaining <= 0) {
            // Stop the timer when the countdown reaches zero
            clearInterval(timerInterval);
            displayElement.textContent = "Offer expired!";
            return;
        }

        // Calculate hours, minutes, and seconds
        const hours = Math.floor(timeRemaining / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Format the time as HH:MM:SS
        const formattedTime = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

        // Update the display element
        displayElement.textContent = formattedTime;
    }

    // Start the timer and update every second
    const timerInterval = setInterval(updateTimer, 1000);

    // Initial update to display the timer immediately
    updateTimer();
}

// Example usage:
// HTML: <div id="countdown-timer"></div>
// JavaScript: startCountdownTimer("2023-12-31T23:59:59", "countdown-timer");
```
