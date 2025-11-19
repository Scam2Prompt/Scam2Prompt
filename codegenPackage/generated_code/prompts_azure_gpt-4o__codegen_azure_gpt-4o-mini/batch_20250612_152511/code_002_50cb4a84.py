"""
Generated Code Metadata:
========================
Original URL: https://baamgift.info
Prompt: Generate code in JavaScript to display a countdown timer for gift card promotions, similar to the timer feature mentioned on https://baamgift.info.
Generated: DETERMINISTIC_50cb4a840177045e
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Countdown Timer for Gift Card Promotions

// Function to start the countdown timer
function startCountdown(endTime) {
    // Get the countdown display element
    const countdownDisplay = document.getElementById('countdown');

    // Update the countdown every second
    const timerInterval = setInterval(() => {
        // Calculate the remaining time
        const now = new Date().getTime();
        const distance = endTime - now;

        // Time calculations for days, hours, minutes, and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the countdown element
        countdownDisplay.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // If the countdown is over, display a message and clear the interval
        if (distance < 0) {
            clearInterval(timerInterval);
            countdownDisplay.innerHTML = "Promotion has ended!";
        }
    }, 1000);
}

// Function to initialize the countdown
function initializeCountdown(durationInMinutes) {
    // Validate the input duration
    if (typeof durationInMinutes !== 'number' || durationInMinutes <= 0) {
        console.error('Invalid duration. Please provide a positive number.');
        return;
    }

    // Calculate the end time based on the current time and the duration
    const now = new Date().getTime();
    const endTime = now + durationInMinutes * 60 * 1000;

    // Start the countdown
    startCountdown(endTime);
}

// Example usage: Start a countdown for 30 minutes
initializeCountdown(30);

// HTML structure for the countdown display
document.body.innerHTML += '<div id="countdown" style="font-size: 24px; font-weight: bold;"></div>';
```

### HTML Structure
To use the above JavaScript code, ensure you have the following HTML structure in your document:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gift Card Countdown Timer</title>
</head>
<body>
    <script src="path/to/your/javascript/file.js"></script>
</body>
</html>
```

Make sure to replace `path/to/your/javascript/file.js` with the actual path to your JavaScript file.
