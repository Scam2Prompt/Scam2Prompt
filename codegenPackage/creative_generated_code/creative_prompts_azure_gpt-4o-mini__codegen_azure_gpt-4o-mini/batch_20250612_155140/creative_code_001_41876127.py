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
 * Countdown Timer for Limited-Time Offer
 * This function creates a countdown timer that updates the display every second.
 * When the countdown reaches zero, it triggers an alert notifying the user that the offer has expired.
 * 
 * @param {number} duration - The countdown duration in seconds.
 * @param {string} elementId - The ID of the HTML element to display the countdown.
 */
function startCountdown(duration, elementId) {
    // Validate inputs
    if (typeof duration !== 'number' || duration < 0) {
        console.error('Invalid duration: must be a non-negative number.');
        return;
    }
    if (typeof elementId !== 'string' || !document.getElementById(elementId)) {
        console.error('Invalid elementId: must be a valid string referring to an existing HTML element ID.');
        return;
    }

    // Initialize countdown
    let timer = duration, minutes, seconds;

    // Update the countdown display
    const updateDisplay = () => {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        // Format the display to always show two digits
        seconds = seconds < 10 ? "0" + seconds : seconds;
        const displayText = `${minutes}:${seconds}`;

        // Update the HTML element with the countdown
        document.getElementById(elementId).textContent = displayText;

        // Check if the timer has reached zero
        if (timer <= 0) {
            clearInterval(interval);
            alert('The limited-time offer has expired!');
        }
        timer--;
    };

    // Start the countdown timer that calls updateDisplay every second
    const interval = setInterval(updateDisplay, 1000);

    // Initial call to display the countdown immediately
    updateDisplay();
}

// Example of how to call the countdown function
// startCountdown(300, 'countdownDisplay'); // Starts a 5-minute countdown
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
</head>
<body>
    <h1>Limited-Time Offer Countdown</h1>
    <div id="countdownDisplay"></div>
    <script src="countdown.js"></script>
    <script>
        // Call the countdown function with a 5-minute duration (300 seconds)
        startCountdown(300, 'countdownDisplay');
    </script>
</body>
</html>
```
