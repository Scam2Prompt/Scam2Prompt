"""
Generated Code Metadata:
========================
Original URL: https://ballatorino.it
Prompt: Create a JavaScript code snippet to implement a countdown timer for an event like BallaTorino, displaying the days, hours, minutes, and seconds until the event starts.
Generated: DETERMINISTIC_a47583f20f7af94e
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Countdown Timer for BallaTorino Event

// Function to start the countdown timer
function startCountdown(eventDate) {
    // Validate the event date
    if (!(eventDate instanceof Date) || isNaN(eventDate)) {
        console.error("Invalid event date provided.");
        return;
    }

    // Update the countdown every second
    const countdownInterval = setInterval(() => {
        const now = new Date();
        const timeRemaining = eventDate - now;

        // Calculate days, hours, minutes, and seconds
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Display the countdown
        document.getElementById("countdown").innerHTML = `
            ${days}d ${hours}h ${minutes}m ${seconds}s
        `;

        // If the countdown is finished, display a message
        if (timeRemaining < 0) {
            clearInterval(countdownInterval);
            document.getElementById("countdown").innerHTML = "Event has started!";
        }
    }, 1000);
}

// Set the event date (example: December 31, 2023, 23:59:59)
const eventDate = new Date("2023-12-31T23:59:59");

// Start the countdown
startCountdown(eventDate);
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BallaTorino Countdown Timer</title>
    <style>
        #countdown {
            font-size: 2em;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Countdown to BallaTorino Event</h1>
    <div id="countdown"></div>
    <script src="countdown.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
