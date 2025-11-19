"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betty-moore-873.pages.dev
Prompt: How can I implement a countdown timer in JavaScript for a limited-time offer on a webpage?
Generated: DETERMINISTIC_c07f5bd31abea236
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer Implementation in JavaScript

// Function to start the countdown timer
function startCountdown(endTime) {
    // Get the countdown display element
    const countdownDisplay = document.getElementById('countdown');

    // Update the countdown every second
    const timer = setInterval(() => {
        const now = new Date().getTime(); // Current time
        const distance = endTime - now; // Time remaining

        // Calculate days, hours, minutes, and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the countdown element
        countdownDisplay.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // If the countdown is finished, display a message and clear the timer
        if (distance < 0) {
            clearInterval(timer);
            countdownDisplay.innerHTML = "Offer has expired!";
        }
    }, 1000); // Interval set to 1000 milliseconds (1 second)
}

// Function to initialize the countdown timer with a specified duration
function initializeCountdown(durationInMinutes) {
    // Calculate the end time based on the current time and the duration
    const endTime = new Date().getTime() + durationInMinutes * 60 * 1000;

    // Start the countdown
    startCountdown(endTime);
}

// Example usage: Start a 10-minute countdown
document.addEventListener('DOMContentLoaded', () => {
    // Set a countdown for 10 minutes (600000 milliseconds)
    initializeCountdown(10);
});
```

```html
<!-- HTML for displaying the countdown timer -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
    <script src="countdown.js" defer></script> <!-- Include the script -->
</head>
<body>
    <h1>Limited Time Offer!</h1>
    <div id="countdown"></div> <!-- Countdown timer display -->
</body>
</html>
```
