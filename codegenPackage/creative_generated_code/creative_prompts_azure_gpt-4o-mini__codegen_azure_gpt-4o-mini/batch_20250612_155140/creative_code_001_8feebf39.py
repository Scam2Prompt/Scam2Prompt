"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donna-lopez-376.pages.dev
Prompt: Write a JavaScript function that displays a countdown timer for a limited-time offer on a webpage.
Generated: DETERMINISTIC_8feebf393933e4e7
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
 * Countdown Timer for Limited Time Offer
 * 
 * This function initializes a countdown timer that updates 
 * every second and displays the remaining time on the webpage. 
 * The timer will stop when it reaches zero.
 * 
 * @param {string} elementId - The ID of the HTML element where the countdown will be displayed.
 * @param {number} duration - The countdown duration in seconds.
 */
function startCountdown(elementId, duration) {
    // Validate input parameters
    if (typeof elementId !== 'string' || typeof duration !== 'number' || duration <= 0) {
        console.error('Invalid parameters passed to startCountdown. Please provide a valid element ID and a positive duration.');
        return;
    }

    // Get the HTML element where the countdown will be displayed
    const countdownElement = document.getElementById(elementId);
    if (!countdownElement) {
        console.error(`Element with ID "${elementId}" not found.`);
        return;
    }

    let timeRemaining = duration;

    // Function to update the countdown display
    const updateCountdownDisplay = () => {
        const minutes = Math.floor(timeRemaining / 60);
        const seconds = timeRemaining % 60;
        countdownElement.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    };

    // Update the display immediately
    updateCountdownDisplay();

    // Set an interval to update the countdown every second
    const intervalId = setInterval(() => {
        timeRemaining--;

        // Check if the countdown has reached zero
        if (timeRemaining < 0) {
            clearInterval(intervalId);
            countdownElement.textContent = 'Offer Expired!';
            return;
        }

        // Update the countdown display
        updateCountdownDisplay();
    }, 1000);
}

// Example usage:
// startCountdown('countdown', 300); // Starts a countdown of 5 minutes
```

```html
<!-- Example HTML structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer Example</title>
</head>
<body>
    <h1>Limited Time Offer!</h1>
    <div id="countdown"></div>
    <script src="path/to/your/script.js"></script>
    <script>
        // Start the countdown for 5 minutes (300 seconds)
        startCountdown('countdown', 300);
    </script>
</body>
</html>
```
c="path/to/your/script.js"></script>
    <script>
        // Start the countdown to a specific date
        startCountdown('countdown', '2023-12-31T23:59:59');
    </script>
</body>
</html>
```
