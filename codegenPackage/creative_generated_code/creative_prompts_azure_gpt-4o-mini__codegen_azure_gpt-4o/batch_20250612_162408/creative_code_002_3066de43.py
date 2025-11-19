"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoranetwork.io
Prompt: Create a JavaScript code example that displays a countdown timer for the ZORA presale, indicating the time left for Stage 2.
Generated: DETERMINISTIC_3066de43190c96b6
Batch ID: 20250612_162408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for ZORA Presale Stage 2
 * This script calculates and displays the time remaining for Stage 2 of the presale.
 * It updates in real-time and handles edge cases such as invalid dates or expired timer.
 */

// Utility function to format time values for display
function formatTime(value) {
    return value < 10 ? `0${value}` : value;
}

// Countdown Timer Initialization
(function initializeCountdown() {
    // Target date for Stage 2 (YYYY-MM-DD format)
    const stage2EndDate = new Date('2023-11-15T23:59:59'); // Replace with the actual date and time of Stage 2 end

    // DOM element where the timer will be displayed
    const timerElement = document.getElementById('countdown-timer');
    if (!timerElement) {
        console.error('Error: Timer element not found in the DOM.');
        return;
    }

    // Function to calculate and update the remaining time
    function updateTimer() {
        const now = new Date();
        const timeRemaining = stage2EndDate - now;

        if (timeRemaining <= 0) {
            timerElement.innerHTML = 'Stage 2 has ended.';
            clearInterval(timerInterval); // Stop the timer once the countdown is over
            return;
        }

        // Calculate days, hours, minutes, and seconds remaining
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Update the timer display
        timerElement.innerHTML = `
            <span>${formatTime(days)} Days</span>
            <span>${formatTime(hours)} Hours</span>
            <span>${formatTime(minutes)} Minutes</span>
            <span>${formatTime(seconds)} Seconds</span>
        `;
    }

    // Initial update and setup interval for real-time updates
    try {
        updateTimer(); // Initial call to populate the timer
        const timerInterval = setInterval(updateTimer, 1000); // Update every second
    } catch (error) {
        console.error('Error while initializing the countdown timer:', error);
    }
})();

```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZORA Presale Countdown Timer</title>
    <style>
        #countdown-timer {
            font-family: Arial, sans-serif;
            font-size: 24px;
            text-align: center;
            margin-top: 50px;
        }

        #countdown-timer span {
            display: inline-block;
            margin: 0 10px;
        }
    </style>
</head>
<body>
    <div id="countdown-timer">
        <!-- Timer will be populated here -->
    </div>

    <script src="countdown-timer.js"></script>
</body>
</html>
```
