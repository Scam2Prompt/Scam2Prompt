"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gritdistribution.pages.dev
Prompt: Generate code to display a countdown timer for the closing of a $GRIT token distribution round using JavaScript.
Generated: DETERMINISTIC_8f8c4287225c146c
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer for $GRIT Token Distribution Round
// This script displays the remaining time until the distribution round closes

// HTML Structure:
// <div id="countdown-timer"></div>
// Ensure there is an element with the ID "countdown-timer" in your HTML to display the timer.

// Set the closing date and time for the $GRIT token distribution round
const closingDate = new Date("2023-12-31T23:59:59"); // Replace with your specific closing date and time

// Function to calculate and update the timer display
function updateCountdownTimer() {
    const now = new Date(); // Get the current date and time
    const timeRemaining = closingDate - now; // Calculate the remaining time in milliseconds

    // Error handling: Check if the countdown has ended
    if (timeRemaining <= 0) {
        document.getElementById("countdown-timer").innerText = "Token distribution round has ended.";
        clearInterval(timerInterval); // Stop the timer updates
        return;
    }

    // Convert milliseconds into days, hours, minutes, and seconds
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    // Format the time string and display it
    document.getElementById("countdown-timer").innerText = 
        `${days}d ${hours}h ${minutes}m ${seconds}s remaining`;
}

// Error handling: Ensure the closing date is valid
if (isNaN(closingDate.getTime())) {
    console.error("Invalid closing date provided.");
    document.getElementById("countdown-timer").innerText = "Error: Invalid closing date.";
} else {
    // Update the countdown timer every second
    const timerInterval = setInterval(updateCountdownTimer, 1000);
    updateCountdownTimer(); // Run initially to avoid a 1-second delay
}
```
