"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Develop a simple JavaScript function to create a countdown timer, like "Days 00 : Hours 00 : Minutes 00 : Seconds 00," for a webpage.
Generated: DETERMINISTIC_f3f1f23e1f46802d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer Function
 * This function creates a countdown timer that displays the remaining time
 * until a specified target date and time in the format "Days 00 : Hours 00 : Minutes 00 : Seconds 00".
 * 
 * @param {string} targetDate - The target date and time in ISO format (e.g., "2023-12-31T23:59:59").
 * @param {HTMLElement} displayElement - The HTML element where the countdown will be displayed.
 */
function startCountdown(targetDate, displayElement) {
    // Validate the target date
    const targetTime = new Date(targetDate).getTime();
    if (isNaN(targetTime)) {
        console.error("Invalid target date provided.");
        return;
    }

    // Update the countdown every second
    const countdownInterval = setInterval(() => {
        const now = new Date().getTime();
        const distance = targetTime - now;

        // Calculate time components
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the specified format
        displayElement.innerHTML = `Days ${days} : Hours ${hours.toString().padStart(2, '0')} : Minutes ${minutes.toString().padStart(2, '0')} : Seconds ${seconds.toString().padStart(2, '0')}`;

        // If the countdown is finished, display a message and clear the interval
        if (distance < 0) {
            clearInterval(countdownInterval);
            displayElement.innerHTML = "Countdown Finished!";
        }
    }, 1000);
}

// Example usage:
// Assuming there is an HTML element with the id "countdownDisplay"
const countdownDisplay = document.getElementById("countdownDisplay");
startCountdown("2023-12-31T23:59:59", countdownDisplay);
```

Make sure to include an HTML element with the id `countdownDisplay` in your HTML file for the countdown to be displayed.
