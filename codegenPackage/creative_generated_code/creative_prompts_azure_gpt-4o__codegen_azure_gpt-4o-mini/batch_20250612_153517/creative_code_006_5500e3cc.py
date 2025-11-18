"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepelovesinu.pages.dev
Prompt: Generate a JavaScript snippet to display a countdown timer for the end of Stage 3 of the Pepe Love Inu token sale, using the provided time format (days, hours, minutes, seconds).
Generated: DETERMINISTIC_5500e3cc554fe743
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer for Pepe Love Inu Token Sale - Stage 3

// Set the end time for Stage 3 (example: December 31, 2023, at 23:59:59)
const endTime = new Date('2023-12-31T23:59:59Z').getTime();

// Function to start the countdown timer
function startCountdown() {
    // Update the countdown every second
    const timerInterval = setInterval(() => {
        // Get the current time
        const now = new Date().getTime();
        
        // Calculate the remaining time
        const remainingTime = endTime - now;

        // If the countdown is finished, clear the interval and display a message
        if (remainingTime < 0) {
            clearInterval(timerInterval);
            document.getElementById('countdown').innerHTML = 'The token sale has ended!';
            return;
        }

        // Calculate days, hours, minutes and seconds from the remaining time
        const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
        const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        // Display the result in the countdown element
        document.getElementById('countdown').innerHTML = 
            `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }, 1000);
}

// Start the countdown when the window loads
window.onload = () => {
    try {
        startCountdown();
    } catch (error) {
        console.error('Error starting countdown:', error);
        document.getElementById('countdown').innerHTML = 'Error initializing countdown.';
    }
};
```

```html
<!-- HTML structure to display the countdown timer -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pepe Love Inu Token Sale Countdown</title>
    <style>
        #countdown {
            font-family: Arial, sans-serif;
            font-size: 2em;
            color: #ff4081; /* Customize the color */
            text-align: center;
            margin-top: 20%;
        }
    </style>
</head>
<body>
    <div id="countdown"></div>
    <script src="countdown.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
