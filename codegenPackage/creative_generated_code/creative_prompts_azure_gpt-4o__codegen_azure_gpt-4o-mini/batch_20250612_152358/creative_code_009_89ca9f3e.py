"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-claim.pages.dev
Prompt: Create a function in JavaScript to display the countdown timer for the next price increase in the WienerAI presale, based on the provided time data.
Generated: DETERMINISTIC_89ca9f3e035c347f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for WienerAI Presale Price Increase
 * This function initializes a countdown timer that displays the remaining time until the next price increase.
 * 
 * @param {Date} targetTime - The future date and time when the price increase occurs.
 * @param {HTMLElement} displayElement - The HTML element where the countdown will be displayed.
 */
function startCountdown(targetTime, displayElement) {
    // Validate input parameters
    if (!(targetTime instanceof Date)) {
        console.error('Invalid target time. Please provide a valid Date object.');
        return;
    }
    
    if (!(displayElement instanceof HTMLElement)) {
        console.error('Invalid display element. Please provide a valid HTML element.');
        return;
    }

    // Update the countdown every second
    const timerInterval = setInterval(() => {
        const now = new Date();
        const remainingTime = targetTime - now;

        // Calculate time components
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));

        // Display the result in the specified HTML element
        displayElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // Clear the interval if the countdown is finished
        if (remainingTime < 0) {
            clearInterval(timerInterval);
            displayElement.innerHTML = "Price increase has occurred!";
        }
    }, 1000);
}

// Example usage of the startCountdown function
const targetDate = new Date('2023-12-31T23:59:59'); // Set your target date and time
const countdownDisplay = document.getElementById('countdown'); // Ensure an element with this ID exists in your HTML
startCountdown(targetDate, countdownDisplay);
```

Make sure to include an appropriate HTML element with the ID `countdown` in your HTML file to see the countdown in action:

```html
<div id="countdown"></div>
```
