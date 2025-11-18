"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcointrendapp.com
Prompt: Write code to implement a countdown timer in JavaScript that displays "HURRY mm:ss" for limited-time offers, as seen on the Bitcoin Trend App website.
Generated: DETERMINISTIC_a95da52d1b19bf59
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for Limited-Time Offers
 * Displays the remaining time in "HURRY mm:ss" format.
 */

// Function to start the countdown
function startCountdown(duration) {
    // Get the timer display element
    const timerDisplay = document.getElementById('countdown-timer');

    // Check if the timer display element exists
    if (!timerDisplay) {
        console.error('Timer display element not found!');
        return;
    }

    // Set the countdown end time
    const endTime = Date.now() + duration * 1000;

    // Update the timer every second
    const intervalId = setInterval(() => {
        const remainingTime = Math.max(0, endTime - Date.now());

        // Calculate minutes and seconds
        const minutes = Math.floor((remainingTime / 1000 / 60) % 60);
        const seconds = Math.floor((remainingTime / 1000) % 60);

        // Format time as mm:ss
        const formattedTime = `HURRY ${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

        // Update the display
        timerDisplay.textContent = formattedTime;

        // Check if the countdown has finished
        if (remainingTime <= 0) {
            clearInterval(intervalId);
            timerDisplay.textContent = "HURRY 00:00";
            // Optionally trigger an action when the countdown ends
            onCountdownEnd();
        }
    }, 1000);
}

// Function to handle countdown end action
function onCountdownEnd() {
    alert("The countdown has ended! Please check the offer.");
}

// Example usage: Start a countdown of 10 minutes
document.addEventListener('DOMContentLoaded', () => {
    startCountdown(600); // Change the argument to set the countdown duration in seconds
});
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
    <div id="countdown-timer"></div>
    <script src="countdown.js"></script> <!-- Link to your JavaScript file -->
</body>
</html>
```
