"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baamgift.info
Prompt: Generate code in JavaScript to display a countdown timer for gift card promotions, similar to the timer feature mentioned on https://baamgift.info.
Generated: DETERMINISTIC_50cb4a840177045e
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for Gift Card Promotions
 * This script creates a countdown timer that counts down to a specified date and time.
 * When the timer reaches zero, it displays a message indicating that the promotion has ended.
 */

// Function to initialize and start the countdown timer
function startCountdown(endTime) {
    // Check if the provided endTime is a valid date
    if (isNaN(new Date(endTime))) {
        console.error("Invalid end time provided. Please provide a valid date string.");
        return;
    }

    // Update the countdown every second
    const countdownInterval = setInterval(() => {
        // Get current time
        const now = new Date().getTime();
        // Calculate the time remaining
        const distance = new Date(endTime).getTime() - now;

        // Time calculations for days, hours, minutes, and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in an HTML element with ID "countdown"
        const countdownElement = document.getElementById('countdown');
        if (countdownElement) {
            countdownElement.innerHTML = `
                ${days}d ${hours}h ${minutes}m ${seconds}s
            `;
        } else {
            console.error("Element with ID 'countdown' not found.");
        }

        // If the countdown is over, display a message and clear the interval
        if (distance < 0) {
            clearInterval(countdownInterval);
            if (countdownElement) {
                countdownElement.innerHTML = "Promotion has ended!";
            }
        }
    }, 1000);
}

// Example usage: Set the countdown to a specific date and time
const promotionEndDate = "2023-12-31T23:59:59"; // Set your promotion end date here
startCountdown(promotionEndDate);
```

```html
<!-- HTML Structure for Countdown Timer -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gift Card Countdown Timer</title>
    <style>
        #countdown {
            font-size: 2em;
            font-family: Arial, sans-serif;
            color: #333;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div id="countdown"></div>
    <script src="countdown.js"></script> <!-- Link to the JavaScript code -->
</body>
</html>
```

Make sure to save the JavaScript code in a file named `countdown.js` and the HTML code in an HTML file. Adjust the `promotionEndDate` variable to set the desired countdown end time.
