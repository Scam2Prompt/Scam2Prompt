"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://papecoinairdropclaim.pages.dev
Prompt: Write a JavaScript function to display a countdown timer for the end of Stage 1 of the $PAPE presale, updating dynamically based on the remaining time.
Generated: DETERMINISTIC_9054c30e9e2cb81b
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for the end of Stage 1 of the $PAPE presale.
 * This function initializes the countdown and updates the display every second.
 * 
 * @param {Date} endTime - The end time of Stage 1 in Date format.
 * @param {HTMLElement} displayElement - The HTML element where the countdown will be displayed.
 */
function startCountdown(endTime, displayElement) {
    // Validate input parameters
    if (!(endTime instanceof Date) || typeof displayElement !== 'object') {
        console.error("Invalid arguments provided to startCountdown function.");
        return;
    }

    // Update the countdown every second
    const timerInterval = setInterval(() => {
        // Calculate the remaining time
        const now = new Date().getTime();
        const remainingTime = endTime.getTime() - now;

        // Time calculations for days, hours, minutes, and seconds
        const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
        const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        // Display the result in the specified format
        displayElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // If the countdown is over, display a message and clear the interval
        if (remainingTime < 0) {
            clearInterval(timerInterval);
            displayElement.innerHTML = "Stage 1 has ended!";
        }
    }, 1000);
}

// Example usage
const endTime = new Date('2023-12-31T23:59:59'); // Set your end time here
const countdownDisplay = document.getElementById('countdown'); // Ensure this element exists in your HTML
startCountdown(endTime, countdownDisplay);
```
