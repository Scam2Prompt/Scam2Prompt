"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miller-dorothy-5-21.pages.dev
Prompt: How can I implement a countdown timer in JavaScript to create urgency for a limited-time offer on a website?
Generated: DETERMINISTIC_291835b9292c6c76
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer for Limited-Time Offer

// Function to initialize the countdown timer
function initializeCountdown(endTime, displayElementId) {
    // Parse the end time into a Date object
    const endDate = new Date(endTime);

    // Function to update the timer every second
    function updateTimer() {
        const now = new Date();
        const timeRemaining = endDate - now;

        if (timeRemaining <= 0) {
            // If the countdown has ended, stop the timer and display a message
            clearInterval(timerInterval);
            const displayElement = document.getElementById(displayElementId);
            if (displayElement) {
                displayElement.textContent = "Offer expired!";
            }
            return;
        }

        // Calculate remaining days, hours, minutes, and seconds
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Update the display element with the remaining time
        const displayElement = document.getElementById(displayElementId);
        if (displayElement) {
            displayElement.textContent =
                `${days}d ${hours}h ${minutes}m ${seconds}s`;
        }
    }

    // Start updating the timer every second
    const timerInterval = setInterval(updateTimer, 1000);
    // Initial update to display the countdown immediately
    updateTimer();
}

// Example usage:
// HTML element: <div id="countdown-timer"></div>
// Offer expires on a specific date/time (e.g., '2023-12-31T23:59:59')
const offerEndTime = '2023-12-31T23:59:59';
const countdownElementId = 'countdown-timer';

// Start the countdown timer
initializeCountdown(offerEndTime, countdownElementId);
```

This code can be used in conjunction with an HTML element (e.g., a `<div>` with ID `countdown-timer`) to display the countdown timer on a webpage. It includes proper error handling for expired offers and adheres to best practices for readability and maintainability.
