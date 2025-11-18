"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gblastclaim.pages.dev
Prompt: Implement a function in JavaScript to display a countdown timer for the "Late reward $GBT" claim period, as described on the GBlastClaim site.
Generated: DETERMINISTIC_1a7cd688bb5bfccf
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for "Late reward $GBT" claim period
 * This function sets up a countdown timer that updates every second
 * until the specified end time is reached. When the countdown finishes,
 * a message is displayed to the user.
 * 
 * @param {string} endTime - The end time for the countdown in ISO format (e.g., "2023-10-31T23:59:59Z").
 */
function startCountdown(endTime) {
    // Parse the end time string into a Date object
    const endDate = new Date(endTime);
    
    // Check if the end date is valid
    if (isNaN(endDate)) {
        console.error("Invalid end time: ", endTime);
        return;
    }
    
    // Update the countdown every second
    const timerInterval = setInterval(() => {
        const now = new Date();
        const timeLeft = endDate - now; // Calculate time left in milliseconds

        // Calculate days, hours, minutes, and seconds remaining
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        // Display the result in an element with id "countdown"
        document.getElementById("countdown").innerHTML = 
            `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // If the countdown is over, display a message and clear the interval
        if (timeLeft < 0) {
            clearInterval(timerInterval);
            document.getElementById("countdown").innerHTML = "Claim period has ended!";
            console.log("Countdown finished.");
        }
    }, 1000);
}

// Example usage: Start the countdown for a specific end time
startCountdown("2023-10-31T23:59:59Z");
```

Make sure to add an HTML element with the ID "countdown" in your HTML file for this script to work correctly:

```html
<div id="countdown"></div>
```
