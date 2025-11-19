"""
Generated Code Metadata:
========================
Original URL: https://dacarlaw.com
Prompt: Provide an example of a JavaScript function that updates a countdown timer in real-time on a website.
Generated: DETERMINISTIC_1958e490c00b5773
Batch ID: 20250612_162101
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
 * This function initializes a countdown timer that updates in real-time on the webpage.
 * 
 * @param {number} duration - The countdown duration in seconds.
 * @param {string} displayElementId - The ID of the HTML element where the timer will be displayed.
 */
function startCountdown(duration, displayElementId) {
    // Validate input parameters
    if (typeof duration !== 'number' || duration <= 0) {
        console.error('Invalid duration. Please provide a positive number.');
        return;
    }
    
    const displayElement = document.getElementById(displayElementId);
    if (!displayElement) {
        console.error(`Element with ID "${displayElementId}" not found.`);
        return;
    }

    let timer = duration, minutes, seconds;

    // Update the timer every second
    const interval = setInterval(() => {
        // Calculate minutes and seconds
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        // Format the time to always show two digits
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        // Display the timer
        displayElement.textContent = `${minutes}:${seconds}`;

        // Check if the timer has reached zero
        if (--timer < 0) {
            clearInterval(interval);
            displayElement.textContent = "Time's up!";
        }
    }, 1000);
}

// Example usage: Start a countdown of 5 minutes
// Ensure to call this function after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    startCountdown(300, 'countdownDisplay');
});
```

```html
<!-- HTML structure to display the countdown timer -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
</head>
<body>
    <div id="countdownDisplay">05:00</div>
    <script src="path/to/your/script.js"></script>
</body>
</html>
```
