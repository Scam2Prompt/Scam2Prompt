"""
Generated Code Metadata:
========================
Original URL: https://donna-lopez-376.pages.dev
Prompt: Write a JavaScript function that displays a countdown timer for a limited-time offer on a webpage.
Generated: DETERMINISTIC_8feebf393933e4e7
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer Function
 * Displays a countdown timer for a limited-time offer on a webpage.
 * 
 * @param {string} elementId - The ID of the HTML element where the timer will be displayed.
 * @param {number} duration - The duration of the countdown in seconds.
 */
function startCountdown(elementId, duration) {
    // Validate input parameters
    if (typeof elementId !== 'string' || typeof duration !== 'number' || duration < 0) {
        console.error('Invalid parameters: elementId must be a string and duration must be a non-negative number.');
        return;
    }

    // Get the HTML element to display the countdown
    const countdownElement = document.getElementById(elementId);
    if (!countdownElement) {
        console.error(`Element with ID "${elementId}" not found.`);
        return;
    }

    // Initialize the countdown time
    let timeRemaining = duration;

    // Update the countdown display
    const updateDisplay = () => {
        const minutes = Math.floor(timeRemaining / 60);
        const seconds = timeRemaining % 60;
        countdownElement.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

        // Check if the countdown has finished
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            countdownElement.textContent = 'Offer has expired!';
        } else {
            timeRemaining--;
        }
    };

    // Start the countdown timer
    const timerInterval = setInterval(updateDisplay, 1000);
    updateDisplay(); // Initial display update
}

// Example usage: Start a countdown of 5 minutes (300 seconds) on an element with ID 'countdown'
startCountdown('countdown', 300);
```

```html
<!-- HTML structure to use with the countdown timer -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
</head>
<body>
    <div id="countdown" style="font-size: 2em; font-weight: bold;"></div>
    <script src="path/to/your/script.js"></script>
</body>
</html>
```
