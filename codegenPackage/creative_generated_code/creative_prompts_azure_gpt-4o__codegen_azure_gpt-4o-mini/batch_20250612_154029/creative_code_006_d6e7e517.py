"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wynn-seven.vercel.app
Prompt: Create a program to display a countdown timer for campaigns, like the time left for the $WYNN Hunt, using JavaScript or Python.
Generated: DETERMINISTIC_d6e7e5177c789f4b
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// countdownTimer.js

/**
 * Countdown Timer for Campaigns
 * This program displays a countdown timer for a specified campaign end date.
 * @param {string} endDate - The end date of the campaign in ISO 8601 format.
 */
class CountdownTimer {
    constructor(endDate) {
        this.endDate = new Date(endDate);
        this.timerInterval = null;
    }

    /**
     * Start the countdown timer.
     * Calls updateTimer every second to update the display.
     */
    start() {
        this.updateTimer(); // Initial call to display immediately
        this.timerInterval = setInterval(() => this.updateTimer(), 1000);
    }

    /**
     * Update the countdown timer display.
     * Calculates the remaining time and updates the DOM element.
     */
    updateTimer() {
        const now = new Date();
        const remainingTime = this.endDate - now;

        if (remainingTime <= 0) {
            clearInterval(this.timerInterval);
            document.getElementById("timer").innerHTML = "Campaign has ended!";
            return;
        }

        const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
        const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        document.getElementById("timer").innerHTML = 
            `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }
}

// Example usage:
const campaignEndDate = '2023-12-31T23:59:59Z'; // Change this to your campaign end date
const countdown = new CountdownTimer(campaignEndDate);
countdown.start();
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
    <script src="countdownTimer.js" defer></script>
</head>
<body>
    <h1>Countdown Timer for Campaign</h1>
    <div id="timer"></div>
</body>
</html>
```

This code consists of a JavaScript class to manage the countdown timer and a simple HTML structure to display the timer. Adjust the `campaignEndDate` variable to set the end date for your specific campaign.
