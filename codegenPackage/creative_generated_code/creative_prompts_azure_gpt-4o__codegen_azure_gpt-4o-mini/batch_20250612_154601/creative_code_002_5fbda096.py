"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-turbo.com
Prompt: Create a JavaScript function to display a countdown timer for the closing of the $TURBO token presale round, updating in real-time.
Generated: DETERMINISTIC_5fbda0962097829f
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Countdown Timer for the $TURBO Token Presale Round
 * This function initializes a countdown timer that updates in real-time.
 * The countdown will display the remaining time until the specified end date.
 *
 * @param {string} endDate - The end date of the presale in ISO format (YYYY-MM-DDTHH:mm:ss).
 * @param {HTMLElement} displayElement - The HTML element where the countdown will be displayed.
 */
function startCountdown(endDate, displayElement) {
    // Ensure the end date is valid
    const targetDate = new Date(endDate);
    if (isNaN(targetDate.getTime())) {
        console.error('Invalid date format. Please use an ISO format (YYYY-MM-DDTHH:mm:ss).');
        return;
    }

    // Update the countdown every second
    const interval = setInterval(() => {
        const now = new Date();
        const distance = targetDate - now;

        // Calculate time components
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the specified element
        if (distance > 0) {
            displayElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        } else {
            clearInterval(interval);
            displayElement.innerHTML = "Presale has ended.";
        }
    }, 1000);
}

// Example usage:
// Assuming there is an element with the ID 'countdown' in the HTML
const countdownElement = document.getElementById('countdown');
const presaleEndDate = '2023-12-31T23:59:59'; // Change to the actual end date of the presale
startCountdown(presaleEndDate, countdownElement);
```
