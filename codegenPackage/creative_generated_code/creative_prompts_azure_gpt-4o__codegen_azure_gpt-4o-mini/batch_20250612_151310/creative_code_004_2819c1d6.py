"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-aevo.pages.dev
Prompt: Develop a countdown timer in JavaScript to display the "END OF FARM BOOST" time remaining, as shown on the Aevo webpage.
Generated: DETERMINISTIC_2819c1d6294ebf9e
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Countdown Timer for "END OF FARM BOOST"

// Set the target date and time for the end of the farm boost
const targetDate = new Date("2023-10-31T23:59:59Z").getTime(); // Adjust date as needed

// Function to start the countdown
function startCountdown() {
    // Update the timer every second
    const countdownInterval = setInterval(() => {
        const now = new Date().getTime(); // Get the current time
        const timeRemaining = targetDate - now; // Calculate the time remaining

        // Time calculations for days, hours, minutes, and seconds
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Display the countdown in the specified format
        displayCountdown(days, hours, minutes, seconds);

        // Check if the countdown is finished
        if (timeRemaining < 0) {
            clearInterval(countdownInterval); // Stop the countdown
            document.getElementById("countdown").innerHTML = "FARM BOOST ENDED"; // Notify that the countdown has ended
        }
    }, 1000);
}

// Function to display the countdown
function displayCountdown(days, hours, minutes, seconds) {
    const countdownElement = document.getElementById("countdown");
    if (countdownElement) {
        countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`; // Update the countdown display
    } else {
        console.error("Countdown element not found in the DOM."); // Log an error if the element is not found
    }
}

// Initialize the countdown when the window loads
window.onload = startCountdown;
```

```html
<!-- HTML to display the countdown timer -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farm Boost Countdown</title>
</head>
<body>
    <h1>Farm Boost Countdown</h1>
    <div id="countdown"></div> <!-- Element to display the countdown -->
    <script src="countdown.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
