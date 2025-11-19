"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Generate a JavaScript function to display a countdown timer for the $WING presale price increase, as shown on the Dopawing website.
Generated: DETERMINISTIC_161f79bae0249444
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays a countdown timer for the $WING presale price increase.
 * @param {string} targetDate - The target date in ISO format (e.g., "2023-12-31T23:59:59")
 * @param {string} elementId - The ID of the HTML element where the countdown will be displayed
 */
function startWingPresaleCountdown(targetDate, elementId) {
    // Validate input parameters
    if (!targetDate || !elementId) {
        console.error('Invalid parameters: targetDate and elementId are required');
        return;
    }

    const countdownElement = document.getElementById(elementId);
    if (!countdownElement) {
        console.error(`Element with ID '${elementId}' not found`);
        return;
    }

    const targetTime = new Date(targetDate).getTime();
    if (isNaN(targetTime)) {
        console.error('Invalid target date format. Please use ISO format (e.g., "2023-12-31T23:59:59")');
        return;
    }

    // Update the countdown every second
    const countdownInterval = setInterval(() => {
        const now = new Date().getTime();
        const distance = targetTime - now;

        // If the countdown is finished
        if (distance < 0) {
            clearInterval(countdownInterval);
            countdownElement.innerHTML = "PRESALE PRICE INCREASED!";
            return;
        }

        // Calculate days, hours, minutes and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result
        countdownElement.innerHTML = `
            <div class="countdown-container">
                <div class="countdown-item">
                    <span class="countdown-value">${days}</span>
                    <span class="countdown-label">Days</span>
                </div>
                <div class="countdown-item">
                    <span class="countdown-value">${hours}</span>
                    <span class="countdown-label">Hours</span>
                </div>
                <div class="countdown-item">
                    <span class="countdown-value">${minutes}</span>
                    <span class="countdown-label">Minutes</span>
                </div>
                <div class="countdown-item">
                    <span class="countdown-value">${seconds}</span>
                    <span class="countdown-label">Seconds</span>
                </div>
            </div>
            <div class="countdown-message">Until $WING Presale Price Increase</div>
        `;
    }, 1000);
}

// Example usage when the DOM is fully loaded:
document.addEventListener('DOMContentLoaded', function() {
    // Replace with actual target date from the Dopawing website
    const presaleEndDate = "2023-12-31T23:59:59";
    startWingPresaleCountdown(presaleEndDate, "wing-presale-countdown");
});
```
