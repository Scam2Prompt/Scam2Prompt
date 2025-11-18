"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-pogai.com
Prompt: Create a countdown timer in JavaScript that dynamically updates in real-time, similar to the one used on the $POGAI token distribution page to show hours, minutes, and seconds remaining.
Generated: DETERMINISTIC_45529f847152106c
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer
 * This script creates a dynamic countdown timer that updates in real-time.
 * It displays hours, minutes, and seconds remaining until a specified end time.
 */

// Function to initialize and start the countdown timer
function startCountdown(endTime) {
    const timerElement = document.getElementById('countdown'); // Get the DOM element to display the timer

    if (!timerElement) {
        console.error('Countdown element not found in the DOM.');
        return;
    }

    // Function to calculate and update the remaining time
    function updateTimer() {
        const now = new Date(); // Get the current time
        const timeRemaining = Math.max(0, endTime - now); // Calculate remaining time in milliseconds

        if (timeRemaining === 0) {
            timerElement.textContent = 'Countdown has ended!';
            clearInterval(intervalId); // Stop the timer when it reaches 0
            return;
        }

        // Convert remaining time from milliseconds to hours, minutes, and seconds
        const hours = Math.floor(timeRemaining / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Update the timer display
        timerElement.textContent = `${hours}h ${minutes}m ${seconds}s`;
    }

    // Update the timer immediately to avoid initial delay
    updateTimer();

    // Set an interval to update the timer every second
    const intervalId = setInterval(updateTimer, 1000);
}

// Example usage:
// Set the end time for the countdown (target date and time)
const targetDate = new Date('2023-12-31T23:59:59'); // Replace with your desired end time
startCountdown(targetDate);

// HTML structure:
// Add this element to your HTML where you want the timer to appear:
// <div id="countdown"></div>
```
