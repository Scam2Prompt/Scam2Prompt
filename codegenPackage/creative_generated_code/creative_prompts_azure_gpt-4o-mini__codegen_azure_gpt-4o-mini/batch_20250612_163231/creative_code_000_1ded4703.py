"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oasysgames.live
Prompt: Generate code to implement a countdown timer for the "Ending Soon" campaigns on OasysGames, using the local time settings provided.
Generated: DETERMINISTIC_1ded47032d92fd7e
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for "Ending Soon" Campaigns on OasysGames
 * This script creates a countdown timer that updates every second.
 * It displays the time remaining until a specified end date and time.
 */

// Function to start the countdown timer
function startCountdown(endTime) {
    // Validate the endTime parameter
    if (!endTime || isNaN(new Date(endTime))) {
        console.error('Invalid end time provided. Please provide a valid date.');
        return;
    }

    const countdownElement = document.getElementById('countdown'); // Ensure there is an element with this ID
    const endDate = new Date(endTime).getTime(); // Convert to milliseconds

    // Update the countdown every second
    const countdownInterval = setInterval(() => {
        const now = new Date().getTime(); // Get current time
        const timeLeft = endDate - now; // Calculate remaining time

        // Calculate days, hours, minutes and seconds
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        // Display the result in the countdown element
        countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // If the countdown is finished, display a message
        if (timeLeft < 0) {
            clearInterval(countdownInterval);
            countdownElement.innerHTML = 'Campaign has ended!';
        }
    }, 1000); // Update every second
}

// Usage example: Call this function with the end date of the campaign
const campaignEndTime = '2023-10-31T23:59:59'; // Example end time (ISO format)
startCountdown(campaignEndTime);
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
    <style>
        #countdown {
            font-size: 24px; /* Styling for the countdown display */
            font-weight: bold;
            color: #ff0000; /* Red color for urgency */
        }
    </style>
</head>
<body>
    <div id="countdown"></div> <!-- Countdown display element -->
    
    <script src="path/to/your/countdown.js"></script><!-- Link to the JavaScript file -->
</body>
</html>
```
